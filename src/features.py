import pandas as pd
import numpy as np
from src.greeks import calculate_bs_delta

def generate_features(df):
    """
    Adds EMAs, Greeks, and Volatility metrics to the dataframe.
    """
    # Technical Indicators
    df['ema_5'] = df['close'].ewm(span=5, adjust=False).mean()
    df['ema_15'] = df['close'].ewm(span=15, adjust=False).mean()
    df['returns'] = df['close'].pct_change()
    
    # Greeks
    # Assuming constant T for simplicity in this demo
    T = 7/365 
    r = 0.065
    
    df['call_delta'] = df.apply(lambda row: calculate_bs_delta(
        row['close'], row['atm_strike'], T, r, row['call_iv']/100, 'call'), axis=1)
        
    # Derived Features
    df['average_iv'] = (df['call_iv'] + df['put_iv']) / 2
    df['pcr_oi'] = df['put_oi'] / df['call_oi']
    df['futures_basis'] = (df['close_fut'] - df['close']) / df['close']
    
    return df.dropna()