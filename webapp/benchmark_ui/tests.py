from django.test import TestCase
from django.urls import reverse


class BenchmarkUITests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Graph-State Noise Benchmark")

    def test_form_submission_returns_results(self):
        response = self.client.post(
            reverse("home"),
            {
                "graph_type": "bell",
                "noise_model": "bit_flip",
                "noise_probability": 0.05,
                "repeats": 10,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Results")
        self.assertContains(response, "Fidelity")
        self.assertContains(response, "Total variation distance")