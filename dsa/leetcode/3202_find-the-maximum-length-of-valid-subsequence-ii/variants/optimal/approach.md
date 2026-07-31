## General

**A fixed sum remainder forces two alternating remainders**

Replace every value by its remainder modulo $k$. Suppose a valid subsequence has common adjacent-sum remainder $s$. For three consecutive selected remainders $a,b,c$,

$$
(a+b)\bmod k=(b+c)\bmod k
$$

implies $a=c$. Thus every valid remainder sequence alternates between at most two values: $a,b,a,b,\ldots$. The special case $a=b$ is a constant-remainder sequence. It is therefore enough to track every ordered pair of possible endpoint remainders.

**Extend the reversed endpoint state**

Let `dp[a][b]` be the longest processed valid subsequence ending in remainder `b` whose preceding alternating remainder is `a`. Its common adjacent-sum remainder is `(a + b) % k`.

When the current value has remainder `b`, try every possible `a`. A sequence stored in `dp[b][a]` ends with the reversed pair and can append the current `b`, producing

`dp[a][b] = dp[b][a] + 1`.

A missing reversed state has length zero, so the update first creates a one-element candidate; the next matching remainder creates a valid pair of length two. For `a == b`, the same cell increments on every occurrence. For different remainders, updates alternate between the two transposed cells. Processing a later matching endpoint never loses a better future choice: it extends the current longest reversed state and replaces an older endpoint with an equal-or-longer sequence.

Every update preserves order because the current element comes after the state it extends. Conversely, every valid subsequence alternates between some pair $(a,b)$, so its elements reproduce these transposed updates in order. The maximum table value is therefore exactly the longest valid subsequence.

## Complexity detail

For each of the $n$ values, the algorithm tries all $k$ possible partner remainders, giving $O(nk)$ time. The table contains $k^2$ integer states, so auxiliary space is $O(k^2)$.

Only `value % k` is stored in the state transition; values up to $10^7$ do not enlarge the table.

## Alternatives and edge cases

- **Fix each target sum remainder:** For every $s\in[0,k-1]$, scan `nums` with a one-dimensional endpoint table and extend remainder `(s-r) % k`. This also takes $O(nk)$ time and can use $O(k)$ space, but it makes a separate pass for every target.
- **Index-pair dynamic programming:** Compare every earlier index with every later index and store the best length for their sum remainder. This is correct but takes $O(n^2)$ time.
- **Require remainder zero:** Incorrect; the shared adjacent-sum remainder may be any value, as the second sample demonstrates.
- **Two elements:** Any two selected positions form a valid subsequence because there is only one adjacent sum.
- **`k = 1`:** Every sum has remainder zero, so the entire array is valid.
- **Equal remainders:** Repeated occurrences may all be selected because every adjacent pair has the same sum remainder.
- **Two-remainder alternation:** Extra occurrences in one run may need to be skipped to preserve the alternating pattern.
- **Large `k`:** Remainders absent from the input still occupy table states under the accepted dense representation.
- **Repeated values:** Each occurrence is a distinct position and can extend a subsequence independently.
