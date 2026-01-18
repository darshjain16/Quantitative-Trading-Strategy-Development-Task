import pandas as pd

def apply_strategy(df):
    """
    Applies 5/15 EMA Crossover with Regime Filter.
    """
    df['signal'] = 0
    
    # Long Condition
    long_cond = (df['ema_5'] > df['ema_15']) & (df['regime'] == 1)
    df.loc[long_cond, 'signal'] = 1
    
    # Short Condition
    short_cond = (df['ema_5'] < df['ema_15']) & (df['regime'] == -1)
    df.loc[short_cond, 'signal'] = -1
    
    return df