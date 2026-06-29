


def solve():
    def get_max(arr):
        return max(arr)

    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Count occurrences of digits based on the current exponent
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        # Update count array to contain actual positions of digits in output
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build output array
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy the sorted values to the original array
        for i in range(n):
            arr[i] = output[i]

    def radix_sort(arr):
        max_val = get_max(arr)

        # Apply counting sort to each digit
        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10


if __name__ == "__main__":
    solve()
