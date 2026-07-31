## General

Let $X$ be the XOR of every element in `nums`. There are only three possible outcomes.

**The whole array already works.** If $X\ne0$, selecting every element gives a valid subsequence of length $n$. No subsequence can be longer, so the answer is $n$.

**No non-zero value exists.** If every element equals zero, every subsequence also has XOR zero. No valid choice exists, and the answer is `0`.

**Delete one non-zero element.** The remaining situation has $X=0$ and contains some value $v\ne0$. Remove one occurrence of $v$. XOR is self-inverse, so the remaining elements have XOR

$$
X\mathbin{\operatorname{XOR}}v=0\mathbin{\operatorname{XOR}}v=v\ne0.
$$

This constructs a valid subsequence of length $n-1$. A length-$n$ subsequence is impossible because it would be the complete array, whose XOR is zero. Therefore $n-1$ is optimal. One scan can compute $X$ while also recording whether any non-zero element exists.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Computing the complete XOR and the non-zero flag takes $O(n)$ time. The two accumulators use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Subsequence dynamic programming by XOR value:** Tracking attainable XORs is unnecessary and can create too many states because values may reach $10^9$.
- **Try deleting every element:** Recomputing the remaining XOR for each deletion takes $O(n^2)$ time; the identity $X\operatorname{XOR}v$ gives the result immediately.
- **Enumerate all subsequences:** There are $2^n$ selections, which is infeasible.
- **Single zero:** No non-zero-XOR subsequence exists, so the answer is `0`.
- **Single non-zero value:** The complete one-element array works, so the answer is `1`.
- **Zeros mixed with non-zero values:** Zeros do not alter XOR, but they still count toward the length of a selected subsequence.
