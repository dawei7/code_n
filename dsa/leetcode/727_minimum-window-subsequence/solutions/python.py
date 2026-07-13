def solve(s1: str, s2: str) -> str:
    target_length = len(s2)
    starts = [-1] * target_length
    best_start = -1
    best_length = len(s1) + 1

    for source_index, character in enumerate(s1):
        for target_index in range(target_length - 1, -1, -1):
            if character != s2[target_index]:
                continue
            if target_index == 0:
                starts[0] = source_index
            elif starts[target_index - 1] != -1:
                starts[target_index] = starts[target_index - 1]

        start = starts[-1]
        if start != -1 and source_index - start + 1 < best_length:
            best_start = start
            best_length = source_index - start + 1

    return "" if best_start == -1 else s1[best_start : best_start + best_length]
