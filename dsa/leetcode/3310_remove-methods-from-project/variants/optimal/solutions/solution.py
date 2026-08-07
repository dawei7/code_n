class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for source, target in invocations:
            graph[source].append(target)

        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]

        while stack:
            method = stack.pop()
            for target in graph[method]:
                if not suspicious[target]:
                    suspicious[target] = True
                    stack.append(target)

        for source, target in invocations:
            if not suspicious[source] and suspicious[target]:
                return list(range(n))

        return [method for method in range(n) if not suspicious[method]]
