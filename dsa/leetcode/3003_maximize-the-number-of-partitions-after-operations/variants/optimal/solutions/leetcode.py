class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        states = {(0, False): 0}

        for character in s:
            original = ord(character) - ord("a")
            next_states = {}

            for (mask, changed), partitions in states.items():
                choices = (original,) if changed else range(26)
                for letter in choices:
                    merged = mask | (1 << letter)
                    next_changed = changed or letter != original

                    if merged.bit_count() > k:
                        key = (1 << letter, next_changed)
                        score = partitions + 1
                    else:
                        key = (merged, next_changed)
                        score = partitions

                    next_states[key] = max(next_states.get(key, -1), score)

            states = next_states

        return max(states.values()) + 1
