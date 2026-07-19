## General
**Compress two support totals into their difference.** Maintain a map from a nonnegative height difference to the greatest possible shorter-support height for that difference. The initial state is difference zero with shorter height zero.

**Consider all three choices for each rod.** Copy the current states so leaving the rod unused remains possible. For a state with difference `difference` and shorter height `shorter`, adding the rod to the taller support produces difference `difference + rod` without changing `shorter`. Adding it to the shorter support produces `abs(difference - rod)`; the new shorter height increases by `min(difference, rod)`, because that much of the rod first closes the gap before any excess makes this side taller.

**Keep only the dominant state for each difference.** If two assignments have the same difference, the one with the greater shorter support is always at least as useful: future rods see the same imbalance and can only preserve or increase both resulting heights from the larger baseline. Discarding the smaller state therefore cannot remove an optimum.

After every rod has been considered, difference zero represents equal supports, and its stored shorter height is their common height. Since every rod transition includes unused, left-support, and right-support choices, the DP covers every valid disjoint assignment and returns the tallest one.

## Complexity detail
Every reachable difference lies from 0 through $S$, so each of $N$ rods updates at most $S+1$ states. This gives $O(NS)$ time. The current and copied difference maps contain $O(S)$ entries and use $O(S)$ space.

## Alternatives and edge cases
- **Track both support totals:** Store every reachable pair `(left, right)` and transition each rod among unused, left, and right choices. This is correct but can require $O(S^2)$ states and $O(NS^2)$ time.
- **Meet in the middle:** Enumerate three choices per rod in each half and combine compatible differences. This can work for $N \le 20$ but is more intricate and still exponential in half the rod count.
- **Use every rod:** Requiring all rods to participate is incorrect; an optimal equal construction may leave rods unused.
- **One rod:** It cannot form two positive supports, so the answer is zero.
- **Duplicate lengths:** Rods are separate physical items even when their lengths match.
- **Zero difference:** The stored value, not the total assigned length, is the height of either support.
