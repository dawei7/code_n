## General

**Each minute adds one Manhattan-distance layer**

Choose the initially colored cell as coordinate $(0,0)$. A cell at $(x,y)$ can be reached from the center in exactly

$$
|x|+|y|
$$

orthogonal moves. This quantity is its Manhattan distance.

At minute one, only distance zero is colored. Each later minute colors every uncolored neighbor of an already colored cell, so after minute $n$, exactly the cells with

$$
|x|+|y|\le n-1
$$

are blue. The shape is a diamond centered at the initial cell.

The initial choice of cell does not affect the count because the grid is infinite and translation does not change neighborhood structure.

**Count one boundary layer**

For a positive distance $r$, the cells satisfying `abs(x) + abs(y) == r` form the boundary of a diamond.

Starting at $(r,0)$ and walking around the four sides, each side contains $r$ steps before reaching the next axis point. The total number of distinct boundary cells is

$$
4r.
$$

For $r=1$, these are the four orthogonal neighbors. For $r=2$, there are eight cells. For $r=3$, there are twelve. This explains the observed sequence of newly colored counts: $4,8,12,\ldots$.

The four axis corners are not double-counted by the $4r$ formula when thought of as four sequences of $r$ directed boundary steps, each contributing its reached cells up to but not duplicating the starting corner.

**Sum all layers through minute `n`**

The center contributes one cell. The later layers have radii $1$ through $n-1$, so the total is

$$
1+\sum_{r=1}^{n-1}4r.
$$

Using the arithmetic-series identity

$$
\sum_{r=1}^{k}r=\frac{k(k+1)}{2},
$$

with $k=n-1$ gives

$$
1+4\cdot\frac{(n-1)n}{2}
=
1+2n(n-1).
$$

The implementation returns this formula as `2 * n * (n - 1) + 1`.

**Alternative row-by-row derivation**

At vertical offset $y$ with $|y|\le n-1$, the remaining horizontal distance is $n-1-|y|$. The row contains

$$
2(n-1-|y|)+1
$$

colored cells. Row lengths increase through odd values up to $2n-1$ at the center, then decrease symmetrically.

Summing these rows gives another compact identity:

$$
n^2+(n-1)^2
=
2n(n-1)+1.
$$

Both derivations count the same diamond and provide a useful cross-check on the formula.

**Why the process cannot create cells outside the diamond**

Every newly colored cell touches a previously blue cell, so a path of at most $n-1$ neighbor steps connects it to the center after $n$ minutes. Its Manhattan distance cannot exceed $n-1$.

Conversely, any cell at distance $r\le n-1$ has a shortest path of $r$ orthogonal moves from the center. Inductively, the path's cell at distance one is colored in minute two, the distance-two cell in minute three, and the target by minute $r+1\le n$. Thus every cell inside the diamond is colored.

This proves that the layer count is exact, not merely a visual pattern extrapolation.

**Check the first few values**

- At $n=1$, radius is zero and the formula gives $2\cdot1\cdot0+1=1$.
- At $n=2$, one layer of four is added, giving $5$.
- At $n=3$, the next layer adds eight, giving $13$.
- At $n=4$, twelve more cells give $25$.

The successive differences are $4(n-1)$, matching the size of the newly exposed radius-$n-1$ boundary.

**Why a closed form is preferable**

An iterative solution could begin at one and add `4*r` for each new minute. That takes $O(n)$ time and is already fast for $10^5$, but the arithmetic series contains no state that needs simulation. The closed form computes the exact same total with a fixed number of operations.

The multiplication order does not affect Python due to arbitrary-precision integers. In fixed-width languages, the largest result is about $2\cdot10^{10}$ for $n=10^5$, so a 64-bit type is required.

## Complexity detail

The function performs a constant number of integer multiplications, additions, and a subtraction, independent of $n$. Under the usual word-RAM model for the constrained integer range, time is $O(1)$ and auxiliary space is $O(1)$.

No grid, set of coordinates, or sequence of layer counts is allocated. The returned integer is the only result.

## Alternatives and edge cases

- **Iterative layer addition:** Add $4,8,\ldots,4(n-1)$ to one. This is correct but takes $O(n)$ time.
- **Grid simulation:** Tracking colored coordinates wastes $O(n^2)$ space and work because only the count is requested.
- **Breadth-first search:** BFS reproduces Manhattan layers but is unnecessary on an obstacle-free infinite grid.
- **Row counting:** Summing diamond row widths leads to the equivalent formula $n^2+(n-1)^2$.
- **First minute:** There are no boundary layers, and the formula correctly returns one.
- **Arbitrary starting cell:** Translation on an infinite grid preserves the count.
- **Meaning of touches:** Orthogonal cell adjacency produces Manhattan diamonds; diagonal adjacency would create a different square-shaped count.
- **Large `n`:** The answer exceeds 32-bit range near the upper constraint, so use 64-bit arithmetic outside Python.
- **No off-by-one layer:** Minute one corresponds to radius zero, making the final radius `n - 1` rather than `n`.
