### Approach: Enumeration

#### Intuition

We enumerate all possible left endpoints $i$ of subarrays and then extend the right endpoint $j$ one position at a time. During this process, we maintain a counter $\textit{cnt}$. If $\textit{nums}[j] = \textit{target}$, we increment $\textit{cnt}$ by $1$; otherwise, we decrement it by $1$.

For a subarray, $\textit{cnt}$ represents the difference between the number of occurrences of $\textit{target}$ and the number of non-$\textit{target}$ elements. Therefore, when $\textit{cnt} > 0$, the number of occurrences of $\textit{target}$ is greater than the number of non-$\textit{target}$ elements, which means $\textit{target}$ appears more than half the length of the subarray. Hence, $\textit{target}$ is the majority element of the subarray, and we increment the answer by $1$.

#### Implementation


```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    ans += 1
        return ans
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n^2)$.
  
  We enumerate all subarrays using two nested loops.

- Space complexity: $O(1)$.

---