"""Solution for linked_list_05: Reverse in Groups of K.

Reverse the linked list in chunks of k nodes. The first
chunk's tail becomes the new list's head; the tail of
each chunk points to the next chunk's (reversed) head.
If the last chunk has fewer than k nodes, leave it alone.
Source: https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/

Inputs passed to solve():
    values: list of n values.
    next: list of n next-pointers (parallel to values).
    head: head node index.
    k: group size (1..3 in the setup).
    n: length of the list.

Goal:
    (new_values, new_next, new_head) - the k-group-reversed list.

Samples:
Sample 1 input:  values = [1, 2, 3, 4, 5], next = [1, 2, 3, 4, -1], head = 0, k = 2, n = 5
Sample 1 output: list = [2, 1, 4, 3, 5]; new_head = 1


"""

def solve(values, next, head, k, n):
    # Write your code here.
    return None
