from functools import lru_cache


def solve(s: str) -> int:
    compressed = "".join(character for index, character in enumerate(s) if index == 0 or character != s[index - 1])

    @lru_cache(None)
    def turns(left: int, right: int) -> int:
        if left > right:
            return 0
        answer = 1 + turns(left + 1, right)
        for middle in range(left + 1, right + 1):
            if compressed[middle] == compressed[left]:
                answer = min(answer, turns(left + 1, middle - 1) + turns(middle, right))
        return answer

    return turns(0, len(compressed) - 1)
