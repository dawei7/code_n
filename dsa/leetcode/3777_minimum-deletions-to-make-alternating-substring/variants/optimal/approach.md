## General

**Convert deletions into equal-adjacent edge counts**

Any binary string consists of maximal runs of equal characters. An alternating subsequence can keep at most one character from each run: keeping two from the same run with no different run between them would place equal characters consecutively.

Keeping one character from every run is achievable because neighboring runs contain opposite characters. Therefore the longest alternating subsequence has exactly one character per run.

For a substring of length $L$ with $R$ runs, minimum deletions are $L-R$. Each run of length $m$ contains $m-1$ equal-adjacent edges, and summing over runs gives

$$
\sum(m-1)=L-R.
$$

Thus the answer for `s[l..r]` is simply the number of indices `i` with `l<i<=r` and `s[i]==s[i-1]`.

**Store one indicator per edge ending position**

The source creates `nums` of length `n`. For `i>=1`,

`nums[i] = int(s[i] == s[i-1])`.

Index `i` represents the edge between characters `i-1` and `i`. A one means that edge forces one deletion; a zero means it already alternates.

`nums[0]` is a sentinel because no edge ends at the first character. It begins at zero and is excluded from every range answer.

**Maintain edge sums in a Fenwick tree**

The Fenwick tree uses one-based positions, so source indicator `nums[i]` is stored at tree position `i+1`. Initialization inserts every one-valued real edge.

`update(x, delta)` adds `delta` to all Fenwick ranges containing position `x`. `query(x)` returns the sum of tree positions 1 through `x`. Both move by the lowest set bit and take $O(\log N)$ time.

For a type-two query `[2,l,r]`, relevant source indicators are `nums[l+1]` through `nums[r]`. Their tree positions are `l+2` through `r+1`. The prefix difference

`bit.query(r+1) - bit.query(l+1)`

keeps exactly that interval. It excludes the boundary edge ending at `l` because the character before `l` is outside the substring.

For a one-character range, `l=r` and the two prefix queries are equal, correctly returning zero.

**A flip changes only its two incident edges**

Flipping `s[j]` cannot affect comparisons that use neither endpoint `j`. Only these indicators may change:

- `nums[j]` for edge $(j-1,j)$, when `j>0`;
- `nums[j+1]` for edge $(j,j+1)$, when `j+1<n`.

Because the alphabet contains only `A` and `B`, flipping exactly one endpoint toggles equality: an equal pair becomes different, and a different pair becomes equal. The source can therefore XOR each affected indicator with one without storing a mutable copy of `s`.

For a current bit `v`, the tree delta is

`(v ^ 1) - v`.

This equals $+1$ for $0\to1$ and $-1$ for $1\to0$. The source computes the delta, toggles `nums`, and updates the corresponding one-based tree position.

**Explain the index-zero sentinel toggle**

The code toggles `nums[j]` unconditionally, even when `j=0`. In that case it changes the sentinel `nums[0]` and tree position one, although there is no real left edge.

This is harmless because every range result subtracts `bit.query(l+1)` with `l>=0`. Tree position one is included in both the right prefix and the subtracted prefix, so it always cancels. A flip at zero also correctly toggles real edge `nums[1]` when the string has a second character.

Repeated flips at zero may alternate the sentinel between zero and one, but cancellation remains exact. This is an implementation quirk, not a claim that an edge exists before the string.

**Why no mutable character array is necessary**

For a two-character alphabet, flipping one character always reverses each incident equality status regardless of the current letter. Future operations need only those statuses to answer deletion queries and to toggle them again.

The source therefore maintains the derived edge array instead of `s` itself. This would not be sufficient for an alphabet with three or more characters: changing one endpoint would not always turn “different” into “equal.” The binary guarantee is essential.

**Trace a state change**

For `"ABB"`, indicators are `[0,0,1]`: edge A-B alternates and edge B-B is equal. Query `[0,2]` sums the real indicators and returns one.

Flipping index two affects only `nums[2]`, toggling it from one to zero. The represented string is now `"ABA"` even though no character array was built. The next full-range sum is zero, so no deletions are needed.

Every range answer equals the current number of equal internal edges, which equals the proven minimum deletion count. Every flip updates exactly the affected real edges, so the invariant remains true throughout the stateful query sequence.

## Complexity detail

Initialization examines $N-1$ edges and performs a Fenwick update for every equal one, costing $O(N\log N)$ worst-case. It could be built in linear time, but that is not the exact source.

Each flip performs at most two real-edge updates plus the harmless sentinel update case, all $O(\log N)$. Each range query performs two prefix sums, also $O(\log N)$. Across $Q$ queries, total time is $O((N+Q)\log N)$.

`nums` and the Fenwick array each store $O(N)$ integers; the returned answers use up to $O(Q)$ output space. Auxiliary data-structure space is $O(N)$.

## Alternatives and edge cases

- **Segment tree:** It can maintain the same edge sums with $O(\log N)$ updates and queries, but a Fenwick tree is smaller for point updates plus range sums.
- **Recompute each substring:** Scanning every requested range can cost $O(NQ)$.
- **Maintain characters and recompare neighbors:** This is valid, but the binary toggle property lets the source update indicators directly.
- **Count equal pairs including edge `(l-1,l)`:** That edge crosses the substring boundary and must be excluded.
- **Assume answer is number of runs:** Minimum deletions are length minus runs, equivalently equal-edge count.
- **Flip at index zero:** The sentinel update cancels from every query; the real right edge is still toggled.
- **Flip at index `n-1`:** Only the left incident edge is real, so the guarded right update is skipped.
- **Single-character string:** There are no real edges, and every type-two answer is zero.
- **Already alternating range:** All internal indicators are zero, producing zero deletions.
- **All-equal range of length `L`:** It has `L-1` equal edges and needs `L-1` deletions.
- **Repeated flip of the same index:** Both affected equality indicators toggle back on the second flip.
- **Range after earlier flips:** The Fenwick state incorporates updates, so queries are correctly stateful.
- **Binary alphabet dependency:** XOR-toggling equality is guaranteed only because every character has exactly one opposite value.
- **Output order:** Answers are appended only for type-two queries and retain their relative query order.
- **Input string:** It remains immutable; `nums` is the maintained state representation.
