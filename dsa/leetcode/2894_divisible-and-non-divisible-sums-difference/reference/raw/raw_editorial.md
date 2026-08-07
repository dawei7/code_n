[TOC]

## Solution

--- 

### Approach 1: Traversal

#### Intuition

Consider the interval $[1, n]$. 

- Let $\textit{num}_1$ be the sum of the integers in this range that aren’t divisible by `m`.
- Let $\textit{num}_2$ be the sum of those that are divisible by `m`.

To capture their combined effect, we introduce a running total called ans.

As we walk through each integer `x` from 1 to `n`:

1. If `x` isn’t divisible by `m`, we add it to ans.
2. If `x` is divisible by `m`, we subtract it from ans.

When the traversal ends, the value stored in ans is exactly the result the problem asks for.

#### Implementation


```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(x if x % m != 0 else -x for x in range(1, n + 1))
```


#### Complexity Analysis

Let $n$ be the given integer.

- Time complexity: $O(n)$.
  
  We traverse all numbers from 1 to n.

- Space complexity: $O(1)$.
  
  Only one integer variable $\textit{ans}$ was used.

### Approach 2: Mathematical Derivation

#### Intuition

First, focus on the numbers that are divisible by `m`.
The *k-th* such number is *k × m*, so their sum is

$$
\text{num}_2
  = m + 2m + \dots + k m
  = (1 + 2 + \dots + k)\,m
  = \frac{k(k+1)}{2}\,m,
$$ -------------- ( 1 )

where

$$
k=\bigl\lfloor\tfrac{n}{m}\bigr\rfloor
$$ 

is the count of multiples of `m` up to `n`.


Next, look at the numbers **not** divisible by `m`.
Their sum is simply the total of the first `n` integers minus $\text{num}_2$:

$$
\text{num}_1
  = (1 + 2 + \dots + n) - \text{num}_2
  = \frac{n(n+1)}{2} - \text{num}_2.
$$  --------------- ( 2 )


Putting the two pieces together, the quantity the problem asks for is

$$
\text{num}_1 - \text{num}_2
  = \left[\frac{n(n+1)}{2} - \text{num}_2\right] - \text{num}_2
  = \frac{n(n+1)}{2} - 2\,\text{num}_2.
$$

Finally, substitute the closed form of $\text{num}_2$:

$$
\boxed{\text{num}_1 - \text{num}_2
       = \frac{n(n+1)}{2} \;-\; k(k+1)\,m.}
$$

This single formula lets us compute the desired result directly, without any iteration.

#### Implementation


```python
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        return n * (n + 1) // 2 - k * (k + 1) * m
```


#### Complexity Analysis

- Time complexity: $O(1)$.

- Space complexity: $O(1)$.
  
  Only one integer variable $\textit{k}$ was used.