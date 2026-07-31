from typing import List


def solve(
    s: str,
    sub: str,
    mappings: List[List[str]],
) -> bool:
    replacements = {(old, new) for old, new in mappings}
    width = len(sub)

    return any(
        all(
            old == new or (old, new) in replacements
            for old, new in zip(sub, s[start : start + width])
        )
        for start in range(len(s) - width + 1)
    )
