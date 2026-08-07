### Approach: Brute Force

#### Intuition

This problem is a simplified version of [3721. Longest Balanced Subarray II](https://leetcode.com/problems/longest-balanced-subarray-ii/), which can be solved directly using a brute force approach.

We can perform an $O(n^2)$ traversal over all possible subarrays. During this process, we use two hash tables to maintain the counts of odd and even numbers within the current subarray, and continuously update the maximum length that satisfies the balanced condition.

In terms of implementation, there are multiple ways to maintain these hash tables. The simplest approach is to initialize new hash tables each time the left boundary of the subarray is fixed, and then update the result while expanding the right boundary.

#### Implementation


```python
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            odd = {}
            even = {}

            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd[nums[j]] = odd.get(nums[j], 0) + 1
                else:
                    even[nums[j]] = even.get(nums[j], 0) + 1

                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)

        return max_len
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n ^ 2)$.
  
  Traversing the interval requires $O(n^2)$, and maintaining the count of elements using a hash table requires $O(1)$.

- Space complexity: $O(n)$.
  
  The hash table requires $O(n)$ space.

---