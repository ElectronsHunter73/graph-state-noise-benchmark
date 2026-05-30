import numpy as np

def get_num_qubits(state):
    if np.log2(state.size) % 1 != 0:
        raise ValueError("State vector size must be a power of 2.")
    return int(np.log2(state.size))

def index_to_bitstring(index, num_qubits):
    if index < 0 or index >= 2**num_qubits:
        raise ValueError("Index out of range for the given number of qubits.")
    return format(index, '0' + str(num_qubits) + 'b')

def bitstring_to_index(bitstring):
    return int(bitstring, 2)

def apply_one_qubit_gate(state, gate, target):
    num_qubits=get_num_qubits(state)
    if gate.shape != (2, 2):
        raise ValueError("Gate must be a 2x2 matrix.")
    
    if target < 0 or target >= num_qubits:
        raise ValueError("Target qubit index out of range.")
    
    new_state=np.zeros(len(state),dtype=complex)
    for old_index in range(len(state)):
        amplitude=state[old_index]
        bitstring=index_to_bitstring(old_index,num_qubits)
        old_bit=int(bitstring[target])
        for new_bit in [0,1]:
            bits=list(bitstring)
            bits[target]=str(new_bit)
            new_bitstring=''.join(bits)
            new_index=bitstring_to_index(new_bitstring)
            new_state[new_index]=new_state[new_index]+gate[new_bit,old_bit]*amplitude
    return new_state

def apply_two_qubit_gate(state, gate, qubit_a, qubit_b):
    num_qubits = get_num_qubits(state)
    if gate.shape != (4, 4):
        raise ValueError("Gate must be 4x4.")
    
    if qubit_a == qubit_b:
        raise ValueError("The two qubits must be different.")
    
    if qubit_a < 0 or qubit_a >= num_qubits:
        raise ValueError("qubit_a does not exist.")
    
    if qubit_b < 0 or qubit_b >= num_qubits:
        raise ValueError("qubit_b does not exist.")
    
    new_state = np.zeros(len(state), dtype=complex)
    for old_index in range(len(state)):
        amplitude = state[old_index]
        bitstring = index_to_bitstring(old_index, num_qubits)
        old_bit_a = int(bitstring[qubit_a])
        old_bit_b = int(bitstring[qubit_b])
        old_gate_index = 2 * old_bit_a + old_bit_b
 
        for new_bit_a in [0, 1]:
            for new_bit_b in [0, 1]:
                bits = list(bitstring)
                bits[qubit_a] = str(new_bit_a)
                bits[qubit_b] = str(new_bit_b)
                new_bitstring = "".join(bits)
                new_index = bitstring_to_index(new_bitstring)
                new_gate_index = 2 * new_bit_a + new_bit_b
                new_state[new_index] = new_state[new_index] + gate[new_gate_index, old_gate_index] * amplitude

    return new_state