# Image Classification using TensorFlow: Web UI and Flask API for Automatic Image Categorization

![Alt text](System_architecture_diagram.png)

<p align="justify">
Imagine that you work for a company that has a large collection of images and needs to automatically classify them into different categories. This task can be time-consuming and error-prone when done manually by human workers.
</p>

<p align="justify">
Your task is develop a solution that can automatically classify images into over 1000 different categories using a Convolutional Neural Network (CNN) implemented in Tensorflow. Your solution will consist of a Web UI and a Python Flask API that serves the CNN.
</p>

<p align="justify">
The Web UI should allow users to upload an image and receive the predicted class for that image. The Python Flask API should receive the uploaded image, preprocess it (e.g. resize, normalize), feed it into the CNN, and return the predicted class as a JSON object. The API should handle errors gracefully and provide informative error messages to the UI if something goes wrong.
</p>



The technologies involved are:
- Docker
- docker-compose
- VS Code or any other IDE of your preference
- Linux subsystem for Windows (WSL2)
- Python is the main programming language
- Flask framework for the API
- HTML for the web UI
- Redis for the communication between microservices
- Tensorflow for loading the pre-trained CNN model
- Locust for doing the stress testing of your solution

## Installation

To run the services using compose:

Only for mac M1 users:
- There is dockerfile for M1 macs model/Dockerfile.M1. This docker file downloads tensoflow compiled for M1
- Change docker-compose.yaml to use that docker file.
- Remove tensorflow for requirements.txt
- Remember change back docker-compose.yaml and requirements.txt in the submission.

```bash
$ docker-compose up --build -d
```

To stop the services:

```bash
$ docker-compose down
```

## Tests

We provide unit tests along with the project that you can run and check from your side the code meets the minimum requirements for deployment. To run just execute:

### 1. Modules

We make use of [multi-stage docker builds](https://docs.docker.com/develop/develop-images/multistage-build/) so we can have into the same Dockerfile environments for testing and also for deploying our service.

#### 1.1. Api

Run:

```bash
$ cd api/
$ docker build -t flask_api_test --progress=plain --target test .
```

You will only need to pay attention to the logs corresponding to the testing code which will look like this:

```bash
#10 [test 1/1] RUN ["pytest", "-v", "/src/tests"]
#10 sha256:707efc0d59d04744766193fe6873d212afc0f8e4b28d035a2d2e94b40826604f
#10 0.537 ============================= test session starts ==============================
#10 0.537 platform linux -- Python 3.8.13, pytest-7.1.1, pluggy-1.0.0 -- /usr/local/bin/python
#10 0.537 cachedir: .pytest_cache
#10 0.537 rootdir: /src
#10 0.537 collecting ... collected 4 items
#10 0.748
#10 0.748 tests/test_api.py::TestIntegration::test_bad_parameters PASSED           [ 25%]
#10 0.757 tests/test_api.py::TestEnpointsAvailability::test_feedback PASSED        [ 50%]
#10 0.769 tests/test_api.py::TestEnpointsAvailability::test_index PASSED           [ 75%]
#10 0.772 tests/test_api.py::TestEnpointsAvailability::test_predict PASSED         [100%]
#10 0.776
#10 0.776 ============================== 4 passed in 0.24s ===============================
#10 DONE 0.8s
```

You are good if all tests are passing.

#### 1.2. Model

Same as api, run:

```bash
$ cd model/
$ docker build -t model_test --progress=plain --target test .
```

### 2. Integration end-to-end

You must have the full pipeline running (see previous section) and the following Python libraries installed:

- [requests==2.28.1](https://requests.readthedocs.io/en/latest/)
- [pytest==7.1.2](https://docs.pytest.org/en/7.1.x/)

You can install them using the file `tests/requirements.txt` with:

```bash
$ pip3 install -r tests/requirements.txt
```

Then, from the project root folder run:
```
$ python tests/test_integration.py
```

If the output looks like this, then the integration tests are passing:

```bash
.
----------------------------------------------------------------------
Ran 2 tests in 0.299s

OK
```
