# Graph State Noise Benchmark
![tests](https://github.com/ElectronsHunter73/graph-state-noise-benchmark/actions/workflows/tests.yml/badge.svg)

This is a small Python project for testing simple graph-state quantum states with basic noise models.

I made this project to practice graph states, simple quantum noise, and basic benchmark metrics. The simulation is written mostly with NumPy, without using Qiskit for the main part.

## What the project does

The project builds three graph states:

- Bell graph state
- 4-qubit star graph state
- 4-qubit line cluster state

Then it applies these noise models:

- bit-flip noise
- dephasing noise
- depolarizing noise
- measurement bit-flip noise

After that, it compares the ideal state and the noisy state using:

- fidelity
- total variation distance

The benchmark script runs all of these cases together in one batch and saves the results.

## Basic idea

A graph state starts with all qubits in the plus state.

Then the code applies a controlled-Z gate between qubits that are connected by an edge.

For example:

Bell graph:

0 --- 1

4-qubit line cluster:

0 --- 1 --- 2 --- 3

4-qubit star graph:

    1
    |
2 --0-- 3

## Project files

The main code is inside:

src/graph_noise/

The files are:

- states.py: creates basic quantum states like |0>, |1>, |+>, and multi-qubit states
- operators.py: contains quantum gates like Pauli gates, Hadamard, and controlled-Z
- operations.py: applies gates to selected qubits
- graphs.py: builds the graph states
- noise.py: contains the noise models
- metrics.py: calculates fidelity, probabilities, and total variation distance
- simulation.py: runs the benchmark logic

The examples folder contains:

- run_benchmarks.py: runs all benchmarks in one batch and saves the results
- plot_results.py: makes plots from the saved results

The tests folder contains basic tests for the project.

## Installation

Create a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

Install the needed packages:

pip install numpy matplotlib pytest

## How to run

Run the benchmark:

python examples/run_benchmarks.py

This saves the results here:

results/benchmark_results.csv

Then make the plots:

python examples/plot_results.py

Run the tests:

python -m pytest -v

## Example output

The benchmark prints results like this:

bell | bit_flip | p=0.0 | fidelity=1.0 | tvd=0.0  
bell | bit_flip | p=0.02 | fidelity=0.98 | tvd=0.0  
bell | bit_flip | p=0.05 | fidelity=0.91 | tvd=0.0  

The exact numbers can change because some of the noise models are random.

Sometimes the total variation distance stays close to zero. This can happen because the measurement probabilities may stay almost the same, even when the quantum state itself changes.

## Tests

The tests check simple things, such as:

- basic states are correct
- graph states have the expected size
- graph states are normalized
- noise with probability zero does not change the state
- metric functions give expected values

Run the tests with:

python -m pytest -v
