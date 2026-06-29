


def solve():
    def next_greater_elements(arr):
        n = len(arr)
        nge = [-1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    nge[i] = arr[j]
                    break

        print(" ".join(map(str, nge)))

    # Read input
    n = int(input())
    arr = list(map(int, input().split()))

    # Find next greater elements
    next_greater_elements(arr)


if __name__ == "__main__":
    solve()
