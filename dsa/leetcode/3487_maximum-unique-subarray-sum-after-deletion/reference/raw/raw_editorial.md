### Approach: Duplicate Removal for Positive Numbers

#### Intuition

The problem essentially requires finding a non-empty subsequence of non-repeating elements that gives the maximum sum. To achieve this, we can greedily collect all positive numbers in a hash set to ensure uniqueness and then sum them. If there are no positive numbers, we return the maximum value from the array.

#### Implementation


```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumsSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)
```


#### Complexity analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.
  
  We traverse the array exactly once, and each operation on the hash table takes constant time in the average case.

- Space complexity: $O(n)$.
  
  This comes mainly from the space used by the hash table to store the positive numbers.