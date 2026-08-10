## General

**Convert every subarray XOR into two prefix XORs**

Define:

$$
P[0]=0,
\qquad
P[t+1]=P[t]\mathbin{\mathrm{xor}}\texttt{nums}[t].
$$

Then the XOR of subarray `nums[l..r]` is:

$$
P[l]\mathbin{\mathrm{xor}}P[r+1].
$$

Every value before `l` appears in both prefixes and cancels under XOR.

For a fixed right endpoint `r`, `P[r + 1]` is fixed. Maximizing the subarray XOR means choosing the best eligible start-prefix `P[l]`.

The source builds all prefix XORs once in `prefix_xor`.

**Valid starts form a suffix for each right endpoint**

The range condition is:

$$
\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r])\le k.
$$

If a window is valid, removing elements from its left cannot increase its maximum-minus-minimum range. Therefore every later start is also valid.

For each `r`, there is a smallest valid start `left`. All starts from `left` through `r` are eligible, and starts before `left` are not.

As `r` increases, extending a window cannot reduce its range. A previously invalid start cannot become valid again, so `left` only moves right. This gives a sliding window.

**Maintain the window maximum and minimum**

`maximum_indices` is a deque of indices whose values decrease from front to back. Before appending `right`, the source removes back indices with value `<= value`. The new value is at least as large and remains in the window longer, so those older values can never again be needed as maxima.

Its front is the current maximum.

`minimum_indices` is symmetric: values increase from front to back, and back indices with value `>= value` are removed. Its front is the current minimum.

After appending the new index, the source can test current range in $O(1)$:

`nums[maximum_indices[0]] - nums[minimum_indices[0]]`.

While that exceeds `k`, it removes the current `left` from all maintained structures and increments `left`.

When an extreme deque's front equals the outgoing index, that front is popped. Other stored indices remain inside the new window.

**The trie stores exactly the eligible start prefixes**

Before processing right endpoint `right`, the source inserts `prefix_xor[right]`. This prefix corresponds to subarray start `l = right` and guarantees the singleton candidate is present.

After any shrinking, the trie contains exactly:

$$
P[\texttt{left}],P[\texttt{left}+1],\ldots,P[\texttt{right}].
$$

These are precisely the start prefixes for every valid subarray ending at `right`.

When the left boundary advances, `update(prefix_xor[left], -1)` removes that start prefix before incrementing `left`. Prefix values can repeat, so the trie needs counts rather than a simple present/absent flag.

**Represent a counted 15-bit binary trie**

Every input is below $2^{15}$. XOR of such values also uses only bits 14 through 0.

Each trie node has:

- a zero-bit child in `zero_child`;
- a one-bit child in `one_child`;
- `count[node]`, the number of active inserted values passing through that node.

The three parallel arrays avoid allocating a separate Python object for every node.

`update(value, delta)` starts at the root, adjusts its count, then follows the value's bits from 14 down to 0. Missing children are created during insertion. Every visited node's count changes by `+1` or `-1`.

Nodes are not physically deleted when their count reaches zero. Query logic ignores zero-count branches, so they can safely remain allocated and later be reused if the same bit path becomes active again.

**Greedily maximize XOR from the highest bit**

To maximize `value XOR stored_prefix`, the query decides bits from 14 down to 0.

At a bit where `value` has 0, choosing a stored 1 makes the XOR bit 1. At a bit where `value` has 1, choosing a stored 0 makes the XOR bit 1. The preferred child is therefore the opposite branch.

If that child exists and has positive count, the source takes it and sets the result bit:

`result |= 1 << bit`.

Otherwise it follows the same-bit child, producing XOR bit zero.

Choosing an available 1 at the highest undecided result bit is always optimal. No combination of lower bits can compensate for losing a higher power of two. The active count guarantees the chosen prefix can be completed through all remaining levels.

The function returns the maximum XOR value itself, not the stored prefix.

**Synchronize the structures for each right endpoint**

For each new `right`, the exact order is:

1. insert start prefix `P[right]` into the trie;
2. add `nums[right]` to both monotonic deques;
3. shrink `left` until the range is valid, removing outgoing prefix XORs and stale extrema;
4. query the trie against `P[right + 1]`;
5. update the global answer.

After step 3, the deques describe element window `[left,right]` and the trie describes its possible start indices. Their boundaries are synchronized.

**Trace the prefix choice**

For any active start `l`, querying with `P[r+1]` produces:

$$
P[r+1]\mathbin{\mathrm{xor}}P[l]
=
\operatorname{XOR}(\texttt{nums}[l..r]).
$$

The trie picks the largest value over every valid `l` at once.

For `[5,4,5,6]` and `k=2`, when `r=3` the minimum valid start is 0 because the full range is $6-4=2$. The active prefixes represent starts 0 through 3. Querying `P[4]` finds the prefix for start 1, yielding XOR $4\mathbin{\mathrm{xor}}5\mathbin{\mathrm{xor}}6=7$.

With `k=1`, invalid wider starts are removed. The singleton start at index 3 always remains eligible and yields value 6.

**Why every candidate considered is valid and the maximum is complete**

Sliding-window monotonicity makes `left` the earliest valid start. The trie contains every and only prefix index from `left` through `right`, so every queried XOR is a valid subarray ending at the current right endpoint.

Conversely, any valid subarray ending there starts at or after `left`, so its prefix is present in the trie. Greedy trie traversal finds the maximum among all of them.

Processing every right endpoint covers every nonempty subarray exactly within its endpoint's candidate set. Taking the global maximum gives the requested answer.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $V=2^{15}$. Each prefix is inserted once and removed at most once. A trie update or query visits $\log_2V=15$ bits, costing $O(\log V)$.

Each index enters and leaves each monotonic deque at most once, adding $O(N)$ total work. Overall time is $O(N\log V)$.

Each distinct inserted bit path can create up to $\log V$ nodes, so the counted trie uses $O(N\log V)$ space in the worst case. Prefix XORs and deques use $O(N)$ additional space. The trie term dominates.

## Alternatives and edge cases

- **Enumerate all valid subarrays:** Maintaining range and XOR incrementally still requires $O(N^2)$ endpoint pairs.
- **Balanced range structure plus XOR scan:** Fast min/max alone is insufficient; scanning all eligible prefix XORs per endpoint remains quadratic.
- **Linear XOR basis:** A basis maximizes XOR over arbitrary combinations of values, not XOR with one selected prefix, so it solves a different problem.
- **k equals zero:** The valid window contains only subarrays whose values are all equal; the sliding range logic enforces this.
- **Singleton subarray:** It is always valid, ensuring at least one active trie prefix before each query.
- **Repeated prefix XOR values:** Node counts allow multiple active copies and prevent one deletion from removing all copies.
- **Zero-count trie nodes:** They remain allocated but are ignored by `maximum_xor`.
- **Duplicate extrema:** The monotonic deques keep the newest equal value, which expires later and preserves the correct range.
- **Value zero:** Its all-zero bit path is handled normally.
- **Inclusive range bound:** Shrinking occurs only when range is `> k`, so equality remains valid.
- **Fixed bit width:** Bits 14 through 0 cover both inputs and every prefix XOR because XOR cannot introduce a bit absent from all operands.
