### Approach: Bitwise Comparison

#### Intuition

We iterate through each digit of the given number $n$, maintaining the largest digit in $\textit{first}$ and the second largest digit in $\textit{second}$. After processing all digits, the product of these two values is the maximum possible product, which is the answer.

#### Implementation


```python
class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        while n > 0:
            x = n % 10
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
            n //= 10
        return first * second
```


#### Complexity Analysis

Let $n$ be the given number.

- Time complexity: $O(\log n)$.

- Space complexity: $O(1)$.

---