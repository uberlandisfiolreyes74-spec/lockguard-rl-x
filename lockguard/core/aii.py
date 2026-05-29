# lockguard/core/aii.py
import numpy as np

class AdversarialIrreversibilityIndex:
    """
    AII - Adversarial Irreversibility Index
    Métrica central de LockGuard RL-X
    """
    
    def __init__(self, weights=None):
        self.weights = weights or {
            "sync": 0.25,
            "concentration": 0.20,
            "impact": 0.25,
            "volatility": 0.15,
            "adversarial": 0.15
        }
    
    def compute(self, actions: np.ndarray, price_delta: float = 0.0, volatility: float = 0.0) -> float:
        """
        Calcula el AII a partir de acciones conjuntas.
        """
        if len(actions) == 0:
            return 0.0
            
        # Synchronization
        sync = abs(np.sum(actions)) / (np.sum(np.abs(actions)) + 1e-8)
        
        # Concentration
        concentration = np.max(np.abs(actions)) / (np.sum(np.abs(actions)) + 1e-8)
        
        # Impact & Volatility (simplificado)
        impact = abs(price_delta)
        vol_factor = min(volatility / 0.05, 1.0)
        
        # Adversarial component (proxy)
        adversarial = np.std(actions) * 1.5
        
        aii = (
            self.weights["sync"] * sync +
            self.weights["concentration"] * concentration +
            self.weights["impact"] * min(impact, 1.0) +
            self.weights["volatility"] * vol_factor +
            self.weights["adversarial"] * min(adversarial, 1.0)
        )
        
        return float(np.clip(aii, 0.0, 1.0))
