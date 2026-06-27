def get_max_subsequence(nums, k):
    stack = []
    drop = len(nums) - k
    for num in nums:
        while drop > 0 and stack and stack[-1] < num:
            stack.pop()
            drop -= 1
        stack.append(num)
    return stack[:k]

def merge(seq1, seq2):
    res = []
    i, j = 0, 0
    while i < len(seq1) or j < len(seq2):
        if seq1[i:] > seq2[j:]:
            res.append(seq1[i])
            i += 1
        else:
            res.append(seq2[j])
            j += 1
    return res

def solve(nums1, nums2, k):
    n, m = len(nums1), len(nums2)
    best = []
    
    # Iterate over how many elements to take from nums1
    for i in range(max(0, k - m), min(k, n) + 1):
        sub1 = get_max_subsequence(nums1, i)
        sub2 = get_max_subsequence(nums2, k - i)
        candidate = merge(sub1, sub2)
        if candidate > best:
            best = candidate
            
    return best
