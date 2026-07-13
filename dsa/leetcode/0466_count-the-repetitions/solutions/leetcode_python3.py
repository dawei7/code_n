class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        target_index = 0
        completed = 0
        blocks = 0
        seen = {0: (0, 0)}
        while blocks < n1:
            for character in s1:
                if character == s2[target_index]:
                    target_index += 1
                    if target_index == len(s2):
                        target_index = 0
                        completed += 1
            blocks += 1

            if target_index in seen:
                previous_blocks, previous_completed = seen[target_index]
                cycle_blocks = blocks - previous_blocks
                cycle_completed = completed - previous_completed
                cycles = (n1 - blocks) // cycle_blocks
                blocks += cycles * cycle_blocks
                completed += cycles * cycle_completed
                seen.clear()
            else:
                seen[target_index] = (blocks, completed)

        return completed // n2
