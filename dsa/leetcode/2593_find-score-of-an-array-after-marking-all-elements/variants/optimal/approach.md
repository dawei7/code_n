## General

The rules define a total priority order: smaller values come first, and equal values are ordered by smaller index. Build every `(value, index)` pair and sort the pairs lexicographically to obtain exactly that order before the marking process starts.

**Why one sorted pass reproduces every choice**

Maintain a Boolean marker for every original position. When a sorted pair is reached, skip it if that position was already marked by an earlier selection. Otherwise, all pairs before it are either already selected or unavailable. Every pair after it has a larger value, or the same value with a larger index. The current position is therefore precisely the smallest unmarked value with the required tie-breaking index, so adding it to the score matches the next mandated step.

After a selection, mark the current position and each in-range neighbor. Those are exactly the positions removed by the problem's operation. The same argument applies to the next unmarked pair, so induction shows that the sorted scan makes the identical sequence of selections as the stated process. Once the scan ends, every possible position has either been selected or marked by a neighbor, and the accumulated sum is the required score.

## Complexity detail

There are $n$ value-index pairs. Sorting them costs $O(n \log n)$ time, and the subsequent scan and constant-size marking work cost $O(n)$ time. The pairs and marker array use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Min-heap simulation:** Push all value-index pairs into a heap and repeatedly pop the next unmarked position. This also takes $O(n \log n)$ time and $O(n)$ space, but sorting is simpler and has lower overhead.
- **Repeated linear search:** Scanning the entire array to locate the next unmarked minimum is correct but can require $O(n^2)$ time.
- **Equal values:** Pair ordering automatically enforces the smaller-index rule; ignoring that rule can change which neighbors remain available and therefore change the score.
- **Already marked positions:** A pair stays in the sorted list even after a neighbor marks it, so the marker check must occur before adding its value.
- **Boundary positions:** Index `0` has no left neighbor and index `n - 1` has no right neighbor; only existing adjacent positions are marked.
- **Large score:** Up to roughly half of $10^5$ values as large as $10^6$ may contribute, so fixed-width implementations need a 64-bit accumulator.
