# tests/test_aii.py
import unittest
import numpy as np
from lockguard.core.aii import AdversarialIrreversibilityIndex

class TestAII(unittest.TestCase):
    
    def setUp(self):
        self.aii = AdversarialIrreversibilityIndex()
    
    def test_aii_normal_behavior(self):
        actions = np.array([0.1, 0.2, -0.1, 0.15])
        score = self.aii.compute(actions)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
    
    def test_aii_high_synchronization(self):
        actions = np.array([0.8, 0.85, 0.82, 0.79])
        score = self.aii.compute(actions)
        self.assertGreater(score, 0.6)  # Alta sincronía → alto AII
    
    def test_aii_bounds(self):
        # Caso extremo
        actions = np.ones(10) * 0.99
        score = self.aii.compute(actions)
        self.assertAlmostEqual(score, 1.0, delta=0.05)
        
        # Caso bajo
        actions = np.zeros(10)
        score = self.aii.compute(actions)
        self.assertAlmostEqual(score, 0.0, delta=0.05)

if __name__ == '__main__':
    unittest.main()
