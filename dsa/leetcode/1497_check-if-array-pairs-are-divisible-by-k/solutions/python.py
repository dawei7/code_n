from collections import Counter


def solve(arr, k):
    k = abs(int(k)) or 1
    counts = Counter(num % k for num in arr)
    if counts.get(0, 0) % 2:
        return False
    for rem in range(1, k):
        if counts.get(rem, 0) != counts.get((-rem) % k, 0):
            return False
    return True
