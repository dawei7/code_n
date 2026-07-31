def solve(arr: list[str]) -> list[str]:
    owner_counts: dict[str, int] = {}

    for word in arr:
        word_substrings: set[str] = set()
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                word_substrings.add(word[start:end])
        for substring in word_substrings:
            owner_counts[substring] = owner_counts.get(substring, 0) + 1

    answer: list[str] = []
    for word in arr:
        best = ""
        for start in range(len(word)):
            for end in range(start + 1, len(word) + 1):
                substring = word[start:end]
                if owner_counts[substring] != 1:
                    continue
                if not best or len(substring) < len(best) or (len(substring) == len(best) and substring < best):
                    best = substring
        answer.append(best)

    return answer
