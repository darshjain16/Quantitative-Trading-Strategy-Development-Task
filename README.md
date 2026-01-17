# Quantitative-Trading-Strategy-Development-Task

## Project Overview
This project implements a complete end-to-end quantitative trading system for the Nifty 50 index. It features a robust data pipeline, regime detection using Hidden Markov Models (HMM), and a trading strategy enhanced by Machine Learning (XGBoost & LSTM) to filter signals.

**Key Objectives:**
- Fetch and process 1-year of 5-minute interval data (Spot, Futures, Options).
- Engineering advanced features including Greeks (Delta, Gamma, Vega) and Volatility measures.
- Detect market regimes (Bull, Bear, Sideways) to adapt trading logic.
- Backtest a 5/15 EMA crossover strategy with ML-based signal filtering.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/darshjain16/Quant_Project.git](https://github.com/darshjain16/Quant_Project.git)

## Install dependencies
pip install -r requirements.txt

## How to Run
1. Navigate to the notebooks/ directory.
2. Open Task_Submission.ipynb in Jupyter Notebook or VS Code.
3. Run all cells sequentially.
-  The notebook will load data from data/, train the HMM and ML models, and display performance metrics.

## Project Structure explanation

├── data/                  # Raw and Processed Datasets (Spot, Futures, Options)
├── models/                # Saved ML Models (XGBoost/LSTM checkpoints)
├── notebooks/             # Main Strategy Notebook (Task_Submission.ipynb)
├── plots/                 # Strategy Performance & Regime Analysis Charts
├── results/               # Data Cleaning Reports & Output Logs
├── src/                   # Python Source Code (Exported Logic)
├── README.md              # Project Documentation
└── requirements.txt       # Python Dependencies

## Key Results Summary
**Outlier Analysis:**
Identified that top performing trades (>3 Sigma) occur predominantly in high-volatility Bull regimes.

**Strategy Performance:**
- Baseline Return: 0.93%
- ML-Enhanced Return: 1.04%
- Sharpe Ratio: -1.03
- Max Drawdown: -24.06%

**Regime Detection:** 
Successfully classified market into 3 distinct states, avoiding whipsaws during sideways markets.

