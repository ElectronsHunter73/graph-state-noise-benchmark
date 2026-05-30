import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.graph_noise.simulation import run_benchmarks


def save_results(results, filename):
    if len(results) == 0:
        return

    folder = os.path.dirname(filename)

    if folder != "":
        os.makedirs(folder, exist_ok=True)

    columns = list(results[0].keys())

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for row in results:
            writer.writerow(row)


def print_results(results):
    for row in results:
        text = (
            row["benchmark"]
            + " | "
            + row["noise"]
            + " | p="
            + str(row["p"])
            + " | fidelity="
            + str(round(row["fidelity"], 4))
            + " | tvd="
            + str(round(row["tvd"], 4))
        )

        print(text)


def main():
    noise_values = [0.0, 0.02, 0.05, 0.1, 0.2]

    results = run_benchmarks(
        noise_values=noise_values,
        repeats=100,
    )

    print_results(results)
    save_results(results, "results/benchmark_results.csv")

    print("")
    print("Saved results to results/benchmark_results.csv")


if __name__ == "__main__":
    main()