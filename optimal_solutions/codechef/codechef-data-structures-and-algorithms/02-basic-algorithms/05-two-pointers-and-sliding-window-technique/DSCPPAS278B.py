


def solve():
    def max_sum_k_elements(arr, k):
        n = len(arr)

        # Calculate the sum of the first k elements
        current_sum = sum(arr[:k])

        # This is the initial maximum sum (taking all k elements from the start)
        max_sum = current_sum

        # Two-pointer technique: start from the end of the array and replace elements from the start
        for i in range(k):
            current_sum = current_sum - arr[k - 1 - i] + arr[n - 1 - i]
            max_sum = max(max_sum, current_sum)

        return max_sum

    if __name__ == "__main__":
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))

        print(max_sum_k_elements(arr, k))


if __name__ == "__main__":
    solve()
