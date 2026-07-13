def _normalize(revision: str) -> str:
    normalized = revision.lstrip("0")
    return normalized or "0"


def solve(version1: str, version2: str) -> int:
    first = version1.split(".")
    second = version2.split(".")
    for index in range(max(len(first), len(second))):
        left = _normalize(first[index] if index < len(first) else "0")
        right = _normalize(second[index] if index < len(second) else "0")
        if len(left) != len(right):
            return -1 if len(left) < len(right) else 1
        if left != right:
            return -1 if left < right else 1
    return 0
