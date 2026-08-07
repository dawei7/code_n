### Approach 1: Sorting

#### Intuition

Sort the array, then traverse the first $n$ elements and check whether each element is equal to $i + 1$. Finally, check whether the last element is equal to $n$.

#### Implementation

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) - 1
        for i in range(n):
            if nums[i] != i + 1:
                return False
        return nums[n] == n
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n\log n)$.

- Space complexity: $O(\log n)$.

---

### Approach 2: Frequency Counting

#### Intuition

Traverse the array and use a frequency array to count the occurrences of each element.

During the traversal, if a number greater than or equal to $n$ is found, the array is invalid, so we can return `false` immediately. The number $n - 1$ can appear at most 2 times, while all other numbers can appear at most once. If any of these conditions are violated, the array is invalid, and we can return `false` early.

If all conditions are satisfied, then the array is a good array, so we return `true`.

#### Implementation

```python
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = [0] * n
        for a in nums:
            if a >= n:
                return False
            if a < n - 1 and count[a] > 0:
                return False
            if a == n - 1 and count[a] > 1:
                return False
            count[a] += 1
        return True
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.

---