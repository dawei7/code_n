def solve(nums: list[int]) -> bool:
    def count_set_bits(n: int) -> int:
        return bin(n).count('1')

    if not nums:
        return True

    prev_max = -1
    curr_min = nums[0]
    curr_max = nums[0]
    prev_bits = count_set_bits(nums[0])

    for i in range(1, len(nums)):
        curr_bits = count_set_bits(nums[i])
        
        if curr_bits == prev_bits:
            curr_min = min(curr_min, nums[i])
            curr_max = max(curr_max, nums[i])
        else:
            if prev_max > curr_min:
                return False
            prev_max = curr_max
            curr_min = nums[i]
            curr_max = nums[i]
            prev_bits = curr_bits
            
    return prev_max <= curr_min
