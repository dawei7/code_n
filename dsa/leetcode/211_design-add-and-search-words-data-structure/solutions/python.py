def solve(operations: list[list[str]]) -> list[bool]:
    root: dict = {}
    results: list[bool] = []

    def search(pattern: str) -> bool:
        states = [root]
        for character in pattern:
            next_states = []
            for node in states:
                if character == ".":
                    next_states.extend(child for key, child in node.items() if key is not None)
                elif character in node:
                    next_states.append(node[character])
            states = next_states
            if not states:
                return False
        return any(None in node for node in states)

    for operation, value in operations:
        if operation == "addWord":
            node = root
            for character in value:
                node = node.setdefault(character, {})
            node[None] = {}
        else:
            results.append(search(value))
    return results
