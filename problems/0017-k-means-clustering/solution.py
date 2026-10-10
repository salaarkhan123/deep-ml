def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    centroids = list(initial_centroids)

    for i in range(max_iterations):

        # Create k empty clusters
        clusters = []

        for j in range(k):
            clusters.append([])

        # Assign each point to closest centroid
        for point in points:

            distances = []

            for centroid in centroids:

                distance = 0

                for p, c in zip(point, centroid):
                    distance += (p - c) ** 2

                distance = distance ** 0.5
                distances.append(distance)

            closest = distances.index(min(distances))

            clusters[closest].append(point)

        # Calculate new centroids
        new_centroids = []

        for cluster in clusters:

            # If cluster is empty, keep old centroid
            if len(cluster) == 0:
                new_centroids.append(centroids[len(new_centroids)])

            else:
                new_centroid = []

                # Go through each coordinate
                for dimension in range(len(cluster[0])):

                    total = 0

                    for point in cluster:
                        total += point[dimension]

                    mean = total / len(cluster)

                    new_centroid.append(mean)

                new_centroids.append(tuple(new_centroid))

        # Update centroids
        centroids = new_centroids

    return centroids