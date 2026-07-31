def solve(words: list[str], k: int) -> list[int]:
    if len(words) - 1 < k:
        return [0] * len(words)

    children: list[dict[str, int]] = [{}]
    counts = [0]
    depths = [0]

    for word in words:
        node = 0
        for character in word:
            next_node = children[node].get(character)
            if next_node is None:
                next_node = len(children)
                children[node][character] = next_node
                children.append({})
                counts.append(0)
                depths.append(depths[node] + 1)
            node = next_node
            counts[node] += 1

    maximum_depth = max(depths)
    valid_at_depth = [0] * (maximum_depth + 1)
    for node in range(1, len(counts)):
        if counts[node] >= k:
            valid_at_depth[depths[node]] += 1

    previous_valid = [0] * (maximum_depth + 1)
    latest = 0
    for depth in range(1, maximum_depth + 1):
        if valid_at_depth[depth] > 0:
            latest = depth
        previous_valid[depth] = latest

    deepest = previous_valid[maximum_depth]
    disabled_by = [-1] * (maximum_depth + 1)
    answer: list[int] = []

    for word_index, word in enumerate(words):
        node = 0
        for character in word:
            node = children[node][character]
            depth = depths[node]
            if counts[node] == k and valid_at_depth[depth] == 1:
                disabled_by[depth] = word_index

        candidate = deepest
        while candidate > 0 and disabled_by[candidate] == word_index:
            candidate = previous_valid[candidate - 1]
        answer.append(candidate)

    return answer
