import numpy as np

def calculate_metrics(df):
    """
    Computes Sharpe, Drawdown, and Total Return.
    """
    # Calculate PnL
    # Strategy PnL = Signal (yesterday) * Return (today)
    df['strategy_pnl'] = df['signal'].shift(1) * df['returns']
    df['cumulative_return'] = (1 + df['strategy_pnl']).cumprod()
    
    # Metrics
    total_return = df['cumulative_return'].iloc[-1] - 1
    sharpe = df['strategy_pnl'].mean() / df['strategy_pnl'].std() * np.sqrt(252*75)
    
    # Max Drawdown
    peak = df['cumulative_return'].cummax()
    drawdown = (df['cumulative_return'] - peak) / peak
    max_drawdown = drawdown.min()
    
    return {
        "Total Return": total_return,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_drawdown
    }