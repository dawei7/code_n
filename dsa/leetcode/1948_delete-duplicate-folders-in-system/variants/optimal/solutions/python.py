from collections import Counter


class Node:
    def __init__(self) -> None:
        self.children: dict[str, Node] = {}
        self.signature_id = 0


def solve(paths: list[list[str]]) -> list[list[str]]:
    root = Node()
    for path in paths:
        node = root
        for name in path:
            node = node.children.setdefault(name, Node())

    signature_ids: dict[tuple[tuple[str, int], ...], int] = {}
    frequencies: Counter[int] = Counter()

    def encode(node: Node, is_root: bool = False) -> int:
        signature = tuple(
            (name, encode(child))
            for name, child in sorted(node.children.items())
        )
        if signature:
            signature_id = signature_ids.setdefault(
                signature,
                len(signature_ids) + 1,
            )
            node.signature_id = signature_id
            if not is_root:
                frequencies[signature_id] += 1
        return node.signature_id

    encode(root, True)

    answer: list[list[str]] = []

    def collect(node: Node, path: list[str]) -> None:
        for name, child in sorted(node.children.items()):
            if (
                child.signature_id
                and frequencies[child.signature_id] > 1
            ):
                continue
            path.append(name)
            answer.append(path.copy())
            collect(child, path)
            path.pop()

    collect(root, [])
    return answer
