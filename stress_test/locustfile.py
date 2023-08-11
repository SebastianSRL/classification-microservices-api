from locust import HttpUser, between, task


class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    @task
    def index_page(self):
        self.client.get("/")

    @task
    def predict_page(self):
        self.client.post("/predict", files={"file": open("dog.jpeg", "rb")})
