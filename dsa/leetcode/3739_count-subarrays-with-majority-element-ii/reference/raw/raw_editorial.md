### Approach: Prefix Sum

#### Intuition

This problem is a data-enhanced version of [3737. Count Subarrays With Majority Element I](https://leetcode.com/problems/count-majority-element-subarrays-i/).

Let the length of the array $\textit{nums}$ be $n$. We transform the array by treating elements equal to $\textit{target}$ as $+1$ and all other elements as $-1$. Under this transformation, $\textit{target}$ is the majority element of a subarray $\textit{nums}[l..r]$ if and only if the sum of the transformed subarray is greater than $0$.

Let $s$ be the prefix sum array of the transformed array, where $s$ has length $n+1$. Then the transformed sum of subarray $\textit{nums}[l..r]$ is

$$
s[r+1] - s[l].
$$

The condition that this sum is greater than $0$ is equivalent to

$$
s[r+1] > s[l].
$$

Therefore, the problem reduces to the following: for each $r$, count the number of indices $l$ satisfying

$$
0 \le l \le r
$$

and

$$
s[l] < s[r+1].
$$

A naive approach checks all possible $l$ for each $r$, resulting in a time complexity of $O(n^2)$, which is too slow.

Notice that every prefix sum lies in the integer range $[-n, n]$. We use a counting array $\textit{pre}$, where $\textit{pre}[v]$ records how many times the prefix sum value $v$ has appeared so far. Then, for the current prefix sum $s[r+1]$, the number of valid indices $l$ is exactly the sum of all entries in $\textit{pre}$ corresponding to values strictly smaller than $s[r+1]$, which is a prefix sum of $\textit{pre}$.

Computing this prefix sum from scratch for every $r$ would still be too expensive. The key observation is that between consecutive positions, the prefix sum changes by only $+1$ or $-1$. Therefore, the upper bound of the prefix-sum query also changes by only one position. This allows us to maintain the result incrementally using a variable $\textit{presum}$, updating it in $O(1)$ time per step:

* When the current transformed value is $+1$, we have $s[r+1] = s[r] + 1$. The query range expands by one value, so we add $\textit{pre}[s[r]]$ to $\textit{presum}$.
* When the current transformed value is $-1$, we have $s[r+1] = s[r] - 1$. The query range shrinks by one value, so we subtract $\textit{pre}[s[r+1]]$ from $\textit{presum}$.

After updating $\textit{presum}$, we record the current prefix sum $s[r+1]$ in $\textit{pre}$ and add $\textit{presum}$ to the answer.

In the implementation, we use a variable $\textit{cnt}$ to represent the current prefix sum. Since prefix sums may be negative and arrays do not support negative indices, all prefix-sum values are shifted by $n$ when stored in $\textit{pre}$.

#### Implementation


```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # represents the number of prefixes with prefix sums -n, -(n-1), ..., 0, 1, ..., n, with index offset n
        pre = [0] * (n * 2 + 1)
        pre[n] = 1
        cnt = n
        ans = presum = 0
        for i in range(n):
            if nums[i] == target:
                presum += pre[cnt]
                cnt += 1
                pre[cnt] += 1
            else:
                cnt -= 1
                presum -= pre[cnt]
                pre[cnt] += 1
            ans += presum
        return ans
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.
  
  This is the space required for the array $\textit{pre}$.

---