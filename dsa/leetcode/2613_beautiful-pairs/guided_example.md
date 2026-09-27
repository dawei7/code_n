# Guided Example: Beautiful Pairs

## 1. The instance, the points it defines, and the required answer

Two arrays of equal length describe one point of the plane per index: index $i$ contributes the point

$$P_i = (\text{nums1}[i],\ \text{nums2}[i]).$$

For the representative input $\text{nums1} = [1,2,3,2,4]$ and $\text{nums2} = [2,3,1,2,3]$ the five points are the following.

| Index $i$ | $\text{nums1}[i]$ | $\text{nums2}[i]$ | Point $P_i$ |
|---|---|---|---|
| 0 | 1 | 2 | $(1, 2)$ |
| 1 | 2 | 3 | $(2, 3)$ |
| 2 | 3 | 1 | $(3, 1)$ |
| 3 | 2 | 2 | $(2, 2)$ |
| 4 | 4 | 3 | $(4, 3)$ |

A pair of indices $i < j$ is beautiful when its Manhattan distance

$$d(i, j) = \lvert \text{nums1}[i] - \text{nums1}[j] \rvert + \lvert \text{nums2}[i] - \text{nums2}[j] \rvert = \lvert \Delta x \rvert + \lvert \Delta y \rvert$$

is as small as possible over all index pairs, and among the pairs attaining that minimum the required output is the lexicographically smallest one. For this instance the required answer is `[0, 3]`, whose distance is $\lvert 1 - 2 \rvert + \lvert 2 - 2 \rvert = 1$.

## 2. The ground truth, computed by inspection

Before any algorithm is designed, the instance's distances must be known, because every method in this lesson is judged by whether it reproduces them. Enumerating the ten index pairs gives the following table, where the last column marks the minimum.

| Pair $(i, j)$ | $\lvert \Delta x \rvert$ | $\lvert \Delta y \rvert$ | $d(i, j)$ | Attains the minimum |
|---|---|---|---|---|
| (0, 1) | 1 | 1 | 2 | no |
| (0, 2) | 2 | 1 | 3 | no |
| (0, 3) | 1 | 0 | 1 | **yes** |
| (0, 4) | 3 | 1 | 4 | no |
| (1, 2) | 1 | 2 | 3 | no |
| (1, 3) | 0 | 1 | 1 | **yes** |
| (1, 4) | 2 | 0 | 2 | no |
| (2, 3) | 1 | 1 | 2 | no |
| (2, 4) | 1 | 2 | 3 | no |
| (3, 4) | 2 | 1 | 3 | no |

The minimum distance is $1$, and two pairs attain it: `(0, 3)` and `(1, 3)`. Lexicographic order compares first indices and then second indices, so `(0, 3)` wins and the answer is `[0, 3]`. Two structural facts are already visible and both matter later. The optimal pair `(0, 3)` is **not** index-adjacent, so no local scan of neighbouring indices can find it. And the tie exists at all, so the comparison performed by any method must be a lexicographic comparison of the triple $(\text{distance}, i, j)$ with $i < j$, not a comparison of distances alone.

## 3. Distance zero, the degenerate case that must be settled first

A Manhattan distance is a sum of two non-negative terms, so it is zero exactly when both coordinates agree: two indices with the same point. A zero-distance pair beats every positive candidate, and it can only occur among indices that share a point. This case deserves its own step because it is the global optimum whenever it exists, and because its tie-break has a cleaner characterization than the general one: among all repeated points, the answer is the pair formed by the earliest index whose point repeats and the next occurrence of that same point.

| Instance | Points | Zero-distance pairs | Answer | Why |
|---|---|---|---|---|
| `nums1=[0,0,0]`, `nums2=[1,1,1]` | three copies of $(0,1)$ | `(0,1)`, `(0,2)`, `(1,2)` | `[0,1]` | the earliest repeated index is 0, paired with its next occurrence 1 |
| `nums1=[0,0,1]`, `nums2=[1,1,0]` | $(0,1)$ twice, then $(1,0)$ | `(0,1)` | `[0,1]` | same rule with a single repeated point |
| `nums1=[0,1,2]`, `nums2=[0,1,0]` | $P_0 = (0,0)$, $P_1 = (1,1)$, $P_2 = (2,0)$ | none | `[0,1]` | no repeats, so the positive-distance search runs |

The second and third rows are constructed probes rather than package cases; they exist to separate "a repeated point exists" from "the earliest indices win", since a method that scans points in coordinate order rather than index order can return `[1,2]` for the first row and miss the lexicographically smaller `[0,1]`. The package's authored instance `nums1=[0,0,0]`, `nums2=[1,1,1]` exercises exactly this trap.

Once it is known that all points are distinct, the minimum distance is at least $1$, and the search can proceed geometrically.

## 4. Divide and conquer on the sorted x-order

Sort the points by $x$ (and break ties by $y$, which is harmless because the index is carried along). A range of the sorted order is then a vertical slab of the plane, and the closest pair inside a slab is found as follows.

1. Split the range at its midpoint index $m$, and let $x^{\ast}$ be the $x$-coordinate of the median point. Recurse on the left part and on the right part, and let $d$ be the better of the two results, compared by the triple $(\text{distance}, i, j)$.
2. Only pairs that straddle the two parts can still improve on $d$. If a point $p$ is farther than $d$ from the split line, then for every point $q$ on the other side the horizontal gap alone satisfies $\lvert \Delta x \rvert > d$, so $d(p,q) > d$ and the pair is hopeless. The surviving points form the **strip** $\lvert x - x^{\ast} \rvert \le d$.
3. Sort the strip by $y$. For a fixed point $p$ in the strip, any partner $q$ further down the strip than $d$ in $y$ has $\lvert \Delta y \rvert > d$, hence $d(p,q) > d$, so the inner scan may **break** as soon as the $y$-gap exceeds $d$.
4. Within one half of the strip, all pairs are already known to be at distance at least $d$. That is a packing constraint: a $d \times d$ window of one half cannot contain an unbounded number of points that are pairwise at Manhattan distance $d$ or more. The number of $y$-window candidates for a single point is therefore bounded by a constant that depends only on the metric, not on the size of the input, which is what keeps the strip scan linear in the strip length.

The strip width uses the *current* best $d$, so improving $d$ early prunes the remaining work immediately; the recursion effectively narrows its own search as it goes.

## 5. Executing the recursion on the instance

Sorting the five points by $(x, y)$ gives the order

$$(1,2)_{i0},\ (2,2)_{i3},\ (2,3)_{i1},\ (3,1)_{i2},\ (4,3)_{i4},$$

where the subscript records the original index. The recursion tree, with each node's range written as a half-open description of that sorted order, evaluates as follows. `inf` denotes "no pair inside this range".

| Node range | Split coordinate $x^{\ast}$ | Left result | Right result | Best before the strip scan | Result returned |
|---|---|---|---|---|---|
| 0–1 | 1 | `inf` | `inf` | `inf` | $(d=1, (0,3))$ |
| 2–2 | 2 | `inf` | `inf` | `inf` | `inf` |
| 0–2 | 2 | $(1, (0,3))$ | `inf` | $(1, (0,3))$ | $(1, (0,3))$ |
| 3–4 | 3 | `inf` | `inf` | `inf` | $(d=3, (2,4))$ |
| 0–4 | 2 | $(1, (0,3))$ | $(3, (2,4))$ | $(1, (0,3))$ | $(1, (0,3))$ |

The leaf ranges 2–2 and the single-point sides contribute nothing, which is why the smallest slabs are handled by the general rule rather than by a special case. The 0–1 node is the only place where the initial best distance is established, and every later node either confirms it or fails to beat it.

At the top node the best known distance is $d = 1$, so the strip keeps points within $1$ of the split line $x^{\ast} = 2$. That excludes the point $(4,3)_{i4}$, whose horizontal gap is $2$. The strip sorted by $y$ is $(3,1)_{i2}, (1,2)_{i0}, (2,2)_{i3}, (2,3)_{i1}$, and the scan visits the following candidates.

| Step | Candidate pair | $y$-gap | $d(i,j)$ | Decision against the incumbent $(1, (0,3))$ |
|---|---|---|---|---|
| 1 | `(0, 2)` | 1 | 3 | worse distance, discarded |
| 2 | `(2, 3)` | 1 | 2 | worse distance, discarded |
| 3 | `(1, 2)` | 2 | — | $y$-gap exceeds $d = 1$, so the inner scan breaks |
| 4 | `(0, 3)` | 0 | 1 | equal distance and equal pair, so the incumbent stands |
| 5 | `(0, 1)` | 1 | 2 | worse distance, discarded |
| 6 | `(1, 3)` | 1 | 1 | equal distance but `(1, 3)` is lexicographically larger than `(0, 3)`, so the incumbent stands |

The scan ends with the pair `(0,3)`, so the answer is `[0, 3]`, matching the ground truth of Section 2. Step 3 is the pruning in action: two points far apart in $y$ are never compared even though both lie in the strip, and step 6 is the tie-break in action, rejecting the equally short but lexicographically larger pair `(1,3)`.

## 6. Invariant and correctness of the divide-and-conquer search

**Node invariant.** A node covering a range $R$ of the $x$-sorted points returns the triple $(\text{distance}, i, j)$ that is minimal in lexicographic key order over all index pairs whose two points both lie in $R$, or the infinite sentinel when $R$ holds fewer than two points. The recursion is well founded because each child range is strictly smaller than its parent.

**Completeness of the combine step.** Any pair inside $R$ either lies wholly in the left part, wholly in the right part, or straddles the split. The first two families are exactly what the recursive calls return; the straddling family is what the strip scan examines. Every straddling pair with $\lvert \Delta x \rvert > d$ is safely ignored, because then $d(p,q) \ge \lvert \Delta x \rvert > d$ and the pair cannot improve on the incumbent. Every straddling pair with $\lvert \Delta x \rvert \le d$ has both points in the strip, so it is present for the scan; among those, the $y$-gap break discards exactly the pairs whose vertical gap already exceeds $d$, which again implies $d(p,q) > d$. Nothing that could improve on the incumbent is skipped, so the returned triple is the true minimum over $R$.

**Soundness.** Every value returned is the distance of an actual index pair, computed from the two points, with the indices normalized so that the smaller one comes first. No quantity is invented, and the sentinel is returned only when no pair exists.

**Tie-breaking.** Pairs are compared by the key $(\text{distance}, i, j)$ with $i < j$; equal keys denote the same pair, so keeping the incumbent on a tie is safe. Distance is compared first because it is the primary criterion, then the first index, then the second, which is exactly the definition of lexicographic order on index pairs. Forcing $i < j$ before comparing is essential: the raw pair `(3, 0)` and the pair `(0, 3)` are the same pair, and an unnormalized comparison would order them incorrectly. The distinct-points precondition matters here as well: the strip reasoning uses $d \ge 1$, and a duplicate point would put two identical points at distance $0$, which the packing and break arguments do not cover — that is why the duplicate scan of Section 3 runs first and returns immediately.

## 7. Boundary cases and traps

| Situation | Authored instance | Correct outcome | The trap it exposes |
|---|---|---|---|
| Repeated points | `nums1=[0,0,0]`, `nums2=[1,1,1]` | `[0,1]` | three zero-distance pairs exist; only the earliest two indices win |
| Equal positive distances | `nums1=[0,1,2]`, `nums2=[0,1,0]` | `[0,1]` | pairs `(0,1)` and `(1,2)` both have distance $1$; lexicographic order decides |
| Same first coordinate | `nums1=[2,2,0,4]`, `nums2=[3,1,2,2]` | `[0,1]` | the closest pair is vertical, and both its points can land in different halves of the split |
| Same first coordinate, larger input | `nums1=[1,2,4,3,2,5]`, `nums2=[1,4,2,3,5,1]` | `[1,4]` | same failure mode at a depth where the strip scan is the only thing that finds the pair |
| Symmetric configurations | `nums1=[6,0,3,6,1,5]`, `nums2=[0,6,3,6,5,1]` | `[0,5]` | `(0,5)` and `(1,4)` are mirror images with equal distance $2$; the index order, not the geometry, breaks the tie |
| Coordinates as large as the length | `nums1=[4,0,4,2,1]`, `nums2=[4,0,3,2,1]` | `[0,2]` | coordinates are unrelated to indices, so no coordinate ordering may be used as an index ordering |

Three further traps are worth stating without an instance. First, a method that compares distances only, and replaces the incumbent whenever a candidate is *at most* as good, will return whichever pair it met last rather than the lexicographically smallest one. Second, the recursion must sort the strip by $y$ **within the node**, not globally, because the strip is a subset that changes with the recursion. Third, the strip filter must use the updated best distance; using a stale larger value keeps points that can no longer improve anything and destroys the pruning.

| Method | Time | Space | Weakness |
|---|---|---|---|
| Enumerate all pairs | $O(n^{2})$ | $O(1)$ | too slow once $n$ reaches $10^{5}$ |
| Sort by $x$, compare neighbours | $O(n \log n)$ | $O(n)$ | wrong: the optimum need not be index-adjacent, as `(0,3)` in this instance shows |
| Transform to Chebyshev coordinates and sweep | $O(n \log n)$ | $O(n)$ | correct, but the tie-break and duplicate handling still have to be written separately |
| Divide and conquer with a strip scan | $O(n \log^{2} n)$ | $O(n)$ | none; this is the method the lesson derives |

## 8. Complexity of the divide-and-conquer search

Let $n$ be the common length of the two arrays, with $n \le 10^{5}$. The duplicate scan costs $O(n)$ expected time with a hash structure keyed by the point. The recursion has depth $O(\log n)$ because each call halves the range. At a node covering $s$ points, filtering the strip takes $O(s)$ and sorting it takes $O(s \log s)$; summed over one level of the recursion tree the ranges are disjoint and cover all $n$ points, so a level costs $O(n \log n)$ in the worst case, and with $O(\log n)$ levels the total is

$$O(n \log^{2} n).$$

The strip scan itself is linear in the strip length, because for each point the inner loop breaks after a constant number of comparisons — the packing argument of Section 4 — so it never dominates the sort. The $O(n \log^{2} n)$ bound can be improved to $O(n \log n)$ by carrying a by-$y$ ordering through the recursion (merging the two children's orders instead of re-sorting), which removes the extra logarithmic factor; the re-sorting formulation is simply the one that keeps the combine step readable.

Auxiliary space is $O(n)$ for the sorted point list and the strip copies, plus $O(\log n)$ frames of recursion depth, so the search never stores more than a constant number of copies of the input. The pairwise enumeration alternative needs $O(1)$ extra space but $O(n^{2})$ time, which is the wrong trade at these constraints: for $n = 10^{5}$ it inspects about $5 \times 10^{9}$ pairs, while the divide-and-conquer search inspects each level's strip once per node.