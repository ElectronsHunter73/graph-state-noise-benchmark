import numpy as np
def zero_state(): 
    return np.array([1,0],dtype=complex)

def one_state():
    return np.array([0,1],dtype=complex)

def plus_state():
    return (zero_state()+one_state())/np.sqrt(2)

def minus_state():
    return (zero_state()-one_state())/np.sqrt(2)

def tensor_product_state(*states):
    if len(states) == 0:
        raise ValueError("At least one state must be provided.")
    result = states[0]
    for state in states[1:]:
        result = np.kron(result, state)
    return result

def computational_basis_state(bitstring):
    states=[]
    for bit in bitstring:
        if bit == '0':
            states.append(zero_state())
        elif bit == '1':
            states.append(one_state())
        else:
            raise ValueError("Bitstring must consist of '0' and '1' characters only.")
    return tensor_product_state(*states)

def n_qubit_plus_state(n):
    if n < 1:
        raise ValueError("Number of qubits must be at least 1.")
    plus = plus_state()
    return tensor_product_state(*[plus]*n) 
def normalize(state):
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return state / norm