


def solve():
    def first_occurrence(arr, n, target):
        left, right = 0, n
        while right - left > 1:
            middle = (right + left) // 2
            if arr[middle] >= target:
                right = middle
            else:
                left = middle
        return right

    def last_occurrence(arr, n, target):
        left, right = 0, n
        while right - left > 1:
            middle = (right + left) // 2
            if arr[middle] > target:
                right = middle
            else:
                left = middle
        return left

    def count_occurrences(arr, n, target):
        return last_occurrence(arr, n, target) - first_occurrence(arr, n, target) + 1


if __name__ == "__main__":
    solve()
