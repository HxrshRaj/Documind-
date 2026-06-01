import pandas as pd


def get_feature_importance(
    model,
    feature_names,
    top_n=10
):

    if not hasattr(
        model,
        "feature_importances_"
    ):
        return None

    importance_df = pd.DataFrame({

        "Feature":
            feature_names,

        "Importance":
            model.feature_importances_

    })

    importance_df = (

        importance_df

        .sort_values(
            by="Importance",
            ascending=False
        )

        .head(top_n)

        .reset_index(
            drop=True
        )

    )

    return importance_df