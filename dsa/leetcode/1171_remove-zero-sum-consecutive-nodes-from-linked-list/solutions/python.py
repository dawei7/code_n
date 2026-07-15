class _DummyNode:
    def __init__(self, value: int, next_node=None):
        self.val = value
        self.next = next_node


def solve(head):
    dummy = _DummyNode(0, head)
    last = {}
    prefix = 0
    current = dummy

    while current is not None:
        prefix += current.val
        last[prefix] = current
        current = current.next

    prefix = 0
    current = dummy
    while current is not None:
        prefix += current.val
        current.next = last[prefix].next
        current = current.next

    return dummy.next
