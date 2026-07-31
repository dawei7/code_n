class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.indices = list(range(combinationLength))
        self.available = True

    def next(self) -> str:
        result = "".join(self.characters[index] for index in self.indices)
        position = len(self.indices) - 1
        while position >= 0 and self.indices[position] == len(self.characters) - len(self.indices) + position:
            position -= 1
        if position < 0:
            self.available = False
        else:
            self.indices[position] += 1
            for suffix in range(position + 1, len(self.indices)):
                self.indices[suffix] = self.indices[suffix - 1] + 1
        return result

    def hasNext(self) -> bool:
        return self.available
