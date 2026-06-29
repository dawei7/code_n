import sys

def next_permutation_manual(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i < 0:
        arr.sort()
        return arr
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = (arr[j], arr[i])
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    N, K = map(int, data[:2])
    index = 2
    for _ in range(K):
        permutation = list(map(int, data[index:index + N]))
        index += N
        next_permutation_manual(permutation)
        print(' '.join(map(str, permutation)))


if __name__ == "__main__":
    solve()
