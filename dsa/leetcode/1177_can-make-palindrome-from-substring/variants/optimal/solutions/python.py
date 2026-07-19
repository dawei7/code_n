def solve(s, queries):
    masks = [0]
    for ch in s:
        masks.append(masks[-1] ^ (1 << (ord(ch) - ord("a"))))

    answers = []
    for left, right, k in queries:
        odd_count = (masks[right + 1] ^ masks[left]).bit_count()
        answers.append(odd_count // 2 <= k)
    return answers
