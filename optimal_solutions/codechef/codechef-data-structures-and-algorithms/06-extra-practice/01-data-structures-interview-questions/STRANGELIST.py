


def solve():
    def flatten(head):
        if not head:
            return head
        stack = []
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child = None
            if not curr.next and stack:
                curr.next = stack.pop()
            curr = curr.next
        return head


if __name__ == "__main__":
    solve()
