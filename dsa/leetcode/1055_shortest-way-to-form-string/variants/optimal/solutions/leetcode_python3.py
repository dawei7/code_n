class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_length = len(source)
        next_position = [
            [-1] * 26
            for _ in range(source_length + 1)
        ]

        for index in range(source_length - 1, -1, -1):
            next_position[index] = next_position[index + 1][:]
            next_position[index][ord(source[index]) - ord("a")] = index

        subsequences = 1
        source_index = 0

        for character in target:
            letter = ord(character) - ord("a")
            position = next_position[source_index][letter]
            if position < 0:
                subsequences += 1
                position = next_position[0][letter]
                if position < 0:
                    return -1
            source_index = position + 1

        return subsequences

