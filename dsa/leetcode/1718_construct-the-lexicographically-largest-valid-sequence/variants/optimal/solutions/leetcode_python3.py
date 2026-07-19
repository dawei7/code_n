class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def search(index: int) -> bool:
            while index < len(sequence) and sequence[index] != 0:
                index += 1
            if index == len(sequence):
                return True

            for value in range(n, 0, -1):
                if used[value]:
                    continue
                if value == 1:
                    sequence[index] = 1
                    used[1] = True
                    if search(index + 1):
                        return True
                    used[1] = False
                    sequence[index] = 0
                    continue

                paired_index = index + value
                if paired_index >= len(sequence) or sequence[paired_index] != 0:
                    continue
                sequence[index] = sequence[paired_index] = value
                used[value] = True
                if search(index + 1):
                    return True
                used[value] = False
                sequence[index] = sequence[paired_index] = 0

            return False

        search(0)
        return sequence
