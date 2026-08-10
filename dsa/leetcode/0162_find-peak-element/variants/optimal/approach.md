## General

**A peak is guaranteed even without global sorting**

The array can rise and fall many times, so ordinary binary search for a known
value does not apply. The useful structure is local: adjacent elements are
never equal, and positions outside the array are treated as negative infinity.

Imagine standing between `nums[mid]` and `nums[mid + 1]`. Their comparison
tells which direction has an uphill step. Following an uphill direction must
eventually reach a peak. The path cannot rise forever past an array boundary,
because the imaginary outside value is smaller than the boundary element.

The method does not need to identify a unique peak. The contract accepts any
index whose value is greater than both neighbors, so it can safely discard a
region while retaining proof that some peak exists in the other region.

**Maintain an inclusive interval containing a peak**

`left` and `right` are valid inclusive indices. Initially they cover the whole
nonempty array, which contains at least one peak.

While `left < right`, the source computes the floor midpoint
`mid = (left + right) >> 1`. Because `mid` is strictly below `right` whenever
the interval has at least two indices, `mid + 1` is always valid. No explicit
boundary check is needed for that neighbor access.

The invariant is not that a particular known peak stays inside. It is that the
current interval is guaranteed to contain at least one peak of the complete
array.

**Choose a side from the local slope**

If `nums[mid] > nums[mid + 1]`, the step from `mid` to the right goes downward.
There is a peak somewhere from `left` through `mid`.

Why include `mid`? It might itself be a peak. If its left neighbor is smaller,
then it is greater on both sides. If its left neighbor is larger, moving left
follows an uphill direction; continuing that process must reach a peak before
leaving the interval. Therefore the source sets `right = mid`.

If `nums[mid] < nums[mid + 1]`, the step goes upward to the right. `mid`
cannot be a peak because its right neighbor is larger. Starting at
`mid + 1` and continuing along any necessary rises must reach a peak no later
than the array's right boundary. The source sets `left = mid + 1`.

Adjacent inequality makes these two cases exhaustive. An equal plateau would
need additional reasoning because it would not reveal an uphill direction.

**Trace a single-peak array**

For `[1,2,3,1]`, begin with `[0,3]`. The midpoint is one, and
`nums[1] < nums[2]`, so a peak is guaranteed in `[2,3]`. The new midpoint is
two. Since three is greater than the next value one, the algorithm keeps
`[2,2]` and returns index two.

At no point does it compare the midpoint with both neighbors. The slope
argument supplies the missing side: if the right side falls, either `mid` is a
peak or an uphill path to its left reaches one.

**Trace multiple peaks and a valley**

For `[1,2,1,3,5,6,4]`, different valid executions may preserve the peak at
index one or the peak at index five. The selected midpoint sequence follows
local slopes and returns one valid answer; it is not required to return the
largest peak or the leftmost peak.

For `[4,3,2,1,5]`, the early comparisons can move left across a falling region
or right across the final rising edge. Although the array contains a valley,
the rule never promises to find a valley. A downward step keeps a region with a
peak to the left, and an upward step keeps a region with a peak to the right.
One of the boundary values is ultimately selected as a peak relative to
negative infinity.

Strictly increasing input converges to the final index. Strictly decreasing
input converges to index zero. Both boundary answers satisfy the imaginary
neighbor definition.

**Why convergence proves the answer**

Each update retains an interval known to contain a peak. It also strictly
reduces the interval:

- `right = mid` lowers the right boundary because `mid < right`;
- `left = mid + 1` raises the left boundary beyond `mid`.

Eventually `left == right`. A one-index interval that is guaranteed to contain
a peak can contain it only at that index, so returning `left` is correct.

The source never modifies `nums`, and all comparisons concern the given
ordering rather than numeric magnitudes or signs.

**Exact-source typing dependency**

The method annotates `nums` as `List[int]` without importing `List`. The native
harness may supply typing context, but a standalone module needs
`from typing import List`. This dependency does not change the algorithm.

## Complexity detail

Let $n$ be the array length. Every iteration reduces the inclusive candidate
interval to at most roughly half its previous size. The loop therefore executes
$O(\log n)$ times, doing constant work per iteration. Time is $O(\log n)$.

Only `left`, `right`, and `mid` are stored. The method is iterative and
allocates no input-sized structure, so auxiliary space is $O(1)$. These bounds
match the manifest.

## Alternatives and edge cases

- **Linear scan:** Return the first index followed by a smaller value, or the final index. It is simple and correct but takes $O(n)$ time.
- **Recursive slope search:** Uses the same halving decisions but adds $O(\log n)$ call-stack space.
- **Check both neighbors at every midpoint:** Finding that one midpoint is not a peak does not by itself choose a safe side; the slope comparison is the key directional evidence.
- **One element:** The loop skips, and index zero is a peak relative to both imaginary neighbors.
- **Strictly increasing:** Every decision moves right, returning the last index.
- **Strictly decreasing:** Every decision keeps the left half, returning index zero.
- **Multiple peaks:** Any one is acceptable; the algorithm does not promise a particular index.
- **Negative values:** The imaginary boundary is negative infinity, still smaller than every real integer.
- **Adjacent equality outside the contract:** A flat midpoint comparison would not select a direction under this two-case source.
- **Safe neighbor access:** `mid + 1` is valid because the loop only computes it while `left < right`.
