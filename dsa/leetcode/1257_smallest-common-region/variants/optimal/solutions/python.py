from typing import List


def solve(regions: List[List[str]], region1: str, region2: str) -> str:
    parent: dict[str, str] = {}
    for group in regions:
        for child in group[1:]:
            parent[child] = group[0]

    ancestors: set[str] = set()
    current = region1
    while True:
        ancestors.add(current)
        if current not in parent:
            break
        current = parent[current]

    current = region2
    while current not in ancestors:
        current = parent[current]
    return current
