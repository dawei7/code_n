"""Optimal solution for trie_02: Word Count with Prefix.

Count the words in the trie that start with prefix.
"""


def solve(words, n, prefix):
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
    cur = root
    for ch in prefix:
        if ch not in children[cur]:
            return 0
        cur = children[cur][ch]
    count = 0

    def dfs(i):
        nonlocal count
        if is_end[i]:
            count += 1
        for nxt in children[i].values():
            dfs(nxt)

    dfs(cur)
    return count
