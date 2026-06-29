


def solve():
    def subarray_sum(nums, n, k):
        count = 0
        sum_ = 0
        sum_map = {0: 1}  # Initialize map with sum 0 occurring once

        for num in nums:
            sum_ += num

            # Check if (sum - k) exists in the map
            if (sum_ - k) in sum_map:
                count += sum_map[sum_ - k]

            # Update the map with the current cumulative sum
            sum_map[sum_] = sum_map.get(sum_, 0) + 1

        return count  # Return the total count of subarrays


if __name__ == "__main__":
    solve()
