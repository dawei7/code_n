from heapq import nlargest


def solve(scores: list[int], edges: list[list[int]]) -> int:
    neighbors = [[] for _ in scores]
    for first, second in edges:
        neighbors[first].append(second)
        neighbors[second].append(first)

    best_neighbors = [nlargest(3, adjacent, key=scores.__getitem__) for adjacent in neighbors]

    answer = -1
    for second, third in edges:
        for first in best_neighbors[second]:
            for fourth in best_neighbors[third]:
                if len({first, second, third, fourth}) == 4:
                    answer = max(
                        answer,
                        scores[first] + scores[second] + scores[third] + scores[fourth],
                    )
    return answer
