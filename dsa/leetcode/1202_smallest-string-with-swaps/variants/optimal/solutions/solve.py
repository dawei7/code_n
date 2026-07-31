from collections import defaultdict


def solve(s: str, pairs: list[list[int]]) -> str:
    parent = list(range(len(s)))
    size = [1] * len(s)

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for first, second in pairs:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            continue
        if size[first_root] < size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        size[first_root] += size[second_root]

    characters = defaultdict(list)
    for index, character in enumerate(s):
        characters[find(index)].append(character)
    for group in characters.values():
        group.sort(reverse=True)

    return "".join(characters[find(index)].pop() for index in range(len(s)))
