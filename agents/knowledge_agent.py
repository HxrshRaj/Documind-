def get_knowledge_summary(
    task
):

    summaries = {

        "Classification":
            "Classification predicts categorical outcomes.",

        "Regression":
            "Regression predicts continuous values.",

        "Clustering":
            "Clustering groups similar observations.",

        "Time Series":
            "Time series analyzes temporal patterns."
    }

    return summaries.get(
        task,
        "No knowledge available."
    )