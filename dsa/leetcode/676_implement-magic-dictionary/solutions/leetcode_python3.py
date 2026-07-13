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

    def search(self, searchWord: str) -> bool:
        def matches(node, index, changed):
            if index == len(searchWord):
                return changed and self._END in node

            character = searchWord[index]
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

