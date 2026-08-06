def solve(matrix: list[list[str]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0])
    if columns <= rows:
        lines = matrix
        width = columns
    else:
        lines = zip(*matrix)
        width = rows

    dp = [0] * (width + 1)
    largest = 0
    for line in lines:
        diagonal = 0
        for c in range(1, width + 1):
            above = dp[c]
            if line[c - 1] == "1":
                dp[c] = 1 + min(dp[c], dp[c - 1], diagonal)
                largest = max(largest, dp[c])
            else:
                dp[c] = 0
            diagonal = above
    return largest * largest
