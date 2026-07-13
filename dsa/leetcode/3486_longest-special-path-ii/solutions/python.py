from collections import defaultdict
from heapq import heappop, heappush
import sys

sys.setrecursionlimit(200000)


def solve(edges: list[list[int]], nums: list[int]) -> list[int]:
    n = len(nums)
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    positions: dict[int, list[int]] = defaultdict(list)
    second_heap: list[tuple[int, int, int]] = []
    third_heap: list[tuple[int, int, int]] = []
    second_version: dict[int, int] = defaultdict(int)
    third_version: dict[int, int] = defaultdict(int)
    prefix = [0] * (n + 1)
    best_length = 0
    best_nodes = 1

    def push_value_state(value: int) -> None:
        stack = positions[value]
        second_version[value] += 1
        if len(stack) >= 2:
            heappush(second_heap, (-stack[-2], value, second_version[value]))
        third_version[value] += 1
        if len(stack) >= 3:
            heappush(third_heap, (-stack[-3], value, third_version[value]))

    def is_current_second(entry: tuple[int, int, int]) -> bool:
        depth, value, version = -entry[0], entry[1], entry[2]
        stack = positions[value]
        return version == second_version[value] and len(stack) >= 2 and stack[-2] == depth

    def is_current_third(entry: tuple[int, int, int]) -> bool:
        depth, value, version = -entry[0], entry[1], entry[2]
        stack = positions[value]
        return version == third_version[value] and len(stack) >= 3 and stack[-3] == depth

    def clean_second() -> None:
        while second_heap and not is_current_second(second_heap[0]):
            heappop(second_heap)

    def clean_third() -> None:
        while third_heap and not is_current_third(third_heap[0]):
            heappop(third_heap)

    def max_third_depth() -> int:
        clean_third()
        return -third_heap[0][0] if third_heap else -1

    def second_largest_pair_start() -> int:
        clean_second()
        if len(second_heap) < 2:
            return -1
        first = heappop(second_heap)
        clean_second()
        result = -second_heap[0][0] if second_heap else -1
        heappush(second_heap, first)
        return result

    def dfs(node: int, parent: int, depth: int, distance: int) -> None:
        nonlocal best_length, best_nodes

        value = nums[node]
        positions[value].append(depth)
        push_value_state(value)

        left = max(max_third_depth() + 1, second_largest_pair_start() + 1)
        length = distance - prefix[left]
        node_count = depth - left + 1
        if length > best_length:
            best_length = length
            best_nodes = node_count
        elif length == best_length and node_count < best_nodes:
            best_nodes = node_count

        for child, weight in graph[node]:
            if child == parent:
                continue
            prefix[depth + 1] = distance + weight
            dfs(child, node, depth + 1, distance + weight)

        positions[value].pop()
        push_value_state(value)

    dfs(0, -1, 0, 0)
    return [best_length, best_nodes]
