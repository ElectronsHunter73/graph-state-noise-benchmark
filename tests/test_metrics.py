import numpy as np

from src.graph_noise.states import zero_state, one_state, plus_state
from src.graph_noise.metrics import (
    state_fidelity,
    state_probabilities,
    total_variation_distance,
    bitstring_probabilities,
)


def test_fidelity_same_state():
    state = plus_state()
    fidelity = state_fidelity(state, state)

    assert np.isclose(fidelity, 1)


def test_fidelity_different_states():
    state_a = zero_state()
    state_b = one_state()

    fidelity = state_fidelity(state_a, state_b)

    assert np.isclose(fidelity, 0)


def test_state_probabilities():
    state = plus_state()
    probabilities = state_probabilities(state)

    assert np.allclose(probabilities, [0.5, 0.5])


def test_total_variation_distance():
    prob_a = np.array([1, 0])
    prob_b = np.array([0, 1])

    distance = total_variation_distance(prob_a, prob_b)

    assert np.isclose(distance, 1)


def test_bitstring_probabilities():
    state = plus_state()
    probabilities = bitstring_probabilities(state)

    assert np.isclose(probabilities["0"], 0.5)
    assert np.isclose(probabilities["1"], 0.5)