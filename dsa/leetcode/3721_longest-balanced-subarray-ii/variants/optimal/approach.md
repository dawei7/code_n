## General

For each right endpoint $r$, imagine one balance value for every possible left endpoint $l \leq r$:

$$
B_r(l) = \#\text{ distinct even values in }\texttt{nums}[l..r]
- \#\text{ distinct odd values in }\texttt{nums}[l..r].
$$

A subarray is balanced exactly when its corresponding balance is zero. When the new value `nums[r]` is even, it adds one only to left endpoints after that value's previous occurrence; earlier left endpoints already contained it. An odd value similarly subtracts one over the same endpoint range. Thus each new element performs one range addition from `last_position[value] + 1` through $r$.

Maintain all endpoint balances in a lazy segment tree storing the minimum and maximum balance in each interval. Neighboring left endpoints differ by at most one, because advancing a left boundary can remove at most one distinct value. Therefore an interval contains a zero whenever its minimum is at most zero and its maximum is at least zero. Descend left child first under that condition to find the earliest balanced left endpoint, which gives the longest balanced subarray ending at $r$.

The range update exactly preserves every $B_r(l)$, and the zero search returns the smallest valid $l$. Testing all right endpoints and maximizing `r - l + 1` consequently considers the longest balanced subarray in the whole array.

## Complexity detail

Let $n$ be `nums.length` and $U$ the maximum allowed value. Each element causes one lazy range addition and one leftmost-zero search, both $O(\log n)$, so time is $O(n\log n)$. The segment tree uses $O(n)$ space and the last-position array uses $O(U)$ space, for $O(n+U)$ auxiliary space. Here $U = 10^5$.

## Alternatives and edge cases

- **Quadratic endpoint scan from problem I:** Maintaining two sets for every left endpoint is correct but costs $O(n^2)$ and cannot handle the increased $10^5$ length limit.
- **Plain prefix parity counts:** Element frequencies do not model distinct values; repeated occurrences require the last-occurrence range update.
- **Minimum without maximum:** A negative minimum alone cannot prove a zero exists. Both extrema are needed to detect a crossing in the unit-step balance sequence.
- **Duplicate value:** Only left endpoints after its previous occurrence gain or lose a distinct value when it appears again.
- **One-element array:** Its balance is either `1` or `-1`, so the answer remains `0`.
- **No balanced subarray:** If no endpoint balance reaches zero, the initialized answer `0` is returned.
