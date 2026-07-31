def solve(s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
    def merge(left, right):
        if left[0] == 0:
            return right
        if right[0] == 0:
            return left
        joins = left[2] == right[1]
        prefix = left[3] + right[3] if joins and left[3] == left[0] else left[3]
        suffix = right[4] + left[4] if joins and right[4] == right[0] else right[4]
        middle = left[4] + right[3] if joins else 0
        return (left[0] + right[0], left[1], right[2], prefix, suffix, max(left[5], right[5], middle))

    length = len(s)
    size = 1
    while size < length:
        size *= 2
    empty = (0, "", "", 0, 0, 0)
    tree = [empty for _ in range(2 * size)]
    for index, character in enumerate(s):
        tree[size + index] = (1, character, character, 1, 1, 1)
    for node in range(size - 1, 0, -1):
        tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    answers = []
    for index, character in zip(queryIndices, queryCharacters):
        node = size + index
        tree[node] = (1, character, character, 1, 1, 1)
        node //= 2
        while node:
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])
            node //= 2
        answers.append(tree[1][5])
    return answers
