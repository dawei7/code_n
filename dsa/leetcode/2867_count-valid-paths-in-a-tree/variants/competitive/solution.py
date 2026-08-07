class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        value = 2
        while value * value <= n:
            if is_prime[value]:
                for multiple in range(value * value, n + 1, value):
                    is_prime[multiple] = False
            value += 1

        graph = [[] for _ in range(n + 1)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        component_size = [0] * (n + 1)
        for start in range(1, n + 1):
            if is_prime[start] or component_size[start]:
                continue

            component_size[start] = -1
            stack = [start]
            nodes = []

            while stack:
                node = stack.pop()
                nodes.append(node)
                for neighbor in graph[node]:
                    if not is_prime[neighbor] and component_size[neighbor] == 0:
                        component_size[neighbor] = -1
                        stack.append(neighbor)

            size = len(nodes)
            for node in nodes:
                component_size[node] = size

        answer = 0
        for prime in range(2, n + 1):
            if not is_prime[prime]:
                continue

            previous = 0
            for neighbor in graph[prime]:
                if is_prime[neighbor]:
                    continue
                size = component_size[neighbor]
                answer += previous * size
                previous += size
            answer += previous

        return answer
