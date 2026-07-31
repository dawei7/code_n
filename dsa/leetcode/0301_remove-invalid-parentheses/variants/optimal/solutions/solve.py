"""Minimum-removal backtracking for LeetCode 301."""


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

    def search(index: int, balance: int, left: int, right: int) -> None:
        if len(s) - index < left + right:
            return
        if index == len(s):
            if balance == 0 and left == 0 and right == 0:
                results.add("".join(path))
            return

        character = s[index]
        if character == "(":
            if left:
                search(index + 1, balance, left - 1, right)
            path.append(character)
            search(index + 1, balance + 1, left, right)
            path.pop()
        elif character == ")":
            if right:
                search(index + 1, balance, left, right - 1)
            if balance:
                path.append(character)
                search(index + 1, balance - 1, left, right)
                path.pop()
        else:
            path.append(character)
            search(index + 1, balance, left, right)
            path.pop()

    search(0, 0, remove_left, remove_right)
    return sorted(results)


def solve(s: str) -> list[str]:
    return _remove_invalid(s)
