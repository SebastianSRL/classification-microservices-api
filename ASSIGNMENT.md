# Sprint project 03: Instructions
> Flask ML API

## Part 1 - Building the basic service

In this project, we will code and deploy an API for serving our own machine learning models. For this particular case, it will be a Convolutional Neural network for images. You don't need to fully understand how this model works because we will see that in detail later. For now, you can check how to use this model in the notebook [14 - THEORY - CNN Example Extra Material.ipynb](https://drive.google.com/file/d/1ADuBSE4z2ZVIdn66YDSwxKv-58U7WEOn/view?usp=sharing).

The project structure is already defined and you will see the modules already have some code and comments to help you get started.

Below is the full project structure:

```
├── api
│   ├── Dockerfile
│   ├── app.py
│   ├── middleware.py
│   ├── views.py
│   ├── settings.py
│   ├── utils.py
│   ├── templates
│   │   └── index.html
│   └── tests
│       ├── test_api.py
│       └── test_utils.py
├── model
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── settings.py
│   └── tests
│       └── test_model.py
├── stress_test
│   └── locustfile.py
├── docker-compose.yml
├── README.md
└── tests
    └── test_integration.py
```

Let's take a quick overview of each module:

- api: It has all the needed code to implement the communication interface between the users and our service. It uses Flask and Redis to queue tasks to be processed by our machine learning model.
    - `api/app.py`: Setup and launch our Flask api.
    - `api/views.py`: Contains the API endpoints. You must implement the following endpoints:
        - *upload_image*: Displays a frontend in which the user can upload an image and get a prediction from our model.
        - *predict*: POST method which receives an image and sends back the model prediction. This endpoint is useful for integration with other services and platforms given we can access it from any other programming language.
        - *feedback*: Endpoint used to get feedback from users when the prediction from our model is incorrect.
    - `api/utils.py`: Implements some extra functions used internally by our api.
    - `api/settings.py`: It has all the API settings.
    - `api/templates`: Here we put the .html files used in the frontend.
    - `api/tests`: Test suite.
- model: Implements the logic to get jobs from Redis and process them with our Machine Learning model. When we get the predicted value from our model, we must encode it on Redis again so it can be delivered to the user.
    - `model/ml_service.py`: Runs a thread in which it gets jobs from Redis, processes them with the model, and returns the answers.
    - `model/settings.py`: Settings for our ML model.
    - `model/tests`: Test suite.
- tests: This module contains integration tests so we can properly check our system's end-to-end behavior is expected.

Your task will be to complete the corresponding code on those parts it's required across all the modules. You can validate it's working as expected using the already provided tests. We encourage you to also write extra test cases as needed.

You can also take a look at the file `System_architecture_diagram.png` to have a graphical description of the microservices and how the communication is performed.

### Recommended way to work across all those files

Our recommendation for you about the order in which you should complete these files is the following:

#### 1. `model` folder

Inside this module, complete:

1. `predict()` function under `model/ml_service.py` file. Then run the tests corresponding to this module and check if they are passing correctly.
2. Then, go for the `classify_process()` function also under `model/ml_service.py` file.

#### 2. `api` folder

Inside this module, complete:

1. `allowed_file()` function under `api/utils.py` file.
2. `feedback()` function under `api/views.py` file. The `/feedback` endpoint will allow API users report when a model prediction is wrong. You will have to store the reported image path and the model prediction to a plain text file inside the folder `/src/feedback` so we can access later to check those cases in which our Machine Learning model failed according to users.

Now run the tests corresponding to this module and check if they are passing correctly.

3. `model_predict()` function under `api/middleware.py` file. This will allow to communicate the API with our ML service.

## Part 2 - Stress testing with *Locust*

For this task, you must complete the file `locustfile.py` from the `stress_test` folder. Make sure to create at least one test for:
- `index` endpoint.
- `predict` endpoint.

### Test scaled services

You can easily launch more instances for a particular service using `--scale SERVICE=NUM` when running `docker-compose up` command (see [here](https://docs.docker.com/compose/reference/up/)). Scale `model` service to 2 or even more instances and check the performance with locust.

Write a short report detailing the hardware specs from the server used to run the service and show a comparison in the results obtained for a different number of users being simulated and instances deployed.

## [Optional] Part 3 - Batch processing

Replace the current model behavior to process the jobs in batches. Check if that improves the numbers when doing stress testing.
