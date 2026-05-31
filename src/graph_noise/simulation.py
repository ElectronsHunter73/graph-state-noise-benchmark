import numpy as np

from .graphs import (
    bell_graph_state,
    star_graph_state,
    four_qubit_cluster_state,
    get_star_edges,
    get_line_edges,
)

from .metrics import (
    state_fidelity,
    state_probabilities,
    total_variation_distance,
)

from .noise import apply_noise, measurement_bit_flip_noise


def get_benchmarks():
    benchmarks = []

    benchmarks.append({
        "name": "bell",
        "state": bell_graph_state(),
        "edges": [(0, 1)],
    })

    benchmarks.append({
        "name": "star_4",
        "state": star_graph_state(4),
        "edges": get_star_edges(4),
    })

    benchmarks.append({
        "name": "cluster_4",
        "state": four_qubit_cluster_state(),
        "edges": get_line_edges(4),
    })

    return benchmarks


def run_state_noise_once(state, noise_name, p):
    ideal_probabilities = state_probabilities(state)

    noisy_state = apply_noise(state, noise_name, p)
    noisy_probabilities = state_probabilities(noisy_state)

    fidelity = state_fidelity(state, noisy_state)
    tvd = total_variation_distance(ideal_probabilities, noisy_probabilities)

    return fidelity, tvd


def run_measurement_noise_once(state, p):
    ideal_probabilities = state_probabilities(state)
    noisy_probabilities = measurement_bit_flip_noise(ideal_probabilities, p)

    fidelity = 1.0
    tvd = total_variation_distance(ideal_probabilities, noisy_probabilities)

    return fidelity, tvd


def run_one_setting(benchmark, noise_name, p, repeats):
    fidelities = []
    tvds = []

    state = benchmark["state"]

    for i in range(repeats):
        if noise_name == "measurement_bit_flip":
            fidelity, tvd = run_measurement_noise_once(state, p)
        else:
            fidelity, tvd = run_state_noise_once(state, noise_name, p)

        fidelities.append(fidelity)
        tvds.append(tvd)

    result = {
        "benchmark": benchmark["name"],
        "noise": noise_name,
        "p": p,
        "fidelity": float(np.mean(fidelities)),
        "tvd": float(np.mean(tvds)),
        "qubits": int(np.log2(len(state))),
        "edges": len(benchmark["edges"]),
        "depth": len(benchmark["edges"]),
    }

    return result


def run_benchmarks(noise_values=None, repeats=100):
    if noise_values is None:
        noise_values = [0.0, 0.02, 0.05, 0.1, 0.2]

    noise_models = [
        "bit_flip",
        "dephasing",
        "depolarizing",
        "measurement_bit_flip",
    ]

    benchmarks = get_benchmarks()
    results = []

    for benchmark in benchmarks:
        for noise_name in noise_models:
            for p in noise_values:
                result = run_one_setting(benchmark, noise_name, p, repeats)
                results.append(result)

    return results