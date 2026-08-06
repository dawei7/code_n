def solve(s: str, wordDict: list[str]) -> bool:
    terminal = None
    trie = {}
    max_word_length = 0
    for word in wordDict:
        node = trie
        for c in word:
            node = node.setdefault(c, {})
        node[terminal] = {}
        max_word_length = max(max_word_length, len(word))

    reachable = [False] * (len(s) + 1)
    reachable[0] = True
    for start in range(len(s)):
        if not reachable[start]:
            continue
        node = trie
        for end in range(start, min(len(s), start + max_word_length)):
            c = s[end]
            if c not in node:
                break
            node = node[c]
            if terminal in node:
                reachable[end + 1] = True
    return reachable[-1]
