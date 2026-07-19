def solve(parents: list[int], queries: list[list[int]]) -> list[int]:
    node_count = len(parents)
    children = [[] for _ in range(node_count)]
    root = 0
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            children[parent].append(node)

    queries_by_node = [[] for _ in range(node_count)]
    maximum_value = node_count - 1
    for query_index, (node, value) in enumerate(queries):
        queries_by_node[node].append((value, query_index))
        maximum_value = max(maximum_value, value)
    highest_bit = maximum_value.bit_length() - 1

    trie = [[-1, -1, 0]]

    def update(value: int, change: int) -> None:
        trie[0][2] += change
        trie_node = 0
        for bit in range(highest_bit, -1, -1):
            direction = (value >> bit) & 1
            next_node = trie[trie_node][direction]
            if next_node == -1:
                next_node = len(trie)
                trie[trie_node][direction] = next_node
                trie.append([-1, -1, 0])
            trie_node = next_node
            trie[trie_node][2] += change

    def maximum_xor(value: int) -> int:
        trie_node = 0
        result = 0
        for bit in range(highest_bit, -1, -1):
            direction = (value >> bit) & 1
            preferred = direction ^ 1
            next_node = trie[trie_node][preferred]
            if next_node != -1 and trie[next_node][2] > 0:
                result |= 1 << bit
                trie_node = next_node
            else:
                trie_node = trie[trie_node][direction]
        return result

    answers = [0] * len(queries)
    stack = [(root, True)]
    while stack:
        node, entering = stack.pop()
        if entering:
            update(node, 1)
            for value, query_index in queries_by_node[node]:
                answers[query_index] = maximum_xor(value)
            stack.append((node, False))
            for child in children[node]:
                stack.append((child, True))
        else:
            update(node, -1)

    return answers
