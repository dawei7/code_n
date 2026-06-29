


def solve():
    def insertNode(head, position, value):
        new_node = Node(value)
        # Insert at the beginning
        if position == 1:
            new_node.next = head
            if head:
                head.prev = new_node
            return new_node
        # Traverse to the node before the insertion point
        curr = head
        curr_pos = 1
        while curr_pos < position - 1:
            curr = curr.next
            curr_pos += 1
        # Insert new_node after curr
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        return head

    def deleteNode(head, position):
        # Delete the first node and update head
        if position == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        # Traverse to the node at the given position
        curr = head
        curr_pos = 1
        while curr_pos < position:
            curr = curr.next
            curr_pos += 1
        # Remove curr from the list
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        return head


if __name__ == "__main__":
    solve()
