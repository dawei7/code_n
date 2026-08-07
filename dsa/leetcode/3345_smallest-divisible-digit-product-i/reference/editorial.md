### Approach: Enumeration

#### Intuition

We simply enumerate integers starting from $n$. Within at most $10$ attempts, we are guaranteed to encounter an integer whose last digit is $0$. Since the product of its digits is then $0$, it is divisible by any positive integer $t$. Therefore, a valid answer is guaranteed to be found within the next $10$ integers.

#### Implementation

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(num: int) -> bool:
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
                if product == 0:
                    break
            return product % t == 0

        while not check(n):
            n += 1
        return n
```

#### Complexity Analysis

Let $n$ be the integer given in the problem.

- Time complexity: $O(10 \log n)$.

- Space complexity: $O(1)$.

---