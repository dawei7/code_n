def solve(arr, k):
    if not arr:
        return 0
    champion = arr[0]
    streak = 0
    needed = max(1, k)
    maximum = max(arr)
    for challenger in arr[1:]:
        if champion > challenger:
            streak += 1
        else:
            champion = challenger
            streak = 1
        if streak >= needed or champion == maximum:
            return champion
    return champion
