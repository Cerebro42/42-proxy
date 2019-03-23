from falcon import API

from .health import HealthResource


def init_api(api: API):
    api.add_route("/health", HealthResource)
