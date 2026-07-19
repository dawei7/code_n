from functools import lru_cache


def solve(s1: str, s2: str) -> bool:
    @lru_cache(None)
    def compatible(first: int, second: int, balance: int) -> bool:
        if first == len(s1) and second == len(s2):
            return balance == 0

        if first < len(s1) and s1[first].isdigit():
            value = 0
            for end in range(first, min(first + 3, len(s1))):
                if not s1[end].isdigit():
                    break
                value = value * 10 + int(s1[end])
                if compatible(end + 1, second, balance + value):
                    return True

        if second < len(s2) and s2[second].isdigit():
            value = 0
            for end in range(second, min(second + 3, len(s2))):
                if not s2[end].isdigit():
                    break
                value = value * 10 + int(s2[end])
                if compatible(first, end + 1, balance - value):
                    return True

        if balance > 0:
            return (
                second < len(s2)
                and s2[second].isalpha()
                and compatible(first, second + 1, balance - 1)
            )
        if balance < 0:
            return (
                first < len(s1)
                and s1[first].isalpha()
                and compatible(first + 1, second, balance + 1)
            )
        return (
            first < len(s1)
            and second < len(s2)
            and s1[first].isalpha()
            and s2[second].isalpha()
            and s1[first] == s2[second]
            and compatible(first + 1, second + 1, 0)
        )

    return compatible(0, 0, 0)
