"""Optimal app-local solution for LeetCode 406."""


def solve(people: list[list[int]]) -> list[list[int]]:
    length = len(people)
    fenwick = [0] * (length + 1)

    def add(index: int, delta: int) -> None:
        while index <= length:
            fenwick[index] += delta
            index += index & -index

    def find_by_order(order: int) -> int:
        index = 0
        step = 1 << (length.bit_length() - 1)
        while step:
            candidate = index + step
            if candidate <= length and fenwick[candidate] < order:
                index = candidate
                order -= fenwick[candidate]
            step >>= 1
        return index + 1

    for position in range(1, length + 1):
        add(position, 1)

    queue: list[list[int] | None] = [None] * length
    for person in sorted(people, key=lambda item: (item[0], -item[1])):
        position = find_by_order(person[1] + 1)
        queue[position - 1] = person.copy()
        add(position, -1)

    return [person for person in queue if person is not None]
