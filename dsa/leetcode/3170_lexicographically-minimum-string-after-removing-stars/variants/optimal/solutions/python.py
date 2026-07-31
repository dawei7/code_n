def solve(s: str) -> str:
    positions = [[] for _ in range(26)]
    removed = [False] * len(s)

    for index, character in enumerate(s):
        if character == "*":
            removed[index] = True
            for bucket in positions:
                if bucket:
                    removed[bucket.pop()] = True
                    break
        else:
            positions[ord(character) - ord("a")].append(index)

    return "".join(
        character
        for index, character in enumerate(s)
        if not removed[index]
    )
