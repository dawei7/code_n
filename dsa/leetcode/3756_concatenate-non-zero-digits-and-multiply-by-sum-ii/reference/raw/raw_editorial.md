### Approach: Prefix Array

#### Intuition

We define `pow10[i]` as (10^i \bmod \textit{MOD}). By precomputing the `pow10` array once, we avoid recomputing these values for every test case.

As in the string-based solution for **3754. Concatenate Non-Zero Digits and Multiply by Sum I**, we build prefix arrays to obtain the values of `x` and `sum` for any prefix of the input string.

We also maintain a third prefix array, `cnt`, where `cnt[i]` denotes the number of non-zero digits in the prefix ending before index `i`.

Using these three prefix arrays, we can compute the values of `x` and `sum` for any query range by taking differences between the corresponding prefix values.

Finally, we compute the answer for each query and return the resulting array.

#### Implementation


```python
MOD = 10**9 + 7
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sum = [0] * (n + 1)
        x = [0] * (n + 1)
        cnt = [0] * (n + 1)
        for i, c in enumerate(s):
            d = int(c)
            sum[i + 1] = sum[i] + d
            x[i + 1] = (x[i] * 10 + d) % MOD if d > 0 else x[i]
            cnt[i + 1] = cnt[i] + (d > 0)

        m = len(queries)
        res = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = cnt[r] - cnt[l]
            res[i] = (x[r] - x[l] * pow10[length]) * (sum[r] - sum[l]) % MOD

        return res
```


#### Complexity Analysis

Let `MAX_N` be the maximum possible string length, $n$ be the length of the input string, and $m$ be the number of queries.

Preprocessing:

- Time complexity: $O(\textit{MAX\_N})$.

- Space complexity: $O(\textit{MAX\_N})$.

For each test case:

- Time complexity: $O(n + m)$.

- Space complexity: $O(n)$.
  
  The returned array is not included in the space complexity.

---