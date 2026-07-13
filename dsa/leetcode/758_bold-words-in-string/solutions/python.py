def solve(words: list[str], s: str) -> str:
    terminal = "#"
    trie: dict[str, dict] = {}
    longest = 0

    for word in words:
        node = trie
        for character in word:
            node = node.setdefault(character, {})
        node[terminal] = {}
        longest = max(longest, len(word))

    difference = [0] * (len(s) + 1)
    for start in range(len(s)):
        node = trie
        farthest_end = -1
        for end in range(start, min(len(s), start + longest)):
            node = node.get(s[end])
            if node is None:
                break
            if terminal in node:
                farthest_end = end + 1
        if farthest_end >= 0:
            difference[start] += 1
            difference[farthest_end] -= 1

    output: list[str] = []
    coverage = 0
    bold_open = False
    for index, character in enumerate(s):
        coverage += difference[index]
        if coverage > 0 and not bold_open:
            output.append("<b>")
            bold_open = True
        elif coverage == 0 and bold_open:
            output.append("</b>")
            bold_open = False
        output.append(character)

    if bold_open:
        output.append("</b>")
    return "".join(output)
