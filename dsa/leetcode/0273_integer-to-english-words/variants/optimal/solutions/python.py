BELOW_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
SCALES = ["", "Thousand", "Million", "Billion"]


def _chunk_words(value: int) -> list[str]:
    words: list[str] = []
    if value >= 100:
        words.extend((BELOW_TWENTY[value // 100], "Hundred"))
        value %= 100
    if value >= 20:
        words.append(TENS[value // 10])
        value %= 10
    if value:
        words.append(BELOW_TWENTY[value])
    return words


def solve(num: int) -> str:
    if num == 0:
        return "Zero"
    groups: list[list[str]] = []
    scale = 0
    while num:
        chunk = num % 1000
        if chunk:
            words = _chunk_words(chunk)
            if SCALES[scale]:
                words.append(SCALES[scale])
            groups.append(words)
        num //= 1000
        scale += 1
    return " ".join(word for group in reversed(groups) for word in group)
