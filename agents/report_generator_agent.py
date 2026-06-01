from agents.report_agent import (
    generate_executive_report
)

from agents.knowledge_agent import (
    get_knowledge_summary
)


def build_report(
    task,
    best_model,
    best_score,
    explanation,
    knowledge
):

    knowledge = (
        get_knowledge_summary(
            task
        )
    )

    report = (
        generate_executive_report(
            task,
            best_model,
            best_score,
            explanation,
            knowledge
        )
    )

    return report