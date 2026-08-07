### Approach: Construction

#### Intuition

We start by placing the smallest $\lfloor \tfrac{n}{2} \rfloor$ positive integers and their negatives into the array. At this point, their sum is $0$.

- When $n$ is even, the array already satisfies the requirements.
- When $n$ is odd, we add $0$ to the array.

Thus, the $n$ numbers are all distinct, and their sum is $0$. This gives us an array that satisfies the requirements.

#### Implementation

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans
```

#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

  Apart from the output array $\textit{ans}$, the extra space used is constant.

---