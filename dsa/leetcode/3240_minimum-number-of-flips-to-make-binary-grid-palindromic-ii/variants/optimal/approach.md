## General

**Why reflections form independent groups**

If every row and column is palindromic, a cell at $(r,c)$ must equal its horizontal reflection, vertical reflection, and diagonal reflection:

$$
(r,c),\quad (r,n-1-c),\quad (m-1-r,c),\quad (m-1-r,n-1-c).
$$

Away from a middle row or middle column, these are four distinct cells. If such a group contains $k$ ones, making all four cells `0` costs $k$, while making all four `1` costs $4-k$. Taking $\min(k,4-k)$ is locally optimal. Either final choice contributes a multiple of four ones, so it can never disturb the divisibility condition.

**How middle pairs control the residue**

When $m$ is odd, the middle row contains horizontally mirrored two-cell groups. When $n$ is odd, the middle column contains vertically mirrored two-cell groups. A mismatched `01` or `10` pair costs one flip, and that flip may produce either `00` or `11`. Therefore, the presence of even one mismatched pair lets us choose whether the collection of middle pairs contributes $0$ or $2$ modulo $4$ without paying beyond the unavoidable mismatch cost.

A matched `00` pair contributes zero ones. A matched `11` pair contributes two ones. If there are no mismatched pairs and the matched pairs contribute $2$ modulo $4$, one entire `11` pair must be changed to `00`, costing two additional flips. Otherwise the pair contribution can already be made divisible by four.

**Why the center must be zero**

If both dimensions are odd, the central cell is its own reflection. All other symmetry groups contain two or four cells, so a center value of `1` is the only possible odd contribution to the final number of ones. It must be flipped to `0`, at a cost equal to its original value.

The four-cell costs, unavoidable middle-pair mismatch costs, center cost, and possible two-flip residue correction concern disjoint cells. Their sum is therefore both achievable and minimal.

## Complexity detail

The four-cell groups and the possible middle pairs cover $O(mn)$ cells, each with constant work. The running time is $O(mn)$. Only counters and indices are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over residues:** Treat every symmetry orbit as a choice and keep minimum costs for residues modulo $4$. This is correct and still linear, but the orbit-size argument reduces the four-state DP to a few counters.
- **Repeated row or column reversal:** Reconstructing reflections while visiting every orbit preserves correctness but introduces avoidable superlinear copying.
- **Make rows palindromic first:** Independent row repairs can conflict with column symmetry; both reflections must be considered together as one orbit.
- A four-cell group containing exactly two ones costs two flips regardless of its chosen final bit.
- A mismatched middle pair supplies the needed modulo-$4$ choice at no cost beyond its mandatory one flip.
- With no mismatched middle pair, an odd number of matched `11` pairs requires exactly two extra flips.
- The unique center of an odd-by-odd grid must finish as `0`.
- A single-cell `0` grid is already valid, while a single-cell `1` grid requires one flip.
- One-row and one-column grids contain only middle pairs and possibly a center, so the same residue reasoning still applies.
- Rectangular grids use the same orbit structure; the dimensions need not be equal.
