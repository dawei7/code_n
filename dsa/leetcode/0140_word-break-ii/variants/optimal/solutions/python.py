from functools import cache


def solve(s: str, word_dict: list[str]) -> list[str]:
    words = set(word_dict)

    @cache
    def sentences(start: int) -> tuple[str, ...]:
        if start == len(s):
            return ("",)
        result: list[str] = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word not in words:
                continue
            for suffix in sentences(end):
                result.append(word if not suffix else word + " " + suffix)
        return tuple(result)

    return list(sentences(0))
