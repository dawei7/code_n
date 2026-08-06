"""Naming-only minimum-removal backtracking candidate for LeetCode 301."""


def _remove_invalid(s: str) -> list[str]:
    remove_left = 0
    remove_right = 0
    for character in s:
        if character == "(":
            remove_left += 1
        elif character == ")":
            if remove_left:
                remove_left -= 1
            else:
                remove_right += 1

    results: set[str] = set()
    path: list[str] = []

    def search(i: int, balance: int, left: int, right: int) -> None:
        if len(s) - i < left + right:
            return
        if i == len(s):
            if balance == 0 and left == 0 and right == 0:
                results.add("".join(path))
            return

        character = s[i]
        if character == "(":
            if left:
                search(i + 1, balance, left - 1, right)
            path.append(character)
            search(i + 1, balance + 1, left, right)
            path.pop()
        elif character == ")":
            if right:
                search(i + 1, balance, left, right - 1)
            if balance:
                path.append(character)
                search(i + 1, balance - 1, left, right)
                path.pop()
        else:
            path.append(character)
            search(i + 1, balance, left, right)
            path.pop()

    search(0, 0, remove_left, remove_right)
    return sorted(results)


def solve(s: str) -> list[str]:
    return _remove_invalid(s)
