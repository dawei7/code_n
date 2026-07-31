## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `a`: The inclusive lower boundary of the middle part.
- `b`: The inclusive upper boundary of the middle part.

The boundaries satisfy `a < b`. Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the minimum number of neighboring-element swaps that can arrange all values less than `a` first, all values in `[a, b]` next, and all values greater than `b` last. Return the count modulo $10^9+7$.
