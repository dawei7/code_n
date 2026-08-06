"""Proposed app-local solution for LeetCode 406: Queue Reconstruction by Height."""


def solve(people: list[list[int]]) -> list[list[int]]:
    n = len(people)
    fenwick = [0] * (n + 1)

    def add(i, delta):
        while i <= n:
            fenwick[i] += delta
            i += i & -i

    def find_by_order(order):
        i = 0
        step = 1 << (n.bit_length() - 1)
        while step:
            j = i + step
            if j <= n and fenwick[j] < order:
                i = j
                order -= fenwick[j]
            step >>= 1
        return i + 1

    for i in range(1, n + 1):
        add(i, 1)

    queue = [None] * n
    for person in sorted(people, key=lambda item: (item[0], -item[1])):
        i = find_by_order(person[1] + 1)
        queue[i - 1] = person
        add(i, -1)

    return queue
