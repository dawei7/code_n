"""Optimal solution for trie_04: Delete Word from Trie.

Decrement per-node counts along the path. The word is
still present iff some other word shares the same path.
"""


def solve(words, n, target):
    children = []
    is_end = []
    count = []

    def new_node():
        children.append({})
        is_end.append(False)
        count.append(0)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        count[cur] += 1
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
            count[cur] += 1
        is_end[cur] = True
    cur = root
    count[cur] -= 1
    for ch in target:
        if ch not in children[cur]:
            return target in words
        cur = children[cur][ch]
        count[cur] -= 1
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur] and count[cur] > 0
