def solve(s: str, queries: list[list[int]]) -> list[int]:
    chars = list(s)
    n = len(chars)
    tree_size = 1
    while tree_size < n:
        tree_size *= 2
    tree = [0] * (2 * tree_size)

    for index in range(1, n):
        tree[tree_size + index] = int(chars[index] == chars[index - 1])
    for node in range(tree_size - 1, 0, -1):
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def assign_edge(index: int) -> None:
        node = tree_size + index
        tree[node] = int(index > 0 and chars[index] == chars[index - 1])
        node //= 2
        while node:
            tree[node] = tree[2 * node] + tree[2 * node + 1]
            node //= 2

    def range_sum(start: int, end: int) -> int:
        start += tree_size
        end += tree_size
        total = 0
        while start < end:
            if start & 1:
                total += tree[start]
                start += 1
            if end & 1:
                end -= 1
                total += tree[end]
            start //= 2
            end //= 2
        return total

    answers = []
    for query in queries:
        if query[0] == 1:
            index = query[1]
            chars[index] = "B" if chars[index] == "A" else "A"
            if index > 0:
                assign_edge(index)
            if index + 1 < n:
                assign_edge(index + 1)
        else:
            left, right = query[1], query[2]
            answers.append(range_sum(left + 1, right + 1))
    return answers
