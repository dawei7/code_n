


def solve():
    def largest_subarray_with_sum_zero(arr):
        prefix_map = {}
        prefix_sum = 0
        max_len = 0

        for i, val in enumerate(arr):
            prefix_sum += val

            if prefix_sum == 0:
                max_len = i + 1  # sum from 0..i is 0

            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum] = i  # store first occurrence

        return max_len


if __name__ == "__main__":
    solve()
