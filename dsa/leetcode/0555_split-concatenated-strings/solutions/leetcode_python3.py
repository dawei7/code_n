from typing import List


class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        oriented = [max(value, value[::-1]) for value in strs]
        best = ""

        for split_index, original in enumerate(strs):
            middle = "".join(
                oriented[split_index + 1 :] + oriented[:split_index]
            )

            for split_word in (original, original[::-1]):
                for cut in range(len(split_word)):
                    candidate = (
                        split_word[cut:] + middle + split_word[:cut]
                    )
                    if candidate > best:
                        best = candidate

        return best

