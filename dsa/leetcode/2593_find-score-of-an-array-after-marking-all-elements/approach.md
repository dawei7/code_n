## General

**The priority rule is exactly a min-heap order**

At every step, the algorithm must choose the smallest value among unmarked positions and break value ties by the smallest index. Python tuple ordering on `(value,index)` does precisely that.

The code creates one pair for every original occurrence and calls `heapify`. Original indices remain attached even though heap order differs from array order, allowing adjacent positions to be marked correctly.

**Track marked positions separately**

`vis[i]` records whether index $i$ has been marked by a previous choice or as a neighbor. Heap entries are not immediately removed when their positions become marked. Instead, they remain as stale entries until they rise to the heap root.

This lazy deletion avoids searching the heap for arbitrary neighbors, an operation a binary heap does not support efficiently.

**The heap root is unmarked at each choice**

At the end of every outer iteration, the inner loop repeatedly pops while `vis[q[0][1]]` is true. Therefore, if the heap remains nonempty, its root is the smallest pair whose position is not marked.

The next outer `heappop` consequently returns exactly the value and smallest-index tie required by the problem. The code can add `x` unconditionally because the cleanup invariant guarantees this popped position is live.

Marked entries deeper in the heap do not matter. A deeper entry cannot be chosen before all smaller tuple entries above it are removed. When a marked entry eventually becomes the root, cleanup discards it before the next score choice.

**Mark the chosen index and its neighbors**

After adding `x` to `ans`, the code sets `vis[i] = True`. It then examines `i - 1` and `i + 1`, marking each if it lies inside the array.

No heap structure changes are needed at that moment. Their tuple entries will be lazily removed later.

Boundary checks ensure index zero has only its right neighbor and index $n-1$ has only its left neighbor.

**Why the simulation is exact**

Assume before an outer iteration that `vis` matches the positions marked by the statement's process and the heap root is the smallest unmarked value-index pair.

Popping the root makes the same deterministic choice as the statement. Adding its value produces the same score increment. Marking itself and valid neighbors produces the same new marked set. Cleanup removes only entries that can no longer be chosen and leaves all unmarked entries in the heap.

If entries remain, tuple heap order makes the new root the next required choice. This preserves the invariant by induction until every entry is removed.

Because the problem's selection rules are deterministic, exact step-by-step simulation proves the returned score.

**Trace the first sample**

For `[2,1,3,4,5,2]`, the smallest heap pair is $(1,1)$. The algorithm adds one and marks indices zero, one, and two.

Among remaining unmarked positions, pair $(2,5)$ is smallest. It adds two and marks indices four and five.

Index three with value four is the only unmarked position left. It adds four. Total score is $1+2+4=7$.

Entries for marked values such as index zero may still have been in the heap, but the cleanup loop removes them whenever they become the root.

**Tie-breaking through tuple ordering**

If two values are equal, Python compares their second tuple components. The smaller index comes out first.

This matters because choosing equal-valued occurrences at different positions can mark different neighbors and change later score. A heap of values alone would lose required information and could simulate the wrong process.

**Why every entry is popped at most once**

An entry leaves the heap either as a scored selection in the outer pop or as a stale marked entry in cleanup. It is never reinserted. Although cleanup is nested inside the outer loop, its total iterations across the whole algorithm are only $O(n)$.

## Complexity detail

Let $n$ be the array length. Building the list takes $O(n)$ time and `heapify` takes $O(n)$. Every one of the $n$ entries is popped exactly once, and each pop costs $O(\log n)$. Total time is $O(n\log n)$.

The heap list and `vis` array each use $O(n)$ space. The input `nums` is read but not modified.

## Alternatives and edge cases

- **Sort value-index pairs once:** Process sorted pairs and skip marked indices. This also takes $O(n\log n)$ time and often has simpler control flow.
- **Linear specialized scan:** Monotone-run reasoning can reproduce the deterministic selections in $O(n)$ time, but it is considerably less direct.
- **Search the array every round:** Repeatedly finding the smallest unmarked value costs $O(n^2)$ in the worst case.
- **Equal values:** Tuple index ordering implements the mandatory smallest-index tie-break.
- **One element:** It is selected, its value is the score, and neighbor checks do nothing.
- **Boundary selection:** Only existing adjacent indices are marked.
- **Marked heap entries:** They are harmless until reaching the root, where lazy cleanup removes them.
- **Positive values:** The score only increases, though heap correctness does not depend on positivity.
- **Input preservation:** All marking state is stored separately in `vis`.
