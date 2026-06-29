class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def remove(head, position):
    if not head:
        return head
    if position == 1:
        return head.next
    current = head
    count = 1
    while current and count < position - 1:
        current = current.next
        count += 1
    if current and current.next:
        current.next = current.next.next
    return head

def insert(head, position, value):
    new_node = Node(value)
    if position == 1:
        new_node.next = head
        return new_node
    current = head
    count = 1
    while current and count < position - 1:
        current = current.next
        count += 1
    if current:
        new_node.next = current.next
        current.next = new_node
    return head

def print_list(head):
    res = []
    current = head
    while current:
        res.append(str(current.val))
        current = current.next
    print(' '.join(res))

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1
    q = int(data[idx])
    idx += 1
    head = None
    tail = None
    for _ in range(n):
        num = int(data[idx])
        idx += 1
        node = Node(num)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    for _ in range(q):
        op = int(data[idx])
        idx += 1
        if op == 0:
            pos = int(data[idx])
            idx += 1
            head = remove(head, pos)
            print_list(head)
        else:
            pos = int(data[idx])
            idx += 1
            value = int(data[idx])
            idx += 1
            head = insert(head, pos, value)
            print_list(head)


if __name__ == "__main__":
    solve()
