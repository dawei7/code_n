## General

**Turn the product test into a potion threshold**

For a positive spell strength $s$, a potion strength $p$ succeeds exactly when

$$
p \ge \left\lceil\frac{\texttt{success}}{s}\right\rceil.
$$

Compute that ceiling with integer arithmetic as
`(success + s - 1) // s`, avoiding floating-point rounding at values up to
$10^{10}$.

**Binary-search the sorted potions**

Sort a copy of `potions`. For each spell, find the first potion not smaller
than its required threshold. Every potion from that position to the end is
successful, while every earlier potion is too weak. Subtract the boundary
index from $m$ and append the count in the original spell order.

Sorted order makes the successful potions one contiguous suffix. The lower
bound finds its exact first position, including a product equal to `success`.
Thus each reported suffix length counts every and only successful potion for
that spell.

## Complexity detail

Let $n=\lvert\texttt{spells}\rvert$ and
$m=\lvert\texttt{potions}\rvert$. Sorting costs $O(m\log m)$, and $n$ binary
searches cost $O(n\log m)$, for $O(m\log m+n\log m)$ total time. The sorted
copy uses $O(m)$ auxiliary space; the returned $O(n)$ array is output space.

## Alternatives and edge cases

- **Test every pair:** Direct product counting is simple and correct but takes $O(nm)$ time.
- **Sort both arrays with original indices:** A two-pointer sweep can achieve $O(n\log n+m\log m)$ time, but must restore spell order.
- **Floating-point division:** A rounded threshold can misclassify boundary products; integer ceiling division is exact.
- **Equality boundary:** A product exactly equal to `success` is successful.
- **No successful potion:** The lower bound is $m$, producing count zero.
- **Every potion succeeds:** The lower bound is zero, producing count $m$.
- **Duplicate strengths:** Each potion occurrence counts separately.
- **Large product:** Use an integer type that safely represents values through $10^{10}$.
