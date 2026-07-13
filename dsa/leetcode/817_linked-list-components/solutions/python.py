class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None, nums: list[int]) -> int:
    selected = set(nums)
    components = 0
    current = head
    while current is not None:
        if current.val in selected and (
            current.next is None or current.next.val not in selected
        ):
            components += 1
        current = current.next
    return components
