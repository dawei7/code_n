### Approach: Find The Pattern

#### Intuition

Enumerate integers that contain only set bits: $1, 3, 7, 15$. We can observe that the pattern of this sequence is that each number is obtained by multiplying the previous number by $2$ and then adding $1$.

We initialize $x = 1$. In each iteration of the loop, we update $x$ as $x = x \times 2 + 1$. The loop continues until $x$ becomes greater than or equal to $n$, and then we return the result.

#### Implementation


```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x
```


#### Complexity Analysis

- Time complexity: $O(\log n)$.
  
  The number of iterations is $O(\log n)$ times.

- Space complexity: $O(1)$.

---