"""Optimal solution for linked_list_05: Reverse in Groups of K.

Walk the list in chunks of k; reverse each chunk. The trick is
to thread the previous chunk's tail to the current chunk's
new head. Return (new_values, new_next, new_head).
"""


def solve(values, next, head, k, n):
    if n == 0 or head == -1 or k <= 1:
        return list(values), list(next), head
    new_next = list(next)
    prev_tail_new = -1
    cur = head
    new_head = -1
    while cur != -1:
        chunk = []
        c = cur
        for _ in range(k):
            if c == -1:
                break
            chunk.append(c)
            c = new_next[c]
        if len(chunk) < k:
            if prev_tail_new != -1:
                new_next[prev_tail_new] = chunk[0]
            break
        for i in range(len(chunk) - 1, 0, -1):
            new_next[chunk[i]] = chunk[i - 1]
        new_next[chunk[0]] = c
        if prev_tail_new != -1:
            new_next[prev_tail_new] = chunk[-1]
        else:
            new_head = chunk[-1]
        prev_tail_new = chunk[0]
        cur = c
    if new_head == -1:
        new_head = head
    return list(values), new_next, new_head
