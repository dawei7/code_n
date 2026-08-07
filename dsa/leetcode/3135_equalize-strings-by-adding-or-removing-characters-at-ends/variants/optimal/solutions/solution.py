class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        previous = [0] * (len(target) + 1)
        longest = 0

        for initial_char in initial:
            current = [0] * (len(target) + 1)

            for target_index, target_char in enumerate(target, 1):
                if initial_char == target_char:
                    current[target_index] = previous[target_index - 1] + 1
                    if current[target_index] > longest:
                        longest = current[target_index]

            previous = current

        return len(initial) + len(target) - 2 * longest
