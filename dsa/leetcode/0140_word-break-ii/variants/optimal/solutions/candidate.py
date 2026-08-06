from functools import cache


def solve(s: str, wordDict: list[str]) -> list[str]:
    words = set(wordDict)
    max_word_length = min(len(s), max(map(len, words)))

    @cache
    def sentences(start: int) -> tuple[str, ...]:
        if start == len(s):
            return ("",)
        result: list[str] = []
        for end in range(start + 1, min(len(s), start + max_word_length) + 1):
            word = s[start:end]
            if word in words:
                for suffix in sentences(end):
                    result.append(word if not suffix else word + " " + suffix)
        return tuple(result)

    return list(sentences(0))
