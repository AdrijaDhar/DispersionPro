# tests/test_ml.py

import unittest
from ml_models.dispersion_predictor import train_dispersion_model, predict_concentration
import numpy as np

class TestMLModel(unittest.TestCase):
    def test_training(self):
        X_train = np.random.rand(100, 5)
        y_train = np.random.rand(100)
        model = train_dispersion_model(X_train, y_train)
        self.assertIsNotNone(model)

    def test_prediction(self):
        X_test = np.random.rand(10, 5)
        predictions = predict_concentration(X_test)
        self.assertEqual(len(predictions), 10)

if __name__ == '__main__':
    unittest.main()
