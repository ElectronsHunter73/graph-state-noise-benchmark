import numpy as np

from src.graph_noise.states import computational_basis_state
from src.graph_noise.noise import (
    bit_flip_noise,
    dephasing_noise,
    depolarizing_noise,
    measurement_bit_flip_noise,
)


def test_bit_flip_noise_zero_probability():
    state = computational_basis_state("00")
    noisy_state = bit_flip_noise(state, 0)

    assert np.allclose(noisy_state, state)


def test_dephasing_noise_zero_probability():
    state = computational_basis_state("00")
    noisy_state = dephasing_noise(state, 0)

    assert np.allclose(noisy_state, state)


def test_depolarizing_noise_zero_probability():
    state = computational_basis_state("00")
    noisy_state = depolarizing_noise(state, 0)

    assert np.allclose(noisy_state, state)


def test_measurement_bit_flip_zero_probability():
    probabilities = np.array([1, 0, 0, 0])
    noisy_probabilities = measurement_bit_flip_noise(probabilities, 0)

    assert np.allclose(noisy_probabilities, probabilities)


def test_measurement_bit_flip_noise():
    probabilities = np.array([1, 0, 0, 0])
    noisy_probabilities = measurement_bit_flip_noise(probabilities, 0.1)

    expected = np.array([0.81, 0.09, 0.09, 0.01])

    assert np.allclose(noisy_probabilities, expected)