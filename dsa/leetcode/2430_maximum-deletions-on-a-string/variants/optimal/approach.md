## General

**Turn every remaining suffix into a state.** Let `best[start]` be the largest number of operations that can delete `s[start:]`. Deleting that entire suffix is always legal, so every state begins with value 1. If the first block of length `length` equals the block immediately after it, the first block may instead be removed and the process continues from `start + length`. That transition contributes `1 + best[start + length]`.

**Compare adjacent blocks without repeatedly slicing them.** For a fixed `start`, define `current_lcp[other]` as the length of the longest common prefix of `s[start:]` and `s[other:]`. When their first characters agree,

$$
\texttt{current\_lcp[other]}
= 1 + \texttt{next\_lcp[other + 1]},
$$

where `next_lcp` is the row previously computed for `start + 1`; otherwise the value is zero. Processing `start` from right to left therefore needs only the current and next rows.

A deletion of `length` characters is legal exactly when `length` fits twice in the remaining suffix and `current_lcp[start + length] >= length`. Checking those lengths and taking the largest transition constructs every legal first move. Because each transition uses an already completed later state, `best[start]` is optimal, and `best[0]` answers the original string.

## Complexity detail

There are $n$ suffix starts. Each row computes at most $n$ longest-common-prefix entries and examines at most half of its remaining offsets, so the total time is $O(n^2)$. The `best` array and two rolling longest-common-prefix rows each contain $O(n)$ values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Full longest-common-prefix table:** Storing every pairwise value supports the same transitions in $O(n^2)$ time but consumes $O(n^2)$ space.
- **Rolling hash:** Prefix hashes can compare blocks efficiently, but hash collisions require extra care or multiple moduli.
- **Direct substring comparisons:** The recurrence remains correct, but repeatedly creating and comparing length-$i$ slices can accumulate $O(n^3)$ character work.
- **No repeated adjacent prefix:** Deleting the entire current string is the only move, so the answer is 1.
- **All characters equal:** Repeatedly deleting one character achieves the maximum possible answer $n$.
- **Nonadjacent repeats:** A matching block farther right does not authorize deletion unless it begins immediately after the prefix.
- **Odd remaining length:** Candidate block lengths stop at the floor of half the suffix length.
