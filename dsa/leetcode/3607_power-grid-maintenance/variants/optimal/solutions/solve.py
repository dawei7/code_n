from heapq import heappop


def solve(
    c: int,
    connections: list[list[int]],
    queries: list[list[int]],
) -> list[int]:
    parent = list(range(c + 1))
    size = [1] * (c + 1)

    def find(station: int) -> int:
        while station != parent[station]:
            parent[station] = parent[parent[station]]
            station = parent[station]
        return station

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        if size[first_root] < size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        size[first_root] += size[second_root]

    for first, second in connections:
        union(first, second)

    component = [find(station) for station in range(c + 1)]
    online_by_component = {}
    for station in range(1, c + 1):
        online_by_component.setdefault(component[station], []).append(station)

    online = [True] * (c + 1)
    answer = []

    for query_type, station in queries:
        if query_type == 2:
            online[station] = False
        elif online[station]:
            answer.append(station)
        else:
            heap = online_by_component[component[station]]
            while heap and not online[heap[0]]:
                heappop(heap)
            answer.append(heap[0] if heap else -1)

    return answer
