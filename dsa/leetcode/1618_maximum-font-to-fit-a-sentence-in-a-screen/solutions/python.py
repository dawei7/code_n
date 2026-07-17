from collections import Counter


def solve(text: str, w: int, h: int, fonts: list[int], fontInfo) -> int:
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
