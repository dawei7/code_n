## General

**Reduce the strings to mismatch positions.** An index whose two characters already agree never needs to be considered directly. Record the increasing positions

$$
p_0,p_1,\ldots,p_{m-1}
$$

where `s1` and `s2` differ. Every allowed operation flips two characters, so the parity of $m$ never changes. An odd mismatch count is therefore impossible, while $m=0$ already has cost zero.

**Interpret adjacent flips as pairing positions.** Two mismatches at positions $p_i<p_j$ can be eliminated with adjacent-pair operations for cost $p_j-p_i$: successive flips move a mismatch boundary along the string until it meets the other one. The arbitrary-pair operation instead connects any two mismatch positions for cost `x`.

Use doubled costs so an endpoint assigned to a future arbitrary-pair operation can contribute `x` now—half of the eventual cost after division by two. Let $F_k$ be the minimum doubled cost for the first $k$ mismatch positions under this accounting. Set $F_0=0$ and $F_1=x$. For $k\ge2$, the newest mismatch has two relevant possibilities:

$$
F_k = \min\left(
F_{k-1}+x,
F_{k-2}+2(p_{k-1}-p_{k-2})
\right).
$$

The first transition assigns another endpoint half of an arbitrary operation's cost. Because the final mismatch count is even and arbitrary endpoints may be paired regardless of distance, these halves combine into valid cost-`x` operations. The second transition pairs the last two positions with adjacent flips and doubles that real cost to stay in the same units.

For adjacent operations on a line, crossing or skipping a still-unresolved mismatch cannot improve a pairing; the endpoints can be uncrossed without increasing total distance. Thus it is sufficient for the adjacent transition to use the last two ordered mismatches. The recurrence considers every optimal final choice, and the requested answer is $F_m/2$.

## Complexity detail

Scanning the strings, collecting mismatch positions, and evaluating the recurrence each take $O(n)$ time. The mismatch list can contain $O(n)$ positions, while only two DP values are retained, so the total auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Full prefix or interval DP:** Recomputing optimal values for every subproblem can model the same choices but takes $O(n^2)$ time and space without improving the result.
- **Always use arbitrary pairs:** This misses cheap nearby mismatches that adjacent flips can eliminate for much less than `x`.
- **Greedily pair the closest mismatches:** A locally shortest gap can interfere with neighboring choices; the DP is needed to compare the resulting global costs.
- **Odd mismatch count:** No sequence of two-bit flips can change odd parity to zero, so the answer is `-1`.
- **Identical strings:** An empty mismatch list returns `0` before the DP initialization is used.
- **Exactly two mismatches:** The recurrence chooses between one arbitrary operation and the adjacent-flip distance, including the special case of neighboring indices.
