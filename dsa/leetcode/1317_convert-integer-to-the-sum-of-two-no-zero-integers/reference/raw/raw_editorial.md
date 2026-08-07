### Approach: Enumeration

#### Intuition

Since the given range of $n$ is $[2, 10000]$, which is relatively small, we can directly enumerate possible values of $A$ in the range $[1, n)$. For each $A$, we compute $B = n - A$ and check whether both $A$ and $B$ contain no zero in their decimal representation.

#### Implementation


```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []
```


#### Complexity Analysis

- Time complexity: $O(n \log n)$.
  
  We enumerate all possible values of $A$ in $O(n)$. For each pair $(A, B)$, we check whether their decimal representations contain a zero. This check takes $O(\log n)$ time, since the number of digits in $A$ and $B$ is $O(\log n)$.

- Space complexity: $O(1)$.

---