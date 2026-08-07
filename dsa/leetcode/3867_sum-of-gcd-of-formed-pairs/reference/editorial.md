### Approach: Simulation

#### Intuition

The problem requires us to construct the array $\textit{prefixGcd}$. According to its definition, we first need to construct the array $\textit{mx}$.

A brute-force approach would compute each $\textit{mx}_i$ independently, resulting in a time complexity of $O(n^2)$, which is too slow. Observe that $\textit{mx}$ is simply the prefix maximum array of $\textit{nums}$. Therefore, we can maintain the current prefix maximum while traversing the array once, allowing us to construct $\textit{mx}$ in linear time.

Once $\textit{mx}$ has been constructed, we can directly compute the array $\textit{prefixGcd}$ according to its definition.

Next, we sort the array $\textit{prefixGcd}$. We then repeatedly pair the smallest remaining element with the largest remaining element and add their greatest common divisor to the answer. This process can be simulated using the two-pointer technique.

Note that if the length of the array is odd, one element will remain unpaired. According to the problem statement, this element should simply be ignored.

#### Implementation

```python
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = []
        prefixMax = -inf

        for x in nums:
            prefixMax = max(prefixMax, x)
            mx.append(prefixMax)

        prefixGcd = [gcd(x, y) for x, y in zip(nums, mx)]
        prefixGcd.sort()

        ans = 0
        left, right = 0, n - 1
        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return ans
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and let $U$ be the maximum value in $\textit{nums}$.

- Time complexity: $O(n\log n + n\log U)$.

  Sorting $\textit{prefixGcd}$ takes $O(n \log n)$ time. Computing each greatest common divisor takes $O(\log U)$ time, and this operation is performed $O(n)$ times.

- Space complexity: $O(n)$.

  Used to store the arrays $\textit{mx}$ and $\textit{prefixGcd}$.

---