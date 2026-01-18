import pandas as pd
import numpy as np

def load_and_clean_data(spot_path, fut_path, opt_path):
    """
    Loads raw CSVs, aligns timestamps, and merges them.
    """
    # Load Data
    df_spot = pd.read_csv(spot_path)
    df_fut = pd.read_csv(fut_path)
    df_opt = pd.read_csv(opt_path)

    # Align Timestamps
    for df in [df_spot, df_fut, df_opt]:
        df.columns = df.columns.str.lower()
        if 'date' in df.columns and 'time' in df.columns:
            df['timestamp'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
        elif 'datetime' in df.columns:
            df['timestamp'] = pd.to_datetime(df['datetime'])
        df.set_index('timestamp', inplace=True)

    # Merge
    df_merged = df_spot.join(df_fut[['close', 'oi']], rsuffix='_fut')
    df_merged = df_merged.join(df_opt[['atm_strike', 'call_iv', 'put_iv', 'call_oi', 'put_oi']], rsuffix='_opt')
    
    # Handle Missing Values
    df_merged.fillna(method='ffill', inplace=True)
    df_merged.dropna(inplace=True)
    
    return df_merged