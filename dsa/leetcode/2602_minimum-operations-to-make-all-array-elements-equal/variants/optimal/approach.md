## General

Sort `nums` so that every query target divides it into one contiguous group below the target and one contiguous group at or above it. Build a prefix-sum array `prefix`, where `prefix[i]` is the sum of the first $i$ sorted values.

**Turning absolute differences into two sums**

For a query $x$, let $k$ be the insertion position returned by a lower-bound binary search. Every index before $k$ contains a value smaller than $x$, so raising those $k$ values costs

$$
xk - \texttt{prefix[k]}.
$$

The remaining $n-k$ values are at least $x$. Their sum is `prefix[n] - prefix[k]`, so lowering them to $x$ costs

$$
\bigl(\texttt{prefix[n]} - \texttt{prefix[k]}\bigr) - x(n-k).
$$

Adding the two expressions gives exactly $\sum_j \lvert \texttt{nums[j]}-x \rvert$. Each unit of absolute difference requires one operation, so no transformation can use fewer operations, and performing those increments or decrements attains the computed total.

Sorting and the prefix sums are shared by all queries. A query only performs one binary search and constant-time arithmetic, and answers are appended in the original query order. The algorithm never modifies its sorted data while answering a query, which also preserves the rule that queries are independent.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and $m = \lvert\texttt{queries}\rvert$. Sorting costs $O(n \log n)$, building prefix sums costs $O(n)$, and the $m$ binary searches cost $O(m \log n)$ in total. Therefore the full running time is $O(n \log n + m \log n)$.

The prefix sums and Python's in-place sorting storage require $O(n)$ auxiliary space. The returned $m$-element answer is output space and is not included in that bound.

## Alternatives and edge cases

- **Direct absolute-difference summation:** Computing every $\lvert a-x \rvert$ separately is simple and correct, but costs $O(nm)$ and repeats the same scan for every query.
- **Separate binary searches:** Using distinct lower and upper bounds also works, but equal-to-target values contribute zero, so a single lower-bound partition is sufficient.
- **Targets outside the value range:** A target below the minimum leaves the left side empty; a target above the maximum leaves the right side empty. The same formulas handle both cases.
- **Duplicate values:** Equal values may fall on the right side of the lower-bound partition, but their zero contribution keeps the result unchanged.
- **Large totals:** Although each input value is at most $10^9$, an answer can be much larger, so fixed-width implementations must use 64-bit arithmetic.
