# ml_models/dispersion_predictor.py

from sklearn.ensemble import RandomForestRegressor
import numpy as np

class DispersionPredictor:
    def __init__(self):
        # Initialize the model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, X_train, y_train):
        """
        Train the model on historical dispersion data.
        Parameters:
            X_train : np.array : Input features (e.g., wind speed, release rate, etc.)
            y_train : np.array : Target values (e.g., measured concentrations)
        """
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        """
        Predict concentration levels based on test data.
        Parameters:
            X_test : np.array : Test features
        Returns:
            np.array : Predicted concentrations
        """
        return self.model.predict(X_test)
