## General

Each array index has exactly three legal roles: it is skipped, appended to the first subsequence, or appended to the second subsequence. This three-way assignment automatically enforces disjointness. The relative order within either subsequence is already fixed by processing `nums` from left to right, and only the GCD of the values assigned to each side matters for future choices.

Let `dp[g1][g2]` count assignments of the processed prefix whose first subsequence has GCD `g1` and whose second has GCD `g2`. Use GCD zero as an internal marker for an empty subsequence; this is safe because every input value is positive. Initially only `dp[0][0] = 1` is possible.

For the next value `x`, copy the table to represent skipping its index. Every old state also produces two more states:

- assigning `x` to the first side changes `g1` to `gcd(g1, x)` and leaves `g2` unchanged;
- assigning `x` to the second side leaves `g1` unchanged and changes `g2` to `gcd(g2, x)`.

The identity $\gcd(0,x)=x$ starts an empty side correctly. A fresh table is required so one index cannot be assigned twice through an update made during the same iteration. All counts are reduced modulo $10^9+7$.

After every processed prefix, the table contains exactly one contribution for every legal three-way assignment, classified by its two resulting GCDs. The three transitions are exhaustive and mutually exclusive, so this statement remains true after the next index. At the end, states `dp[g][g]` with $g>0$ are precisely the assignments forming two non-empty subsequences with equal GCD. Summing those diagonal states gives the requested ordered-pair count.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. Both GCD coordinates range from $0$ through $V$. Scanning the $(V+1)^2$ table for every element takes $O(nV^2)$ time. The current and next tables each contain $O(V^2)$ entries, so the auxiliary space is $O(V^2)$.

## Alternatives and edge cases

- **Enumerate all subsequence assignments:** Trying the three roles for every index takes $O(3^n)$ time, which is infeasible for $n=200$.
- **Store the subsequences themselves:** Their values and order contain far more information than future decisions need; the pair of current GCDs is a sufficient state.
- **One in-place table:** Reading counts written for the current value can assign that same index repeatedly or to both sides, violating disjointness.
- **Empty subsequences:** States with a zero coordinate are useful during construction but must not contribute to the answer; only positive diagonal GCDs are summed.
- **Ordered pairs:** Assigning one index set to the first side and another to the second differs from swapping those assignments.
- **Repeated values:** Equal values at different indices are still separate choices, while a single index can belong to at most one side.
- **Single input value:** It cannot populate both non-empty sides, so the result is zero.
