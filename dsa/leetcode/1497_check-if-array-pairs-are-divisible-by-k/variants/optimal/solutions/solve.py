from collections import Counter


def solve(arr, k):
    counts = Counter(value % k for value in arr)

    for remainder, count in counts.items():
        complement = (-remainder) % k
        if remainder == complement:
            if count % 2 != 0:
                return False
        elif count != counts[complement]:
            return False

    return True
