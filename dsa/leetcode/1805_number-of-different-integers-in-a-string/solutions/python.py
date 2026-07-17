def solve(word: str) -> int:
    distinct = set()
    start = 0

    while start < len(word):
        if not word[start].isdigit():
            start += 1
            continue

        end = start
        while end < len(word) and word[end].isdigit():
            end += 1

        normalized = word[start:end].lstrip("0")
        distinct.add(normalized or "0")
        start = end

    return len(distinct)
