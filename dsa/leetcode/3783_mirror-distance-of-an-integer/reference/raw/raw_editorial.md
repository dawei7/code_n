### Approach: Mathematics

#### Intuition

We reverse the decimal digits of the integer $n$ to obtain its mirror number $\textit{rev}$. Specifically, in each step, we extract the last digit of $n$ using $n \bmod 10$, update $\textit{rev}$ as $\textit{rev} \times 10 + (n \bmod 10)$, and then update $n$ to $\left\lfloor \frac{n}{10} \right\rfloor$. We repeat this process until $n = 0$.

The final answer is $|n - \textit{rev}|$.

#### Implementation


```python
class Solution:
    def reverse(self, n: int) -> int:
        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10
        return res

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
```


#### Complexity Analysis

Let $n$ be the input integer.

- Time complexity: $O(\log n)$.
  
  The reversal process iterates through each digit of $n$, and the number of digits is $O(\log n)$.

- Space complexity: $O(1)$.

---