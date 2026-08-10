## General

**Build the best product for every smaller total.**

The exact source uses bottom-up dynamic programming, not the mathematical “use as many threes as possible” formula named in the manifest. It evaluates all two-part split points for every total from `2` through `n` and reuses products already computed for smaller totals.

Define

$$
f[i]=\text{the maximum product obtainable by splitting }i
\text{ into at least two positive integers}.
$$

The phrase “at least two” matters. Returning `i` itself is not a legal answer for state `i`, even when leaving it whole would be numerically larger than splitting it. However, when `i` is only one part of a larger decomposition, it may legally remain unsplit. The transition explicitly handles both roles.

The table has length `n + 1` so each total is also its index. It is initialized with ones. For the meaningful base state `f[2]`, the only split is `1 + 1`, giving product one. The loops calculate that value naturally. Entries `f[0]` and `f[1]` are not public problem answers; their initial ones act as harmless small-state values when a remainder of one appears.

**Choose one final part `j`.**

For a current total `i`, the inner loop tries every `j` from `1` through `i - 1`. This creates two positive pieces:

$$
(i-j)+j=i.
$$

The part `j` is kept as one factor. For the remainder `i - j`, there are two meaningful choices.

First, keep the remainder whole. Then the decomposition has exactly two parts and product

$$
(i-j)j.
$$

This candidate is essential for small totals and for cases where further breaking the remainder would reduce its contribution. For example, splitting `4` at `j = 2` gives the legal product $2\cdot2=4$.

Second, break the remainder according to its already computed optimum. This produces

$$
f[i-j]j.
$$

Because `i - j < i`, the outer loop has already finalized `f[i - j]`. This candidate represents decompositions with at least three total parts when the remainder's optimum genuinely uses two or more parts.

The source updates `f[i]` with the maximum of its current value and both candidates:

`max(f[i], f[i - j] * j, (i - j) * j)`.

Equivalently, it multiplies `j` by the better of leaving `i - j` whole and using its best legal split.

**Why only one side needs the dynamic-programming value.**

One might expect a candidate such as `f[j] * f[i - j]`. It is not required. Any complete decomposition of `i` contains some final positive part `j`; all other parts sum to `i - j`. The transition can designate one actual part of the decomposition as `j` and place the complete remaining decomposition inside `f[i - j]`.

If the remainder has only one part, the direct `(i - j) * j` candidate covers it. If it has two or more, `f[i - j] * j` covers it. Since every possible `j` is tried, this representation includes every legal decomposition regardless of how many pieces appear on either conceptual side of an original split.

The recurrence is asymmetric only in notation. Exhaustive choice of the singled-out factor makes it complete.

**Walk through the first few states.**

For `i = 2`, only `j = 1` is available. Both candidates equal one, so `f[2] = 1`, representing `1 + 1`.

For `i = 3`, split `1 + 2` gives product two, so `f[3] = 2`.

For `i = 4`, the split at `j = 2` considers the direct product

$$
(4-2)\cdot2=4,
$$

which beats products involving a split remainder. Thus `f[4] = 4`, representing `2 + 2`.

For `i = 5`, choosing `j = 2` can leave remainder `3` whole, giving $3\cdot2=6$. The table records six.

The values continue as

$$
f[6]=9,\quad
f[7]=12,\quad
f[8]=18,\quad
f[9]=27,\quad
f[10]=36.
$$

At total ten, one route to `36` chooses `j = 4` and uses `f[6] = 9`, yielding $4\cdot9=36$. The stored state for six corresponds to `3 + 3`, so the full decomposition is `4 + 3 + 3`, matching the example.

**Why every stored product is legal.**

The direct candidate uses two positive parts because `1 <= j < i`. The recursive candidate takes a legal decomposition of positive remainder `i - j` and adds the positive part `j`. It therefore contains at least three parts when the remainder is split, or still forms a legal two-part structure in tiny initialized cases.

Every multiplication preserves the same total sum: the remainder parts sum to `i - j`, and adding `j` restores `i`. Thus the source never compares an impossible product.

**Why the maximum is optimal.**

Use induction over `i`. State `2` is correct. Assume all smaller meaningful states are optimal. Take any legal decomposition of `i` and select one of its parts as `j`.

If only one other part remains, its product is exactly `(i - j) * j`, which the source tests. If two or more other parts remain, their product cannot exceed the optimal stored `f[i - j]` by the induction hypothesis, so the full decomposition cannot exceed `f[i - j] * j`, also tested.

Therefore every legal decomposition is bounded by one candidate considered for its chosen `j`. Since every candidate itself describes a legal decomposition, taking the maximum produces exactly the optimum. The outer loop eventually proves and returns `f[n]`.

## Complexity detail

For each `i` from `2` through `n`, the inner loop performs `i - 1` iterations. Their total is

$$
\sum_{i=2}^{n}(i-1)=\frac{n(n-1)}{2},
$$

so the exact implementation takes $O(n^2)$ time.

The table contains `n + 1` integers and uses $O(n)$ auxiliary space. The loops and temporary products require only constant additional storage.

The manifest describes exponentiation based on the optimal structure of threes and lists $O(\log n)$ time with $O(1)$ space. That is not the checked-in source. The source has nested loops and a full DP table, so its actual bounds are $O(n^2)$ time and $O(n)$ space. The small constraint $n\le58$ keeps this implementation practical.

## Alternatives and edge cases

- **Closed-form threes-and-twos structure:** For `n > 3`, use as many `3`s as possible, except replace a remainder `1` plus one `3` by `2 + 2`. Fast exponentiation yields the manifest's $O(\log n)$ time and $O(1)$ space, but this logic is not in the source.

- **Top-down memoization:** Define the same state recursively and cache each total. It preserves $O(n^2)$ time and $O(n)$ storage but adds recursive overhead.

- **Greedy repeated subtraction of three:** Multiply by three while the remaining sum exceeds four, then multiply by the final `2`, `3`, or `4`. This runs in $O(n)$ arithmetic steps and constant auxiliary space.

- **`n = 2`:** The only valid decomposition is `1 + 1`, and the table returns one.

- **`n = 3`:** The best required split is `1 + 2`, product two. The direct candidate is necessary because treating three as an unsplit public answer would violate the at-least-two-parts rule.

- **Remainder one:** A factor of one does not improve a product, but split enumeration still handles it safely. Better candidates such as converting `3 + 1` into `2 + 2` win automatically.

- **Why initialize with one:** Products of positive integers are at least one, and the base split of two is one. The loops overwrite larger states whenever a better legal product exists.

- **Integer size:** The constraint ensures the optimum fits ordinary challenge expectations; Python integers also grow automatically, so multiplication cannot overflow.
