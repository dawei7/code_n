def solve(nums1: list[int], nums2: list[int], diff: int) -> int:
    # Transform the inequality:
    # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
    # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
    # Let arr[k] = nums1[k] - nums2[k]
    # arr[i] - arr[j] <= diff  =>  arr[i] - diff <= arr[j]
    
    arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, count_l = merge_sort(arr[:mid])
        right, count_r = merge_sort(arr[mid:])
        
        count = count_l + count_r
        
        # Count pairs (i, j) where left[i] - diff <= right[j]
        # Since both halves are sorted, we use two pointers
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] - diff > right[j]:
                j += 1
            count += (len(right) - j)
            
        # Standard merge step
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, count

    _, total_pairs = merge_sort(arr)
    return total_pairs
