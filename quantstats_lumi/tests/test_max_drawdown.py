import unittest
from quantstats_lumi import stats  # Adjust the import path based on your project structure
import pandas as pd

class TestMaxDrawdown(unittest.TestCase):

    def test_max_drawdown_positive_returns(self):
        returns = [0.01, 0.02, 0.015, 0.03, 0.025]
        # Manually calculate expected max drawdown
        cumulative = (1 + pd.Series(returns)).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        expected_max_drawdown = drawdown.min()
        result = stats.max_drawdown(returns)
        self.assertAlmostEqual(result, expected_max_drawdown, places=4)
    
    def test_max_drawdown_negative_returns(self):
        returns = [-0.01, -0.02, -0.015, -0.03, -0.025]
        # Manually calculate expected max drawdown
        cumulative = (1 + pd.Series(returns)).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        expected_max_drawdown = drawdown.min()
        result = stats.max_drawdown(returns)
        self.assertAlmostEqual(result, expected_max_drawdown, places=4)

    def test_max_drawdown_mixed_returns(self):
        returns = [0.01, -0.02, 0.015, -0.03, 0.025]
        # Manually calculate expected max drawdown
        cumulative = (1 + pd.Series(returns)).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        expected_max_drawdown = drawdown.min()
        result = stats.max_drawdown(returns)
        self.assertAlmostEqual(result, expected_max_drawdown, places=4)
    
    def test_max_drawdown_non_numeric_input(self):
        returns = ["a", "b", "c"]
        with self.assertRaises(ValueError):
            stats.max_drawdown(returns)
    
    def test_max_drawdown_empty_input(self):
        returns = []
        with self.assertRaises(ValueError):
            stats.max_drawdown(returns)
    
    def test_max_drawdown_realistic_scenario(self):
        # Simulated realistic returns
        returns = [0.001, 0.002, 0.003, 0.002, 0.001, -0.001, 0.002, 0.001, 0.002, 0.003]
        # Manually calculate expected max drawdown
        cumulative = (1 + pd.Series(returns)).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        expected_max_drawdown = drawdown.min()
        result = stats.max_drawdown(returns)
        self.assertAlmostEqual(result, expected_max_drawdown, places=4)

if __name__ == '__main__':
    unittest.main()