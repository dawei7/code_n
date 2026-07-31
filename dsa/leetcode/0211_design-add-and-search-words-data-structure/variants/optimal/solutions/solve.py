class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for character in word:
            node = node.setdefault(character, {})
        node[None] = {}

    def search(self, word: str) -> bool:
        states = [self.root]
        for character in word:
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


def solve(operations: list[list[str]]) -> list[bool]:
    dictionary = WordDictionary()
    results: list[bool] = []
    for operation, value in operations:
        if operation == "addWord":
            dictionary.addWord(value)
        elif operation == "search":
            results.append(dictionary.search(value))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return results
