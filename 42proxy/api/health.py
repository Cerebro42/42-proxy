class HealthResource:
    def on_get(self, resp):
        resp.media = {"alive": "true"}

