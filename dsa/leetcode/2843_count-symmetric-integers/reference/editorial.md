
## Solution

---

### Approach 1: Enumeration

#### Intuition

Enumerate all numbers from $\textit{low}$ to $\textit{high}$:

- If it is a two-digit number and is a multiple of 11, then it is a symmetric integer.
- If it is a four-digit number, calculate the sum of the thousands and hundreds digits, as well as the sum of the tens and ones digits. If they are equal, it is a symmetric (even) integer.

Finally, it returns the number of symmetric integers in the range.

#### Implementation

```python
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res
```

#### Complexity Analysis

- Time complexity: $O(high - low)$.

We enumerate all numbers from $\textit{low}$ to $\textit{high}$ and check whether they are symmetric integers in $O(1)$ each time.

- Space complexity: $O(1)$.

Only a few additional variables are needed.