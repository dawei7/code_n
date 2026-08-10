## General

**Understand the triangle's adjacency pattern**

Row $i$ contains coordinates one through $2i-1$. Consecutive coordinates in one row share a side.

The alternating triangle orientations also create cross-row edges: an odd-positioned triangle $(i,2q-1)$ shares a side with even-positioned triangle $(i+1,2q)$ immediately below it.

These horizontal and diagonal connections are why a repeating row pattern can make every initially white triangle acquire two red neighbors.

The exact solution always selects top triangle $(1,1)$ and then processes rows from bottom to top using a four-phase pattern.

**The four initial-color patterns**

Variable `k` cycles through zero, one, two, and three as row index `i` decreases.

- Phase zero colors every odd position `1,3,5,...,2i-1`.
- Phase one colors only position two.
- Phase two colors odd positions `3,5,...,2i-1`, omitting position one.
- Phase three colors only position one.

Then `k = (k + 1) % 4` repeats the pattern for the next four rows above.

All produced coordinates lie in their row: the range endpoints and the single positions are valid whenever their corresponding phase can occur.

**Why a row of odd seeds fills itself**

In phase zero, every even-positioned triangle lies horizontally between two red odd-positioned triangles.

It therefore has at least two red neighbors and can be colored. Once all even positions are added, the entire row is red.

This fully seeded odd row acts as support for neighboring rows in the four-row motif.

**How the sparse rows support one another**

The remaining three phase patterns are not meant to fill independently. Their seeds cooperate with the complete or partially seeded rows immediately above and below.

The local propagation repeats as follows:

- the phase-two row already has every odd seed except its leftmost one;
- the phase-three row above supplies the cross-row support that lets the phase-two row fill its missing even position near the left boundary;
- the phase-one row below supplies support for its missing leftmost odd position;
- once these boundary positions turn red, horizontal adjacency propagates across the rows;
- the next phase-zero row above supplies alternating cross-row support for the phase-three row, while the already completed row below supplies the other required neighbors.

Each newly colored triangle has either two horizontal red neighbors or one horizontal and one cross-row red neighbor. The same finite local sequence repeats every four rows.

At the top boundary, explicitly selected $(1,1)$ closes the final partial motif.

**A more concrete four-row propagation**

Label four consecutive phase rows from bottom upward as $A,B,C,D$, with the next row above beginning another $A$ pattern.

- Row $A$ has all odd triangles red, so its even triangles fill.
- Row $C$ has odd seeds from position three onward. Its even position two gets support from row $D$'s position one and its red neighbor at position three; then its missing position one gets support from row $B$ and the newly red even position. Other gaps between odd seeds fill.
- Row $B$ starts at position two. Completed row $A$ supports its odd positions, while completed row $C$ supports successive even positions, letting red color propagate across.
- Row $D$ starts at position one. Odd seeds in the next $A$ row above support successive even positions, and completed row $C$ below supports the intervening odd positions.

Thus the initial pattern admits an explicit ordering that turns the whole block red. Repeating blocks covers all rows.

**Why the construction has minimum size**

The whole triangle contains:

$$
N=n^2
$$

unit triangles.

Count adjacency edges between unit triangles. All small triangles have $3n^2$ side incidences. The outer boundary has $3n$ unit sides counted only once; every internal shared side is counted twice. Therefore, the number of neighbor edges is:

$$
E=\frac{3n^2-3n}{2}
=
\frac{3n(n-1)}{2}.
$$

Suppose $K$ triangles are initially red. Every one of the other $N-K$ triangles needs at least two edges to triangles that became red earlier.

Charge two such edges when that triangle turns red. One undirected edge can be charged at most once—by its later-colored endpoint. Hence:

$$
2(N-K)\le E.
$$

Rearranging:

$$
K
\ge
N-\frac E2
=
\frac{n^2+3n}{4}.
$$

Since $K$ is integral:

$$
K\ge\left\lceil\frac{n(n+3)}4\right\rceil.
$$

**The pattern meets the lower bound**

Counting coordinates emitted by the four phases, together with $(1,1)$, gives exactly:

$$
\left\lceil\frac{n(n+3)}4\right\rceil
$$

initial red triangles.

This can be checked by grouping processed rows into blocks of four: phase-zero contributes all $i$ odd positions, phase one contributes one, phase two contributes all but the first odd position, and phase three contributes one. The remainder rows at the top are completed by the fixed root coordinate.

The propagation argument proves this many seeds are sufficient, while the edge-count argument proves fewer cannot suffice. Therefore, the returned set is minimum.

**Trace small sizes**

For $n=1$, only `[1,1]` is returned. One seed is obviously necessary.

For $n=2$, phase zero on row two selects positions one and three, plus the root. The remaining triangle $(2,2)$ has the two horizontal red neighbors and turns red. Three equals $\lceil2\cdot5/4\rceil$.

For $n=3$, row three contributes positions one, three, and five; row two phase one contributes position two; the root is selected. This gives five seeds, matching the example and lower bound.

**Why any valid answer is allowed**

The contract permits any minimum-size set. The four-row pattern is deterministic and convenient, but it is not claimed to be the only optimal construction.

The output order is bottom-to-top after the root, which has no semantic effect because the coordinates form a set of initially red triangles.

## Complexity detail

The nested range loops append exactly the output coordinates. Their count is $\Theta(n^2)$ in the asymptotic worst case, so time is $O(n^2)$.

The returned list itself contains $\Theta(n^2)$ coordinates in the worst case and uses $O(n^2)$ space. Aside from output, only row, column, and phase variables use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search all initial subsets:** Exponential in $n^2$ and infeasible.
- **Simulate after choosing the pattern:** Useful for verification but unnecessary to construct the proven percolating set.
- **Different optimal pattern:** Allowed if it meets the same lower bound and percolates.
- **`n = 1`:** The fixed root is the complete answer.
- **Partial final four-row block:** The root seed handles the top boundary.
- **Coordinate parity:** Odd-position ranges and the two single even/odd anchors must remain exactly aligned.
- **Bottom-up phase order:** `k` advances as rows decrease, so changing loop direction changes the construction.
- **Minimum proof:** Sufficiency alone is not enough; the global edge-count lower bound establishes optimality.
- **Output order:** It does not affect which triangles start red.
- **Large `n`:** The output itself is quadratic, matching the algorithm's time and space.
