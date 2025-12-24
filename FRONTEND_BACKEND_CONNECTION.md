# Frontend ↔ Backend Connection Status

## ✅ Connection Complete

The frontend is now **fully connected** to **Text2SQL_V2-main** backend.

## 🔧 Configuration Summary

### Backend: Text2SQL_V2-main
- **Location**: `src/Text2SQL_V2-main/`
- **Port**: `5000` (default)
- **Features**: 
  - ✅ Text2SQL chatbot with email notifications
  - ✅ 10+ REST API endpoints
  - ✅ CORS enabled
  - ✅ Data layer with precomputed KPIs

### Frontend Configuration

#### 1. API Client (`src/components/floating-bot/api.ts`)
```typescript
// Chatbot endpoint
TEXT2SQL_API_URL = http://localhost:5000 (local) or env var

// REST API endpoints  
API_BASE_URL = http://localhost:5000 (local) or env var
```

#### 2. Vite Proxy (`vite.config.ts`)
```typescript
"/api/text2sql" → http://localhost:5000
```

## 📡 API Endpoints Connected

### Chatbot
- ✅ `POST /query` - Text2SQL chatbot (with email notifications)

### REST APIs (All Connected)
- ✅ `GET /store-kpis` → `src/api/storeKpis.ts`
- ✅ `GET /store-shelf-performance` → `src/api/storeShelfPerformance.ts`
- ✅ `GET /dc-kpis` → `src/api/dcKpis.ts`
- ✅ `GET /dc-inventory-age` → `src/api/dcInventoryAge.ts`
- ✅ `GET /dc-days-cover` → `src/api/dcDaysCover.ts`
- ✅ `GET /factory-kpis` → `src/api/factoryKpis.ts`
- ✅ `GET /factory-hourly-production` → `src/api/factoryHourlyProduction.ts`
- ✅ `GET /factory-dispatch-planning` → `src/api/factoryDispatchPlanning.ts`
- ✅ `GET /node-health` → `src/api/nodeHealth.ts`
- ✅ `GET /global-kpis` → `src/api/globalKpis.ts`

## 🚀 Quick Start

### 1. Start Backend
```bash
cd src/Text2SQL_V2-main
pip install -r requirements.txt
python app.py
# Backend runs on http://localhost:5000
```

### 2. Start Frontend
```bash
npm install
npm run dev
# Frontend runs on http://localhost:8080
```

### 3. Verify Connection
- Open browser → `http://localhost:8080`
- Check browser console (should see no CORS errors)
- Test chatbot (floating bot icon)
- Navigate to dashboard pages (should load data)

## 🔍 Environment Variables (Optional)

Create `.env` in project root:

```env
# For local development (defaults work without this)
VITE_TEXT2SQL_API_URL=http://localhost:5000

# For production deployment
# VITE_TEXT2SQL_API_URL=https://text2sql-v2.onrender.com
```

## ✅ Verification Checklist

- [x] Frontend API client configured
- [x] Vite proxy configured  
- [x] All REST API endpoints connected
- [x] Chatbot endpoint connected
- [x] CORS enabled on backend
- [x] Response formats match TypeScript interfaces
- [x] Query parameters match backend expectations

## 🎯 What Works Now

1. **Chatbot**: 
   - Natural language queries → SQL → Results
   - Email notifications on write operations
   - Visualizations when requested

2. **Dashboard Pages**:
   - Command Center (`/`) - Global KPIs, Node Health, Maps
   - Factory (`/factory`) - Factory KPIs, Production, Dispatch Planning
   - DC (`/dc`) - DC KPIs, Inventory Age, Days of Cover
   - Store (`/store`) - Store KPIs, Shelf Performance

3. **All REST APIs**: 
   - Real-time data from precomputed KPIs
   - Fast responses (data layer precomputation)
   - Consistent data across all endpoints

## 📝 Notes

- Backend must be running before frontend can fetch data
- Factory endpoints require `predictions.csv` (already present)
- Email notifications require SMTP configuration in backend `.env`
- All endpoints use same backend URL (unified configuration)

## 🐛 Troubleshooting

**Issue**: CORS errors
- ✅ Backend has CORS configured
- Check backend logs for CORS initialization

**Issue**: 404 errors
- Verify backend is running: `curl http://localhost:5000/health`
- Check vite proxy target URL

**Issue**: Empty data
- Check backend logs for data layer initialization
- Verify CSV files exist in `datasets/` folder

---

**Status**: ✅ **FULLY CONNECTED AND READY TO USE**

