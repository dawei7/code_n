def solve(arr, a, b, c):
    good = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    good += 1
    return good
