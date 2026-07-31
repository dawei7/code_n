## General

**Order values to expose contiguous ranges**

Sort all occurrences. Begin a group at the smallest value not yet assigned.
Every following value no more than `k` above that group minimum can join the
same group. Once a value exceeds the limit, start the next group at that value
and continue.

**Why taking the full feasible prefix is optimal**

Let $x$ be the smallest uncovered value. Any valid partition must place $x$ in
some group whose maximum is at most $x+k$. Consequently, no value greater than
$x+k$ can share that group. The greedy choice includes every currently
uncovered occurrence within this unavoidable boundary, so it covers at least
as much as the group containing $x$ in any alternative solution.

Replacing that alternative first group by the greedy range cannot increase
the number of groups needed for the remaining larger values. Repeating the
exchange at each new smallest uncovered value proves that the greedy count is
minimal. Finally, values assigned to one range can always be read at their
original indices to form a valid subsequence.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Sorting takes $O(n \log n)$ time, and
the greedy scan takes $O(n)$ additional time. Copying and sorting the values
uses $O(n)$ auxiliary space in the app-friendly implementation.

## Alternatives and edge cases

- **Repeated minimum selection:** Extracting the next smallest value by rescanning all remaining values produces the same greedy groups but can take $O(n^2)$ time.
- **Frequency sweep:** Since values are bounded by $10^5$, a counting array can solve the problem in $O(n+U)$ time and $O(U)$ space for value range $U$.
- **Original-order greedy:** Grouping adjacent input positions can be suboptimal because distinct subsequences may interleave.
- **Zero `k`:** Each distinct value needs its own group, while duplicate occurrences may stay together.
- **Large `k`:** If the global maximum minus minimum is at most `k`, one subsequence suffices.
- **Duplicates:** Equal occurrences never enlarge a group's range.
- **Boundary equality:** A value exactly `k` above the group minimum still belongs to that group.
- **Subsequence order:** After value-based assignment, retaining original index order within every group satisfies the subsequence definition.
