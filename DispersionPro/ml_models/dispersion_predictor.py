# ml_models/dispersion_predictor.py

from sklearn.ensemble import RandomForestRegressor
import pickle

def train_dispersion_model(X_train, y_train):
    """
    Trains a machine learning model to predict pollutant concentrations.

    Parameters:
    X_train: np.array - Training features.
    y_train: np.array - Training labels.

    Returns:
    model: Trained machine learning model.
    """
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    # Save the model
    with open('ml_models/dispersion_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return model

def predict_concentration(X_test):
    """
    Predicts concentrations using the trained machine learning model.

    Parameters:
    X_test: np.array - Test features.

    Returns:
    predictions: np.array - Predicted concentrations.
    """
    with open('ml_models/dispersion_model.pkl', 'rb') as f:
        model = pickle.load(f)
    predictions = model.predict(X_test)
    return predictions
