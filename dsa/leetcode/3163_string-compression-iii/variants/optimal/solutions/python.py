def solve(word: str) -> str:
    pieces: list[str] = []
    start = 0
    while start < len(word):
        end = start
        while end < len(word) and word[end] == word[start] and end - start < 9:
            end += 1
        pieces.append(str(end - start))
        pieces.append(word[start])
        start = end
    return "".join(pieces)
