### Approach: Prefix Sum

#### Intuition

We solve this problem using two traversals.

In the first traversal, we iterate through the array from left to right while maintaining a variable $\textit{leftSum}$, which represents the sum of all elements to the left of the current position. We store this value in $\textit{ans}[i]$, and then add $\textit{nums}[i]$ to $\textit{leftSum}$.

In the second traversal, we iterate through the array from right to left while maintaining a variable $\textit{rightSum}$, which represents the sum of all elements to the right of the current position. At this point, $\textit{ans}[i]$ already stores the sum of all elements to the left of position $i$, so we update $\textit{ans}[i]$ to $|\textit{ans}[i] - \textit{rightSum}|$. Then, we add $\textit{nums}[i]$ to $\textit{rightSum}$.

#### Implementation


```python
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left_sum = 0
        for i in range(n):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - right_sum)
            right_sum += nums[i]

        return ans
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.
  
  The space occupied by the return value is not included.

---