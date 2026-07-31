## General

**Turning a block XOR into one prefix key.** Let $p_i$ be the XOR of the first $i$ elements, with $p_0=0$. A block that begins at cut $j$ and ends immediately before cut $i$ has XOR $p_i\mathbin{\mathrm{xor}}p_j$. It equals a required value $t$ exactly when

$$
p_j=p_i\mathbin{\mathrm{xor}}t.
$$

This equation identifies the prefix-XOR key of every earlier cut that could precede the new block.

**Encoding the required alternation.** Define $E_i$ as the number of ways to partition the first $i$ elements into an even number of valid blocks, and $O_i$ as the corresponding count for an odd number of blocks. The empty prefix supplies the base state $E_0=1$ and $O_0=0$. Appending a `target1` block changes an even block count into an odd one; appending a `target2` block changes an odd block count into an even one. Therefore,

$$
O_i=\sum_{\substack{0\le j<i\\p_j=p_i\mathbin{\mathrm{xor}}\texttt{target1}}}E_j,
\qquad
E_i=\sum_{\substack{0\le j<i\\p_j=p_i\mathbin{\mathrm{xor}}\texttt{target2}}}O_j.
$$

The parity state ensures that the first block must use `target1` and that every later block receives the correct alternating requirement.

**Aggregating all legal previous cuts.** Maintain two maps. For each prefix XOR, the first stores the sum of $E_j$ over processed cuts and the second stores the sum of $O_j$. At cut $i$, one lookup in the even map computes $O_i$, and one lookup in the odd map computes $E_i$. Only after both lookups are complete are the new states added under key $p_i$. This order enforces $j<i$, so an empty block is never counted.

Every transition counted by the maps appends one non-empty block with the required XOR to a previously valid partition. Conversely, removing the last block from any valid partition leaves exactly the prior parity state under the prefix key selected by the equation above. The transitions therefore count every valid partition once and only once. Since a valid final partition may contain either an odd or an even number of blocks, the result is $(O_N+E_N)\bmod (10^9+7)$.

## Complexity detail

Let $N$ be the length of `nums`. Each cut performs a constant number of expected-time hash-map operations, so the expected running time is $O(N)$. At most $N+1$ prefix states are accumulated, giving $O(N)$ auxiliary space. All stored counts are reduced modulo $1{,}000{,}000{,}007$.

The benchmark defines size as $N$. Its alternating zero-one sequence repeatedly exercises both parity transitions and produces many valid partitions. The accepted implementation aggregates equal prefix states, while the slower control scans every earlier cut for both transition types, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Quadratic cut dynamic programming:** Computing the same $E_i$ and $O_i$ recurrences by testing every $j<i$ is direct and correct, but costs $O(N^2)$ time.
- **Prefix-XOR-indexed arrays:** Because every input value is below $2^{17}$, every prefix XOR is also below $2^{17}$. Two fixed arrays can replace the maps in $O(N+2^{17})$ time and $O(2^{17})$ space, but the maps initialize only states that occur.
- **Recursive partition enumeration:** Trying every next block boundary exposes the definition clearly, but has exponentially many partition paths unless equivalent prefix-XOR and parity states are aggregated.
- **One block:** The whole array contributes one valid partition exactly when its XOR equals `target1`; no `target2` block is required.
- **Non-empty blocks:** Query the aggregate maps before inserting the current cut, preventing a transition from a prefix to itself.
- **Zero-valued targets and elements:** XOR zero is ordinary data; map membership and stored counts must not be tested through truthiness.
- **Distinct targets:** `target1 != target2` is guaranteed, but their alternation is still governed by block parity rather than by inspecting a block's value afterward.
- **Large counts:** Apply the modulus while accumulating each map entry as well as when returning the final sum.
