## General

**Represent each point by the square size needed to include it**

An axis-aligned square centered at the origin with half-side length $d$ contains point $(x,y)$ exactly when

$$
\lvert x\rvert\le d\quad\text{and}\quad\lvert y\rvert\le d.
$$

These two inequalities are equivalent to

$$
\max(\lvert x\rvert,\lvert y\rvert)\le d.
$$

The exact solution calls this required half-side length the point's distance and groups point indices by

`max(abs(x), abs(y))`.

This is the Chebyshev distance from the origin. As a square grows, it includes groups in nondecreasing Chebyshev distance.

**Process an entire boundary layer together**

The dictionary `g` maps each distance $d$ to all point indices lying on that square boundary. The code sorts the distinct distances and processes them from smallest outward.

Set `vis` contains tags of every point accepted at a strictly smaller distance, plus tags already inspected in the current layer. Before accepting a layer, the code checks every point index in it:

- if `s[i]` is already in `vis`, including this distance would put two points with the same tag inside the square, so the method returns the number `ans` from all earlier layers;
- otherwise, the tag is added to `vis`.

Only after every tag in the layer passes does `ans` increase by the whole layer size.

Delaying the count update is essential because the boundary is inclusive. A square large enough to include one point at distance $d$ includes every point whose distance is also $d$. We cannot choose only a harmless subset of a boundary layer. If two equal tags occur in the same group, the first is tentatively added and the second detects the duplicate; returning the old `ans` excludes the entire layer, as required.

**Why stopping at the first conflict is optimal**

Before the first conflicting distance $d$, all points in smaller layers have distinct tags, so the square with half-side just below $d$—or at the previous processed distance—is valid and contains `ans` points.

At distance $d$, at least two included points share a tag. Every larger square contains all points from distance $d$ as well, because squares are nested as their side length grows. Therefore, no later square can become valid again. Returning immediately loses no possible larger valid answer.

If all groups pass, the square expanded through the farthest point includes every point with unique tags, and `ans` equals the total number of points.

**Examples**

Suppose two points with tag `'c'` both have distance 1. They lie on the same first boundary. A half-side below 1 contains neither; a half-side of 1 contains both because boundary points count as inside. No square can contain exactly one of them, so the method detects the duplicate within the group and returns zero.

If tag `'a'` first occurs at distance 2 and again at distance 5, layers below 5 can be accepted. When distance 5 is reached, `'a'` is already in `vis`, so the answer through distance 4 is returned.


After a complete distance group has been accepted:

- `ans` equals the number of points at all processed distances;
- `vis` contains exactly their tags;
- all tags in `vis` are distinct;
- a square with half-side equal to the current distance is valid.

The invariant is true before processing any group. A group with no repeated tag preserves it after all of its points and tags are added. A detected repetition proves the current and every larger square invalid, while the previous invariant supplies an achievable answer. Thus the returned number is maximal.

**Relation to the manifest**

The manifest describes a different linear method that tracks each tag's nearest radii and a conflict threshold. The exact source instead builds distance groups and sorts them. Its correctness is sound, but its time and space bounds must reflect grouping and sorting rather than the manifest summary.

## Complexity detail

Let $n$ be the number of points and $g$ the number of distinct Chebyshev distances.

Building the dictionary and lists takes $O(n)$ expected time. Sorting the $g$ distance keys costs $O(g\log g)$. Every point is then inspected at most once. Total expected time is

$$
O(n+g\log g),
$$

which is $O(n\log n)$ in the worst case when all distances are distinct.

The dictionary lists collectively store all $n$ point indices, using $O(n)$ space. The sorted key list uses $O(g)$ space. The tag set has at most 26 entries because tags are lowercase English letters, but this does not dominate the groups. Exact auxiliary space is therefore $O(n)$.

This contradicts the manifest's $O(n)$ time and $O(1)$ space, which describe the alternative nearest/second-nearest-tag strategy, not the exact code.

Output space is one integer. Python sorting may also use temporary memory proportional to the number of keys.

## Alternatives and edge cases

- **Nearest two radii per tag:** For each of 26 tags, track its two smallest point distances. The smallest second occurrence is the first invalid boundary; count nearest occurrences strictly below it. This achieves $O(n)$ time and $O(1)$ alphabet-bounded space.
- **Sort points directly:** Sort `(distance, tag)` pairs and scan equal-distance batches. It has the same $O(n\log n)$ time and can avoid dictionary-of-lists organization.
- **Binary search square size:** A validity predicate can count tags inside a candidate radius, but repeated scans or preprocessing make it more complicated than finding the first conflict directly.
- **Euclidean distance:** It is wrong for axis-aligned squares. The required radius is `max(abs(x), abs(y))`, not a square root.
- **Duplicate tag in one layer:** The entire layer must be excluded because all boundary points enter simultaneously.
- **Duplicate tag across layers:** The second occurrence makes that layer and every larger square invalid.
- **Point on boundary:** It is included by the problem statement, which is why the comparison uses “at most” conceptually and layers are atomic.
- **Side length zero:** Points at the origin have distance zero and are processed first. Distinct coordinates allow at most one actual origin point.
- **First layer invalid:** The method returns zero, representing a zero-size or smaller square that contains no conflicting points.
- **All tags distinct:** Every group is accepted and the answer is $n$.
- **Same distance, all distinct tags:** The whole group is safely added at once.
- **Tentative tags before conflict:** The code may add some current-layer tags before finding a duplicate, but it returns immediately and never counts the layer, so this mutation has no effect on the answer.
