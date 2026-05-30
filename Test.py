from src.graph_noise.simulation import run_benchmarks

results = run_benchmarks(repeats=10)

for row in results[:5]:
    print(row)