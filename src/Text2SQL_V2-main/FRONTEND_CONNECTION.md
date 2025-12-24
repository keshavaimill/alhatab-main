# Frontend Connection Guide for Text2SQL_V2-main

## ✅ Connection Status

The frontend is now configured to connect to **Text2SQL_V2-main** backend.

## 🔧 Configuration Files Updated

### 1. **Frontend API Client** (`src/components/floating-bot/api.ts`)
- ✅ `TEXT2SQL_API_URL` - Points to Text2SQL_V2-main backend
- ✅ `API_BASE_URL` - Points to same backend for REST API endpoints
- ✅ Defaults to `http://localhost:5000` for local development
- ✅ Can be overridden via environment variables

### 2. **Vite Proxy** (`vite.config.ts`)
- ✅ `/api/text2sql` proxy configured to point to Text2SQL_V2-main
- ✅ Defaults to `http://localhost:5000` for local development
- ✅ Can be overridden via `VITE_TEXT2SQL_API_URL` environment variable

## 🌐 Environment Variables

Create a `.env` file in the **project root** (not in Text2SQL_V2-main folder) with:

```env
# Backend API URL (for both chatbot and REST APIs)
# Local development:
VITE_TEXT2SQL_API_URL=http://localhost:5000

# Production (when deployed):
# VITE_TEXT2SQL_API_URL=https://text2sql-v2.onrender.com

# Alternative: Use separate variable for REST APIs (optional)
# VITE_API_BASE_URL=https://text2sql-v2.onrender.com
```

## 🚀 Local Development Setup

### Step 1: Start Text2SQL_V2-main Backend

```bash
cd src/Text2SQL_V2-main
pip install -r requirements.txt

# Create .env file with your API keys
# LLM_PROVIDER=google
# GOOGLE_API_KEY=your_key_here
# MAIL_USERNAME=your_email@example.com
# MAIL_PASSWORD=your_password
# ALERT_EMAILS=recipient@example.com

python app.py
```

Backend will start on `http://localhost:5000`

### Step 2: Start Frontend

```bash
# In project root
npm install
npm run dev
```

Frontend will start on `http://localhost:8080` (or port specified in vite.config.ts)

### Step 3: Verify Connection

1. **Chatbot**: Open floating bot and send a query
2. **REST APIs**: Check browser Network tab - all API calls should go to `localhost:5000`

## 📡 API Endpoints Available

### Chatbot Endpoint
- **POST** `/query` - Text2SQL chatbot with email notifications

### REST API Endpoints (from V1)
- **GET** `/store-kpis?store_id=...`
- **GET** `/store-shelf-performance?store_id=...`
- **GET** `/dc-kpis?dc_id=...`
- **GET** `/dc-inventory-age?dc_id=...`
- **GET** `/dc-days-cover?dc_id=...&sku_id=...`
- **GET** `/factory-kpis?factory_id=...&line_id=...`
- **GET** `/factory-hourly-production?factory_id=...&line_id=...`
- **GET** `/factory-dispatch-planning?factory_id=...&line_id=...`
- **GET** `/node-health`
- **GET** `/global-kpis`
- **GET** `/health`

## 🔍 Troubleshooting

### Issue: CORS Errors
**Solution**: Backend has CORS configured. If you see CORS errors:
1. Check that backend is running on port 5000
2. Verify `flask-cors` is installed: `pip install flask-cors`
3. Check backend logs for CORS configuration

### Issue: 404 Not Found
**Solution**: 
1. Verify backend is running: `curl http://localhost:5000/health`
2. Check vite proxy configuration
3. Verify endpoint paths match between frontend and backend

### Issue: Chatbot Not Working
**Solution**:
1. Check browser console for errors
2. Verify `TEXT2SQL_API_URL` in `api.ts`
3. Test backend directly: `curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"question":"test"}'`

### Issue: REST API Endpoints Not Working
**Solution**:
1. Verify data layer initialized: Check backend logs for "✅ Global data layer initialized"
2. Check if `predictions.csv` exists (required for factory endpoints)
3. Verify `API_BASE_URL` in frontend API files

## 📝 Frontend API Files Using Backend

All these files import `API_BASE_URL` from `api.ts`:
- `src/api/dcKpis.ts`
- `src/api/dcInventoryAge.ts`
- `src/api/dcDaysCover.ts`
- `src/api/factoryKpis.ts`
- `src/api/factoryHourlyProduction.ts`
- `src/api/factoryDispatchPlanning.ts`
- `src/api/storeKpis.ts`
- `src/api/storeShelfPerformance.ts`
- `src/api/nodeHealth.ts`
- `src/api/globalKpis.ts`

## ✅ Verification Checklist

- [ ] Backend starts without errors
- [ ] `/health` endpoint returns `{"status": "healthy"}`
- [ ] Chatbot sends queries successfully
- [ ] REST API endpoints return data
- [ ] No CORS errors in browser console
- [ ] Email notifications work (for write operations)
- [ ] All dashboard pages load data correctly

## 🎯 Production Deployment

For production, update environment variables:

```env
VITE_TEXT2SQL_API_URL=https://text2sql-v2.onrender.com
```

Or set it in your deployment platform (Vercel, Netlify, etc.) environment variables.

The backend URL should match where Text2SQL_V2-main is deployed.

