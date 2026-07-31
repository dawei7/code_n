def solve(s):
    first = [len(s)] * 1024
    first[0] = -1
    mask = 0
    answer = 1

    for index, character in enumerate(s):
        mask ^= 1 << int(character)
        answer = max(answer, index - first[mask])
        for digit in range(10):
            answer = max(answer, index - first[mask ^ (1 << digit)])
        if first[mask] == len(s):
            first[mask] = index

    return answer
