## General

Removing every eligible index would perform $k=\lvert\texttt{targetIndices}\rvert$ operations. Some eligible characters may have to remain because they participate in the chosen occurrence of `pattern`. Therefore maximizing removals is equivalent to finding a subsequence embedding of `pattern` that uses as few eligible source positions as possible. If that minimum is $c$, the answer is $k-c$.

Mark the eligible source positions in a Boolean array. Let `minimum_kept[j]` be the minimum number of eligible positions used by any embedding of the first $j$ pattern characters within the source prefix processed so far. Initially, matching the empty prefix costs zero and every nonempty prefix is unreachable.

When processing `source[i]`, it may be skipped without changing any state. If it equals `pattern[j]`, it may extend an embedding of length $j$ at additional cost one when index $i$ is removable, or zero otherwise. Update pattern lengths from right to left. That direction prevents the same source character from extending multiple positions during one iteration, preserving the subsequence rule.

Every possible embedding is formed by a sequence of these extensions, and each transition adds exactly the number of eligible positions it commits to keeping. Taking the minimum at every state therefore yields the smallest eligible-character cost for the complete pattern. The contract guarantees the pattern is initially a subsequence, so the final state is reachable.

## Complexity detail

Let $n=\lvert\texttt{source}\rvert$ and $m=\lvert\texttt{pattern}\rvert$. For each source character, the algorithm scans all $m$ pattern positions, taking $O(nm)$ time. The removable-position flags use $O(n)$ space and the rolling dynamic-programming array uses $O(m)$ space, for $O(n+m)$ total auxiliary space.

## Alternatives and edge cases

- **Two-dimensional dynamic programming:** Storing a state for every source prefix and pattern prefix has the same $O(nm)$ time but consumes $O(nm)$ space, which is unnecessarily large at length 3000.
- **Greedily keep the earliest match:** The earliest available pattern character can occupy a removable position even when a later non-removable occurrence would allow more deletions.
- **Try removal subsets:** There are $2^k$ subsets of eligible indices, so explicit choice enumeration is infeasible.
- **Pattern equals source:** Every source position is required by the only length-$n$ embedding, so no eligible character can be removed.
- **Eligible characters outside every embedding:** Such positions never add to the minimum kept cost and are all counted as successful removals.
- **Fixed original indices:** Marking removability by the original index matches the contract because removing a character does not renumber the remaining positions.
