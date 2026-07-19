## General
**View each operation as a reachable interval**

An original value $v$ can become any integer in $[v-k,v+k]$; using $x=0$ also covers the choice to make no effective change. Let $a=\min(\texttt{nums})$ and $b=\max(\texttt{nums})$. No operation can raise the original minimum beyond $a+k$, and no operation can lower the original maximum below $b-k$. Therefore, if these endpoint intervals remain disjoint, every result has score at least

$$
(b-k)-(a+k)=b-a-2k.
$$

This bound is attainable. Raise the minimum toward $a+k$, lower the maximum toward $b-k$, and place every intermediate value inside that remaining interval; each intermediate value's reachable interval intersects it. If $a+k \geq b-k$, the reachable intervals of all elements share a common value, so every element can be made equal and the score becomes zero.

The answer is consequently $\max(0,b-a-2k)$. Only the original minimum and maximum affect it, so one scan is sufficient.

## Complexity detail
Finding the minimum and maximum examines each of the $n$ values once, giving $O(n)$ time. Apart from those two extrema, no data structure grows with the input, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sort the array:** The first and last sorted values give the same formula, but sorting costs $O(n\log n)$ time.
- **Compare every pair:** Computing the original spread as the largest pairwise difference is correct but takes $O(n^2)$ time.
- **Enumerate all changes:** Each index has $2k+1$ possible integer adjustments, making direct combination search exponential and unnecessary.
- **One element:** Its score is always zero regardless of `k`.
- **Zero adjustment range:** When `k = 0`, the original score cannot change.
- **Overlapping endpoint intervals:** If $b-a \leq 2k$, clamp the formula at zero because a score cannot be negative.
- **Interior values:** They cannot force a wider final range than the adjusted original extremes.
- **Duplicate extremes:** Repeated minimum or maximum values can all receive the same endpoint adjustment independently.
