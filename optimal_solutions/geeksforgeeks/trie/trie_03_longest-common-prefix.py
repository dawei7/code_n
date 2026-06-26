"""Optimal solution for trie_03: Longest Common Prefix.

Walk the trie from the root. While the current node has
exactly one child and is not a word end, descend.
"""


def solve(words, n):
    if n == 0:
        return ""
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    out = []
    cur = root
    while len(children[cur]) == 1 and not is_end[cur]:
        ch, nxt = next(iter(children[cur].items()))
        out.append(ch)
        cur = nxt
    return "".join(out)
