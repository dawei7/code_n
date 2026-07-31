## General

Let `prefix[t]` be the total damage in the first `t` rooms, with `prefix[0] = 0`. Consider a zero-based room `i` and a run beginning at room `j <= i`. After entering `i`, that run has

$$
\texttt{hp}-(\texttt{prefix[i+1]}-\texttt{prefix[j]})
$$

health. It earns the point precisely when this quantity is at least `requirement[i]`. Rearranging gives

$$
\texttt{prefix[j]}\geq
\texttt{prefix[i+1]}+\texttt{requirement[i]}-\texttt{hp}.
$$

Thus, rather than simulating every run, count how many possible start prefixes `prefix[0]` through `prefix[i]` meet this lower bound. Every damage value is positive, so the prefix sums are strictly increasing. A lower-bound binary search finds the first qualifying prefix, and the suffix length is the number of runs that score at room `i`.

Process rooms from left to right. Before handling room `i`, the stored prefix list contains exactly the possible start prefixes through `prefix[i]`. Add the binary-search count for that room, then append `prefix[i+1]`. Each counted pair corresponds to one starting run that earns at that room, and the algebra above proves that every such earned point is counted. Summing these per-room contributions therefore equals the requested sum of all run scores.

## Complexity detail

Let $N$ be the number of rooms. Each room performs one binary search over at most $N$ prefix sums, so the running time is $O(N\log N)$. The prefix array stores $N+1$ cumulative values and uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Simulate every starting room:** Following every suffix directly is faithful to the definition but visits $O(N^2)$ room/run pairs.
- **Fenwick tree over compressed prefixes:** It can count prefixes above each threshold in $O(\log N)$ time, but positivity already keeps the prefix array sorted, making ordinary binary search simpler.
- **Post-damage comparison:** The requirement is checked only after applying the current room's damage, not before it.
- **Equality earns a point:** Remaining health equal to `requirement[i]` satisfies the inclusive `at least` condition.
- **Non-positive health:** A run continues after health reaches zero or below; later rooms are still visited even if they cannot restore health.
- **No skipped rooms:** Each start selects a suffix, not an arbitrary subsequence of rooms.
- **Large total:** At most $N(N+1)/2$ points can be earned, which exceeds a signed 32-bit integer when $N=10^5$.
