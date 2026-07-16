def solve(arr, k):
    champion = arr[0]
    streak = 0
    for challenger in arr[1:]:
        if champion > challenger:
            streak += 1
        else:
            champion = challenger
            streak = 1
        if streak == k:
            return champion
    return champion
