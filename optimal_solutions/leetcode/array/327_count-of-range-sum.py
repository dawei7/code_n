def solve(nums: list[int], lower: int, upper: int) -> int:
    # Calculate prefix sums: P[i] is the sum of nums[0...i-1]
    prefix_sums = [0]
    for x in nums:
        prefix_sums.append(prefix_sums[-1] + x)
    
    def count_while_merge_sort(left: int, right: int) -> int:
        if right - left <= 1:
            return 0
        
        mid = (left + right) // 2
        count = count_while_merge_sort(left, mid) + count_while_merge_sort(mid, right)
        
        # Count valid pairs (i, j) such that lower <= P[j] - P[i] <= upper
        # where left <= i < mid <= j < right
        j_start = j_end = mid
        for i in range(left, mid):
            while j_start < right and prefix_sums[j_start] - prefix_sums[i] < lower:
                j_start += 1
            while j_end < right and prefix_sums[j_end] - prefix_sums[i] <= upper:
                j_end += 1
            count += (j_end - j_start)
        
        # Standard merge step to keep prefix_sums sorted
        prefix_sums[left:right] = sorted(prefix_sums[left:right])
        return count

    return count_while_merge_sort(0, len(prefix_sums))
