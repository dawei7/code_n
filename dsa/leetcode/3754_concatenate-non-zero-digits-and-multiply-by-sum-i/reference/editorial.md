### Approach 1: Traverse from Left to Right

#### Intuition

Convert the input integer $n$ into a string $s$, then traverse the digits from left to right while simulating the process described in the problem statement.

#### Implementation

```python
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        for c in str(n):
            d = int(c)
            sum += d
            if d > 0:
                x = x * 10 + d
        return x * sum
```

#### Complexity Analysis

- Time complexity: $O(\log n)$.

- Space complexity: $O(\log n)$.

---

### Approach 2: Traverse from Right to Left

#### Intuition

Instead of converting the integer into a string, we repeatedly divide $n$ by $10$ to traverse its digits from right to left. During the traversal, we update both $x$ and $\textit{sum}$.

Whenever we encounter a non-zero digit, we append it to $x$. Since the digits are processed from right to left, we maintain a variable $\textit{pow10}$ that stores the current power of $10$, allowing us to place each non-zero digit in its correct position within $x$.

#### Implementation

```python
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x, sum, pow10 = 0, 0, 1
        while n > 0:
            d = n % 10
            sum += d
            if d > 0:
                x += d * pow10
                pow10 *= 10
            n //= 10
        return x * sum
```

#### Complexity Analysis

- Time complexity: $O(\log n)$.

- Space complexity: $O(1)$.

---