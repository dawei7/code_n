### Approach: Sorting

#### Intuition

To minimize the difference between the highest and lowest scores among the selected $k$ students, we must select them continuously from the sorted array. This is because if we skip a certain index $i$ during the selection, replacing the current highest score in the selection with $\textit{nums}[i]$ will not increase the highest score. Consequently, the difference between the highest and lowest scores will also not increase. Therefore, there must exist an optimal selection scheme in which $k$ consecutive elements are chosen from the sorted array.

Based on this observation, we first sort the array $\textit{nums}$ in ascending order. Then, we traverse $\textit{nums}$ using a sliding window of fixed size $k$. Let the left boundary of the sliding window be $i$. The right boundary is then $i + k - 1$, and the difference between the highest and lowest scores among these $k$ students is $\textit{nums}[i + k - 1] - \textit{nums}[i]$.

The final answer is the minimum value among all possible $\textit{nums}[i + k - 1] - \textit{nums}[i]$.

#### Implementation


```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n \log n)$.
  
  Sorting the array takes $O(n \log n)$ time, and the subsequent sliding window traversal takes $O(n)$ time.

- Space complexity: $O(\log n)$ or $O(n)$.
  
  This is the stack space required for sorting.

---