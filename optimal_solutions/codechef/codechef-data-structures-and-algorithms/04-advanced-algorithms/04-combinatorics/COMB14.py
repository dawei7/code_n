


def solve():
    def selection_sort(arr, n):
        for i in range(n):
            min_val = arr[i]
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < min_val:
                    min_val = arr[j]
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    if __name__ == "__main__":
        n = int(input())

        arr = [int(x) for x in input().split()]

        selection_sort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()


if __name__ == "__main__":
    solve()
