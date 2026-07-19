"""App-local reference solution for LeetCode 1847."""

from bisect import bisect_left, bisect_right


def solve(rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
    room_ids = sorted(room_id for room_id, _ in rooms)
    positions = {room_id: index + 1 for index, room_id in enumerate(room_ids)}
    tree = [0] * (len(room_ids) + 1)

    def add(index: int) -> None:
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def prefix(index: int) -> int:
        total = 0
        while index:
            total += tree[index]
            index -= index & -index
        return total

    def kth(order: int) -> int:
        index = 0
        step = 1 << (len(room_ids).bit_length() - 1)
        while step:
            following = index + step
            if following < len(tree) and tree[following] < order:
                index = following
                order -= tree[following]
            step >>= 1
        return index + 1

    rooms_by_size = sorted(rooms, key=lambda room: room[1], reverse=True)
    indexed_queries = sorted(
        (
            (minimum_size, preferred, query_index)
            for query_index, (preferred, minimum_size) in enumerate(queries)
        ),
        reverse=True,
    )
    answer = [-1] * len(queries)
    room_index = 0

    for minimum_size, preferred, query_index in indexed_queries:
        while (
            room_index < len(rooms_by_size)
            and rooms_by_size[room_index][1] >= minimum_size
        ):
            add(positions[rooms_by_size[room_index][0]])
            room_index += 1

        total = prefix(len(room_ids))
        if total == 0:
            continue

        candidates: list[int] = []
        left_count = prefix(bisect_right(room_ids, preferred))
        if left_count:
            candidates.append(room_ids[kth(left_count) - 1])

        count_before_right = prefix(bisect_left(room_ids, preferred))
        if count_before_right < total:
            candidates.append(room_ids[kth(count_before_right + 1) - 1])

        answer[query_index] = min(
            candidates, key=lambda room_id: (abs(room_id - preferred), room_id)
        )

    return answer
