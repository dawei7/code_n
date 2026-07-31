from typing import List


class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def find_by_order(self, order: int) -> int:
        index = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            candidate = index + step
            if candidate <= self.size and self.tree[candidate] < order:
                index = candidate
                order -= self.tree[candidate]
            step >>= 1
        return index


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        tile_count = len(colors)
        breakpoints = FenwickTree(tile_count)
        length_counts = FenwickTree(tile_count + 1)
        length_sums = FenwickTree(tile_count + 1)

        bad_edges = [index for index in range(tile_count) if colors[index] == colors[(index + 1) % tile_count]]
        bad_count = len(bad_edges)

        for edge in bad_edges:
            breakpoints.add(edge, 1)

        def arc_length(first: int, second: int) -> int:
            return (second - first) % tile_count or tile_count

        def change_length(length: int, delta: int) -> None:
            length_counts.add(length, delta)
            length_sums.add(length, delta * length)

        if bad_count:
            for index, edge in enumerate(bad_edges):
                change_length(arc_length(edge, bad_edges[(index + 1) % bad_count]), 1)

        def insert_breakpoint(edge: int) -> None:
            nonlocal bad_count
            if bad_count == 0:
                breakpoints.add(edge, 1)
                change_length(tile_count, 1)
                bad_count = 1
                return

            rank_before = breakpoints.prefix_sum(edge - 1)
            predecessor = breakpoints.find_by_order(rank_before if rank_before else bad_count)
            successor = breakpoints.find_by_order(rank_before + 1 if rank_before < bad_count else 1)

            change_length(arc_length(predecessor, successor), -1)
            change_length(arc_length(predecessor, edge), 1)
            change_length(arc_length(edge, successor), 1)
            breakpoints.add(edge, 1)
            bad_count += 1

        def remove_breakpoint(edge: int) -> None:
            nonlocal bad_count
            if bad_count == 1:
                change_length(tile_count, -1)
                breakpoints.add(edge, -1)
                bad_count = 0
                return

            rank = breakpoints.prefix_sum(edge)
            predecessor = breakpoints.find_by_order(rank - 1 if rank > 1 else bad_count)
            successor = breakpoints.find_by_order(rank + 1 if rank < bad_count else 1)

            change_length(arc_length(predecessor, edge), -1)
            change_length(arc_length(edge, successor), -1)
            change_length(arc_length(predecessor, successor), 1)
            breakpoints.add(edge, -1)
            bad_count -= 1

        answer = []
        for query in queries:
            if query[0] == 1:
                size = query[1]
                if bad_count == 0:
                    answer.append(tile_count)
                    continue

                shorter_count = length_counts.prefix_sum(size - 1)
                shorter_sum = length_sums.prefix_sum(size - 1)
                eligible_count = bad_count - shorter_count
                eligible_sum = tile_count - shorter_sum
                answer.append(eligible_sum - (size - 1) * eligible_count)
                continue

            index, new_color = query[1], query[2]
            if colors[index] == new_color:
                continue

            affected_edges = ((index - 1) % tile_count, index)
            was_bad = [colors[edge] == colors[(edge + 1) % tile_count] for edge in affected_edges]
            colors[index] = new_color

            for edge, old_status in zip(affected_edges, was_bad):
                new_status = colors[edge] == colors[(edge + 1) % tile_count]
                if old_status and not new_status:
                    remove_breakpoint(edge)
                elif not old_status and new_status:
                    insert_breakpoint(edge)

        return answer


def solve(colors: list[int], queries: list[list[int]]) -> list[int]:
    return Solution().numberOfAlternatingGroups(colors, queries)
