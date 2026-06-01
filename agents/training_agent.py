from sklearn.model_selection import train_test_split

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from utils.preprocessing import (
    preprocess_data
)


def train_models(
    df,
    target_column,
    task
):

    df = preprocess_data(
        df,
        target_column
    )

    X = df.drop(
        columns=[target_column]
    )

    y = df[target_column]

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    model_outputs = {}

    if task == "Classification":

        models = {
            "Logistic Regression":
                LogisticRegression(
                    max_iter=1000
                ),

            "Random Forest Classifier":
                RandomForestClassifier(
                    random_state=42
                )
        }

    elif task == "Regression":

        models = {
            "Linear Regression":
                LinearRegression(),

            "Random Forest Regressor":
                RandomForestRegressor(
                    random_state=42
                )
        }

    else:
        return None

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        model_outputs[name] = {

            "model": model,

            "feature_names":
                X.columns.tolist(),

            "y_true":
                y_test,

            "y_pred":
                predictions
        }

    return model_outputs