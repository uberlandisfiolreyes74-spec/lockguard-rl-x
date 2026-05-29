"""
LockGuard RL-X - Causalidad Adversarial (A-CIM)
===============================================
Implementación de métricas de causalidad para detectar influencia engañosa
entre agentes en entornos multi-agente.
"""

import numpy as np
from collections import defaultdict
import pandas as pd


class AdversarialCausalInterventionMatrix:
    """
    A-CIM: Adversarial Causal Intervention Matrix
    Mide la influencia causal entre agentes, incluyendo influencia engañosa.
    """
    
    def __init__(self, n_agents: int, decay_factor: float = 0.95, window_size: int = 50):
        self.n_agents = n_agents
        self.decay = decay_factor
        self.window = window_size
        
        # Matrices principales
        self.cim = np.zeros((n_agents, n_agents))          # Causal Influence
        self.ucs = np.zeros((n_agents, n_agents))          # Unexplained Correlation Score
        self.action_history = []                           # Buffer de acciones
        
    def update(self, actions: np.ndarray, market_signals: np.ndarray = None):
        """
        Actualiza la matriz A-CIM con nuevas acciones.
        actions: array de forma (n_agents,)
        """
        self.action_history.append(actions.copy())
        if len(self.action_history) > self.window:
            self.action_history.pop(0)
        
        if len(self.action_history) < 3:
            return self.cim, self.ucs
        
        # Convertir a array
        history = np.array(self.action_history)  # (t, n_agents)
        
        # Calcular influencia causal (simplificado con correlación condicional)
        for i in range(self.n_agents):
            for j in range(self.n_agents):
                if i == j:
                    continue
                
                # Correlación entre acción i y acción j (lag-1)
                if len(history) > 1:
                    corr = np.corrcoef(history[:-1, i], history[1:, j])[0, 1]
                    self.cim[i, j] = self.decay * self.cim[i, j] + (1 - self.decay) * corr
        
        # Unexplained Correlation Score (UCS) - influencia no explicada por señales de mercado
        if market_signals is not None:
            for i in range(self.n_agents):
                for j in range(self.n_agents):
                    if i == j:
                        continue
                    # Correlación residual
                    self.ucs[i, j] = max(0, np.corrcoef(actions[i], actions[j])[0,1] - 0.3)
        
        return self.cim, self.ucs
    
    def get_top_influencers(self, agent_id: int, top_k: int = 3):
        """Retorna los agentes con mayor influencia causal sobre agent_id"""
        influences = self.cim[:, agent_id]
        top_indices = np.argsort(influences)[-top_k:]
        return top_indices, influences[top_indices]
    
    def get_suspicious_pairs(self, threshold: float = 0.65):
        """Retorna pares de agentes con alta influencia + UCS"""
        suspicious = []
        for i in range(self.n_agents):
            for j in range(i+1, self.n_agents):
                score = abs(self.cim[i,j]) + self.ucs[i,j]
                if score > threshold:
                    suspicious.append((i, j, score))
        return sorted(suspicious, key=lambda x: x[2], reverse=True)
    
    def summary(self):
        """Resumen de causalidad"""
        total_influence = np.sum(np.abs(self.cim))
        avg_influence = total_influence / (self.n_agents * (self.n_agents - 1))
        
        return {
            "total_causal_influence": total_influence,
            "avg_influence_per_pair": avg_influence,
            "max_influence": np.max(np.abs(self.cim)),
            "suspicious_pairs": len(self.get_suspicious_pairs())
        }


# Ejemplo de uso
if __name__ == "__main__":
    acim = AdversarialCausalInterventionMatrix(n_agents=8)
    
    # Simular varias rondas
    for t in range(100):
        actions = np.random.normal(0, 1, 8)
        acim.update(actions)
    
    print("📊 Resumen A-CIM:")
    print(acim.summary())
    print("\nPares más sospechosos:")
    print(acim.get_suspicious_pairs(threshold=0.6))
