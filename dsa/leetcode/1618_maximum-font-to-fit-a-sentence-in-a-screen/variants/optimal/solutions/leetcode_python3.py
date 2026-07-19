from collections import Counter
from typing import List


class Solution:
    def maxFont(
        self,
        text: str,
        w: int,
        h: int,
        fonts: List[int],
        fontInfo: "FontInfo",
    ) -> int:
        frequencies = Counter(text)

        def fits(font: int) -> bool:
            if fontInfo.getHeight(font) > h:
                return False
            width = sum(
                frequency * fontInfo.getWidth(font, character)
                for character, frequency in frequencies.items()
            )
            return width <= w

        left = 0
        right = len(fonts) - 1
        answer = -1
        while left <= right:
            middle = (left + right) // 2
            if fits(fonts[middle]):
                answer = fonts[middle]
                left = middle + 1
            else:
                right = middle - 1
        return answer
