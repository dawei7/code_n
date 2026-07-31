## General

**Analyze one bit independently**

Fix a bit position and let $c$ be the number of array values having that bit set. The effective value's bit is one precisely when `nums[k]` has the bit and at least one of `nums[i]` or `nums[j]` has it. There are $c$ choices for $k$. Among the $n^2$ ordered pairs $(i,j)$, exactly $(n-c)^2$ have the bit absent from both values. The number of effective values contributing a one at this bit is therefore

$$
c\bigl(n^2-(n-c)^2\bigr)=c^2(2n-c).
$$

XOR retains the bit only when this count is odd. Modulo two, $c^2(2n-c) \equiv c^3 \equiv c$. Thus the final bit is set exactly when an odd number of input values contain it. That is also the defining per-bit behavior of XORing every element of `nums`.

Consequently, the full triplet expression equals `nums[0] ^ nums[1] ^ ... ^ nums[n - 1]`. A single running XOR computes all bit parities simultaneously.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. The algorithm visits every array value once, taking $O(n)$ time. The running result occupies one integer, so the auxiliary-space bound is $O(1)$.

## Alternatives and edge cases

- **Enumerate all ordered triplets:** Directly evaluating the definition takes $O(n^3)$ time and is infeasible for $n = 10^5$.
- **Collapse only the innermost XOR:** XORing `nums[k]` first and then iterating every ordered pair is correct but still costs $O(n^2)$ time.
- **Count each bit explicitly:** Testing the roughly 30 relevant bit positions across all values also gives $O(n)$ time under fixed-width integers, but a direct running XOR is simpler and avoids an extra constant factor.
- **One element:** The sole triplet evaluates to that element, matching the running XOR.
- **Duplicate values:** Two equal values cancel bit for bit; only the parity of each value's contribution matters.
- **Repeated indices:** The parity derivation counts all ordered choices independently and therefore includes triplets where indices coincide.
