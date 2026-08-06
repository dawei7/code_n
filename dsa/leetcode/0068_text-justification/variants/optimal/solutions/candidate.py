def solve(words: list[str], maxWidth: int) -> list[str]:
    lines: list[str] = []
    i = 0

    while i < len(words):
        start = i
        letters = 0
        while i < len(words) and letters + len(words[i]) + (i - start) <= maxWidth:
            letters += len(words[i])
            i += 1

        count = i - start
        if i == len(words) or count == 1:
            line = " ".join(words[start:i]).ljust(maxWidth)
        else:
            gaps = count - 1
            base, extra = divmod(maxWidth - letters, gaps)
            pieces: list[str] = []
            for j in range(gaps):
                pieces.append(words[start + j])
                pieces.append(" " * (base + (j < extra)))
            pieces.append(words[i - 1])
            line = "".join(pieces)
        lines.append(line)

    return lines
