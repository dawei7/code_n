## General

**View every result as a partition.** Let `prefix[i]` be the sum of the first
$i$ values. A final element ending at prefix boundary $i$ and starting after
boundary $j$ has sum `prefix[i] - prefix[j]`. For each boundary $j$, store
`groups[j]`, the greatest number of non-decreasing blocks achievable for that
prefix, and `last_sum[j]`, the smallest possible last block sum among those
maximum-length partitions.

A new block from $j$ through $i-1$ is valid exactly when

$$
\texttt{prefix[i]}-\texttt{prefix[j]}\ge\texttt{last\_sum[j]},
$$

or equivalently when the predecessor threshold
`prefix[j] + last_sum[j]` does not exceed `prefix[i]`. A valid predecessor
produces `groups[j] + 1` blocks and new last sum
`prefix[i] - prefix[j]`.

**Choose the rightmost feasible predecessor.** Positive input values make
prefix sums strictly increasing, and optimal group counts cannot decrease as
the processed prefix grows. Among feasible candidates, the latest boundary
therefore has the greatest available group count; when counts tie, its larger
prefix sum also yields the smallest new last block. This is precisely the
state needed for the current boundary.

**Keep only undominated thresholds.** Store candidate boundaries in a deque
whose thresholds increase from front to back. Before processing boundary
`i`, discard the front while the second candidate is already feasible; the
remaining front is the rightmost feasible candidate. After forming the new
state, remove back candidates with thresholds at least as large as the new
threshold. The new boundary has no fewer groups, a later prefix, and an
easier threshold, so each removed state can never be preferable later. Append
the new boundary. This maintains the invariant for the next prefix.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Every prefix boundary is appended once
and removed from the deque at most once, so the algorithm takes $O(N)$ time.
The prefix sums, dynamic-programming states, and deque use $O(N)$ auxiliary
space.

## Alternatives and edge cases

- **Try every previous boundary:** The direct dynamic program checks all $j<i$ and takes $O(N^2)$ time.
- **Binary-search threshold propagation:** Strictly increasing prefix sums support an $O(N\log N)$ solution, but the monotonic deque removes the logarithmic factor.
- **Greedily merge the first decrease:** A local repair can change the sum that constrains several later blocks and need not maximize the final length.
- **Already non-decreasing input:** Keeping every value as its own block achieves length $N$.
- **Single element:** Its only possible result has length one.
- **Positive values:** Positivity makes prefix sums strictly increasing and is essential to the candidate-order argument.
- **Equal block sums:** They are valid because the target order is non-decreasing, not strictly increasing.

