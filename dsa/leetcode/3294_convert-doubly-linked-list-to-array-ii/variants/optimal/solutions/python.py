class _Node:
    def __init__(self, value: int) -> None:
        self.val = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


def solve(node: dict[str, object]) -> list[int]:
    values = list(node["values"])
    node_index = int(node["node_index"])
    nodes = [_Node(int(value)) for value in values]
    for index in range(1, len(nodes)):
        nodes[index - 1].next = nodes[index]
        nodes[index].prev = nodes[index - 1]

    current = nodes[node_index]
    while current.prev is not None:
        current = current.prev

    result = []
    while current is not None:
        result.append(current.val)
        current = current.next
    return result
