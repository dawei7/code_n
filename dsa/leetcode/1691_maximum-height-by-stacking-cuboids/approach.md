## General

**Normalize every cuboid’s rotation**

A cuboid’s three dimensions may be permuted by rotation. Sorting each dimension list produces a canonical triple

$$
d_0\le d_1\le d_2.
$$

This normalization removes the need to try six orientations explicitly. Two rotatable cuboids can be ordered componentwise exactly when their sorted triples can be ordered componentwise. Matching smallest with smallest, middle with middle, and largest with largest is the most permissive aligned comparison.

The source treats `d_2`, the largest dimension, as height. This maximizes that cuboid’s vertical contribution, while `d_0` and `d_1` form its other axes. In a componentwise-compatible stack, using the sorted axes gives a feasible orientation and no smaller height than choosing another dimension vertically.

**Sort cuboids into a possible stacking order**

After normalizing inner lists, `cuboids.sort()` lexicographically sorts the triples. For any earlier index `j < i`:

- either `cuboids[j][0] < cuboids[i][0]`, or
- their first dimensions tie and later dimensions determine order.

Thus the first dimension of `j` is automatically no greater than the first dimension of `i`. The transition only needs to explicitly check:

`cuboids[j][1] <= cuboids[i][1]` and `cuboids[j][2] <= cuboids[i][2]`.

Together with sorted order, these are all three componentwise fit conditions.

**Define the stack-height state**

`f[i]` is the maximum height of a valid stack whose bottom cuboid is `cuboids[i]`. Every cuboid used above it comes from an earlier, componentwise smaller triple.

The source initially leaves `f[i]` at zero. It scans all `j < i`. If cuboid `j` can fit on `i`, then a best stack with bottom `j` can be placed on top of `i`. `f[j]` is the height of that upper stack.

The loop stores the maximum such `f[j]`. After considering all possible immediate upper stack bottoms, it adds `cuboids[i][2]`, the height of the current bottom cuboid.

If no earlier cuboid fits, `f[i]` becomes only `cuboids[i][2]`, representing a one-cuboid stack.

**Why `f[j]` can be reused as a whole stack**

Every cuboid in the stack represented by `f[j]` is componentwise no larger than cuboid `j`, and `j` is componentwise no larger than `i`. Componentwise comparison is transitive, so every cuboid above remains compatible when that whole stack is placed on `i`.

The DP therefore does not need to remember the full chosen sequence, only its total height and bottom dimensions.

**Trace the first example conceptually**

Each cuboid is sorted internally:

- `[50,45,20]` becomes `[20,45,50]`;
- `[95,37,53]` becomes `[37,53,95]`;
- `[45,23,12]` becomes `[12,23,45]`.

Lexicographic sorting places `[12,23,45]`, then `[20,45,50]`, then `[37,53,95]`. Each earlier triple fits componentwise on the later one. The DP accumulates heights `45 + 50 + 95 = 190`.

**Why the maximum DP value is the answer**

Every transition creates a valid stack because all three normalized dimensions satisfy the fit relation. Thus every `f[i]` is achievable.

Conversely, take an optimal stack and write each cuboid as its sorted triple. Componentwise fit orders those triples consistently with the global lexicographic sort. Its bottom appears at some index `i`, and the cuboid directly above appears earlier at some `j` satisfying the transition. Inductively, the DP can reproduce the entire stack and its height.

The optimal stack may end with any cuboid at the bottom, so `max(f)` selects the best among all possibilities.

## Complexity detail

Let `n` be the number of cuboids. Sorting three dimensions inside each cuboid is constant-size work, totaling $O(n)$. Sorting the `n` triples costs $O(n\log n)$.

The nested DP examines every ordered pair `j < i`, costing $O(n^2)$ time, which dominates sorting. The `f` array uses $O(n)$ space. Python’s list sort may also use $O(n)$ temporary workspace, so total auxiliary space remains $O(n)$.

The source mutates both each inner dimension list and the outer `cuboids` order.

## Alternatives and edge cases

- **Enumerate all six rotations:** Build orientation states and run a larger DP. It is correct but unnecessary because sorting dimensions gives a canonical componentwise representation.
- **Longest-path graph:** Create an edge when one normalized cuboid fits on another and find the maximum-weight path in the resulting DAG. This is equivalent to the sorted DP with more explicit structure.
- **No two cuboids fit:** Every `f[i]` is just that cuboid’s largest dimension, and the answer is the tallest single cuboid.
- **Identical cuboids:** Non-strict `<=` permits stacking all of them, so their heights add.
- **Equal one or two dimensions:** Equality is allowed by the placement rule and the transition.
- **One cuboid:** Its sorted largest dimension is chosen as height and returned.
- **Subset choice:** The DP may skip any cuboid because transitions are optional and `max(f)` does not require using all items.
- **Lexicographic ordering:** It guarantees the first-dimension inequality for earlier candidates, which is why the code checks only indices one and two.
- **Rotation mutation:** Sorting an inner list changes its stored orientation representation but preserves the physical cuboid’s available dimensions.
- **Input reuse:** Callers needing the original dimension order should pass a copy because the exact source sorts in place.
- **Positive dimensions:** Every added height increases the stack total, so there is no reason to include an incompatible or negative-contribution cuboid.
