from src.graph_noise.graphs import bell_graph_state
from src.graph_noise.metrics import state_fidelity, state_probabilities, bitstring_probabilities, qubit_count

state = bell_graph_state()

print(state_fidelity(state, state))
print(state_probabilities(state))
print(bitstring_probabilities(state))
print(qubit_count(state))