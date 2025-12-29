import { API_BASE_URL } from "@/components/floating-bot/api";

export interface HourlySalesData {
  hour: string;
  sales: number;
  forecast: number;
}

export const fetchStoreHourlySales = async (
  storeId: string,
): Promise<HourlySalesData[]> => {
  if (!API_BASE_URL) {
    throw new Error("API_BASE_URL is not configured. Please set VITE_TEXT2SQL_API_URL in your .env file.");
  }
  
  const params = new URLSearchParams({ store_id: storeId });
  const response = await fetch(`http://localhost:5000/store-hourly-sales?${params.toString()}`);

  if (!response.ok) {
    throw new Error(`Failed to fetch hourly sales data: ${response.statusText}`);
  }

  return response.json();
};

