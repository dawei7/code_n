import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = (data[0], data[1])
    arr = data[2:2 + n]
    j = n - 1
    answer_i = answer_j = -1
    for i in range(n):
        if i >= j:
            break
        while j >= 0 and arr[i] + arr[j] > k:
            j -= 1
        if j >= 0 and arr[i] + arr[j] == k:
            answer_i, answer_j = (i, j)
    print(answer_i, answer_j)


if __name__ == "__main__":
    solve()
