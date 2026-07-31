class Solution:
    def treeQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        adjacency = [[] for _ in range(n + 1)]
        weights = {}
        for left, right, weight in edges:
            adjacency[left].append((right, weight))
            adjacency[right].append((left, weight))
            weights[(min(left, right), max(left, right))] = weight

        parent = [0] * (n + 1)
        initial_distance = [0] * (n + 1)
        entry = [0] * (n + 1)
        exit_time = [0] * (n + 1)
        timer = 0
        stack = [(1, 0, 0, False)]

        while stack:
            node, previous, distance, exiting = stack.pop()
            if exiting:
                exit_time[node] = timer
                continue

            parent[node] = previous
            initial_distance[node] = distance
            entry[node] = timer
            timer += 1
            stack.append((node, previous, distance, True))
            for neighbor, weight in reversed(adjacency[node]):
                if neighbor != previous:
                    stack.append((neighbor, node, distance + weight, False))

        fenwick = [0] * (n + 1)

        def add(index: int, delta: int) -> None:
            index += 1
            while index <= n:
                fenwick[index] += delta
                index += index & -index

        def point(index: int) -> int:
            total = 0
            index += 1
            while index:
                total += fenwick[index]
                index -= index & -index
            return total

        answer = []
        for query in queries:
            if query[0] == 1:
                _, left, right, new_weight = query
                key = (min(left, right), max(left, right))
                delta = new_weight - weights[key]
                weights[key] = new_weight
                child = left if parent[left] == right else right
                add(entry[child], delta)
                if exit_time[child] < n:
                    add(exit_time[child], -delta)
            else:
                node = query[1]
                answer.append(initial_distance[node] + point(entry[node]))

        return answer
