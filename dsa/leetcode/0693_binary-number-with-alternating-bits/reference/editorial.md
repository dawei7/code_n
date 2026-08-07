[TOC]

### Approach #1: Convert to String [Accepted]

**Intuition and Algorithm**

Let's convert the given number into a string of binary digits. Then, we should simply check that no two adjacent digits are the same.

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)
        return all(bits[i] != bits[i+1]
                   for i in range(len(bits) - 1))
```

**Complexity Analysis**

* Time Complexity: $O(1)$. For arbitrary inputs, we do $O(w)$ work, where $w$ is the number of bits in `n`. However, $w \leq 32$.

* Space complexity: $O(1)$, or alternatively $O(w)$.

---

### Approach #2: Divide By Two [Accepted]

**Intuition and Algorithm**

We can get the last bit and the rest of the bits via `n % 2` and `n // 2` operations. Let's remember `cur`, the last bit of `n`. If the last bit ever equals the last bit of the remaining, then two adjacent bits have the same value, and the answer is `False`.  Otherwise, the answer is `True`.

Also note that instead of `n % 2` and `n // 2`, we could have used operators `n & 1` and $n >\ge 1$ instead.

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True
```

**Complexity Analysis**

* Time Complexity: $O(1)$. For arbitrary inputs, we do $O(w)$ work, where $w$ is the number of bits in `n`. However, $w \leq 32$.

* Space complexity: $O(1)$.