from falcon import API, MEDIA_JSON

from .api import init_api


def create_api() -> API:
    api = API(media_type=MEDIA_JSON)
    init_api(api)
    return api
