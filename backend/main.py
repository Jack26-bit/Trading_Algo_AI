from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.finnhub_client import finnhub_client
from ai.model import ai_agent
from ai.environment import TradingEnv
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="AI Trading Backend")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StockRequest(BaseModel):
    symbol: str

@app.get("/")
async def root():
    return {"message": "AI Trading Backend is API Live"}

@app.get("/api/quote/{symbol}")
async def get_quote(symbol: str):
    data = finnhub_client.get_quote(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data

@app.get("/api/candles/{symbol}")
async def get_candles(symbol: str, resolution: str = "D"):
    df = finnhub_client.get_stock_candles(symbol, resolution)
    if df.empty:
        raise HTTPException(status_code=404, detail="Data not found")
    return df.to_dict(orient="records")

@app.post("/api/train/{symbol}")
async def train_agent(symbol: str):
    # Fetch ample history for training
    df = finnhub_client.get_stock_candles(symbol, resolution="D", count=500)
    if df.empty:
        raise HTTPException(status_code=404, detail="Not enough data to train")
    
    # Run training in background (simplified here to be synchronous for MVP)
    # In production, use BackgroundTasks
    try:
        msg = ai_agent.train(df, total_timesteps=5000)
        return {"status": "success", "message": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class PredictRequest(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    holdings: float
    balance: float
    net_worth_diff: float

@app.post("/api/predict")
async def predict_action(data: PredictRequest):
    # Construct observation vector matching Environment
    obs = np.array([
        data.open, data.high, data.low, data.close, data.volume,
        data.holdings, data.balance, data.net_worth_diff
    ], dtype=np.float32)
    
    action = ai_agent.predict(obs)
    return {"action": action} # 0=Hold, 1=Buy, 2=Sell

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
