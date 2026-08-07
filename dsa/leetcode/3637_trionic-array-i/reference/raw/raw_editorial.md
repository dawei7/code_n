### Approach 1: Evaluating the Validity of the Boundaries

#### Intuition

We can determine whether an array is a three-part array by checking if there exist indices $p$, $q$, and $\textit{flag}$ such that $0 < p < q < \textit{flag} = n - 1$.

Alternatively, we can identify each segment by examining its monotonicity and length. For the array to be valid, each segment must be strictly monotonic, and every segment must contain at least two elements.

#### Implementation


```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        p = i - 1

        while i < n and nums[i - 1] > nums[i]:
            i += 1
        q = i - 1

        while i < n and nums[i - 1] < nums[i]:
            i += 1
        flag = i - 1

        return (p != 0) and (q != p) and (flag == n - 1 and flag != q)
```


#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

### Approach 2: Counting the Number of Turning Points

#### Intuition

We can also determine whether an array is a three-part array by counting how many **increasing or decreasing** segments it contains.

More specifically, the array must follow the pattern **increase -> decrease -> increase**. Therefore, the first segment must be strictly increasing, and there must be exactly two turning points in the array.

#### Implementation


```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] >= nums[1]:
            return False

        count = 1
        for i in range(2, n):
            if nums[i - 1] == nums[i]:
                return False
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
                count += 1

        return count == 3
```


#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---