def generate_clustering_report(
    score
):

    return f"""
Clustering Analysis Complete.

Silhouette Score:
{score}

Higher scores indicate
better cluster separation.

KMeans clustering
was successfully executed.
"""