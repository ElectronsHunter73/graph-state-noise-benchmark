import numpy as np

from src.graph_noise.graphs import (
    bell_graph_state,
    star_graph_state,
    four_qubit_cluster_state,
    get_star_edges,
    get_line_edges,
)


def test_bell_graph_state_size():
    state = bell_graph_state()

    assert len(state) == 4
    assert np.isclose(np.linalg.norm(state), 1)


def test_star_graph_state_size():
    state = star_graph_state(4)

    assert len(state) == 16
    assert np.isclose(np.linalg.norm(state), 1)


def test_cluster_graph_state_size():
    state = four_qubit_cluster_state()

    assert len(state) == 16
    assert np.isclose(np.linalg.norm(state), 1)


def test_star_edges():
    edges = get_star_edges(4)

    assert edges == [(0, 1), (0, 2), (0, 3)]


def test_line_edges():
    edges = get_line_edges(4)

    assert edges == [(0, 1), (1, 2), (2, 3)]