import plotly.express as px


def create_performance_chart(
    performance_df,
    task
):
    """
    Create model comparison chart.
    """

    if task == "Classification":

        metric = "F1 Score"

    else:

        metric = "R2 Score"

    fig = px.bar(
        performance_df,
        x="Model",
        y=metric,
        title=f"{metric} Comparison",
        text=metric
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Model",
        yaxis_title=metric,
        height=500
    )

    return fig