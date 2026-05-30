import numpy as np
from src.graph_noise.noise import measurement_bit_flip_noise
probs = np.array([1, 0, 0, 0])
print(measurement_bit_flip_noise(probs, 0.1))