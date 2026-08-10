## General

**Treat the two arrays as points**

Index $i$ represents the two-dimensional point

$$
P_i=(\texttt{nums1[i]},\texttt{nums2[i]}).
$$

The requested expression is the Manhattan distance

$$
d(P_i,P_j)=|x_i-x_j|+|y_i-y_j|.
$$

The task is therefore to find a closest pair of points, while retaining original indices and using lexicographic index order to break distance ties.

The exact solution handles distance zero first, then applies divide and conquer to the remaining distinct-coordinate points.

**Resolve duplicate coordinates before recursion**

The dictionary `pl` maps each coordinate pair $(x,y)$ to the list of original indices having that point. If a coordinate appears more than once, two copies have Manhattan distance zero, the smallest distance possible.

The second pass scans original indices from left to right. At the first index `i` belonging to a duplicated coordinate, it returns

`[i, pl[(x, y)][1]]`.

Because `i` is the earliest first component among every zero-distance pair encountered, and list element one is the second occurrence of that same coordinate, this is the lexicographically smallest zero-distance pair. Once distance zero exists, no later geometric work can improve the distance, so immediate return is correct.

This preprocessing also makes every point passed to divide and conquer coordinate-distinct. That fact supports the geometric packing argument used to bound comparisons in a strip.

**Sort by the first coordinate**

Each point is stored as tuple `(x, y, original_index)`, and `points.sort()` orders primarily by $x$, then by $y$, then by index. Recursive call `dfs(l, r)` operates on a contiguous portion of this order.

The midpoint `m` divides the points into left range $[l,m]$ and right range $[m+1,r]$. A range with fewer than two points returns infinity and placeholder indices, because it contains no pair.

The two recursive calls find the best pair fully inside each half. The code chooses the smaller distance; if distances tie, it chooses the lexicographically smaller pair of original indices. Let the resulting best distance be $D$.

At this point, the only possibly better pair not yet covered has one point in each half.

**Restrict attention to a vertical strip**

Let $x_m$ be the midpoint point's first coordinate. A cross-half pair with distance at most $D$ cannot use a point whose horizontal distance from $x_m$ exceeds $D$. Manhattan distance is at least horizontal distance alone.

The list comprehension therefore keeps only points satisfying

$$
|x-x_m|\le D.
$$

Any cross pair capable of improving the current answer lies inside this strip. The code sorts the strip list `t` by $y$.

For one point `t[i]`, later strip points have nondecreasing $y$. As soon as

$$
y_j-y_i>D,
$$

their Manhattan distance is already greater than $D$ regardless of $x$, and every still-later point has an even larger $y$ difference. The inner loop can safely break.

For every pair that survives this test, the code calculates its exact Manhattan distance. It sorts the two original indices into `pi < pj`, then replaces the answer when the distance is smaller or when equal distance comes with a lexicographically smaller pair.

**Why the strip scan includes every necessary pair**

Pairs wholly within one recursive half were already evaluated by that half. Consider a cross pair with distance below the selected half-distance $D$.

The left point lies no farther than $D$ horizontally to the left of the dividing coordinate, and the right point lies no farther than $D$ to its right; otherwise their mutual horizontal separation alone would exceed $D$. Both therefore enter `t`.

Their absolute $y$ difference is at most their full Manhattan distance, so it is also at most $D$. Once `t` is sorted by $y$, the inner scan reaches this pair before its break condition can fire. The pair is evaluated.

Equal-distance pairs are included as well because both filters use inclusive `<= D` logic. That is necessary for lexicographic tie improvement even when the numerical optimum has already been found.

**Why only a constant number of nearby strip points matter**

At a recursive merge, each half has no internal pair with distance below $D$. In a bounded strip portion of vertical height $D$, points from the same half must therefore be separated under Manhattan distance by at least $D$.

This separation permits only a constant number of distinct points from each half inside a rectangle of width $2D$ and height $D$. Consequently, after sorting by $y$, each point can have only a constant number of later candidates before the $y$ gap exceeds $D$. This is the Manhattan counterpart of the packing argument in closest-pair algorithms.

The nested loops look quadratic syntactically, but the geometric separation inherited from the recursive half solutions prevents quadratic comparisons within a merge. Duplicate coordinates, which would violate strict separation at distance zero, were removed by the early-return phase.

**Tie-breaking is part of every merge**

The helper returns triple `(distance, pi, pj)`. When choosing between left and right recursive results, it compares distance first, then `pi`, then `pj`. The strip update applies the same order.

This consistency means `dfs(l, r)` has a stronger invariant than merely returning some closest pair: it returns the lexicographically smallest pair among all minimum-distance pairs in its range. The base cases satisfy the invariant vacuously, and the merge considers the best left, best right, and all competitive cross pairs, so induction proves it for the full array.

**Trace the role of original indices**

Sorting rearranges points geometrically, so positions inside `points` are not valid answer indices. Every tuple carries its original third component. Before comparing or returning a candidate, the code orders these two original values.

For example, if geometric order encounters original indices seven and two, the candidate must be represented as `[2,7]`. Without this normalization, lexicographic comparison could select the wrong answer even though all distances were correct.

**The exact algorithm versus the manifest summary**

The manifest describes an $x$-sweep with two segment trees. The stored solution instead uses divide and conquer plus a $y$-sorted strip at every recursion node. Both target the closest Manhattan pair, but their data flow and precise complexity are different. This explanation follows the executable source.

## Complexity detail

Let $n$ be the number of points. Duplicate grouping and the duplicate scan take expected $O(n)$ time and $O(n)$ space. Sorting all points initially takes $O(n\log n)$ time.

At a recursion node containing $s$ points, constructing the strip costs $O(s)$ and sorting that strip by $y$ costs $O(s\log s)$. The packing argument bounds the subsequent candidate comparisons by $O(s)$. The recurrence is therefore

$$
T(s)=2T(s/2)+O(s\log s),
$$

which gives $O(n\log^2 n)$ time for this exact implementation. The manifest's $O(n\log n)$ applies to its segment-tree sweep or to a divide-and-conquer implementation that maintains $y$ order across merges rather than sorting each strip anew.

The coordinate map, point list, and largest strip use $O(n)$ space. Temporary lists on a recursion path have geometrically decreasing sizes, summing to $O(n)$, and recursion depth is $O(\log n)$. Total space is $O(n)$.

## Alternatives and edge cases

- **Segment-tree sweep:** Transform Manhattan expressions and query the best prior point on either side of the current $y$ coordinate in $O(n\log n)$ time, matching the manifest but requiring careful tie-aware tree values.
- **Maintain merge order by $y$:** A classical closest-pair divide and conquer can avoid sorting at every level and reduce the exact strategy to $O(n\log n)$.
- **Brute force:** Checking all $\binom n2$ pairs is simple but costs $O(n^2)$ and cannot handle $10^5$ points.
- **Duplicate coordinates:** Their distance is zero; the preprocessing returns the lexicographically smallest such pair immediately.
- **Equal minimum distances:** Every comparison must use original-index lexicographic order after comparing distance.
- **Same $x$ coordinate:** Tuple sorting and inclusive strip membership keep such points; the divide may split them without losing cross pairs.
- **Same $y$ coordinate:** The inner scan still evaluates them because their $y$ difference is zero.
- **Two points:** Recursive halves are singletons, and the merge evaluates the only pair.
- **Original versus sorted indices:** Only tuple field two may appear in the returned pair.
- **Inclusive strip boundary:** Points at horizontal or vertical difference exactly $D$ must remain eligible because they may improve the lexicographic tie.
