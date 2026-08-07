### Approach: Prefix Sum

#### Intuition

Let the prefix sum of the array $\textit{nums}$ be defined as
$\textit{prefixSum}[i] = \sum_{j = 0}^i \textit{nums}[j]$.

Then the sum of a subarray $[j, i]$ is
$\textit{sum}(j, i) = \textit{prefixSum}[i] - \textit{prefixSum}[j - 1]$.

The problem requires that the length of the non-empty subarray be divisible by $k$, which means

$(i - j + 1) \bmod k = 0$

From this, we obtain

$i \bmod k = (j - 1) \bmod k$

Let $\textit{kSum}[l]$ store the minimum prefix sum among all prefix sums whose indices have remainder $l$ when divided by $k$. Based on the derivation above, for each index $i$, we only need to find the minimum prefix sum $\textit{prefixSum}[j - 1]$ whose remainder matches that of $i$, that is $\textit{kSum}[i \bmod k]$. This gives the maximum subarray sum ending at $i$:

$\textit{prefixSum}[i] - \textit{kSum}[i \bmod k]$

The final answer is the maximum value over all indices.

#### Implementation

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = 0
        maxSum = -sys.maxsize
        kSum = [sys.maxsize // 2] * k
        kSum[k - 1] = 0
        for i in range(n):
            prefixSum += nums[i]
            maxSum = max(maxSum, prefixSum - kSum[i % k])
            kSum[i % k] = min(kSum[i % k], prefixSum)
        return maxSum
```

#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(k)$.

---