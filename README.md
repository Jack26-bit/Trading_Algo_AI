# Trading_Algo_AI
# Navi Trade: AI-Powered Autonomous Trading

![Status](https://img.shields.io/badge/Status-Development-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Navi Trade** is an experimental AI trading platform that uses **Reinforcement Learning (RL)** to learn profitable trading strategies. It features a real-time paper trading simulation where you can watch the AI agent analyze market data and execute trades.

---

##  Features

-   **🧠 AI Trader**: Uses a **PPO (Proximal Policy Optimization)** agent trained via `stable-baselines3`. The AI is rewarded for profit ("Points System") and penalized for losses.
-   **📈 Interactive Dashboard**: A premium dark-mode UI built with **Next.js** and **Recharts**, visualizing live market data with gradient-filled area charts.
-   **🎮 Paper Trading Simulation**: Watch the AI play out historical data candle-by-candle. Tracks:
    -   Cash Balance
    -   Holdings
    -   Net Worth
    -   P/L (Profit/Loss)
-   **🔄 Mock Data Fallback**: Automatically generates realistic stock data (Random Walk + Volatility) if the live API limit is reached.

---

##  Tech Stack

### Frontend (User Interface)
-   **Framework**: [Next.js 14](https://nextjs.org/) (React/TypeScript)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/)
-   **Charts**: [Recharts](https://recharts.org/)
-   **Icons**: Lucide React

### Backend (AI Brain)
-   **API**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
-   **Reinforcement Learning**: [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
-   **Environment**: [Gymnasium](https://gymnasium.farama.org/) (Custom Trading Environment)
-   **Data Source**: [Finnhub API](https://finnhub.io/)

---

##  Installation & Setup

### Prerequisites
-   Node.js & npm
-   Python 3.9+

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/navi-trade.git
cd navi-trade
```

### 2. Backend Setup
The backend runs the AI model and API.

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate venv
# Windows:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m uvicorn main:app --reload --port 8000
```

### 3. Frontend Setup
The frontend runs the dashboard.

Open a **new terminal**:
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Visit **[http://localhost:3000](http://localhost:3000)** to launch the app! 🚀

---

##  How to Use

1.  **Select a Ticker**: Choose a stock (e.g., AAPL, TSLA) from the dropdown.
2.  **Train AI System**: Click the button to let the agent study historical price action.
    -   *Note: This runs a training loop in the background.*
3.  **Run Simulation**: Click "Run Sim" to watch the AI trade on the data step-by-step.
4.  **Monitor Portfolio**: Watch your Net Worth grow (or shrink!) based on the AI's decisions.

---

##  Disclaimer

This project is for **educational and research purposes only**. The trading algorithms are experimental and should **NOT** be used for real financial trading. There is a significant risk of loss in financial trading.
