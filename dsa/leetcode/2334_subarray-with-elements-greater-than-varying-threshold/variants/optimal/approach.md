## General

**Activate indices from high values to low values**

For a candidate minimum value `v`, consider all indices whose numbers are at least `v`. Consecutive active indices form subarrays in which every element is at least `v`.

The exact solution sorts pairs `(nums[i], i)` in descending order. As it processes an index, all previously active positions have values greater than or equal to the current `v`. It connects the current index to active immediate neighbors, forming maximal contiguous active components.

Each component is represented by union-find, with `size[root]` storing its length.

**Union only adjacent active positions**

Initially every index is its own set of size one, and `vis` marks no index active. When processing `i`, the method merges it with `i - 1` if that neighbor is active and with `i + 1` if active.

No nonadjacent positions are merged because a valid answer must be a contiguous subarray. After these unions, the set containing `i` represents a contiguous block whose processed values are all at least `v`.

The current index is marked visited after the validity check. It can still participate in unions before that mark because its singleton parent and size were initialized in advance. Once the iteration continues, later neighbors see it as active.

Path compression in `find` shortens representative chains. `merge` attaches one root under another and adds sizes, preserving the component length.

**Test the entire current component**

Let `k = size[find(i)]`. Every element in this active component is at least the current value `v`. The required condition is

`every element > threshold / k`.

It is sufficient to test the minimum lower bound `v`. For positive integers, the code's condition

`v > threshold // k`

is equivalent to `v \cdot k > threshold`, and hence to `v > threshold / k`. Using integer division avoids floating-point precision.

If the test succeeds, the whole active component is a valid subarray of length `k`, so the method may return that size immediately. The problem accepts any valid length.

**Why processing equal values incrementally is safe**

The descending sort also orders equal-value pairs by descending index because tuples are reversed as a whole. During the first equal-valued index, not all positions with that value are active yet, so its component may be smaller than the final threshold component.

This cannot create a false positive: every currently joined element still has value at least `v`. It also cannot lose a solution. As additional equal-valued indices are processed, they merge with active neighbors, and the relevant component grows. The last necessary equal-valued activation will expose the full block.

**Why every valid subarray will be discovered**

Suppose some subarray of length `q` is valid, and let `v` be its minimum element. Every element in it is at least `v`. By the time all positions of value `v` in that subarray have been processed, its indices belong to one active component of length `k >= q`.

Validity gives `v > threshold / q`. Since `k >= q`, `threshold / k <= threshold / q`, so `v > threshold / k` as well. When the component reaches that size during activation, the check succeeds and returns a valid component length.

Therefore returning `-1` after all activations means no valid subarray exists.

**The exact source is union-find, not a monotonic stack**

The manifest summary describes the alternative linear-time monotonic-stack solution. The provided Optimal source instead sorts indices and uses disjoint sets. Its correctness comes from descending activation and contiguous component sizes, and its literal time includes sorting.

## Complexity detail

Let `n` be the array length. Sorting `n` value-index pairs costs `O(n \log n)` time. Each index performs at most two unions and a constant number of finds. With path compression but no rank or size-based attachment, a conservative bound remains within `O(n \log n)` here, and sorting already dominates.

The parent, size, active-marker, and sorted-pair arrays each use `O(n)` space. The recursive `find` can use stack space proportional to a parent chain before compression; arbitrary attachment can create longer chains than ranked union.

The input `nums` is not modified. Products are avoided in the exact check, though Python integers would safely hold them.

## Alternatives and edge cases

- **Monotonic stack:** Find each value's widest interval where it is the minimum, then test `value * width > threshold`. This achieves `O(n)` time and `O(n)` space and matches the manifest summary.
- **For every length, use a sliding minimum:** Repeating a window-minimum computation for all lengths costs quadratic time.
- **Binary search the answer length:** Validity is not simply monotone by length for arbitrary arrays, so ordinary binary search on `k` is unsafe.
- **Merge nonadjacent active indices:** That would create a set that is not a subarray. Only immediate active neighbors may join.
- **Use `>= threshold // k`:** The source condition is strictly greater. Equality may fail the original strict inequality and must not be accepted.
- **Floating-point division:** Comparing `v * k > threshold` or the exact integer-division form avoids precision issues for values up to `10^9`.
- **One valid element:** A component of size one succeeds exactly when its value is greater than `threshold`.
- **All values equal:** Components grow as equal indices activate. A sufficiently long block may become valid even if a singleton is not.
- **Several valid lengths:** The method returns the first size discovered in descending activation order; any is permitted.
- **Whole array valid:** Eventually all indices join, and the final component test detects it.
- **No valid subarray:** Every activation test fails and the method returns `-1`.
- **Current `vis` timing:** The current node is merged before being marked active, but initialized DSU state makes that valid; the mark is needed only for later iterations.
- **Tie ordering:** Reverse tuple sorting affects when equal indices activate but not correctness.
- **Input preservation:** Sorting creates a separate pair list and leaves `nums` unchanged.
