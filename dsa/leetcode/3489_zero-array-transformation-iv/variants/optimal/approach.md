## General

**Separate the indices**

A query permits any subset of its covered range. Selecting index `i` neither requires nor prevents selecting another index in the same query. Therefore the complete array can reach zero after a prefix exactly when, for every index `i`, some subset of the decrement values from covering queries sums to `nums[i]`.

Maintain this subset-sum reachability independently per index. Bit $s$ of `possible[i]` is 1 when the processed queries can supply an exact total decrement of $s$ at index `i`. Initially only sum zero is reachable, so every bitset begins as `1`.

For query `[left, right, value]`, update every still-unsatisfied covered index with

`possible[i] |= possible[i] << value`.

The unchanged bits represent omitting `i` from the query's subset; shifted bits represent selecting it. Mask away sums above `nums[i]`, since positive future decrements can never bring an overshoot back to the target.

**Stop at the first successful prefix**

Track how many positive targets are not yet reachable. When an update first sets target bit `nums[i]`, mark that index satisfied and decrement the counter. Reachability is monotonic, so a satisfied index never needs another update. The first query after which the counter reaches zero is exactly the minimum valid prefix. If the counter is initially zero, return 0; if it remains positive after all queries, return `-1`.

## Complexity detail

Let $n$ be the array length and $q$ the number of queries. Each query visits at most $n$ covered indices, giving $O(nq)$ updates. The bitsets are Python integers clipped to at most $V+1\le1001$ bits, a fixed legal bound; under the problem's bounded domain each update has constant cost. If bit width is parameterized, the bit-operation factor is $O(\lceil V/w\rceil)$ machine words.

There are $n$ bounded bitsets plus $O(n)$ masks and state flags, so auxiliary space is $O(n)$ under the legal bound, or $O(n\lceil V/w\rceil)$ when bit width is explicit.

## Alternatives and edge cases

- **Binary search the prefix:** monotonicity allows it, but rebuilding every index's subset-sum state for each check adds an unnecessary logarithmic factor.
- **Boolean knapsack arrays:** implement the same recurrence without packed bits but spend $O(V)$ work per covered index and query.
- **Total decrement only:** is insufficient because exact query values form a subset-sum problem; values `2` and `2` cannot produce target 3.
- **Independent subsets:** one query may decrement some covered indices and omit others.
- **Already zero:** every target bit zero is initially reachable, so the answer is 0.
- **Overshoot:** sums beyond an index's target can be discarded permanently because all decrement values are positive.
- **Satisfied index:** later queries may omit it, so its state need not be updated again.
