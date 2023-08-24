# SalesForecast API with mlforecast
Welcome to the Sales Forecast API repository! This project provides a Flask-based API for generating sales predictions using machine learning models from the `mlforecast` package. It's designed to help you quickly deploy and use sales forecasting models.

## Features
* Flask-based API for generating sales predictions.
* Supports various machine learning models from the `mlforecast` package for accurate forecasts.
* Interactive Jupyter Notebook for exploring, training, and evaluating models.


## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt.`
3. Make sure your trained machine learning models are saved in the model_pkl directory.
4. Start the Flask server by running: `python api.py.`
Jupyter Notebook (mlforecast.ipynb)
The mlforecast.ipynb notebook could explore, train, and evaluate machine learning models for sales forecasting. It covers various techniques and models, offering insights into model selection and evaluation. It could save the model result to csv to have a better comparison.

#### Data Preprocessing
Before using SalesForecast, you need to preprocess the data into a dictionary format and generate embeddings from text information. Follow these steps:

1. Open `mlforecast.ipynb`
2. Execute the notebook to preprocess the data and store the model in the model_pkl/ directory. This allows the API to load the model for predictions.


## API Documentation

Welcome to MlForecast API, a tool for making sales predictions using machine learning models. This API offers a prediction endpoint that takes input data and returns sales predictions based on trained machine learning models.

**Base URL:** `http://127.0.0.1:5000/`

### Endpoints

#### `POST /prediction`

- **Description:** Get sales predictions using machine learning models.
- **Request:**
  - `model` (str): Name of the machine learning model to use.
  - `data` (list of float): List of input data values.
  - `predict_length` (int): Number of periods to predict.
- **Response:**
```json
  {
    "prediction": [predicted_values]
  }
```
 
- **Example**:

  **Request:**

  ```json
  {
      "model": "A003_228644",
      "data": [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 5, 8, 2],
      "predict_length": 3
  }
  ```
  **Response:**

  ```json
  {
      "prediction": [
          19.67,
          19.61,
          19.77
      ]
  }
  ```

### Note
* Ensure all data is sent in JSON format for the `/prediction` endpoint.
* The server will respond with JSON data for the prediction request.
* The available machine learning models are loaded from the model_pkl directory and can be specified in the model field of the request.

## File Structure
* `api.py`: Contains the Flask web API for making sales predictions using machine learning models.
* `utils.py`: Provides utility functions for loading machine learning models from pickle files.
* `mlforecast.ipynb`: Jupyter Notebook for exploring, training, and evaluating machine learning models for sales forecasting. It can also save model results to CSV files for better comparison.
* `model_pkl/`: Directory to store trained machine learning models in pickle format.


## Relevant References
* [mlforecast Package GitHub Repository](https://github.com/nixtla/mlforecast): Scalable machine 🤖 learning for time series forecasting
* [Article: "Forecasting with Machine Learning Models" on Towards Data Science](https://towardsdatascience.com/forecasting-with-machine-learning-models-95a6b6579090)