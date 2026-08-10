## General

For every subarray we need the square of its distinct-value count. With up to $10^5$ elements, enumerating all endpoint pairs is too slow. The solution instead processes right endpoints from left to right and maintains the distinct count for every possible left endpoint at once.

After processing right endpoint $r$, define $D_l$ as the number of distinct values in `nums[l..r]`. The contribution of all subarrays ending at $r$ is

$$
\sum_{l=0}^{r}D_l^2.
$$

If a data structure maintains all $D_l$, supports adding one to a continuous range of left endpoints, and reports the sum of their squares, each new right endpoint can be handled efficiently. The source uses a lazy segment tree for exactly those operations.

**Which left endpoints change when a value arrives**

Let `value = nums[r]`, and let $p$ be its most recent previous position, or $-1$ if it has not appeared.

- For $l\le p$, subarray `nums[l..r-1]` already contains `value` at position $p$. Appending another copy does not change its distinct count.
- For $p<l\le r$, the previous occurrence lies outside `nums[l..r-1]`. Appending `value` introduces a new distinct value, so $D_l$ increases by one.

Therefore the update is one range addition:

`add(last_position[value] + 1, r, 1)`.

Afterward, `last_position[value]` becomes $r$. This range rule is the crucial observation that turns $O(n)$ work for one right endpoint into $O(\log n)$.

**What each segment-tree node stores**

For the left-endpoint interval represented by a node, `sums[node]` stores $\sum D_l$, and `square_sums[node]` stores $\sum D_l^2$. The root covers all indices $0$ through $n-1$.

Suppose every value in a node interval of length $q$ receives increment $c$. Algebra gives

$$
(D_l+c)^2=D_l^2+2cD_l+c^2.
$$

Summing over the interval produces

$$
\sum(D_l+c)^2
=
\sum D_l^2+2c\sum D_l+c^2q.
$$

That is the exact `apply` update:

`square_sums += 2 * increment * sums + increment * increment * length`,

followed by

`sums += increment * length`.

Both aggregates are reduced modulo $10^9+7$. The pending increment is accumulated in `lazy[node]` so a fully covered interval can be changed without immediately descending to every leaf.

**Why lazy propagation remains correct**

When a later partial update needs a node's children, `push` applies the stored increment to each child and clears the parent tag. Each child's two aggregates are adjusted by the same algebraic identity. Thus the children become current before recursion continues.

After a partial update, the parent recomputes both aggregates as the modular sum of its children. A fully covered update calls `apply` and stops; a partial update pushes, recurses only into intersecting children, then merges.

**Accumulate one family of subarrays at a time**

After updating for right endpoint $r$, the root's `square_sums[1]` equals the sum of $D_l^2$ over all starts. Positions $l>r$ have never been updated and remain zero, so including the full root range adds no unwanted contribution. The solution adds this root value to `answer`.

Every nonempty subarray has one unique right endpoint. When that endpoint is processed, its left endpoint's leaf contains its exact distinct count. Therefore its squared count is included once, and only once.

For `[1,2,1]`, right endpoint $0$ adds one to starts $0..0$, giving counts $[1]$. Endpoint $1$ has a new value and updates starts $0..1$, giving $[2,1]$. At endpoint $2$, the previous $1$ was at $0$, so only starts $1..2$ increase, producing $[2,2,1]$. The squared sums are $1$, $5$, and $9$, totaling $15$.

## Complexity detail

There is one segment-tree range update per array position. A lazy range update visits $O(\log n)$ nodes, and reading the root is $O(1)$. Dictionary lookup and update are expected $O(1)$. Total expected time is $O(n\log n)$.

The three tree arrays each have $4n$ entries, so they use $O(n)$ space. The last-position dictionary contains at most one entry per distinct value, also $O(n)$. Recursive segment-tree calls use $O(\log n)$ stack depth. Overall auxiliary space is $O(n)$.

All aggregates are kept modulo $10^9+7$. The lazy increments themselves are not reduced, but each position is incremented at most $n$ times, and Python integers safely hold them.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining a set while extending each left endpoint takes $O(n^2)$ time, which is appropriate for version I but not for this input size.
- **Rebuild distinct counts for every right endpoint:** Scanning all starts after each append is also $O(n^2)$. The previous-occurrence boundary proves all changing starts form one interval.
- **Segment tree stores both moments:** Keeping only $\sum D_l$ cannot recover $\sum D_l^2$. The square-update formula requires both the first and second moments.
- **First occurrence:** With previous position $-1$, update range $[0,r]$; the new value is absent from every subarray ending before $r$.
- **Consecutive duplicate:** If the previous position is $r-1$, only start $r$ changes. Every longer subarray already contains that value.
- **Positions after the current right endpoint:** Their leaves remain zero, so the full-root square sum is still exactly the contribution of valid starts.
- **Modulo arithmetic:** Addition and the polynomial range-update identity are compatible with taking residues, so reducing node aggregates cannot alter the final modular answer.
- **Empty array is irrelevant:** The contract guarantees at least one element, allowing the tree to be built over range $0..n-1$.
- **Source provenance:** The local editorial is unavailable; this explanation follows the exact checked-in segment-tree implementation and its update formulas.
