class CombinationIterator:
    def __init__(self, characters, combination_length):
        self.characters = characters
        self.indices = list(range(combination_length))
        self.available = True

    def next(self):
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

    def hasNext(self):
        return self.available


def solve(characters, combination_length, operations):
    iterator = CombinationIterator(characters, combination_length)
    output = []
    for method, arguments in operations:
        if method == "next":
            output.append(iterator.next(*arguments))
        elif method == "hasNext":
            output.append(iterator.hasNext(*arguments))
        else:
            raise ValueError(f"unknown operation: {method}")
    return output
