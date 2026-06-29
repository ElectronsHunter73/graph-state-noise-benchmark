from django.shortcuts import render

from .forms import BenchmarkForm
from graph_noise.web_runner import run_web_benchmark


def home(request):
    result = None
    error_message = None

    if request.method == "POST":
        form = BenchmarkForm(request.POST)

        if form.is_valid():
            graph_type = form.cleaned_data["graph_type"]
            noise_model = form.cleaned_data["noise_model"]
            noise_probability = form.cleaned_data["noise_probability"]
            repeats = form.cleaned_data["repeats"]
            try:
                result = run_web_benchmark(
                    graph_type=graph_type,
                    noise_model=noise_model,
                    noise_probability=noise_probability,
                    repeats=repeats,
                )
            except ValueError as error:
                error_message = str(error)
    else:
        form = BenchmarkForm()

    return render(
        request,
        "benchmark_ui/home.html",
        {
            "form": form,
            "result": result,
            "error_message": error_message,
        },
    )