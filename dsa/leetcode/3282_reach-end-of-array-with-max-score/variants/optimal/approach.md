## General

**Decompose jumps into crossed unit edges**

A jump from $i$ to $j$ crosses the unit edges $(i,i+1)$ through $(j-1,j)$. Its score $(j-i)\cdot\texttt{nums}[i]$ is exactly `nums[i]` contributed once for each crossed edge. Any complete path crosses every edge from `0` to `n - 1` exactly once, using the value at the most recent chosen departure index.

For the edge from $k$ to $k+1$, its departure index can be any visited index at or before $k$. No value after $k$ can contribute because it has not been reached. Thus this edge's contribution is at most the maximum of `nums[0..k]`.

That upper bound is attainable for every edge simultaneously. Whenever a new prefix maximum appears, jump to its index; otherwise keep the earlier maximum as the active departure across later edges. This constructs a valid increasing path whose rate on each edge equals the prefix maximum.

Scan `nums` except its final element, maintain the greatest value seen, and add it once per edge. The final element is never a departure point because the path ends there, so it does not affect the score.

## Complexity detail

The scan processes each of the first $n-1$ values once, using $O(n)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming over all jumps:** Computing the best score at every destination from every earlier index is correct but costs $O(n^2)$ time.
- **Always jump directly to the end:** This is optimal only when `nums[0]` remains the prefix maximum.
- **Jump at every index:** Extra jumps do not help when the new departure value is no larger than the active prefix maximum.
- A one-element array has no crossed edges and returns `0`.
- A strictly decreasing array uses the first value for every edge.
- A strictly increasing array benefits from visiting every new maximum.
- Equal prefix maxima are interchangeable and leave the total unchanged.
- The last array value never contributes, even when it is the largest.
- The maximum total can exceed 32-bit range, so fixed-width languages need a wide integer type.
