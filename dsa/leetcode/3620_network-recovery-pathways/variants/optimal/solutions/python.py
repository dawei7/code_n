from collections import deque


def solve(edges: list[list[int]], online: list[bool], k: int) -> int:
    node_count = len(online)
    adjacency = [[] for _ in range(node_count)]
    indegree = [0] * node_count

    for source, target, cost in edges:
        adjacency[source].append((target, cost))
        indegree[target] += 1

    queue = deque(
        node for node in range(node_count) if indegree[node] == 0
    )
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor, _ in adjacency[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    def feasible(minimum_cost: int) -> bool:
        distance = [k + 1] * node_count
        distance[0] = 0

        for node in topological_order:
            if not online[node] or distance[node] > k:
                continue
            for neighbor, cost in adjacency[node]:
                new_distance = distance[node] + cost
                if (
                    online[neighbor]
                    and cost >= minimum_cost
                    and new_distance < distance[neighbor]
                    and new_distance <= k
                ):
                    distance[neighbor] = new_distance

        return distance[-1] <= k

    costs = sorted({cost for _, _, cost in edges})
    answer = -1
    left = 0
    right = len(costs) - 1

    while left <= right:
        middle = (left + right) // 2
        if feasible(costs[middle]):
            answer = costs[middle]
            left = middle + 1
        else:
            right = middle - 1

    return answer
