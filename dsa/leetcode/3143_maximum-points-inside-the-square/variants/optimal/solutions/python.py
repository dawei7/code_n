import math

def solve(points: list[list[int]], s: str) -> int:
    # min_dist[char] stores the smallest Chebyshev distance for a given tag
    # second_min_dist stores the smallest distance where a tag conflict occurs
    min_dist = {}
    second_min_dist = float('inf')

    for i in range(len(points)):
        x, y = points[i]
        char = s[i]
        # Chebyshev distance from origin is max(|x|, |y|)
        dist = max(abs(x), abs(y))

        if char in min_dist:
            # If we've seen this char, update the conflict threshold
            # using the second-smallest distance for this specific tag.
            second_min_dist = min(second_min_dist, max(dist, min_dist[char]))
            # Keep track of the absolute minimum for this char
            min_dist[char] = min(min_dist[char], dist)
        else:
            min_dist[char] = dist

    count = 0
    # Any point with distance strictly less than the conflict threshold is valid
    for char in min_dist:
        if min_dist[char] < second_min_dist:
            count += 1

    return count
