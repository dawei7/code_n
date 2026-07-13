def solve(operations: list[list[str]]) -> list[bool]:
    root: dict = {}
    results: list[bool] = []
    for operation, value in operations:
        if operation == "insert":
            node = root
            for character in value:
                node = node.setdefault(character, {})
            node[None] = {}
            continue
        node = root
        for character in value:
            if character not in node:
                node = None
                break
            node = node[character]
        results.append(node is not None and (operation == "startsWith" or None in node))
    return results
