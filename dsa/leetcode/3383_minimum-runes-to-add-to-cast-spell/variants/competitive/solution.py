from typing import List


class Solution:
    def minRunesToAdd(
        self,
        n: int,
        crystals: List[int],
        flowFrom: List[int],
        flowTo: List[int],
    ) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for source, target in zip(flowFrom, flowTo):
            graph[source].append(target)
            reverse_graph[target].append(source)

        reachable = [False] * n
        stack = list(crystals)
        for node in crystals:
            reachable[node] = True
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not reachable[neighbor]:
                    reachable[neighbor] = True
                    stack.append(neighbor)

        visited = [False] * n
        finish_order = []
        for start in range(n):
            if visited[start]:
                continue
            visited[start] = True
            stack = [(start, False)]
            while stack:
                node, expanded = stack.pop()
                if expanded:
                    finish_order.append(node)
                    continue
                stack.append((node, True))
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append((neighbor, False))

        component = [-1] * n
        component_count = 0
        for start in reversed(finish_order):
            if component[start] != -1:
                continue
            component[start] = component_count
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in reverse_graph[node]:
                    if component[neighbor] == -1:
                        component[neighbor] = component_count
                        stack.append(neighbor)
            component_count += 1

        component_reachable = [False] * component_count
        for node in range(n):
            if reachable[node]:
                component_reachable[component[node]] = True

        has_unreachable_incoming = [False] * component_count
        for source, target in zip(flowFrom, flowTo):
            source_component = component[source]
            target_component = component[target]
            if source_component != target_component and not component_reachable[target_component]:
                has_unreachable_incoming[target_component] = True

        return sum(
            not component_reachable[index] and not has_unreachable_incoming[index] for index in range(component_count)
        )
