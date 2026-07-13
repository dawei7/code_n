def solve(arr):
    if len(arr) <= 2:
        return True
    ordered = sorted(arr)
    diff = ordered[1] - ordered[0]
    return all(ordered[i] - ordered[i - 1] == diff for i in range(2, len(ordered)))
