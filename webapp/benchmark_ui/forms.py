from django import forms


class BenchmarkForm(forms.Form):
    GRAPH_CHOICES = [
        ("bell", "Bell graph state"),
        ("star_4", "4-qubit star/GHZ graph state"),
        ("cluster_4", "4-qubit cluster state"),
    ]

    NOISE_CHOICES = [
        ("bit_flip", "Bit-flip noise"),
        ("dephasing", "Dephasing noise"),
        ("depolarizing", "Depolarizing noise"),
        ("measurement_bit_flip", "Measurement bit-flip noise"),
    ]

    graph_type = forms.ChoiceField(choices=GRAPH_CHOICES)
    noise_model = forms.ChoiceField(choices=NOISE_CHOICES)
    noise_probability = forms.FloatField(
        min_value=0.0,
        max_value=1.0,
        initial=0.05,
        help_text="Choose a value between 0 and 1.",
    )
    repeats = forms.IntegerField(
        min_value=1,
        max_value=1000,
        initial=100,
        help_text="Number of repeated runs.",
    )
    