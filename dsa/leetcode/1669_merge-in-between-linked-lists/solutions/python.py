def solve(list1, a: int, b: int, list2):
    before = list1
    for _ in range(a - 1):
        before = before.next

    after = before
    for _ in range(b - a + 2):
        after = after.next

    tail = list2
    while tail.next is not None:
        tail = tail.next

    before.next = list2
    tail.next = after
    return list1
