


def solve():
    def search_insert_position(arr, n, k):
        left = 0
        right = n - 1

        while left <= right:
            middle = (left + right) // 2

            if arr[middle] == k:
                return middle
            elif arr[middle] > k:
                right = middle - 1
            else:
                left = middle + 1

        return left


if __name__ == "__main__":
    solve()
