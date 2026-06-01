def get_best_model(
    performance_df,
    task
):

    if task == "Classification":

        metric = "F1 Score"

    else:

        metric = "R2 Score"

    best_score = performance_df[
        metric
    ].max()

    best_models = performance_df[
        performance_df[
            metric
        ] == best_score
    ]["Model"].tolist()

    return (
        best_models,
        best_score,
        metric
    )