# Time:  precompute: O(sqrt(r) * logr + r) = O(sqrt(r) * logr), r = max(nums)
#        runtime:    O(n)
# Space: O(r)

# precompute, bitmasks, two pointers
def precompute(n):
    l = n.bit_length()
    palindromes = []
    for d in range(1, l+1):
        h = (d+1)//2
        for prefix in range(1<<(h-1), 1<<h):
            p = t = prefix
            t >>= d%2
            for _ in range(h-d%2):
                p = (p<<1)|(t&1)
                t >>= 1
            if p <= n:
                palindromes.append(p)
    lookup = [float("inf")]*(n+1)
    i = 0
    for x in range(1, n+1):
        while i < len(palindromes):
            if palindromes[i] > x:
                break
            i += 1
        if i < len(palindromes):
            lookup[x] = min(lookup[x], palindromes[i]-x)
        if i-1 >= 0:
            lookup[x] = min(lookup[x], x-palindromes[i-1])
    return lookup

MAX_NUM = 5000
LOOKUP = precompute(MAX_NUM)
class Solution:
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [LOOKUP[x] for x in nums]
