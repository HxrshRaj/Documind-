from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

import numpy as np


def evaluate_classification(y_true, y_pred):

    return {
        "Accuracy": round(
            accuracy_score(y_true, y_pred),
            4
        ),

        "Precision": round(
            precision_score(
                y_true,
                y_pred,
                average="weighted"
            ),
            4
        ),

        "Recall": round(
            recall_score(
                y_true,
                y_pred,
                average="weighted"
            ),
            4
        ),

        "F1 Score": round(
            f1_score(
                y_true,
                y_pred,
                average="weighted"
            ),
            4
        )
    }


def evaluate_regression(y_true, y_pred):

    rmse = np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )

    return {
        "R2 Score": round(
            r2_score(
                y_true,
                y_pred
            ),
            4
        ),

        "RMSE": round(
            rmse,
            4
        ),

        "MAE": round(
            mean_absolute_error(
                y_true,
                y_pred
            ),
            4
        )
    }