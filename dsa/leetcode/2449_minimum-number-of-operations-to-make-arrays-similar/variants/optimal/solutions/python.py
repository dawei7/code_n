def solve(nums: list[int], target: list[int]) -> int:
    # Separate numbers by parity because operations only affect numbers of the same parity
    nums_even = sorted([x for x in nums if x % 2 == 0])
    nums_odd = sorted([x for x in nums if x % 2 != 0])
    
    target_even = sorted([x for x in target if x % 2 == 0])
    target_odd = sorted([x for x in target if x % 2 != 0])
    
    def calculate_ops(n_list, t_list):
        ops = 0
        for n, t in zip(n_list, t_list):
            # If n < t, we need to add to n, which is half the difference
            if n < t:
                ops += (t - n) // 2
        return ops
    
    # The total operations is the sum of positive differences divided by 2.
    # Since the sum of differences is 0, the sum of positive differences 
    # equals the absolute sum of negative differences.
    return calculate_ops(nums_even, target_even) + calculate_ops(nums_odd, target_odd)
