def solve(s: str, k: int) -> bool:
    if k == 0:
        return True

    first = [len(s)] * 26
    last = [-1] * 26
    for index, character in enumerate(s):
        code = ord(character) - ord("a")
        first[code] = min(first[code], index)
        last[code] = index

    intervals = []
    for code in range(26):
        if last[code] == -1:
            continue

        left = first[code]
        right = last[code]
        index = left
        valid = True

        while index <= right:
            nested = ord(s[index]) - ord("a")
            if first[nested] < left:
                valid = False
                break
            right = max(right, last[nested])
            index += 1

        if valid and not (left == 0 and right == len(s) - 1):
            intervals.append((right, left))

    intervals.sort()
    selected = 0
    previous_end = -1

    for right, left in intervals:
        if left > previous_end:
            selected += 1
            previous_end = right
            if selected >= k:
                return True

    return False
