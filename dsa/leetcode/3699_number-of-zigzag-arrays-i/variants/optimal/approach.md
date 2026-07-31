## General

Because adjacent elements cannot be equal, each adjacent pair has exactly one comparison direction: up or down. If two consecutive comparisons were both up, their three elements would be strictly increasing; if both were down, the three would be strictly decreasing. Therefore, a valid array is exactly one whose comparison directions alternate.

**Record the final value and direction.** Let $m=r-l+1$, and index the available values from $0$ through $m-1$ after subtracting `l`. For an array of a fixed length, let `ending_up[x]` count arrays that end at value index `x` with an upward final comparison, and define `ending_down[x]` analogously.

For length two, `ending_up[x] = x` because any of the `x` smaller values may precede `x`. Similarly, `ending_down[x] = m - 1 - x`.

**Extend only from the opposite direction.** An array ending with an upward comparison into `x` must extend an array whose previous comparison was downward and whose last value `y` satisfies $y<x$. Thus

$$
\operatorname{nextUp}[x]=\sum_{y<x}\operatorname{endingDown}[y].
$$

The symmetric transition is

$$
\operatorname{nextDown}[x]=\sum_{y>x}\operatorname{endingUp}[y].
$$

A left-to-right prefix sum evaluates every upward transition together in $O(m)$ time, and a right-to-left suffix sum does the same for downward transitions. These transitions preserve different adjacent values through their strict inequalities and force alternating directions, so every counted array is valid. Conversely, removing the last value from any valid array leaves exactly the opposite-direction state used by its transition, so no valid array is omitted. After reaching length `n`, sum both state arrays and apply the modulus.

## Complexity detail

Let $m=r-l+1$. Each of the $n-2$ extensions performs two linear scans of the $m$ values, so the time complexity is $O(nm)$. The current and next direction-count arrays use $O(m)$ auxiliary space. All counts are reduced modulo $10^9+7$ while they are accumulated.

## Alternatives and edge cases

- **Cubic transition search:** Testing every prior value separately for every destination implements the same recurrence in $O(nm^2)$ time, which is unnecessary because each transition range is a prefix or suffix.
- **Enumerate complete arrays:** There are $m^n$ candidate arrays before filtering, far beyond the legal limits.
- **Two available values:** Every valid array must alternate those values, producing exactly two arrays for every legal `n`.
- **Shifted ranges:** Only the number $m=r-l+1$ affects the count; adding the same offset to all permitted values preserves every comparison.
- **Modulo arithmetic:** Counts grow rapidly, so partial prefix and suffix sums must also be reduced modulo $10^9+7$.
