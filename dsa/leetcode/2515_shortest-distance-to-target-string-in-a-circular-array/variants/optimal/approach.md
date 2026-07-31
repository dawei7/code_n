## General

**Two simple arcs connect any pair of positions**

For a target occurrence at index `i`, let `direct_distance = abs(i - startIndex)`. Moving along the ordinary index interval uses that many steps. The other route goes around the circular boundary and has length `n - direct_distance`. Any route that changes direction repeats an edge and cannot be shorter than one of these two simple arcs, so the shortest distance to `i` is their minimum.

**Evaluate every occurrence in one scan**

Scan all array positions. Whenever the word equals `target`, compute the two arc lengths and update the smallest distance found. This considers every legal destination and assigns each its true shortest circular distance, so the final minimum is the shortest distance to any occurrence. If no position matches, the unchanged sentinel yields `-1`.

## Complexity detail

Let $n=\lvert\texttt{words}\rvert$. The scan examines every word once and performs constant work for a match, taking $O(n)$ time. It stores only the array length, one distance, and the current best value, requiring $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Expand in both directions:** Checking positions at distance `0, 1, 2, ...` can stop at the first match and is also $O(n)$ time, but the index-distance formula is easier to verify for every occurrence.
- **Store all matching indices:** Collecting matches before computing distances remains $O(n)$ time but uses unnecessary $O(n)$ space.
- **Simulate paths to every match:** Walking clockwise and counterclockwise separately for each destination is correct but can take $O(n^2)$ time when many positions match.
- **Starting position matches:** The answer is `0`; the direct distance formula handles it immediately.
- **Target absent:** No candidate updates the sentinel, so return `-1`.
- **One-word array:** A matching word has distance `0`; a nonmatching word is absent.
- **Opposite index in an even array:** Both arcs have length $n/2$, and either yields the same answer.
