def generate_executive_report(
    task,
    best_model,
    best_score,
    explanation,
    retrieved_knowledge
):

    report = f"""
DOCUMIND EXECUTIVE REPORT

===================================

Detected Task:
{task}

===================================

Recommended Model:
{best_model}

Performance Score:
{best_score}

===================================

Business Interpretation:

{explanation}

===================================

Retrieved Domain Knowledge:

{retrieved_knowledge}

===================================

Deployment Recommendation:

The selected model should be considered
for further tuning, validation and
production deployment.

===================================
"""

    return report