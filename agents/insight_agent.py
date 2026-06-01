def generate_dataset_insights(
    profile,
    task
):

    insights = []

    rows = profile["rows"]

    columns = profile["columns"]

    missing = profile["missing_values"]

    if rows < 100:

        insights.append(
            "Dataset is relatively small."
        )

    elif rows < 10000:

        insights.append(
            "Dataset size is suitable for most machine learning algorithms."
        )

    else:

        insights.append(
            "Large dataset detected."
        )

    if missing > 0:

        insights.append(
            f"{missing} missing values were detected and handled during preprocessing."
        )

    else:

        insights.append(
            "No missing values detected."
        )

    insights.append(
        f"{columns} features were identified for analysis."
    )

    insights.append(
        f"Detected task type: {task}."
    )

    return insights