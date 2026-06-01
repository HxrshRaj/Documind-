def generate_report(
    task,
    best_model,
    performance_df,
    retrieved_knowledge
):

    report = f"""
DOCUMIND AI RECOMMENDATION REPORT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detected Task:
{task}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recommended Model:
{best_model}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model Performance Summary:

{performance_df.to_string(index=False)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Retrieved Domain Knowledge:

{retrieved_knowledge}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final Recommendation:

The selected model achieved the strongest
overall performance based on evaluation metrics.

The recommendation is supported by both
empirical model performance and retrieved
domain-specific best practices.

This model should be considered the primary
candidate for deployment and further tuning.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    return report