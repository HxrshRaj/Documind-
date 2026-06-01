def adapt_explanation(
    explanation,
    level
):

    if level == "Beginner":

        return (
            "BEGINNER MODE\n\n"
            + explanation
        )

    elif level == "Intermediate":

        return (
            "INTERMEDIATE MODE\n\n"
            + explanation
        )

    else:

        return (
            "EXPERT MODE\n\n"
            + explanation
        )