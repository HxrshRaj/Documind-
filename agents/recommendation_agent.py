def generate_recommendation(
    task
):

    recommendations = {

        "Classification":
            [
                "Logistic Regression",
                "Random Forest Classifier"
            ],

        "Regression":
            [
                "Linear Regression",
                "Random Forest Regressor"
            ],

        "Clustering":
            [
                "KMeans"
            ],

        "Time Series":
            [
                "Trend Analysis",
                "Forecasting Models"
            ]
    }

    return recommendations.get(
        task,
        []
    )