def solve(arr):
    rank = {value: i + 1 for i, value in enumerate(sorted(set(arr)))}
    return [rank[value] for value in arr]
