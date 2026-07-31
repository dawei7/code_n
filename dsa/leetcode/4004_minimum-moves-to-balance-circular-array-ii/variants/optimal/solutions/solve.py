from heapq import heappop, heappush


def solve(balance: list[int]) -> int:
    if sum(balance) < 0:
        return -1

    demand = sum(-value for value in balance if value < 0)
    if demand == 0:
        return 0

    n = len(balance)
    source = n
    sink = n + 1
    graph = [[] for _ in range(n + 2)]

    def add_edge(start: int, end: int, capacity: int, cost: int) -> None:
        forward = [end, len(graph[end]), capacity, cost]
        backward = [start, len(graph[start]), 0, -cost]
        graph[start].append(forward)
        graph[end].append(backward)

    for index, value in enumerate(balance):
        if value > 0:
            add_edge(source, index, value, 0)
        elif value < 0:
            add_edge(index, sink, -value, 0)

    for index in range(n):
        neighbor = (index + 1) % n
        add_edge(index, neighbor, demand, 1)
        add_edge(neighbor, index, demand, 1)

    infinity = 10**30
    potential = [0] * (n + 2)
    delivered = 0
    answer = 0

    while delivered < demand:
        distance = [infinity] * (n + 2)
        parent_node = [-1] * (n + 2)
        parent_edge = [-1] * (n + 2)
        distance[source] = 0
        heap = [(0, source)]

        while heap:
            current_distance, node = heappop(heap)
            if current_distance != distance[node]:
                continue

            for edge_index, edge in enumerate(graph[node]):
                next_node, _, capacity, cost = edge
                if capacity == 0:
                    continue
                candidate = current_distance + cost + potential[node] - potential[next_node]
                if candidate < distance[next_node]:
                    distance[next_node] = candidate
                    parent_node[next_node] = node
                    parent_edge[next_node] = edge_index
                    heappush(heap, (candidate, next_node))

        for node in range(n + 2):
            if distance[node] < infinity:
                potential[node] += distance[node]

        amount = demand - delivered
        path_cost = 0
        node = sink
        while node != source:
            previous = parent_node[node]
            edge_index = parent_edge[node]
            edge = graph[previous][edge_index]
            amount = min(amount, edge[2])
            path_cost += edge[3]
            node = previous

        node = sink
        while node != source:
            previous = parent_node[node]
            edge_index = parent_edge[node]
            edge = graph[previous][edge_index]
            edge[2] -= amount
            graph[node][edge[1]][2] += amount
            node = previous

        delivered += amount
        answer += amount * path_cost

    return answer
