from django.views.generic import TemplateView


class SimulatorView(TemplateView):
    template_name = "savings/simulator.html"