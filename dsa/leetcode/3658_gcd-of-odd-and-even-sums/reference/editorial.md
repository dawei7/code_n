### Approach 1: Euclidean Algorithm

#### Intuition

To compute the greatest common divisor (GCD) of two integers, we can use the Euclidean algorithm.

The key observation behind the Euclidean algorithm is that the greatest common divisor of two integers is equal to the greatest common divisor of the **second integer** and the **remainder when the first integer is divided by the second integer**. Formally,

$\textit{gcd}(a, b) = \textit{gcd}(b, a \bmod b)$

We define $\textit{gcd}(a, 0) = a$, which naturally leads to a recursive implementation. Specifically, for $\textit{gcd}(x, y)$:

* If $y \ne 0$, then $\textit{gcd}(x, y) = \textit{gcd}(y, x \bmod y)$.
* Otherwise, $\textit{gcd}(x, y) = x$.

To compute the required values $\textit{sumOdd}$ and $\textit{sumEven}$, we can directly apply the arithmetic series formulas:

$\textit{sumOdd} = 1 + 3 + \cdots + (2n - 1) = n^2$

$\textit{sumEven} = 2 + 4 + \cdots + 2n = n(n + 1)$

#### Implementation

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(x: int, y: int) -> int:
            return x if y == 0 else gcd(y, x % y)

        return gcd(n * n, n * (n + 1))
```

#### Complexity Analysis

- Time complexity: $O(\log(n))$.

- Space complexity: $O(\log(n))$.

  In the worst case, the recursion depth is $O(\log n)$.

---

### Approach 2: Mathematics

#### Intuition

Observe that $\textit{gcd}(n^2, n(n + 1)) = n \times \textit{gcd}(n, n + 1)$

Since two consecutive integers are always coprime, $\textit{gcd}(n, n + 1) = 1$

Therefore, $\textit{gcd}(n^2, n(n + 1)) = n$

which is exactly the required answer.

#### Implementation

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
```

#### Complexity Analysis

- Time complexity: $O(1)$.

- Space complexity: $O(1)$.

---