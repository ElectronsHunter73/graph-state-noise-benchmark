from .simulation import get_benchmarks, run_one_setting


def run_web_benchmark(graph_type, noise_model, noise_probability, repeats=100):
    """
    Run one graph-state noise benchmark from the Django interface.
    """

    benchmarks = get_benchmarks()

    selected_benchmark = None

    for benchmark in benchmarks:
        if benchmark["name"] == graph_type:
            selected_benchmark = benchmark
            break

    if selected_benchmark is None:
        raise ValueError(f"Unknown graph type: {graph_type}")

    result = run_one_setting(
        benchmark=selected_benchmark,
        noise_name=noise_model,
        p=noise_probability,
        repeats=repeats,
    )

    return result