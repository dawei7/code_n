


def solve():
    class Solution:
        def subarraySum(self, arr, k: int) -> int:
            prefix_count = defaultdict(int)
            prefix_count[0] = 1  # base case

            curr_sum = 0
            count = 0

            for num in arr:
                curr_sum += num
                rem = curr_sum - k
                if rem in prefix_count:
                    count += prefix_count[rem]
                prefix_count[curr_sum] += 1

            return count


if __name__ == "__main__":
    solve()
