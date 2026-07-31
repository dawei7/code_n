## General

For each index `i`, maintain two best scores ending at `i`. `up[i]` ends with an upward comparison, and `down[i]` ends with a downward comparison. A singleton has no last direction, so its value initializes both states and may later precede either kind of first comparison.

To append `nums[i]` as an upward step, the previous value must be strictly smaller and its state must be `down`; symmetrically, a downward step needs a strictly larger previous value in state `up`. Only indices `j <= i - k` are eligible. Therefore

$$
\begin{aligned}
\texttt{up[i]} &= \texttt{nums[i]} + \max\left(0,\max_{j\le i-k,\ \texttt{nums[j]}<\texttt{nums[i]}}\texttt{down[j]}\right),\\
\texttt{down[i]} &= \texttt{nums[i]} + \max\left(0,\max_{j\le i-k,\ \texttt{nums[j]}>\texttt{nums[i]}}\texttt{up[j]}\right).
\end{aligned}
$$

Process indices from left to right and delay every state until it becomes eligible. Immediately before computing index `i`, insert exactly the states from index `i - k`; previously inserted states remain available, so the data structures represent precisely all indices at most `i - k`.

Coordinate-compress the values. One max-Fenwick tree stores `down` scores by increasing rank, allowing a prefix query over strictly smaller values. A second tree stores `up` scores by reversed rank, turning strictly larger values into another prefix query. Both queries exclude the current rank, which enforces strict inequalities even when duplicate values occur.

Each transition considers every legal predecessor summarized by the appropriate range maximum, and every represented predecessor already alternates correctly. Conversely, the final comparison of any valid multi-element subsequence is either upward or downward, so its preceding score appears in exactly the queried opposite-direction state. Taking the maximum of all states therefore yields the optimal valid score.

## Complexity detail

Coordinate compression takes $O(n\log n)$ time. Each index performs at most two Fenwick updates and two queries, each in $O(\log n)$ time, so the total remains $O(n\log n)$. The ranks, two DP arrays, and two Fenwick trees use $O(n)$ extra space.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Scan every eligible predecessor for both transition directions. This is direct and useful as an oracle, but takes $O(n^2)$ time when `k` is small.
- **Iterative segment trees:** Two range-maximum segment trees implement the same transitions in $O(n\log n)$ time and are a useful independent formulation, at the cost of larger constant factors.
- **Distance equal to `n`:** No two indices can meet the gap, so the answer is the largest singleton value.
- **Equal values:** Equal consecutive selections violate strict alternation; excluding the current compressed rank is essential.
- **First comparison:** Initializing both states with the singleton score permits either an upward or downward first edge without inventing a previous direction.
- **Positive values:** Extending a valid state increases its score, but an incompatible comparison or insufficient index gap must still be rejected.
- **Large score:** A valid subsequence can contain many values up to $10^5$, so fixed-width implementations need a 64-bit score.
