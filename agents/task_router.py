from agents.time_series_agent import (
    detect_time_series
)


def route_task(
    df,
    detected_task
):

    if detect_time_series(df):

        return "Time Series"

    return detected_task