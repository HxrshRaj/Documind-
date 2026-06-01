from pathlib import Path


def save_report(
    report_text,
    filename="documind_report.txt"
):

    reports_folder = Path(
        "reports"
    )

    reports_folder.mkdir(
        exist_ok=True
    )

    file_path = (
        reports_folder /
        filename
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            report_text
        )

    return file_path