def recommend_models(task):
    """
    Recommend models based on detected ML task.
    """

    recommendations = {

        "Classification": {
            "models": [
                "Random Forest Classifier",
                "XGBoost Classifier",
                "Logistic Regression"
            ],
            "reason":
            "These models are effective for categorical prediction tasks and provide a good balance between performance and interpretability."
        },

        "Regression": {
            "models": [
                "Linear Regression",
                "Random Forest Regressor",
                "XGBoost Regressor"
            ],
            "reason":
            "These models are commonly used for continuous value prediction and can handle both linear and non-linear relationships."
        },

        "Clustering": {
            "models": [
                "K-Means",
                "DBSCAN",
                "Hierarchical Clustering"
            ],
            "reason":
            "These models are suitable for discovering patterns and groups in unlabeled datasets."
        },

        "Time Series": {
            "models": [
                "ARIMA",
                "Prophet",
                "LSTM"
            ],
            "reason":
            "These models are widely used for forecasting and temporal pattern analysis."
        }
    }

    return recommendations.get(task)