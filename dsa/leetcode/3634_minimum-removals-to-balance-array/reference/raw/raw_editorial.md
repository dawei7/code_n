### Approach: Sorting + Two Pointers

#### Intuition

We first sort the array $\textit{nums}$. After removing some elements to make the array balanced, let the minimum element in the remaining array be $\textit{min}$ and the maximum element be $\textit{max}$. All elements strictly smaller than $\textit{min}$ and strictly larger than $\textit{max}$ must be removed. Removing any element within the range $[\textit{min}, \textit{max}]$ is unnecessary.

Based on this observation, we can use a two-pointer technique. The left pointer $\textit{left}$ starts at the beginning of the sorted array and represents the position of the minimum element $x$ of the current candidate subarray. The right pointer $\textit{right}$ moves to the right until it reaches the first element that is strictly greater than $k \times x$, or until it goes out of bounds.

At this point, the left-closed and right-open interval $[\textit{left}, \textit{right})$ represents a balanced subarray, whose length is $\textit{right} - \textit{left}$.

As the left pointer moves to the right, the right pointer never moves backward. For each position of $\textit{left}$, we can update the answer as $n - (\textit{right} - \textit{left})$, where $n$ is the length of the array $\textit{nums}$.

#### Implementation


```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = n
        right = 0
        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            ans = min(ans, n - (right - left))

        return ans
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n \log n)$.
  
  Sorting takes $O(n \log n)$ time, and the two-pointer traversal takes $O(n)$ time.

- Space complexity: $O(\log n)$ or $O(n)$.
  
  This includes the stack space required by the sorting process, since built-in sorting implementations typically use a variant of quicksort or timsort.

---