# 🔐 Network Security — Phishing Website Detection

An end-to-end Machine Learning and MLOps project for detecting **phishing websites** using security-related website and URL features.

The project covers the complete ML lifecycle:

**Data Collection → MongoDB → Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation → MLflow/DagsHub Tracking → FastAPI → Prediction**

---

## 📌 Table of Contents

* [About the Project](#-about-the-project)
* [Problem Statement](#-problem-statement)
* [Project Objective](#-project-objective)
* [How the System Works](#-how-the-system-works)
* [Project Architecture](#-project-architecture)
* [Tech Stack](#-tech-stack)
* [Project Structure](#-project-structure)
* [Dataset](#-dataset)
* [MongoDB](#-mongodb)
* [Data Ingestion](#-data-ingestion)
* [Data Validation](#-data-validation)
* [Data Transformation](#-data-transformation)
* [Model Training](#-model-training)
* [Model Evaluation](#-model-evaluation)
* [MLflow and DagsHub](#-mlflow-and-dagshub)
* [FastAPI Application](#-fastapi-application)
* [Prediction Workflow](#-prediction-workflow)
* [Output](#-output)
* [Environment Variables](#-environment-variables)
* [Installation](#-installation)
* [How to Run the Project](#-how-to-run-the-project)
* [API Endpoints](#-api-endpoints)
* [Docker](#-docker)
* [AWS Deployment](#-aws-deployment)
* [Future Improvements](#-future-improvements)
* [Author](#-author)

---

# 📖 About the Project

**Network Security** is an end-to-end Machine Learning project designed to identify whether a website is potentially **phishing** or **legitimate** based on different security-related features.

The project is not only a Machine Learning model. It demonstrates how a machine learning system can be developed as a complete pipeline with:

* Data ingestion
* Data validation
* Data transformation
* Model training
* Model evaluation
* Model serialization
* Experiment tracking
* API development
* Prediction
* Output generation

The project also uses **MongoDB** for data storage and **MLflow with DagsHub** for experiment tracking and model-training monitoring.

---

# 🎯 Problem Statement

Phishing websites are designed to imitate legitimate websites and trick users into providing sensitive information.

The objective of this project is to build a Machine Learning system that can classify a website based on security-related features and predict whether it belongs to the phishing category.

The system takes structured feature data as input and produces a prediction.

### Prediction

The model produces a classification result such as:

```text
Phishing
```

or

```text
Legitimate
```

---

# 🎯 Project Objective

The main objectives of this project are:

1. Store and manage dataset information.
2. Build a reusable data ingestion pipeline.
3. Validate incoming data against a predefined schema.
4. Transform numerical and categorical data for Machine Learning.
5. Train multiple Machine Learning models.
6. Select the best-performing model.
7. Save the trained model and preprocessing object.
8. Track experiments using MLflow.
9. Track experiments remotely using DagsHub.
10. Expose the trained model through FastAPI.
11. Allow users to upload CSV data.
12. Generate predictions.
13. Save prediction results into a CSV file.
14. Display prediction results through an HTML template.

---

# 🔄 How the System Works

The complete workflow of the project is:

```text
                    ┌─────────────────┐
                    │     Dataset     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    MongoDB      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Ingestion  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Validation │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │Data Transformation│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Model Training  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Best ML Model   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
              ┌───────────┐    ┌──────────────┐
              │  MLflow   │    │   DagsHub    │
              └───────────┘    └──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   CSV Upload    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Prediction    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Prediction CSV  │
                    │ + HTML Table    │
                    └─────────────────┘
```

---

# 🏗️ Project Architecture

The project follows a modular Machine Learning pipeline architecture.

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Model Trainer
   ↓
Saved Model
   ↓
FastAPI Prediction API
```

The project separates different responsibilities into different components instead of keeping the entire Machine Learning workflow inside one Python file.

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Machine Learning

* NumPy
* Pandas
* Scikit-learn

## Data Processing

* Pandas
* NumPy
* Scikit-learn preprocessing

## Database

* MongoDB
* PyMongo

## API

* FastAPI
* Uvicorn

## Experiment Tracking

* MLflow
* DagsHub

## Frontend / Presentation

* HTML
* Jinja2 Templates

## Environment Management

* Python Virtual Environment
* `.env`

## Containerization

* Docker

## Deployment

* AWS — planned deployment stage

---

# 📁 Project Structure

The project follows a modular structure similar to:

```text
Network Security/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── networksecurity/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── constant/
│   │   └── training_pipeline/
│   │
│   ├── configuration/
│   │
│   ├── entity/
│   │
│   ├── exception/
│   │
│   ├── logging/
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   └── utils/
│       ├── main_utils/
│       └── ml_utlils/
│
├── config/
│   └── schema.yaml
│
├── Artifacts/
│   └── ...
│
├── final_models/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── predict_output/
│   └── output.csv
│
└── templates/
    └── table.html
```

> The exact contents of generated `Artifacts` directories can change between pipeline runs because artifact paths are generated during execution.

---

# 📊 Dataset

The dataset contains features related to website and URL characteristics that can be used to identify phishing websites.

Examples of features include:

```text
having_IP_Address
URL_Length
Shortining_Service
SSLfinal_State
Google_Index
...
```

The target column used by the training pipeline is:

```text
Result
```

The dataset is processed through the complete pipeline before being used for model training.

---

# 🗄️ MongoDB

MongoDB is used as the database layer for storing the dataset.

The application connects to MongoDB using the connection URL stored in an environment variable.

The project uses:

```text
MONGO_DB_URL
```

The database and collection names are defined through the project's training-pipeline constants.

MongoDB is used as part of the data ingestion workflow before the data enters the Machine Learning pipeline.

---

# 📥 Data Ingestion

The **Data Ingestion** component is responsible for obtaining the dataset and creating the train/test datasets required by the next pipeline stages.

The ingestion stage produces a `DataIngestionArtifact`.

The artifact contains paths for:

```text
train_data_path
test_data_path
row_data_path
```

The generated files are stored under the project's artifact directory.

Example:

```text
Artifacts/
└── <timestamp>/
    └── DataIngestion/
        ├── train.csv
        └── test.csv
```

The exact generated directory can vary based on the execution timestamp.

---

# ✅ Data Validation

The Data Validation component checks whether the ingested data follows the expected schema.

The schema configuration is maintained in:

```text
config/schema.yaml
```

The validation process checks the structure of the dataset before allowing it to continue through the pipeline.

The component generates a `DataValidationArtifact`.

The artifact contains information such as:

```text
validation_status
validation_train_file_path
valid_test_file_path
invalid_train_file_path
invalid_test_file_path
drift_report_file_path
```

A successful validation produces:

```text
validation_status=True
```

This prevents invalid or unexpected data from directly entering the transformation and training stages.

---

# 🔄 Data Transformation

The Data Transformation component prepares the validated data for Machine Learning.

The transformation process includes preprocessing of the input features.

The project uses Scikit-learn preprocessing techniques such as:

* `SimpleImputer`
* `StandardScaler`
* categorical feature encoding

The transformed data is then converted into a format suitable for model training.

The preprocessing object is saved so that the **same transformation used during training can also be used during prediction**.

The saved preprocessing object is:

```text
final_models/preprocessor.pkl
```

This is important because the prediction API must apply the same preprocessing pipeline to new input data.

---

# 🤖 Model Training

The Model Trainer component trains Machine Learning models using the transformed training data.

The training pipeline evaluates candidate models and selects the best-performing model according to the project's model evaluation logic.

The final trained model is saved as:

```text
final_models/model.pkl
```

The trained preprocessing pipeline is saved as:

```text
final_models/preprocessor.pkl
```

Therefore, the prediction system requires both:

```text
model.pkl
preprocessor.pkl
```

---

# 📈 Model Evaluation

Model evaluation is performed during the model training stage to determine the performance of the trained models.

The objective is to identify a suitable model for the phishing website classification problem.

The selected model is then serialized and stored for later inference.

---

# 📊 MLflow and DagsHub

MLflow is used for **experiment tracking**.

DagsHub is used as the remote platform for MLflow tracking.

The project is connected to:

```text
DagsHub
```

Repository owner:

```text
MDSalman22415
```

Repository:

```text
NetwokSecurity
```

The DagsHub initialization is:

```python
import mlflow
import dagshub

dagshub.init(
    repo_owner="MDSalman22415",
    repo_name="NetwokSecurity",
    mlflow=True
)
```

This allows training runs and MLflow experiment information to be tracked remotely.

The project previously used local SQLite-based MLflow tracking, but the current configuration uses DagsHub instead.

### Current MLflow Architecture

```text
Model Training
      ↓
    MLflow
      ↓
    DagsHub
      ↓
Remote Experiment Tracking
```

MLflow warnings such as:

```text
artifact_path is deprecated
```

are warnings from the MLflow API and do not indicate that model training has failed.

---

# 🚀 FastAPI Application

The project exposes the trained Machine Learning model through FastAPI.

The main API application is:

```text
app.py
```

The FastAPI application provides the following routes.

---

## 🏠 Home Route

```http
GET /
```

The root route redirects the user to the FastAPI Swagger documentation.

```text
/
 ↓
/docs
```

---

## 📚 Swagger Documentation

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

This can be used to test the API endpoints.

---

# 🏋️ Training API

The training endpoint is:

```http
GET /train
```

When called, it creates a `TrainingPipeline` object and executes:

```python
train_pipeline.run_pipeline()
```

The complete training pipeline is therefore triggered through the API.

A successful request returns:

```text
Training is successful
```

---

# 🔮 Prediction API

The prediction endpoint is:

```http
POST /predict
```

The endpoint accepts a CSV file.

The CSV file is read using Pandas:

```python
df = pd.read_csv(file.file)
```

The API then loads:

```text
final_models/preprocessor.pkl
final_models/model.pkl
```

The model and preprocessing object are combined through the project's `NetworkModel` utility.

The prediction is generated using:

```python
y_pred = network_model.predict(df)
```

The predictions are added to the uploaded dataframe:

```python
df["predicted_column"] = y_pred
```

---

# 🔁 Prediction Workflow

The prediction process is:

```text
User
 │
 │ Upload CSV
 ▼
FastAPI /predict
 │
 ▼
Read CSV with Pandas
 │
 ▼
Load preprocessor.pkl
 │
 ▼
Load model.pkl
 │
 ▼
Transform input data
 │
 ▼
Generate prediction
 │
 ▼
Add predicted_column
 │
 ├───────────────┐
 ▼               ▼
output.csv     HTML Table
```

---

# 📄 Prediction Output

Prediction results are stored inside:

```text
predict_output/
```

The generated file is:

```text
predict_output/output.csv
```

The application creates the directory automatically if it does not exist:

```python
os.makedirs("predict_output", exist_ok=True)
```

The prediction column is:

```text
predicted_column
```

The API also converts the dataframe into an HTML table and displays it using:

```text
templates/table.html
```

---

# 🌐 HTML Template

The prediction result is rendered using the Jinja2 template:

```text
templates/table.html
```

The dataframe is converted to HTML using:

```python
table_html = df.to_html(classes="table table-striped")
```

The generated table is then passed to the template.

---

# 🔐 Environment Variables

The project uses environment variables for configuration values.

Create a `.env` file in the project root.

Example:

```env
MONGO_DB_URL=your_mongodb_connection_string
```

The application loads environment variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

The MongoDB URL is retrieved using:

```python
mongo_db_url = os.getenv("MONGO_DB_URL")
```

### Important

Do not commit the `.env` file to GitHub.

Add it to:

```text
.gitignore
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Network-Security
```

---

## 2. Create Virtual Environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

The project uses dependencies including:

```text
pandas
numpy
scikit-learn
pymongo
fastapi
uvicorn
python-multipart
jinja2
python-dotenv
mlflow
dagshub
certifi
```

The complete dependency list should be taken from the project's `requirements.txt`.

---

# ▶️ How to Run the Project

There are two primary ways to work with the project:

### Option 1 — Run the training pipeline directly

The project's training pipeline can be executed through the corresponding pipeline entry point.

### Option 2 — Run FastAPI

Start the FastAPI application with:

```powershell
uvicorn app:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

# 🧪 Run Training

Open:

```text
http://127.0.0.1:8000/train
```

or use the Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Execute:

```http
GET /train
```

The training pipeline runs through:

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Saving
      ↓
MLflow / DagsHub Tracking
```

---

# 🔮 Run Prediction

Start the FastAPI server:

```powershell
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
POST /predict
```

Click:

```text
Try it out
```

Upload a CSV file containing the expected input features.

Then execute the request.

The system will:

1. Read the uploaded CSV.
2. Load the saved preprocessor.
3. Load the trained model.
4. Transform the input.
5. Generate predictions.
6. Add the prediction column.
7. Save the output CSV.
8. Render the result as an HTML table.

---

# 📌 Important Generated Files

After successful training, important model files include:

```text
final_models/
├── model.pkl
└── preprocessor.pkl
```

Prediction output:

```text
predict_output/
└── output.csv
```

Pipeline artifacts:

```text
Artifacts/
└── <timestamp>/
    └── ...
```

---

# 🐳 Docker

The project can also be containerized using Docker.

A typical Docker workflow is:

```text
Source Code
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Docker Container
    ↓
FastAPI Application
```

Build the image:

```bash
docker build -t network-security .
```

Run the container:

```bash
docker run -p 8000:8000 network-security
```

The API can then be accessed through:

```text
http://localhost:8000
```

The exact Docker configuration should follow the project's current `Dockerfile`.

---

# ☁️ AWS Deployment

AWS deployment is the next stage of the project.

The purpose of AWS deployment is to make the trained Machine Learning API available from a remote server instead of only running it locally.

The deployment architecture can be:

```text
User
  ↓
Internet
  ↓
AWS EC2
  ↓
Docker Container
  ↓
FastAPI
  ↓
ML Model
  ↓
Prediction
```

A practical deployment approach for this project is:

```text
Docker
  ↓
AWS EC2
  ↓
Run FastAPI container
```

AWS deployment is not required for the Machine Learning model itself. It is the production/deployment stage that makes the API accessible outside the local development environment.

---

# 🔮 Future Improvements

Possible future improvements include:

* Deploy the FastAPI application on AWS.
* Add a simple user-facing frontend.
* Add URL-based prediction instead of only CSV upload.
* Improve prediction result presentation.
* Add more monitoring.
* Add automated CI/CD.
* Add model versioning.
* Add additional security checks.
* Improve API authentication and authorization.
* Add production logging and monitoring.

---

# 🧩 Complete Project Flow

The complete project can be summarized as:

```text
                    NETWORK SECURITY
                           │
                           ▼
                  Phishing Detection
                           │
                           ▼
                    Dataset / MongoDB
                           │
                           ▼
                    Data Ingestion
                           │
                           ▼
                    Data Validation
                           │
                           ▼
                  Data Transformation
                           │
                           ▼
                    Model Training
                           │
                           ▼
                     Best Model
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
          MLflow                       Model
             │                           │
          DagsHub                       │
                                         ▼
                                    FastAPI API
                                         │
                                         ▼
                                    CSV Upload
                                         │
                                         ▼
                                     Prediction
                                         │
                           ┌─────────────┴─────────────┐
                           ▼                           ▼
                     output.csv                  HTML Table
```

---

# 💡 What This Project Demonstrates

This project demonstrates practical experience with an end-to-end Machine Learning system rather than only training a model in a notebook.

It covers:

* Python development
* Machine Learning
* Data preprocessing
* Data validation
* Database integration
* Modular ML architecture
* Model training
* Model serialization
* Experiment tracking
* MLflow
* DagsHub
* FastAPI
* REST API development
* CSV-based inference
* HTML template rendering
* Docker
* Cloud deployment preparation

---

# 👨‍💻 Author

**MD Salman**

BCA — Computer Applications
Mewar University

---

# ⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.
