class MagicDictionary:
    _END = "$"

    def __init__(self):
        self.root = {}

    def buildDict(self, dictionary: list[str]) -> None:
        self.root = {}
        for word in dictionary:
            node = self.root
            for character in word:
                node = node.setdefault(character, {})
            node[self._END] = True

    def search(self, search_word: str) -> bool:
        def matches(node, index, changed):
            if index == len(search_word):
                return changed and self._END in node

            character = search_word[index]
            exact = node.get(character)
            if exact is not None and matches(exact, index + 1, changed):
                return True

            if not changed:
                for next_character, child in node.items():
                    if next_character not in (self._END, character):
                        if matches(child, index + 1, True):
                            return True
            return False

        return matches(self.root, 0, False)


def solve(operations: list[str], arguments: list[list]) -> list[bool | None]:
    dictionary = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == "MagicDictionary":
            dictionary = MagicDictionary()
            output.append(None)
        elif operation == "buildDict":
            assert dictionary is not None
            dictionary.buildDict(args[0])
            output.append(None)
        elif operation == "search":
            assert dictionary is not None
            output.append(dictionary.search(args[0]))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output

