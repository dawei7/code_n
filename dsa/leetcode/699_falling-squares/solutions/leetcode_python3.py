from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        coordinates = sorted({
            coordinate
            for left, side in positions
            for coordinate in (left, left + side)
        })
        coordinate_index = {
            coordinate: index
            for index, coordinate in enumerate(coordinates)
        }
        segment_count = len(coordinates) - 1
        tree = [0] * (4 * segment_count)
        lazy = [None] * (4 * segment_count)

        def push(node: int) -> None:
            assigned = lazy[node]
            if assigned is None:
                return
            for child in (node * 2, node * 2 + 1):
                tree[child] = assigned
                lazy[child] = assigned
            lazy[node] = None

        def query(node, segment_left, segment_right, query_left, query_right):
            if query_left <= segment_left and segment_right <= query_right:
                return tree[node]
            push(node)
            middle = (segment_left + segment_right) // 2
            maximum = 0
            if query_left <= middle:
                maximum = query(
                    node * 2,
                    segment_left,
                    middle,
                    query_left,
                    query_right,
                )
            if query_right > middle:
                maximum = max(
                    maximum,
                    query(
                        node * 2 + 1,
                        middle + 1,
                        segment_right,
                        query_left,
                        query_right,
                    ),
                )
            return maximum

        def assign(
            node,
            segment_left,
            segment_right,
            query_left,
            query_right,
            height,
        ):
            if query_left <= segment_left and segment_right <= query_right:
                tree[node] = height
                lazy[node] = height
                return
            push(node)
            middle = (segment_left + segment_right) // 2
            if query_left <= middle:
                assign(
                    node * 2,
                    segment_left,
                    middle,
                    query_left,
                    query_right,
                    height,
                )
            if query_right > middle:
                assign(
                    node * 2 + 1,
                    middle + 1,
                    segment_right,
                    query_left,
                    query_right,
                    height,
                )
            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        answer = []
        global_maximum = 0

        for left, side in positions:
            query_left = coordinate_index[left]
            query_right = coordinate_index[left + side] - 1
            top = query(
                1,
                0,
                segment_count - 1,
                query_left,
                query_right,
            ) + side
            assign(
                1,
                0,
                segment_count - 1,
                query_left,
                query_right,
                top,
            )
            global_maximum = max(global_maximum, top)
            answer.append(global_maximum)

        return answer
