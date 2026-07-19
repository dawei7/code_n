## General
**Encode inclusive intervals as boundary changes**

Create a difference array over the coordinate domain. For every inclusive interval `[start, end]`, add one at `start` and subtract one at `end + 1`. The subtraction occurs after the covered endpoint, which preserves inclusive semantics.

**Sweep the active coverage**

Take prefix sums from coordinate one through `right`. The running total equals the number of input intervals covering the current integer. Once the sweep reaches `left`, any total of zero proves that the target integer is uncovered and the answer is `false`. If the sweep reaches `right` without finding such a point, return `true`.

Each interval contributes precisely on its inclusive coordinate span: its addition is active starting at `start`, and its subtraction removes that contribution only after `end`. Therefore the prefix total is positive exactly at covered coordinates, making the target check exact.

## Complexity detail
Writing two boundary changes for each of the $N$ intervals takes $O(N)$ time. Sweeping through at most $V$ coordinates takes $O(V)$, for $O(N+V)$ total time. The difference array contains $O(V)$ entries. Under the stated bound $V\le50$, this storage is also a fixed small constant in absolute terms.

## Alternatives and edge cases
- **Nested coverage tests:** For every target integer, scan intervals until one covers it. This is straightforward but takes $O(NV)$ time in the worst case.
- **Boolean marking:** Mark every coordinate inside every interval, then inspect the target range; it is correct but can write $O(NV)$ positions.
- **Inclusive endpoint:** Place the negative difference at `end + 1`, not at `end`.
- **Single-point target:** That one integer still must be covered.
- **Adjacent intervals:** `[1,2]` and `[3,4]` jointly cover all integers from one through four without a gap.
- **Overlapping intervals:** Multiple coverage only raises the prefix count; it does not change the boolean result.
- **Irrelevant outside intervals:** Coverage entirely outside `[left, right]` cannot fill a gap inside it.
