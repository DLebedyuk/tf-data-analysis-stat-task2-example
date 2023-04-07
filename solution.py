import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 461920076 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = np.mean(x) / 92
    scale = np.sqrt(np.var(x) / 92**2) * np.sqrt(2 / (1 - np.exp(-2)))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
