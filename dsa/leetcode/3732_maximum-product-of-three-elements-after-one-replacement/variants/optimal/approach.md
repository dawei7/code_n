## General

**Use the replacement as one selected factor**

Choose any two original elements at distinct indices. Since the array has at least three positions, a third index is available for the mandatory replacement. Replacing that third element by either $10^5$ or $-10^5$ lets its sign agree with the product of the chosen pair, producing

$$
10^5\lvert ab\rvert.
$$

No other construction can do better: every replacement has absolute value at most $10^5$, and the absolute product of its two other selected factors is bounded by the largest absolute pair product among the original elements. Therefore the answer is exactly $10^5$ times the product of the two largest absolute values in `nums`.

Scan once while retaining the largest and second-largest magnitudes. Repeated magnitudes must occupy both slots when they occur at different indices. Their original signs do not matter because the replacement sign can always make the final product nonnegative.

## Complexity detail

Let $n$ be the length of `nums`. One pass examines every value, so time is $O(n)$. Only two magnitudes are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort by absolute value:** Taking the last two magnitudes after sorting is correct but costs $O(n\log n)$ time and $O(n)$ space for a copy.
- **Enumerate pairs:** Testing all original pairs makes the same choice in $O(n^2)$ time.
- **Exactly one replacement:** The method always uses a distinct third index as the replaced factor, so it never treats replacement as optional.
- **Two zeros among three elements:** At least one zero remains outside any single replacement, forcing product zero.
- **Negative pair:** Choose a positive replacement; for a positive pair, choose either positive or negative as needed to keep the product positive.
- **Repeated maximum magnitude:** Two equal magnitudes from different indices are both valid factors and must both be retained.
- **Large result:** Three factors of magnitude $10^5$ produce $10^{15}$, requiring a 64-bit integer in fixed-width languages.
