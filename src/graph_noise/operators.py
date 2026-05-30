import numpy as np


def identity():

    return np.array([[1, 0], [0, 1]], dtype=complex)

def pauli_x():
    return np.array([[0, 1], [1, 0]], dtype=complex)

def pauli_y():
    return np.array([[0, -1j], [1j, 0]], dtype=complex)

def pauli_z():
    return np.array([[1, 0], [0, -1]], dtype=complex)

def hadamard():
    return (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)

def cz():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, -1]], dtype=complex)

def tensor_product(*operators):
    if len(operators) == 0:
        raise ValueError("At least one operator must be provided.")
    result = operators[0]
    
    for operator in operators[1:]:
        result = np.kron(result, operator)
    
    return result
