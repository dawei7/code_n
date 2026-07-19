def solve(nums: list[int]) -> list[int]:
    # Coordinate compression to map values to [1, unique_count]
    sorted_unique = sorted(list(set(nums)))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
    m = len(sorted_unique)

    # Binary Indexed Tree to store frequencies
    def update(bit, idx, val):
        while idx <= m:
            bit[idx] += val
            idx += idx & (-idx)

    def query(bit, idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    bit1 = [0] * (m + 1)
    bit2 = [0] * (m + 1)
    
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    
    update(bit1, rank[nums[0]], 1)
    update(bit2, rank[nums[1]], 1)
    
    for i in range(2, len(nums)):
        val = nums[i]
        r = rank[val]
        
        # Count elements > val: total_elements - count(<= val)
        count1 = len(arr1) - query(bit1, r)
        count2 = len(arr2) - query(bit2, r)
        
        if count1 > count2:
            arr1.append(val)
            update(bit1, r, 1)
        elif count2 > count1:
            arr2.append(val)
            update(bit2, r, 1)
        else:
            if len(arr1) <= len(arr2):
                arr1.append(val)
                update(bit1, r, 1)
            else:
                arr2.append(val)
                update(bit2, r, 1)
                
    return arr1 + arr2
