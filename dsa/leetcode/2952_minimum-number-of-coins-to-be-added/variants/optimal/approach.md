## General

**Track one continuous coverage interval.** Sort the existing coin values and
maintain `reachable` so that every value from $1$ through `reachable` can be
formed from the coins processed so far. Initially `reachable = 0`, representing
an empty positive interval. If the next coin has value `coin <= reachable + 1`,
then combining it with every sum from $0$ through `reachable` creates the
adjacent interval from `coin` through `coin + reachable`. There is no gap, so
coverage extends through `reachable + coin`.

**Patch the first missing value.** If the next existing coin is greater than
`reachable + 1`, no processed coin can form the first missing value
`reachable + 1`. Any added coin larger than that value also leaves the gap, so
every valid completion must add a coin no larger than `reachable + 1`.
Choosing exactly `reachable + 1` is best: it bridges the gap and maximizes the
new covered endpoint at `2 * reachable + 1`. This forced, maximally extending
choice proves each patch is greedy-optimal.

Continue consuming usable existing coins or adding the forced patch until
`reachable >= target`. At that point the invariant directly guarantees every
required value is obtainable, while the forced-choice argument shows no
solution can use fewer added coins.

## Complexity detail

Let $N=\lvert\texttt{coins}\rvert$. Sorting takes $O(N\log N)$ time. Each
existing coin is consumed once, and every added coin at least doubles the
covered range plus one, so the scan and patches take $O(N+\log\texttt{target})$
time. Since `target` is bounded by the problem constraints, sorting dominates
the stated $O(N\log N)$ bound. The sorted copy uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Subset-sum dynamic programming:** Explicitly marking every obtainable value can take $O(N\cdot\texttt{target})$ time and does not exploit continuous coverage.
- **Quadratic selection sorting:** It preserves the same greedy decisions but raises sorting time to $O(N^2)$.
- **Coin exactly reachable plus one:** It closes the next gap and should be consumed rather than replaced by an added coin.
- **Duplicate coins:** Each occurrence is a distinct selectable array element and can extend coverage separately.
- **Unsorted input:** Coin order does not affect which subsequences sums exist, so sorting is valid.
- **Coins above target:** They may remain unused once coverage reaches `target` and cannot repair an earlier missing value.
- **Target equals one:** The answer is zero if coin `1` exists and one otherwise.
