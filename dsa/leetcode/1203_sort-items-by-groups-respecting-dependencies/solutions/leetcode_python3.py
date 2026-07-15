from collections import deque
from typing import List


class Solution:
    def sortItems(
        self,
        n: int,
        m: int,
        group: List[int],
        beforeItems: List[List[int]],
    ) -> List[int]:
        assigned_group = group[:]
        group_count = m
        for item in range(n):
            if assigned_group[item] == -1:
                assigned_group[item] = group_count
                group_count += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        group_graph = [[] for _ in range(group_count)]
        group_indegree = [0] * group_count

        for current in range(n):
            for previous in beforeItems[current]:
                item_graph[previous].append(current)
                item_indegree[current] += 1
                previous_group = assigned_group[previous]
                current_group = assigned_group[current]
                if previous_group != current_group:
                    group_graph[previous_group].append(current_group)
                    group_indegree[current_group] += 1

        def topological_order(graph: List[List[int]], indegree: List[int]) -> List[int]:
            ready = deque(index for index, degree in enumerate(indegree) if degree == 0)
            order = []
            while ready:
                node = ready.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        ready.append(neighbor)
            return order if len(order) == len(graph) else []

        item_order = topological_order(item_graph, item_indegree)
        group_order = topological_order(group_graph, group_indegree)
        if not item_order or not group_order:
            return []

        items_by_group = [[] for _ in range(group_count)]
        for item in item_order:
            items_by_group[assigned_group[item]].append(item)

        return [item for group_id in group_order for item in items_by_group[group_id]]
