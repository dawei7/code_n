def solve(mat, k):
    strengths = [(sum(row), i) for i, row in enumerate(mat)]
    strengths.sort()
    return [i for _, i in strengths[:k]]
