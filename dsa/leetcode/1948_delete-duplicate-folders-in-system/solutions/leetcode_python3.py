from collections import Counter
from typing import List


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.signature_id = 0


class Solution:
    def deleteDuplicateFolder(
        self,
        paths: List[List[str]],
    ) -> List[List[str]]:
        root = Node()
        for path in paths:
            node = root
            for name in path:
                node = node.children.setdefault(name, Node())

        signature_ids = {}
        frequencies = Counter()

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

        answer = []

        def collect(node: Node, path: List[str]) -> None:
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
