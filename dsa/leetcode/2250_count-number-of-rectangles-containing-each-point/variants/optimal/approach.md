## General

**Containment becomes two lower-bound conditions**

Every rectangle starts at `(0,0)` and ends at `(l,h)`. Since point coordinates are positive under the constraints, point `(x,y)` is contained exactly when

$$
l \ge x \quad \text{and} \quad h \ge y.
$$

The challenge is to count rectangles satisfying both inequalities for up to fifty thousand points.

**Exploit the small height universe**

Rectangle lengths can be as large as `10^9`, but heights are only one through one hundred. The solution groups rectangle lengths by exact height:

`d[y].append(x)`

where local `x` is rectangle length and `y` is rectangle height.

After all rectangles are bucketed, each height's length list is sorted. The code iterates `d.keys()` and replaces each list with its sorted order in place. Updating values without adding or removing keys is safe during key iteration.

**Answer one point by scanning eligible heights**

For point `(x,y)`, a containing rectangle must have height at least `y`. The loop

`for h in range(y, 101)`

visits every possible eligible height through the maximum one hundred. Heights below `y` are ignored because those rectangles cannot contain the point vertically.

Within exact-height bucket `h`, the sorted list `xs` contains rectangle lengths. `bisect_left(xs, x)` finds the first position whose length is at least point coordinate `x`. Therefore,

`len(xs) - bisect_left(xs, x)`

is the number of rectangles in that bucket satisfying `l >= x`.

Summing this over all heights `h >= y` counts exactly the rectangles satisfying both dimensions.

**Why edge points count**

Both containment boundaries are inclusive. Starting the height loop at `y` includes rectangles with `h = y`. `bisect_left` inserts before values equal to `x`, so lengths exactly equal to `x` are included in the suffix count.

Using `bisect_right` would incorrectly exclude equal-length rectangles.

**Default empty buckets**

`d` is a `defaultdict(list)`. Accessing `d[h]` for a height with no rectangles yields an empty list. Its length and insertion index are both zero, contributing nothing.

These accesses may create empty dictionary entries during point processing, but there are at most 101 height keys, so this does not affect asymptotic storage.

**Why every counted rectangle contains the point**

A rectangle counted in bucket `h` came from a loop value `h >= y`. Its length lies in the suffix starting at the first value at least `x`, so `l >= x`. Since the rectangle begins at the origin and point coordinates are nonnegative, both containment conditions hold.

**Why every containing rectangle is counted**

Take a rectangle containing point `(x,y)`. Its height `h` is at least `y`, so the height loop visits its bucket. Its length `l` is at least `x`, so it appears at or after the `bisect_left` boundary and contributes one. Every rectangle lives in exactly one height bucket, preventing duplicates.

**Preserve point order**

The method processes `points` in their original order and appends one `cnt` immediately for each. It does not sort points, so the returned positions correspond directly to input indices.

**Trace a bucket**

Suppose height five has sorted lengths `[1,2,7,10]` and the point's x-coordinate is two. `bisect_left` returns index one, and the suffix has three lengths: two, seven, and ten. All three contain the point horizontally.

If the point's y-coordinate is four, height five is among the visited buckets. If its y-coordinate is six, that bucket is skipped.

## Complexity detail

Let `R` be the number of rectangles, `P` the number of points, and `H = 100` the maximum height. Sorting all buckets costs at most `O(R \log R)` in total.

Each point scans at most `H` height values and performs a binary search costing `O(\log R)` in the worst case. Query time is `O(PH \log R)`, so total time is `O(R \log R + PH \log R)`.

Buckets store every rectangle length once plus at most `H` lists, using `O(R + H)` space. The answer uses `O(P)` required output space.

Because `H` is fixed at one hundred, the per-point height scan is effectively a small constant factor.

## Alternatives and edge cases

- **Test every rectangle for every point:** It takes `O(RP)` time and ignores the bounded-height opportunity.
- **Sweep points and rectangles by x:** A Fenwick tree over heights can achieve strong asymptotic performance, but requires offline sorting and more machinery.
- **One global length list:** It loses height information, so rectangles too short vertically would be counted.
- **Use `bisect_right`:** It would exclude rectangles whose right edge is exactly at the point's x-coordinate.
- **Point on top edge:** Height equality is included because scanning starts at `y`.
- **Point on right edge:** Length equality is included by `bisect_left`.
- **No eligible height:** The loop may be empty only beyond the stated range; within constraints, empty buckets simply contribute zero.
- **Empty exact-height bucket:** `defaultdict` returns an empty list and binary search contributes zero.
- **Duplicate dimensions:** Rectangles are unique, but equal lengths may appear at different heights and are counted independently.
- **Large x-coordinate:** Insertion may be at the list end, giving zero for that bucket.
- **Small y-coordinate:** More height buckets are considered, as required.
- **Output ordering:** Points are never rearranged.
