import matplotlib.pyplot as plt
import base64
import pandas as pd
from io import BytesIO
from utils.llm_factory import load_llm

class SummarizerAgent:
    def __init__(self):
        self.llm = load_llm(0.2)

    def summarize(self, q, df):
        # Handle empty dataframe
        if df.empty:
            return f"No data found for your query: '{q}'. Please try rephrasing your question or check if the data exists in the database."
        
        # Get data sample - use more rows for better context
        num_rows = len(df)
        sample_size = min(10, num_rows)  # Show up to 10 rows for context
        data_sample = df.head(sample_size).to_string() if sample_size > 0 else "No data available"
        
        # Get column info for better context
        columns_info = f"Columns: {', '.join(df.columns.tolist())}"
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if numeric_cols:
            columns_info += f"\nNumeric columns: {', '.join(numeric_cols)}"
        
        # Build a more detailed prompt
        prompt = f"""
You are a senior data analyst. Analyze the following query results and provide a clear, concise summary.

Question: {q}

{columns_info}

Data sample ({sample_size} of {num_rows} rows):
{data_sample}

Instructions:
- If the data is meaningful, provide 2-3 short bullet points with key insights
- Focus on the most important numbers, trends, or patterns
- Use plain language that a business user would understand
- If the data seems incomplete or unclear, mention that

Provide your analysis:
"""
        try:
            response = self.llm.invoke(prompt)
            summary = response.content if hasattr(response, "content") else str(response)
            
            # Validate the response isn't generic
            generic_phrases = [
                "dataset is currently empty",
                "no data points or variables are available",
                "need to acquire and load the relevant data",
                "no data available for analysis"
            ]
            
            if any(phrase.lower() in summary.lower() for phrase in generic_phrases):
                # Return a more helpful message based on actual data
                if num_rows > 0:
                    return f"Found {num_rows} result(s) for your query. Here are the key details:\n\n" + data_sample[:500] + ("..." if len(data_sample) > 500 else "")
                else:
                    return f"No data found matching your query: '{q}'. Please try rephrasing or check if the data exists."
            
            return summary
        except Exception as e:
            print(f"Error in summarizer: {str(e)}")
            # Fallback to basic summary
            if num_rows > 0:
                return f"Query returned {num_rows} row(s). Data columns: {', '.join(df.columns.tolist()[:5])}"
            else:
                return f"No data found for: '{q}'"
    
    # ---------------------------------------------
    # Detect chart type based on question
    # ---------------------------------------------
    def detect_chart_type(self, question: str):
        q = question.lower()

        if "line" in q or "trend" in q or "time series" in q:
            return "line"
        if "bar" in q or "compare" in q or "comparison" in q:
            return "bar"
        if "scatter" in q or "relationship" in q or "correlation" in q:
            return "scatter"
        if "hist" in q or "distribution" in q:
            return "hist"
        if "pie" in q:
            return "pie"

        return "auto"  # fallback

    def generate_viz(self, question, df):
        if df.empty:
            return None, None

        chart_type = self.detect_chart_type(question)
        plt.figure(figsize=(10, 6))

        # Auto-select columns
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        non_numeric_cols = df.select_dtypes(exclude="number").columns.tolist()

        # Detect time-series columns (datetime-like or time-related)
        time_cols = []
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ["time", "date", "timestamp", "forecast_time"]):
                time_cols.append(col)
            # Also check if column contains datetime-like strings
            elif df[col].dtype == 'object':
                try:
                    pd.to_datetime(df[col].head(10))
                    time_cols.append(col)
                except:
                    pass

        # Prepare data for plotting - aggregate if needed
        plot_df = df.copy()
        
        # If we have time-series data with multiple values per timestamp, aggregate
        if time_cols and numeric_cols:
            time_col = time_cols[0]
            # Check if there are duplicate timestamps
            if plot_df[time_col].duplicated().any():
                # Aggregate numeric columns by time column
                agg_dict = {col: 'sum' for col in numeric_cols}
                plot_df = plot_df.groupby(time_col, as_index=False).agg(agg_dict)
                # Sort by time for proper line/bar charts
                try:
                    plot_df[time_col] = pd.to_datetime(plot_df[time_col])
                    plot_df = plot_df.sort_values(time_col)
                except:
                    plot_df = plot_df.sort_values(time_col)

        # default selections
        x = time_cols[0] if time_cols else (non_numeric_cols[0] if non_numeric_cols else df.columns[0])
        y = numeric_cols[0] if numeric_cols else None

        # ---------------------------------------------
        # CHART TYPE HANDLERS
        # ---------------------------------------------
        try:
            if chart_type == "line" or (chart_type == "auto" and time_cols):
                if y is None:
                    return None, None
                # For time-series, use line chart
                ax = plot_df.plot.line(x=x, y=y, figsize=(10, 6), marker='o', markersize=4)
                ax.set_xlabel(x.replace('_', ' ').title())
                ax.set_ylabel(y.replace('_', ' ').title())
                ax.set_title(f"{y.replace('_', ' ').title()} Over Time")
                ax.grid(True, alpha=0.3)
                plt.xticks(rotation=45, ha='right')

            elif chart_type == "bar":
                if y is None:
                    return None, None
                ax = plot_df.plot.bar(x=x, y=y, figsize=(10, 6))
                ax.set_xlabel(x.replace('_', ' ').title())
                ax.set_ylabel(y.replace('_', ' ').title())
                ax.set_title(f"{y.replace('_', ' ').title()} by {x.replace('_', ' ').title()}")
                plt.xticks(rotation=45, ha='right')

            elif chart_type == "scatter":
                if len(numeric_cols) < 2:
                    return None, None
                ax = plot_df.plot.scatter(x=numeric_cols[0], y=numeric_cols[1], figsize=(10, 6))
                ax.set_xlabel(numeric_cols[0].replace('_', ' ').title())
                ax.set_ylabel(numeric_cols[1].replace('_', ' ').title())
                ax.set_title(f"{numeric_cols[1].replace('_', ' ').title()} vs {numeric_cols[0].replace('_', ' ').title()}")
                ax.grid(True, alpha=0.3)

            elif chart_type == "hist":
                if y is None:
                    return None, None
                ax = plot_df[y].plot.hist(figsize=(10, 6), bins=20)
                ax.set_xlabel(y.replace('_', ' ').title())
                ax.set_ylabel("Frequency")
                ax.set_title(f"Distribution of {y.replace('_', ' ').title()}")
                ax.grid(True, alpha=0.3)

            elif chart_type == "pie":
                if y is None:
                    return None, None
                # Limit to top 10 for readability
                plot_data = plot_df.set_index(x)[y]
                if len(plot_data) > 10:
                    plot_data = plot_data.nlargest(10)
                ax = plot_data.plot.pie(autopct="%1.1f%%", figsize=(10, 6))
                ax.set_ylabel("")
                ax.set_title(f"{y.replace('_', ' ').title()} Distribution")

            # fallback → auto (line chart if time-series, otherwise bar)
            else:
                if time_cols and y:
                    ax = plot_df.plot.line(x=x, y=y, figsize=(10, 6), marker='o', markersize=4)
                    ax.set_xlabel(x.replace('_', ' ').title())
                    ax.set_ylabel(y.replace('_', ' ').title())
                    ax.grid(True, alpha=0.3)
                    plt.xticks(rotation=45, ha='right')
                else:
                    plot_df.plot(figsize=(10, 6))

            # ---------------------------------------------
            # Export PNG for frontend
            # ---------------------------------------------
            buf = BytesIO()
            plt.tight_layout()
            plt.savefig(buf, format="png", dpi=100, bbox_inches='tight')
            buf.seek(0)
            encoded = base64.b64encode(buf.read()).decode("utf-8")
            plt.close()

            return encoded, "image/png"

        except Exception as e:
            print(f"Plot error: {e}")
            import traceback
            traceback.print_exc()
            plt.close()
            return None, None
