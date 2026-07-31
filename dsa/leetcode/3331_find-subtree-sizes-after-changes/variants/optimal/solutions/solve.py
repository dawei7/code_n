def solve(parent: list[int], s: str) -> list[int]:
    node_count = len(parent)
    children = [[] for _ in range(node_count)]
    for node in range(1, node_count):
        children[parent[node]].append(node)

    character_paths = [[] for _ in range(26)]
    subtree_sizes = [1] * node_count
    stack = [(0, True)]

    while stack:
        node, entering = stack.pop()
        character = ord(s[node]) - ord("a")

        if entering:
            character_paths[character].append(node)
            stack.append((node, False))
            for child in reversed(children[node]):
                stack.append((child, True))
            continue

        character_paths[character].pop()
        if node == 0:
            continue

        if character_paths[character]:
            final_parent = character_paths[character][-1]
        else:
            final_parent = parent[node]
        subtree_sizes[final_parent] += subtree_sizes[node]

    return subtree_sizes
