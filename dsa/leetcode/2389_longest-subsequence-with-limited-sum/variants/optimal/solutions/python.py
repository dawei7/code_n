import bisect

def solve(nums: list[int], queries: list[int]) -> list[int]:
    # Step 1: Sort the nums array to ensure we pick the smallest elements first
    nums.sort()
    
    # Step 2: Compute prefix sums of the sorted nums array
    prefix_sums = []
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sums.append(current_sum)
        
    # Step 3: For each query, use binary search on the prefix_sums array
    ans = []
    for query in queries:
        # bisect_right returns an insertion point which comes after (to the right of)
        # any existing entries of the query value.
        # This index directly corresponds to the count of elements in nums
        # whose sum is less than or equal to the query.
        #
        # Example: nums = [1, 2, 4, 5], prefix_sums = [1, 3, 7, 12]
        # If query = 10:
        # bisect.bisect_right(prefix_sums, 10) returns 3.
        # This means prefix_sums[0] (1), prefix_sums[1] (3), prefix_sums[2] (7)
        # are all <= 10. prefix_sums[2] (value 7) is the sum of the first 3 elements of nums.
        # So, the maximum length is 3.
        length = bisect.bisect_right(prefix_sums, query)
        ans.append(length)
        
    return ans
