from collections import deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        length = len(num)
        positions = [deque() for _ in range(10)]
        for index, character in enumerate(num):
            positions[ord(character) - ord("0")].append(index)

        removed = [0] * (length + 1)

        def removed_through(index: int) -> int:
            total = 0
            index += 1
            while index > 0:
                total += removed[index]
                index -= index & -index
            return total

        def mark_removed(index: int) -> None:
            index += 1
            while index <= length:
                removed[index] += 1
                index += index & -index

        answer = []
        for _ in range(length):
            for digit in range(10):
                if not positions[digit]:
                    continue

                original_index = positions[digit][0]
                swaps = original_index - removed_through(original_index)
                if swaps > k:
                    continue

                k -= swaps
                positions[digit].popleft()
                mark_removed(original_index)
                answer.append(chr(ord("0") + digit))
                break

        return "".join(answer)
