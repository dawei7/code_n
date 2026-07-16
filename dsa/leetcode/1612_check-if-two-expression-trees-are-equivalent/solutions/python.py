from collections import defaultdict


def solve(root1, root2) -> bool:
    balance: dict[str, int] = defaultdict(int)

    def collect(node, delta: int) -> None:
        if node.val == "+":
            collect(node.left, delta)
            collect(node.right, delta)
        else:
            balance[node.val] += delta

    collect(root1, 1)
    collect(root2, -1)
    return all(count == 0 for count in balance.values())
