import numpy as np

def state_fidelity(state_a, state_b):
    if len(state_a) != len(state_b):
        raise ValueError("States must have the same size.")

    norm_a = np.linalg.norm(state_a)
    norm_b = np.linalg.norm(state_b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("State cannot be zero.")

    state_a = state_a / norm_a
    state_b = state_b / norm_b

    overlap = np.vdot(state_a, state_b)

    return float(abs(overlap) ** 2)


def state_probabilities(state):
    probabilities = np.abs(state) ** 2
    total = np.sum(probabilities)

    if total == 0:
        raise ValueError("State cannot be zero.")

    return probabilities / total


def total_variation_distance(prob_a, prob_b):
    if len(prob_a) != len(prob_b):
        raise ValueError("Probability lists must have the same size.")

    distance = 0

    for i in range(len(prob_a)):
        distance += abs(prob_a[i] - prob_b[i])

    return 0.5 * distance


def bitstring_probabilities(state):
    probabilities = state_probabilities(state)
    num_qubits = int(np.log2(len(state)))

    result = {}

    for i in range(len(probabilities)):
        bitstring = format(i, f"0{num_qubits}b")
        result[bitstring] = float(probabilities[i])

    return result


def qubit_count(state):
    num_qubits = int(np.log2(len(state)))

    if 2 ** num_qubits != len(state):
        raise ValueError("State size must be a power of 2.")

    return num_qubits


def edge_count(edges):
    return len(edges)