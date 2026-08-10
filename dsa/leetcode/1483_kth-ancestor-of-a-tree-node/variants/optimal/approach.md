## General

**Precompute power-of-two jumps.** Following parent pointers one step at a time would cost `O(k)` per query. Binary lifting stores ancestors at distances one, two, four, eight, and so on, allowing any `k` to be assembled from its binary bits.

`p[node][j]` is the ancestor `2^j` steps above `node`, or `-1` if it does not exist. Column zero is filled directly from `parent` because `2^0=1`.

For higher columns, if the halfway ancestor `p[i][j-1]` exists, jumping another `2^(j-1)` from it yields the full `2^j` ancestor. The assignment looks up the same previous column on that halfway node.

If halfway is `-1`, the full jump is impossible and the entry remains `-1`.

**Why eighteen columns suffice.** The constraints bound `n` and `k` by fifty thousand, below `2^16`. Columns zero through seventeen cover jump sizes through `2^17`, more than enough. The fixed width is a constraint-based form of `O(log n)`.

**Answer by decomposing k.** The query loops from the largest bit down. If bit `i` of `k` is set, it replaces `node` with its `2^i` ancestor. The sum of all taken jump sizes equals `k`.

If a required jump returns `-1`, no kth ancestor exists. The loop breaks before indexing the table with negative one and returns `-1`.

For `k=13`, binary representation uses eight, four, and one. The method performs those three jumps instead of thirteen individual steps. Jump order does not change the final ancestor along a single parent chain; descending order detects impossible large jumps early.
Column zero is correct by definition. If column `j-1` is correct, two successive jumps of its length reach exactly `2^j` levels. Induction proves every table entry.
Each selected bit moves upward by its represented power of two. After processing all bits, the total movement is `k`. If any partial movement passes the root, the requested ancestor cannot exist; otherwise the final node is exactly kth ancestor.

The root's parent is `-1`, so its higher entries remain nonexistent naturally.

**Trace table construction.** If node seven's parent is node five, then `p[7][0] = 5`. If node five's parent is two, `p[7][1]` looks up `p[5][0]` and becomes two, representing two steps. If node two's four-step ancestor is unavailable, later entries that depend on it remain negative one. Each cell composes two already-known equal-length jumps.

**Trace a query.** For a request of five ancestors, binary five is four plus one. The loop first takes the column-two jump of four levels. If that succeeds, it later takes the column-zero parent jump. Intermediate columns whose bits are zero do nothing. The final node is five edges above the start.

**Why no depth array is required.** A depth check could reject `k` larger than a node's depth immediately, but the sentinel table already detects the same condition. Every nonexistent jump is recorded as `-1`, and the query stops when it encounters one.

**The table is immutable after construction.** Parent relationships never change, so preprocessing cost is paid once and every later query reuses the same jump information. This is the central tradeoff: linear-logarithmic preparation and storage produce logarithmic query time across as many as fifty thousand calls.

**Bit-test precedence.** The expression `k >> i & 1` means shift `k` right by `i` and inspect its lowest bit. A nonzero result says the `2^i` component participates in the binary decomposition. Writing parentheses could make this clearer, but Python's operator precedence gives the intended evaluation.

## Complexity detail

Table construction fills `18n` entries, which is `O(n log n)` time and space in general. One query inspects eighteen bits, or `O(log n)` time and `O(1)` extra space.

Across `Q` queries, total time is `O((n+Q) log n)` and retained space is `O(n log n)`, matching the manifest.

The fixed integer table avoids recursion and does not depend on tree height during a query.

## Alternatives and edge cases

- **Walk parent pointers:** It uses no preprocessing but costs `O(k)` per query.
- **Store root paths:** It can answer by depth indexing but may duplicate large path data.
- **Dynamic log width:** Compute `bit_length(n)` instead of hardcoding eighteen for portability to larger constraints.
- **k equals one:** Column zero gives the direct parent.
- **Query at the root:** Every positive ancestor request returns `-1`.
- **k exceeds node depth:** A jump eventually reaches `-1`.
- **Exact node depth:** The result is root zero.
- **Chain tree:** Binary lifting reduces long walks to logarithmic jumps.
- **Shallow branching tree:** The same table works independently of shape.
- **Missing halfway ancestor:** Higher jumps remain `-1`.
- **Break after -1:** It prevents accidental Python negative indexing.
- **Bit order:** Largest-to-smallest and smallest-to-largest both sum correctly; descending is conventional.
- **Fixed 18 columns:** It is safe only because of the stated maximum `n` and `k`.
- **Leaf versus internal node:** Query behavior depends only on the parent chain, not on whether the starting node has children.
- **Many repeated queries:** Preprocessing is reused; no table work is repeated.
- **Parent array ordering:** Nodes need not be processed topologically because column zero is filled for every node before higher columns.
- **Negative-one sentinel:** It is never used as a table row because the query breaks immediately and construction skips it.
