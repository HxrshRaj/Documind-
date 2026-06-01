def generate_explanation(
    task,
    best_model,
    best_score
):

    if task == "Classification":

        return f"""
Task Type: Classification

Recommended Model:
{best_model}

Selection Reason:
Highest F1 Score ({best_score})

Business Insight:

The selected model balances precision and recall
effectively, making it suitable for real-world
classification scenarios.

Recommendation:

Proceed with feature analysis and deployment
testing using the selected model.
"""

    elif task == "Regression":

        return f"""
Task Type: Regression

Recommended Model:
{best_model}

Selection Reason:
Highest R² Score ({best_score})

Business Insight:

The selected model explains the largest proportion
of variance in the target variable.

Recommendation:

Proceed with error analysis and deployment
testing using the selected model.
"""

    return "No explanation available."