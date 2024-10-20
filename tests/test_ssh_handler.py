import unittest
from src.metrics import collect_metrics

class TestMetrics(unittest.TestCase):
    def test_collect_metrics(self):
        #mock the ssh client and test if the metrics are collected correctly
        self.assertIsNotNone(collect_metrics(None))

if __name__ == "__main__":
    unittest.main()