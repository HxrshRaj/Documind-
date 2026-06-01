def get_report_filename(
    task
):

    task_name = (
        task.lower()
        .replace(
            " ",
            "_"
        )
    )

    return (
        f"documind_{task_name}_report.txt"
    )