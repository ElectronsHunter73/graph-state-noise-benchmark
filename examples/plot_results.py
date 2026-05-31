import csv
import os

import matplotlib.pyplot as plt


def read_csv_file(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["p"] = float(row["p"])
            row["fidelity"] = float(row["fidelity"])
            row["tvd"] = float(row["tvd"])
            data.append(row)

    return data


def get_names(data, column):
    names = []

    for row in data:
        if row[column] not in names:
            names.append(row[column])

    return names


def get_rows(data, benchmark, noise):
    rows = []

    for row in data:
        if row["benchmark"] == benchmark and row["noise"] == noise:
            rows.append(row)

    rows.sort(key=lambda row: row["p"])

    return rows


def plot_metric(data, benchmark, metric):
    noise_models = get_names(data, "noise")

    plt.figure()

    for noise in noise_models:
        rows = get_rows(data, benchmark, noise)

        x_values = []
        y_values = []

        for row in rows:
            x_values.append(row["p"])
            y_values.append(row[metric])

        plt.plot(x_values, y_values, marker="o", label=noise)

    plt.xlabel("Noise probability")
    plt.ylabel(metric)
    plt.title(benchmark + " " + metric)
    plt.legend()
    plt.grid(True)

    filename = "results/" + benchmark + "_" + metric + ".png"
    plt.savefig(filename)
    plt.close()


def main():
    filename = "results/benchmark_results.csv"

    if not os.path.exists(filename):
        print("Run examples/run_benchmarks.py first.")
        return

    os.makedirs("results", exist_ok=True)

    data = read_csv_file(filename)
    benchmarks = get_names(data, "benchmark")

    for benchmark in benchmarks:
        plot_metric(data, benchmark, "fidelity")
        plot_metric(data, benchmark, "tvd")

    print("Plots saved in results folder.")


main()