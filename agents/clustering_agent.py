from sklearn.cluster import KMeans

from sklearn.metrics import (
    silhouette_score
)


def run_clustering(
    X
):

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(
        X
    )

    score = silhouette_score(
        X,
        labels
    )

    return {
        "clusters": 3,
        "silhouette_score":
            round(score, 4)
    }