## General

**Sort to expose the cheapest legal final value**

Each move increases one value by exactly one; no value may decrease. After sorting `nums`, process values from smallest to largest and assign each element the smallest final value that is both at least its original value and strictly greater than the preceding assigned value.

This produces unique final values while never spending an increment earlier than necessary.

Variable `y` stores the final value assigned to the previously processed element. It starts at `-1` because inputs are nonnegative. This lets the first zero, if present, remain zero.

**Deriving the formula**

Suppose current original value is `x`.

Because decrementing is forbidden, its final value must be at least `x`. Because processed final values are strictly increasing and `y` is their largest value, the new final value must also be at least `y + 1`.

The smallest integer satisfying both requirements is `max(y + 1, x)`. The code assigns this to `y` and adds `y - x` to `ans`.

If `x > y`, there is no collision and `x` remains unchanged. If `x <= y`, it moves just beyond `y`.

**Why sorting is legitimate**

The problem asks only for the minimum move count, not which original index receives which final value. Equal or reordered elements are interchangeable for this cost calculation.

Sorting lets final assignments be treated in increasing order. Any feasible unique destinations can be matched to sorted originals in sorted order without increasing total increment cost. Crossing two assignments would send a smaller original farther while assigning a smaller destination to a larger original, which cannot help under increment-only moves.

Thus the ordered problem has the same optimum as the original one.

**Why the greedy choice is optimal**

Assume earlier elements have been assigned optimally and their last value is `y`. Every feasible solution for current `x` must choose at least `max(y + 1, x)`. This is a lower bound imposed by uniqueness and the ban on decrements.

The algorithm chooses exactly that lower bound. Choosing anything larger spends extra moves now and raises the minimum destination for later elements. It cannot create a later saving because future values also move only upward.

By induction, after every prefix the assigned values are unique, the accumulated cost is minimum, and `y` is the smallest possible final maximum. The complete total is globally minimum.

**Trace with interacting duplicates**

For `[3, 2, 1, 2, 1, 7]`, sorting gives `[1, 1, 2, 2, 3, 7]`.

- First `1` stays at one for cost zero.
- Second `1` becomes two for cost one.
- First original `2` becomes three for cost one.
- Second original `2` becomes four for cost two.
- Original `3` becomes five for cost two.
- `7` is already above five and stays seven for cost zero.

The total is six. Duplicates can push later values that were initially different, so moving only duplicate copies while freezing all other values would be wrong.

For `[1, 2, 2]`, assignments are `1, 2, 3` and the cost is one.

**Why gaps are handled correctly**

If `y = 4` and the next original is ten, the formula chooses ten, not five. Filling unused values five through nine would require decreasing ten, which is illegal. The formula respects both existing gaps and the one-way operation.

## Complexity detail

Let `n` be the number of values.

Python's in-place sort takes `O(n log n)` time in the worst case, and the greedy scan takes `O(n)`. The exact implementation therefore uses `O(n log n)` time.

The scan itself uses `O(1)` state. Python's sorting implementation may use `O(n)` temporary memory in the worst case, and it mutates the input order.

The current manifest lists `O(n + M)` time and `O(M)` space. Those are bounds for the editorial's counting approach, not this checked-in sorting solution. This explanation follows the exact code.

## Alternatives and edge cases

- **Frequency counting:** Count occurrences through maximum value `M` and carry duplicates forward. This can achieve `O(n + M)` time and `O(M)` space when the value range is affordable.
- **Hash-set probing:** Increment duplicates until an unused value appears. Without acceleration, long duplicate runs repeatedly test the same occupied values.
- **Disjoint-set next-free lookup:** Map occupied values to their next candidates and compress paths. It can avoid sorting but is more complicated.
- **Already unique values:** Each `x` exceeds `y`, so all values remain unchanged and the answer is zero.
- **All values identical:** They receive consecutive destinations beginning at their common original value. Any gap would add needless cost.
- **Large gaps:** Whenever `x > y`, the formula keeps `x` unchanged.
- **Zero values:** Initial `y = -1` allows the first zero to remain zero.
- **Input mutation:** `nums.sort()` changes the caller's order. Sort a copy if preservation is required.
- **Thirty-two-bit result guarantee:** It protects fixed-width implementations. Python integers remain safe regardless.
- **Original indices:** The code does not reconstruct destinations by input position because only the minimum total is requested.
