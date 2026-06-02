#  DocuMind – Autonomous Agentic AI Orchestrator for Data Science

##  Overview

DocuMind is an Agentic AI-powered Data Science Assistant that automates the end-to-end machine learning workflow using a multi-agent architecture.

Users can upload a dataset, and DocuMind automatically:

* Profiles the dataset
* Detects the ML task
* Recommends suitable models
* Trains and evaluates models
* Generates explainability insights
* Retrieves domain knowledge
* Produces executive reports
* Provides deployment recommendations

The system combines traditional machine learning pipelines with LLM-powered knowledge enhancement to assist both technical and non-technical users.

---

##  Problem Statement

Data science workflows often require multiple tools and significant manual effort for:

* Dataset analysis
* Model selection
* Training
* Evaluation
* Reporting
* Knowledge retrieval

DocuMind addresses this challenge through an autonomous multi-agent system that orchestrates the entire workflow from data upload to executive reporting.

---

## 🏗️ Architecture

```text
Dataset Upload
       │
       ▼
Data Profiling Agent
       │
       ▼
Task Detection Agent
(Classification / Regression / Clustering / Time Series)
       │
       ▼
Knowledge Agent
       │
       ▼
Groq LLM Agent
       │
       ▼
Model Recommendation Agent
       │
       ▼
Training Agent
       │
       ▼
Evaluation Agent
       │
       ▼
Explainability Agent
       │
       ▼
Executive Report Generator
       │
       ▼
Download Report Agent
```

---

## 🤖 Implemented Agents

### 1. Profiler Agent

* Dataset profiling
* Shape analysis
* Missing value analysis
* Feature inspection

### 2. Task Detection Agent

Automatically detects:

* Classification
* Regression

### 3. Task Override Agent

Allows manual selection of:

* Classification
* Regression
* Clustering
* Time Series

### 4. Knowledge Agent

Provides domain-specific ML knowledge.

### 5. Groq LLM Agent

Enhances retrieved knowledge using:

* Llama 3.1 8B Instant
* Groq API

### 6. Recommendation Agent

Suggests appropriate ML models based on task type.

### 7. Training Agent

Supports:

* Random Forest Classifier
* Logistic Regression
* Random Forest Regressor
* Linear Regression
* XGBoost Models

### 8. Evaluation Agent

Evaluates models using:

* Accuracy
* F1 Score
* R² Score

### 9. Explainability Agent

Generates business-friendly explanations.

### 10. Feature Importance Agent

Identifies the most influential features.

### 11. Clustering Agent

Implements:

* K-Means Clustering
* Silhouette Score Analysis

### 12. Time Series Agent

Detects temporal datasets and provides forecasting guidance.

### 13. Report Generator Agent

Creates executive summaries and deployment recommendations.

### 14. Download Report Agent

Exports generated reports.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Machine Learning

* Scikit-learn
* XGBoost

### LLM Integration

* Groq API
* Llama 3.1 8B Instant

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Environment Management

* Python Dotenv

---

##  Supported Tasks

### Classification

Examples:

* Customer Churn Prediction
* Titanic Survival Prediction
* Spam Detection

### Regression

Examples:

* House Price Prediction
* Sales Forecasting
* Revenue Prediction

### Clustering

Examples:

* Customer Segmentation
* User Behavior Analysis

### Time Series

Examples:

* Demand Forecasting
* Trend Analysis
* Seasonal Pattern Analysis

---

## 🔍 Key Features

✅ Automated Dataset Profiling

✅ ML Task Detection

✅ Model Recommendations

✅ Automated Model Training

✅ Performance Evaluation

✅ Feature Importance Analysis

✅ Explainable AI Insights

✅ LLM-Powered Knowledge Enhancement

✅ Executive Report Generation

✅ Downloadable Reports

✅ Interactive Dashboard

---

## 📁 Project Structure

```text
DocuMind
│
├── agents/
├── knowledge_base/
├── utils/
├── reports/
├── app.py
├── requirements.txt
└── README.md
```

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/HxrshRaj/Documind-.git
cd Documind-
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

* Automated Hyperparameter Optimization
* SHAP Explainability
* PDF Report Export
* Advanced RAG Knowledge Base
* AutoML Integration
* Deep Learning Support
* Multi-Dataset Analysis
* Real-Time Monitoring Dashboard

---

## 👨‍💻 Author

**Harsh Raj**

B.Tech – Computer Science Engineering

SRM University AP

---

## 📜 License

This project is developed for educational, research, and demonstration purposes.
