from src.graph_noise.states import computational_basis_state
from src.graph_noise.operators import pauli_x, cz
from src.graph_noise.operations import apply_one_qubit_gate, apply_two_qubit_gate

state = computational_basis_state("00")
print(apply_one_qubit_gate(state, pauli_x(), target=1))

state = computational_basis_state("11")
print(apply_two_qubit_gate(state, cz(), 0, 1))