import numpy as np
from hmmlearn.hmm import GaussianHMM

class RegimeDetector:
    def __init__(self, n_components=3):
        self.model = GaussianHMM(n_components=n_components, covariance_type="full", n_iter=100, random_state=42)
        
    def fit_predict(self, returns, iv):
        """
        Trains HMM and returns regime labels (Bull=+1, Bear=-1, Side=0)
        """
        X = np.column_stack([returns, iv])
        self.model.fit(X)
        regimes = self.model.predict(X)
        
        # Map regimes based on Mean Returns
        # Highest Return -> Bull (+1), Lowest -> Bear (-1)
        means = self.model.means_[:, 0]
        sorted_idx = np.argsort(means)
        map_dict = {sorted_idx[0]: -1, sorted_idx[1]: 0, sorted_idx[2]: 1}
        
        return [map_dict[r] for r in regimes]