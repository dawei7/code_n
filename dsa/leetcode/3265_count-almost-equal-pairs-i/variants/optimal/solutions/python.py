def solve(nums: list[int]) -> int:
    def is_almost_equal(a: int, b: int) -> bool:
        if a == b:
            return True
        
        s1 = str(a)
        s2 = str(b)
        
        # Pad the shorter string with leading zeros
        max_len = max(len(s1), len(s2))
        s1 = s1.zfill(max_len)
        s2 = s2.zfill(max_len)
        
        if s1 == s2:
            return True
            
        # Check if one swap makes them equal
        diff_indices = []
        for i in range(max_len):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        if len(diff_indices) != 2:
            return False
            
        i, j = diff_indices
        # Check if swapping s1[i] and s1[j] makes it equal to s2
        s1_list = list(s1)
        s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
        
        return "".join(s1_list) == s2

    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if is_almost_equal(nums[i], nums[j]):
                count += 1
    return count
