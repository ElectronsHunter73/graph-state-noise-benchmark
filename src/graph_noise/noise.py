import numpy as np
from .operators import pauli_x, pauli_y, pauli_z
from .operations import apply_one_qubit_gate, get_num_qubits

def check_probability(p):
    if p < 0 or p > 1:
        raise ValueError("Probability must be between 0 and 1.")


def bit_flip_noise(state, p):
    check_probability(p)
    noisy_state = state.copy()
    num_qubits = get_num_qubits(state)
    for qubit in range(num_qubits):
        if np.random.random() < p:
            noisy_state = apply_one_qubit_gate(noisy_state, pauli_x(), qubit)

    return noisy_state

def dephasing_noise(state, p):
    check_probability(p)
    noisy_state = state.copy()
    num_qubits = get_num_qubits(state)

    for qubit in range(num_qubits):
        if np.random.random() < p:
            noisy_state = apply_one_qubit_gate(noisy_state, pauli_z(), qubit)

    return noisy_state


def depolarizing_noise(state, p):
    check_probability(p)
    noisy_state = state.copy()
    num_qubits = get_num_qubits(state)
    gates = [pauli_x(), pauli_y(), pauli_z()]

    for qubit in range(num_qubits):
        if np.random.random() < p:
            gate_number = np.random.randint(0, 3)
            noisy_state = apply_one_qubit_gate(noisy_state, gates[gate_number], qubit)
    return noisy_state


def bitstring_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1

    return distance


def measurement_bit_flip_noise(probabilities, p):
    check_probability(p)
    size = len(probabilities)
    num_qubits = int(np.log2(size))
    if 2 ** num_qubits != size:
        raise ValueError("Probability vector size must be a power of 2.")
    
    noisy_probabilities = np.zeros(size)
    for old_index in range(size):
        old_bits = format(old_index, "0" + str(num_qubits) + "b")

        for new_index in range(size):
            new_bits = format(new_index, "0" + str(num_qubits) + "b")
            distance = bitstring_distance(old_bits, new_bits)

            prob = (p ** distance) * ((1 - p) ** (num_qubits - distance))
            noisy_probabilities[new_index] += probabilities[old_index] * prob

    return noisy_probabilities


def apply_noise(state, noise_name, p):
    if noise_name == "bit_flip":
        return bit_flip_noise(state, p)

    if noise_name == "dephasing":
        return dephasing_noise(state, p)

    if noise_name == "depolarizing":
        return depolarizing_noise(state, p)

    raise ValueError("Unknown noise model.")