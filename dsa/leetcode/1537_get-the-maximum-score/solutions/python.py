def solve(nums1, nums2):
    mod = 10**9 + 7
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    a = sorted(nums1)
    b = sorted(nums2)
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sum1 += a[i]
            i += 1
        elif a[i] > b[j]:
            sum2 += b[j]
            j += 1
        else:
            value = a[i]
            block1 = 0
            while i < len(a) and a[i] == value:
                block1 += a[i]
                i += 1
            block2 = 0
            while j < len(b) and b[j] == value:
                block2 += b[j]
                j += 1
            best = max(sum1, sum2) + max(block1, block2)
            sum1 = best
            sum2 = best
    sum1 += sum(a[i:])
    sum2 += sum(b[j:])
    return max(sum1, sum2) % mod
