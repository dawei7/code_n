## General
**Use strict descent as a dependency order**

Let `best[i]` be the maximum number of positions visitable when starting at `i`, including `i`. Every legal next index has a strictly smaller value, so `best[i]` depends only on states at lower heights. Sort all indices by `arr[i]` ascending and evaluate them in that order. Equal-valued indices may appear in either order because no jump is permitted between them.

For each index, scan outward separately to the left and right for at most `d` positions. Stop a directional scan as soon as it leaves the array or reaches a value greater than or equal to the starting value. Every lower position encountered before that barrier is a legal destination, so use its already-computed state to update `best[i]` with `1 + best[j]`.

The scan enumerates exactly the legal outgoing jumps: it includes every lower destination within range until the first blocking value, and excludes that blocker and everything behind it. Because lower destinations were processed earlier, each transition extends an already-optimal suffix. Induction through ascending values establishes every state, and the largest state permits the best arbitrary start.

## Complexity detail
Sorting $n$ indices takes $O(n\log n)$ time. Each index examines at most $d$ positions in each direction, taking $O(nd)$ additional time. The index order and dynamic-programming array use $O(n)$ space.

## Alternatives and edge cases
- **Memoized depth-first search:** The same strict-descent graph supports cached recursion in $O(nd)$ time, but a legal long chain can approach or exceed Python's recursion depth.
- **Repeated relaxation:** Updating every jump across $n$ full passes eventually finds all path lengths but takes $O(n^2d)$ time.
- **Single position:** The starting index alone gives an answer of 1.
- **Equal values:** They cannot be destinations and block all positions farther in that direction.
- **Lower intermediate values:** They do not block a longer jump and remain possible destinations themselves.
- **Higher or equal barrier:** No position beyond it is reachable directly from the current index.
- **Arbitrary start:** Return the maximum state, not only the state for index 0.
- **Direction changes:** A sequence may alternate left and right as long as each individual jump satisfies the rules.
