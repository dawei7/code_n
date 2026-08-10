## General

A static prefix array gives constant-time range sums, but one changed element invalidates every later prefix. Recomputing those prefixes after each update could cost linear time. A Fenwick tree, also called a Binary Indexed Tree, stores overlapping partial sums so that both a point change and a prefix sum touch only logarithmically many entries.

The source uses one-based positions inside the tree:

- original array index 0 corresponds to Fenwick position 1;
- original index `i` corresponds to position `i + 1`;
- Fenwick prefix query `query(x)` returns the sum of the first `x` original elements, covering original indices 0 through `x - 1`.

The extra tree entry at index 0 is a sentinel. No data value is stored there.

**What a Fenwick entry stores**

For a positive position $x$, define

$$
\operatorname{lowbit}(x)=x\mathbin{\&}(-x).
$$

The expression isolates the least significant 1 bit of $x$. In a Fenwick tree, `c[x]` stores the sum of a block ending at $x$ whose length is `lowbit(x)`. Its inclusive one-based interval is

$$
[x-\operatorname{lowbit}(x)+1,\ x].
$$

Examples make the pattern concrete:

| `x` | Binary form | `lowbit(x)` | Block summarized by `c[x]` |
| --- | --- | --- | --- |
| 1 | `001` | 1 | `[1, 1]` |
| 2 | `010` | 2 | `[1, 2]` |
| 3 | `011` | 1 | `[3, 3]` |
| 4 | `100` | 4 | `[1, 4]` |
| 6 | `110` | 2 | `[5, 6]` |

Larger powers of two summarize larger aligned ranges. These carefully overlapping blocks let the structure move between a position and the next relevant containing block with simple bit arithmetic.

**Adding a delta at one position**

`BinaryIndexedTree.update(x, delta)` means “increase the logical value at one-based position `x` by `delta`.” It is an additive operation, not an assignment.

The value belongs to `c[x]` and also to every larger Fenwick block whose interval contains position `x`. After updating one tree entry, the source moves to

`x += x & -x`.

This jumps to the next ancestor block that contains the original position. Repeating until `x > n` updates every stored partial sum affected by the point change and no unrelated block.

For example, in a tree of sufficient size, changing position 3 visits positions 3, 4, 8, and so on. Entry 3 covers `[3, 3]`, entry 4 covers `[1, 4]`, and entry 8 covers `[1, 8]`; all contain logical position 3.

Because `lowbit(x)` is at least one for positive `x`, each update step strictly increases `x`. The loop always terminates after moving through at most one relevant node per binary scale.

**Reading a prefix sum**

`query(x)` returns the sum of one-based positions 1 through `x`, which equals the first `x` original elements.

It begins with `s = 0`, adds `c[x]`, and then moves to

`x -= x & -x`.

The block stored at `c[x]` covers the trailing portion of the still-unaccounted prefix. Subtracting its length moves immediately before that block. The next entry covers the next trailing block, and the process repeats until `x` reaches zero.

These blocks are disjoint and together cover the full prefix. For example, `query(7)` uses a block ending at 7 of length 1, then a block ending at 6 of length 2, then a block ending at 4 of length 4. They cover `[7,7]`, `[5,6]`, and `[1,4]`, exactly positions 1 through 7 without overlap.

Each subtraction clears the least significant set bit, so the number of iterations is at most the number of bits needed to represent $n$.

**Building the initial structure**

The constructor creates a zero-filled tree of size `len(nums) + 1`. It enumerates `nums` starting at 1, so initial value `v` at original index `i - 1` is added with `tree.update(i, v)`.

Applying one point update for every input value constructs all Fenwick partial sums. The tree does not retain a separate `nums` list; its aggregated blocks become the authoritative state.

For `nums = [1, 3, 5]`, the relevant internal entries after construction are:

- `c[1] = 1`, summarizing the first value;
- `c[2] = 4`, summarizing values 1 and 3;
- `c[3] = 5`, summarizing the third value.

`query(3)` adds `c[3]` and `c[2]`, giving $5+4=9$.

**Turning assignment into an additive change**

The public method `update(index, val)` must assign a new value, but the Fenwick method only adds a difference. If the current array value is `prev`, the required additive change is

$$
\Delta=val-prev.
$$

Adding this difference changes the logical value from `prev` to

$$
prev+(val-prev)=val.
$$

Because no separate array copy exists, the source recovers `prev` with `sumRange(index, index)`. A single-element range sum is exactly the current value at that index. It then calls `tree.update(index + 1, val - prev)` using the one-based Fenwick position.

In the example, assigning original index 1 from 3 to 2 gives `delta = -1`. Adding `-1` to Fenwick position 2 changes `c[2]` from 4 to 3. The full prefix then becomes $5+3=8$, matching `[1, 2, 5]`.

**Answering an inclusive range**

`query(right + 1)` sums original indices 0 through `right`. `query(left)` sums original indices 0 through `left - 1`. Subtracting cancels the part before the desired interval:

$$
\operatorname{sumRange}(left,right)
=
\operatorname{query}(right+1)-\operatorname{query}(left).
$$

The `+1` on the right includes the original element at `right`. The unshifted `left` already counts exactly how many original elements precede the range. This is the same half-open prefix-boundary convention used by ordinary prefix sums, with Fenwick queries computing those prefixes dynamically.

**Why updates and queries remain consistent**

Initially, each source value is added to every Fenwick block that contains its position, so every `c[x]` equals the sum of its defined interval. A point update adds the same delta to exactly the blocks containing the changed position, preserving that statement. Unaffected blocks remain correct.

A query decomposes its prefix into disjoint stored blocks, so it returns the exact current prefix sum. The difference of two exact current prefixes is the exact current inclusive range. Therefore, any sequence of assignments and queries is answered using all changes made so far.

## Complexity detail

Let $n$ be the array length and $q$ the total number of update and range-sum operations.

One Fenwick `update` or `query` visits $O(\log n)$ entries. The constructor performs one update for each of $n$ initial values, so this exact build costs $O(n\log n)$ time.

A public assignment calls one single-element `sumRange`, which performs two Fenwick queries, followed by one Fenwick update. A constant number of logarithmic operations is still $O(\log n)$.

A public `sumRange` performs two prefix queries and costs $O(\log n)$. Across $q$ mixed operations, total time after construction is $O(q\log n)$, giving the manifest's combined bound

$$
O((n+q)\log n).
$$

The Fenwick array has $n+1$ integers, so auxiliary space is $O(n)$. The source avoids a second length-$n$ copy of current values by querying a point before assignment. `__slots__` removes per-object attribute dictionaries but does not change the asymptotic bound.

## Alternatives and edge cases

- **Iterative segment tree:** Store values in leaves and range sums in parent nodes. It also supports $O(\log n)$ assignments and queries with $O(n)$ space, but usually requires about twice as many array slots and more boundary logic.
- **Linear-time Fenwick construction:** Copy values into the tree and propagate each node once to its parent, building in $O(n)$. The exact source uses the simpler repeated-update build, so its constructor is $O(n\log n)$.
- **Keep a separate current-value array:** Then assignment can read `prev` in $O(1)$ rather than issuing a point query. This uses another $O(n)$ array and keeps update asymptotically $O(\log n)$.
- **Static prefix sums:** They answer queries in $O(1)$ but require $O(n)$ repair after an assignment, making them unsuitable for mixed mutable operations.
- **Direct array storage:** Assignment is $O(1)$ and a range sum is $O(n)$ in the worst case. It favors updates too strongly when both operation types can be frequent.
- **Square-root decomposition:** Block sums give approximately $O(\sqrt n)$ range queries and $O(1)$ updates, a valid middle ground but asymptotically slower for queries than Fenwick.
- **Passing an assignment value directly as the delta:** This would add `val` to the old value rather than replace it. The source must subtract `prev` first.
- **Zero-based Fenwick calls:** Position zero has `lowbit(0) = 0`, so an update loop would never advance. Original indices must be shifted by one.
- **Inclusive right boundary:** `query(right + 1)` is required to include `nums[right]`; using `query(right)` would exclude it.
- **Range starts at zero:** `query(left)` becomes `query(0)`, whose loop performs no iterations and returns zero naturally.
- **Single-element query:** The difference of neighboring prefixes recovers exactly the current value, which is also how public updates find `prev`.
- **Assigning the existing value:** `delta` is zero. The Fenwick traversal adds zero to its ancestors, preserving all sums.
- **Negative values and deltas:** Fenwick sums use ordinary addition, so negative entries and downward assignments work without any ordering assumption.
- **One-element array:** The tree has entries 0 and 1. Every update and query touches at most position 1 and remains valid.
- **Maximum operation count:** Each operation visits only logarithmically many tree nodes, avoiding a full-array scan under the stated $3\cdot10^4$ calls.
