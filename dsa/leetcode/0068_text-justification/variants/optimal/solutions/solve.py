def solve(words: list[str], maxWidth: int) -> list[str]:
    lines: list[str] = []
    index = 0

    while index < len(words):
        start = index
        letters = 0
        while index < len(words) and letters + len(words[index]) + (index - start) <= maxWidth:
            letters += len(words[index])
            index += 1

        count = index - start
        if index == len(words) or count == 1:
            line = " ".join(words[start:index]).ljust(maxWidth)
        else:
            gaps = count - 1
            base, extra = divmod(maxWidth - letters, gaps)
            pieces: list[str] = []
            for offset in range(gaps):
                pieces.append(words[start + offset])
                pieces.append(" " * (base + (offset < extra)))
            pieces.append(words[index - 1])
            line = "".join(pieces)
        lines.append(line)

    return lines
