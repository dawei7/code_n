### Approach: One Pass

#### Intuition

Let $L$ be the number of $\textit{'L'}$ characters in $\textit{moves}$, $R$ be the number of $\textit{'R'}$ characters in $\textit{moves}$, and $B$ be the number of $\textit{'\_'}$ characters in $\textit{moves}$.

The distance from the current position to the origin, ignoring $\textit{'\_'}$, is $|L - R|$. To maximize the final distance from the origin, all $\textit{'\_'}$ characters should be assigned in the same direction as the current movement, resulting in a maximum distance of $|L - R| + B$.

#### Implementation

```python
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")
```

#### Complexity Analysis

Let $n$ be the length of $\textit{moves}$.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---