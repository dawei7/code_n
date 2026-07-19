from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        seen = {s1}

        while queue:
            current, swaps = queue.popleft()
            first_mismatch = next(
                index for index in range(len(current)) if current[index] != s2[index]
            )

            for index in range(first_mismatch + 1, len(current)):
                if current[index] != s2[first_mismatch] or current[index] == s2[index]:
                    continue

                characters = list(current)
                characters[first_mismatch], characters[index] = (
                    characters[index],
                    characters[first_mismatch],
                )
                neighbor = "".join(characters)
                if neighbor == s2:
                    return swaps + 1
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, swaps + 1))

        return 0
