## General

**Count multiplicities, not source indices.** A sub-multiset is determined by how many copies of each distinct value it contains. Compress `nums` into a frequency map. Let `dp[s]` be the number of multiplicity selections from the value types processed so far whose sum is exactly $s$.

Zeros require separate care. If zero occurs $z$ times, a sub-multiset can contain any of $0,1,\ldots,z$ copies, giving exactly $z+1$ choices without changing its sum. Initialize `dp[0] = z + 1`; subsequent positive-value transitions propagate that factor to every reachable sum.

**Turn the bounded transition into a sliding window.** Suppose positive value $v$ occurs $c$ times. The new count for sum $s$ is

$$
\textit{next}[s]=\sum_{k=0}^{c}\textit{dp}[s-kv],
$$

where terms with negative indices are omitted. Sums with different residues modulo $v$ are independent. Moving from $s-v$ to $s$ adds `dp[s]` to the previous window and removes `dp[s-(c+1)v]` once that oldest term exists. Therefore

$$
\textit{next}[s]
=\textit{dp}[s]+\textit{next}[s-v]-\textit{dp}[s-(c+1)v].
$$

Start `next` as a copy of `dp` to cover sums below $v$, then scan upward so `next[s-v]` is already available. Apply every addition and subtraction modulo $10^9+7$.

The invariant is that after each distinct value, `dp[s]` counts every legal choice of processed multiplicities summing to $s$ exactly once. The displayed transition partitions those choices by the number of new copies, so it preserves the invariant. After all values are processed, summing `dp[l]` through `dp[r]` counts exactly the requested sub-multisets.

## Complexity detail

Building the frequency map costs $O(n)$ time. Each of the $D$ distinct positive values scans at most `r + 1` states, for total time $O(n+Dr)$. Two arrays of length `r + 1` are retained at a time, so the auxiliary space is $O(r)$.

## Alternatives and edge cases

- **Loop over every allowed copy count:** The direct bounded-knapsack formula is correct but can take $O(nr)$ time when one value has many copies.
- **Treat equal elements as distinct:** Ordinary 0/1 subset DP over source indices overcounts, because selecting either occurrence of the same value can describe the same sub-multiset.
- **Binary-split multiplicities:** Power-of-two bundles reduce repeated copies but still represent identical multiplicity totals through multiple bundle choices unless implemented with great care.
- **Zero values:** There are $z+1$ zero multiplicities, not $2^z$ subsets of distinguishable zero positions.
- **Range includes zero:** The empty multiset and every allowed zero-only multiplicity must be counted.
- **Values above `r`:** Positive copies of such a value cannot contribute to a tracked sum, but choosing zero copies remains represented by the copied DP state.
- **Modulo subtraction:** Normalize after removing the expired window term so counts remain in the required residue class.
