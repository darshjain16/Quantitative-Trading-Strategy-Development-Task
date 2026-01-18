import numpy as np
from scipy.stats import norm

def calculate_bs_delta(S, K, T, r, sigma, option_type='call'):
    """
    Calculates Black-Scholes Delta.
    """
    if sigma <= 0 or T <= 0:
        return 0.5
        
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1