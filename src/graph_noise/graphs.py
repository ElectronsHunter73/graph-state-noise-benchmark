from .states import n_qubit_plus_state
from .operators import cz
from .operations import apply_two_qubit_gate

def graph_state(num_qubits, edges):
    if num_qubits < 1:
        raise ValueError("Number of qubits must be at least 1.")
    state = n_qubit_plus_state(num_qubits)
    for edge in edges:
        state = apply_two_qubit_gate(state, cz(), edge[0], edge[1])
        return state
def bell_graph_state():
    return graph_state(2, [(0, 1)])

def line_graph_state(num_qubits):
    edges=[]
    for i in range(num_qubits-1):
        edges.append((i,i+1))
        return graph_state(num_qubits,edges)
    
def four_qubit_cluster_state():
    return line_graph_state(4)

def star_graph_state(num_qubits):
    if num_qubits < 2:
        raise ValueError("Number of qubits must be at least 2.")
    edges=[]
    for i in range(1,num_qubits):
        edges.append((0,i))
    return graph_state(num_qubits,edges)

def get_line_edges(num_qubits):
    edges = []

    for i in range(num_qubits - 1):
        edges.append((i, i + 1))

    return edges


def get_star_edges(num_qubits):
    edges = []

    for i in range(1, num_qubits):
        edges.append((0, i))

    return edges