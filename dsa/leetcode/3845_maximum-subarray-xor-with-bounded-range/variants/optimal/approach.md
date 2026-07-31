## General

**Valid starts form one sliding interval**

Fix a right endpoint $r$. If `nums[l:r + 1]` satisfies the range bound, then removing elements from its left cannot increase its maximum-minus-minimum difference. The valid start indices are therefore a suffix $[L,r]$. Maintain the smallest such $L$ while advancing $r$. A decreasing deque exposes the current maximum and an increasing deque exposes the current minimum. Each new value removes weaker indices from the backs; when the exposed difference exceeds `k`, advance $L$ and remove an expired front index when necessary.

**Prefix XOR converts each subarray into a pair query**

Define `prefix_xor[0] = 0` and `prefix_xor[i + 1] = prefix_xor[i] XOR nums[i]`. Cancellation of equal prefixes gives

$$
\operatorname{xor}(l,r)=\texttt{prefix\_xor}[l]
\mathbin{\mathrm{XOR}}\texttt{prefix\_xor}[r+1].
$$

For the fixed right endpoint, every valid candidate is obtained by pairing `prefix_xor[r + 1]` with one prefix indexed by $l\in[L,r]$. Store exactly those eligible prefix values in a counted binary trie. Before processing endpoint $r$, insert `prefix_xor[r]`. Whenever $L$ moves, decrement the count along the path for the expired `prefix_xor[L]`. Nodes may remain allocated, but a branch is usable only when its count is positive; stale prefixes can never influence a later answer.

**Greedy trie descent maximizes the XOR**

All prefix values are below $2^{15}$, so inspect bits 14 through 0. At one bit, first follow a positive-count child carrying the opposite bit from the query value, because that sets the current result bit to one. If no active opposite child exists, follow the equal-bit child. Higher bits dominate every combination of lower bits, so this greedy choice produces the largest XOR against any currently eligible prefix.

After the range window is restored for $r$, the trie contains every and only `prefix_xor[l]` with $l\in[L,r]$. The query therefore examines exactly all valid subarrays ending at $r$ and selects their maximum value. Taking the maximum over every right endpoint covers every valid nonempty subarray, proving the returned answer is global.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$, $V=2^{15}$, and $B=\log_2V=15$. Each index enters and leaves each monotonic deque at most once. Every prefix is inserted once, removed at most once, and queried once through $B$ trie levels. The total time is $O(N\log V)$, which is linear in $N$ under the fixed 15-bit source bound.

The prefix array, two deques, and trie contain $O(N)$ logical entries. A non-compacted array trie can create at most $O(N\log V)$ nodes, giving the stated $O(N\log V)$ auxiliary-space bound; with fixed $B$, this is $O(N)$ in the input length.

The benchmark defines size as $N$ and keeps every subarray range-valid while varying prefix XORs across eight bits. This forces a quadratic enumeration control to inspect all $N(N+1)/2$ subarrays, whereas counted-trie solutions retain $O(N\log V)$ growth.

## Alternatives and edge cases

- **Enumerate every subarray:** Extend each left endpoint while maintaining its XOR, minimum, and maximum. This is straightforward and correct but requires $O(N^2)$ time even when every subarray is valid.
- **Ordered multiset for the range window:** A balanced multiset can maintain the minimum and maximum in $O(\log N)$ per endpoint, but it does not replace the separate maximum-XOR data structure; the two monotonic deques give amortized $O(1)$ range maintenance.
- **Uncounted trie:** Inserting prefix XORs without deletion allows an expired start index to produce an attractive but invalid XOR after $L$ advances.
- **Insert timing:** For endpoint $r$, `prefix_xor[r]` must be present because the length-one subarray starting at $r$ is always a valid candidate.
- **Prefix zero:** `prefix_xor[0] = 0` represents subarrays beginning at index zero and must participate while start zero remains valid.
- **Zero range bound:** When `k = 0`, a multi-element subarray is valid only if all its elements are equal; isolated elements remain valid.
- **Zero values:** Both input values and XOR results may be zero, so zero cannot be used as an empty-trie sentinel.
- **Duplicate prefixes:** Different starts may have the same prefix XOR. Per-node counts ensure removing one occurrence does not erase another active occurrence.
- **Value boundary:** Values up to `32767` require bits 14 through 0; no higher prefix-XOR bit can be set.
