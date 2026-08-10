## General

**Build only parity-valid prefixes.** A permutation is alternating when adjacent numbers have different parity. The source constructs permutations left to right and refuses any choice that would put two odd values or two even values together.

`t` is the current prefix. `vis[j]` records whether number `j` from $1$ through $n$ is already used. The recursive parameter `i` is the next position, which also equals `len(t)`.

At each position, the loop considers `j` in increasing numeric order. A choice is legal when:

- `vis[j]` is false, preserving the permutation property;
- either this is the first position, or `t[-1] % 2 != j % 2`, preserving alternating parity.

When legal, the source appends `j`, marks it, recurses, then undoes both changes. This backtracking restoration allows the next candidate to reuse `j` in a different prefix while ensuring it appears only once within any one permutation.

**The base case saves an independent answer.** When `i >= n`, the prefix contains exactly $n$ distinct numbers from the range $1..n$, so it is a complete permutation. Every adjacent choice was parity-checked, making it alternating.

The source appends `t[:]` rather than `t`. This copy is essential: `t` is mutated during later backtracking. Storing the same list reference would make all result rows change together and eventually become empty.

**Lexicographic order emerges directly from traversal order.** The candidate loop always tries $1,2,\ldots,n$. Depth-first search fully emits every completion of a smaller prefix before moving to the next larger candidate at the first differing position. That is exactly lexicographic ordering. No final sort is required.

For $n=3$, starting with $1$ forces the next value to be the only even value $2$, then $3$, producing `[1,2,3]`. Starting with $2$ eventually runs out of even values after choosing an odd and cannot complete. Starting with $3$ produces `[3,2,1]`. They are emitted in the required order.

**Why pruning is both safe and complete.** If a prefix ends with parity $p$, every valid completion must choose the opposite parity next. Rejecting same-parity `j` cannot discard a valid permutation because it would violate the condition immediately. Rejecting visited values is required by the definition of permutation.

Conversely, take any alternating permutation. At depth zero, its first value is considered. At every later depth, its next value is unvisited and has opposite parity from the prefix end, so the DFS follows that branch. It eventually reaches the base case and outputs the permutation. Thus all and only valid answers are generated.

The parity counts explain why some prefixes become dead ends. For odd $n$, there is one more odd number than even number, so every full alternating permutation must begin and end odd. The code does not encode this as a special rule; a branch beginning even eventually finds no legal unused number and returns naturally.

For $n=1$, the loop chooses $1$, immediately reaches the base case, and returns `[[1]]`. There is no adjacent pair to violate.

**No duplicate outputs are possible.** Each root-to-leaf choice sequence is one ordered list of distinct numbers. Two different DFS branches differ at their first different chosen number and therefore produce different permutations. The visited array and deterministic positions ensure uniqueness without a result set.

## Complexity detail

Let $A$ be the number of alternating permutations returned, and let $P$ be the number of valid prefixes visited, including dead-end prefixes. Copying the $A$ outputs costs $O(An)$. At each non-leaf prefix, the source scans all $n$ candidate numbers, so exact search overhead is $O(nP)$.

A conservative factorial bound is $P=O(n!)$, giving $O(n\cdot n!)$ worst-case time. The manifest's output-sensitive $O(An)$ description captures result construction but suppresses rejected candidate checks and dead prefixes; the source-faithful bound is $O(nP+An)$. With $n\le10$, this backtracking search is intended to be feasible.

The recursion stack, current prefix, and visited array use $O(n)$ auxiliary space. The required output occupies $O(An)$ additional space; manifest space convention excludes returned results.

## Alternatives and edge cases

- **Generate all permutations then filter:** It explores every one of $n!$ leaves even when parity fails near the front. Immediate pruning avoids most invalid branches.
- **Choose from separate odd/even lists:** Alternating between parity pools can reduce candidate scans, but numeric merge order must be handled carefully to preserve lexicographic output.
- **Sort results afterward:** It is unnecessary because ascending candidate order already emits lexicographically.
- **Odd \(n\):** There is one extra odd number, so complete solutions start with odd. Even-start branches die naturally.
- **Even \(n\):** Odd and even counts match, so valid permutations may start with either parity.
- **\(n=1\):** The singleton permutation is valid because it has no adjacent elements.
- **Copy at completion:** Appending `t` without slicing would store a mutable shared object and corrupt all answers.
- **Visited restoration:** Failing to clear `vis[j]` after recursion would incorrectly ban that number from sibling branches.
- **Parity restoration:** Popping `t` restores the previous last value, so sibling legality checks use the correct prefix.
- **Complexity terminology:** Output size is substantial, but the exact nested candidate scans also visit prefixes that never become outputs; they should be included in a literal runtime analysis.
