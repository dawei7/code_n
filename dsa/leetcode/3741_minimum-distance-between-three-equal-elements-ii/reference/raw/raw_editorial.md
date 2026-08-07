### Approach: Traversal + Hash Table

#### Intuition

By analyzing the problem, we observe that the distance of a valid triplet is equivalent to the perimeter of a generalized triangle. Regardless of the order of the three selected indices, this distance simplifies to twice the length of the segment formed by the two endpoints. In other words, if the leftmost index is $i$ and the rightmost index is $k$, then the required distance is $2 \times (k - i)$.

From this observation, it follows that the minimum distance must come from valid triplets formed by three consecutive occurrences of the same value. Based on this insight, we can efficiently track adjacent occurrences using a structure similar to linked lists. Specifically, we maintain predecessor or successor relationships to quickly locate neighboring indices and compute distances.

Here, we explain the approach using a successor array. The predecessor-based approach is symmetric and can be derived similarly.

We define a successor array $\textit{next}$, where $\textit{next}[i]$ stores the next occurrence index of $\textit{nums}[i]$ in the array. To construct this array, we traverse $\textit{nums}$ in reverse while using a hash table to record the most recent occurrence of each value.

Next, we traverse the array from left to right. Using the $\textit{next}$ array, we can find the next two consecutive occurrences of the same value in $O(1)$ time. This allows us to form a valid triplet, compute its distance, and update the minimum answer.


#### Implementation


```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [-1] * n
        occur = {}
        ans = n + 1

        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]
            occur[nums[i]] = i

        for i in range(n):
            second_pos = nxt[i]
            if second_pos != -1:
                third_pos = nxt[second_pos]
                if third_pos != -1:
                    ans = min(ans, third_pos - i)

        return -1 if ans == n + 1 else ans * 2
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n)$.
  
  We traverse the array once in reverse to build the $\textit{next}$ array and once forward to compute the answer. Each hash table operation takes $O(1)$ time on average.

- Space complexity: $O(n)$.
  
  The $\textit{next}$ array and the hash table together require $O(n)$ space.

---