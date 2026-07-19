## General
**Identify the current level's numeric range.** A label $x$ at zero-based depth $h=\lfloor\log_2 x\rfloor$ belongs to the ordinary row range

$$
[2^h,\;2^{h+1}-1].
$$

Zigzag ordering reverses positions on alternating rows, but the same labels remain in that range.

**Mirror before moving to the parent.** Within a row whose endpoints are `start` and `end`, the mirror of `x` is `start + end - x`. In ordinary left-to-right labelling, the mirrored node's parent is obtained by integer division by two. Therefore the zigzag parent is computed directly as `label = (start + end - label) // 2`.

**Climb and reverse.** Append the current label, replace it by its zigzag parent, and repeat until the root has been appended. This produces the path from target to root; reversing it gives the requested order.

Mirroring maps the displayed zigzag position to the corresponding ordinary-tree label at the same position. Ordinary integer division then selects exactly that position's parent. Applying this transformation at every depth follows the unique tree edges to the root, so reversing the collected labels yields precisely the root-to-target path.

## Complexity detail
Each parent step decreases the depth by one, so there are $d+1=O(\log L)$ iterations. The returned path stores one label per level and therefore uses $O(\log L)$ space; all other state is constant-size.

## Alternatives and edge cases
- **Materialize labelled rows:** Building every row through the target preserves tree positions but costs $O(L)$ time and space.
- **Convert the entire path to ordinary labels:** Mirror the target based on row parity, compute ordinary ancestors, then mirror selected levels back; it has the same asymptotic complexity but more parity bookkeeping.
- **Root label:** For `label = 1`, the loop records only `[1]`.
- **Level endpoints:** The leftmost and rightmost numeric labels mirror to one another, so both powers of two and values just below them test the formula's boundaries.
- **Alternating direction:** The endpoint-sum formula works on every row without a separate odd/even branch.
