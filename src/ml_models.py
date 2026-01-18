from xgboost import XGBClassifier
import numpy as np

class MLFilter:
    def __init__(self):
        self.model = XGBClassifier(eval_metric='logloss', use_label_encoder=False)
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        
    def predict(self, X):
        return self.model.predict(X)
        
    def save(self, path):
        self.model.save_model(path)