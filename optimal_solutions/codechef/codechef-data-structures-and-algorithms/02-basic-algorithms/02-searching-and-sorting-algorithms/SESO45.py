


def solve():
    def counting_sort(arr):
        if len(arr) == 0:
            return arr

        # Find the maximum value in the array
        max_val = max(arr)

        # Create count array with all zeros
        count = [0] * (max_val + 1)

        # Store the count of each element in count array
        for num in arr:
            count[num] += 1

        # Build the output array using the count array
        sorted_index = 0
        for i, cnt in enumerate(count):
            while cnt > 0:
                arr[sorted_index] = i
                sorted_index += 1
                cnt -= 1

        return arr


if __name__ == "__main__":
    solve()
