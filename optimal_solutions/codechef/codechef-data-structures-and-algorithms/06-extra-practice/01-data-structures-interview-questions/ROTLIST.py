


def solve():
    def rotateRight(head, R):
        if not head or not head.next or R == 0:
            return head
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head
        R = R % length
        steps_to_new_tail = length - R - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head


if __name__ == "__main__":
    solve()
