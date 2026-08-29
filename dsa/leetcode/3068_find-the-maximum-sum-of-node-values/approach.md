## General

**Reduce edge operations to an even-parity choice of nodes.** Applying an edge operation toggles exactly its two endpoints with XOR $k$. Repeating the same edge twice cancels because

$$
(x\mathbin{\mathrm{XOR}}k)\mathbin{\mathrm{XOR}}k=x.
$$

Only whether each edge is used an odd or even number of times matters. Every operation changes the toggle parity of two nodes, so the total number of nodes toggled an odd number of times must be even.

**Why every even node subset is reachable in a connected tree.** Pair the desired toggled nodes arbitrarily. For each pair, apply the operation on every edge along their unique tree path. The two path endpoints are toggled once; every internal path node is incident to two chosen edges and is toggled twice, canceling. Combining paths realizes the desired even subset, with repeated edge uses canceling by parity.

Therefore the actual tree shape no longer affects optimization. This is why the exact source never reads `edges`: its only needed fact is the guarantee that the graph is connected.

**Dynamic programming over toggle parity.** After processing some prefix of `nums`:

- `f0` is the maximum sum with an even number of toggled nodes;
- `f1` is the maximum sum with an odd number.

Initially, selecting no nodes gives even sum zero, so `f0=0`. An odd selection is impossible before processing any value, so `f1=-inf`.

For current value $x$, leaving it unchanged preserves parity and adds $x$. Toggling it changes parity and adds $x\mathbin{\mathrm{XOR}}k$.

The new even state is the better of:

$$
\text{old }f_0+x
\quad\text{and}\quad
\text{old }f_1+(x\mathbin{\mathrm{XOR}}k).
$$

The new odd state is the better of:

$$
\text{old }f_1+x
\quad\text{and}\quad
\text{old }f_0+(x\mathbin{\mathrm{XOR}}k).
$$

The simultaneous assignment in Python evaluates both right-hand sides using the old states, preventing the current node from being processed twice.

**Return only the even state.** A reachable edge-operation result must toggle an even number of nodes, so `f0` is the answer after all values. `f1` is maintained only as an intermediate state that may become even when a later node is toggled.

**A trace.** For `nums=[1,2,1]` and $k=3$, each XOR alternative is `[2,1,2]`. Individually choosing the better value would toggle nodes 0 and 2, already an even count, giving total 6. The DP discovers the same selection through parity transitions.

**Relation to the “repair smallest loss” explanation.** Another derivation chooses the better of $x$ and $x\oplus k$ independently, then repairs parity if an odd number of toggles were chosen. The exact source does not explicitly calculate gains or a repair loss; it performs a two-state parity DP. Both express the same constraint, but documentation should follow the executed recurrence.
After each processed prefix, `f0` and `f1` are maxima over all toggle choices of the corresponding parity. For the next node, every choice either keeps or flips parity, and the transitions enumerate both possibilities. Induction proves the final even maximum is optimal over exactly the reachable subsets.

## Complexity detail

The loop visits $N$ node values once and performs constant arithmetic per value, giving $O(N)$ time.

Only two DP scalars are retained, so auxiliary space is $O(1)$. The input arrays are not modified. `edges` is unused, but omitting it from the processing is justified by the connected-tree parity proof.

Python integers safely hold the total sum under the stated constraints.

## Alternatives and edge cases

- **Independent greedy plus parity repair:** Sum each node's better state and, if toggle count is odd, subtract the smallest absolute gain. It also achieves $O(N)$ time and $O(1)$ space.
- **Tree DP:** Tracking toggle choices per subtree works but stores unnecessary structural state because any even subset is reachable globally.
- **Enumerate edge subsets:** There are exponentially many, and many produce the same node parity pattern.
- **No beneficial XOR values:** Keeping every node yields the original sum with even zero toggles.
- **Exactly one beneficial toggle:** It cannot be chosen alone; the DP compares pairing it with another toggle against leaving it unchanged.
- **Tied original and XOR values:** Either choice has the same contribution, and parity state keeps whichever is useful.
- **Two-node tree:** The only nontrivial operation toggles both nodes, matching the even-subset rule.
- **Edges unused:** This is intentional for any connected tree, not an accidental omission.
- **Disconnected graph:** The global even-subset claim would change to even parity per component, but the contract guarantees a tree.
- **Simultaneous assignment:** Both new states must use old `f0` and `f1`.
- **Why negative infinity is essential:** Initializing the impossible odd state to zero would allow transitions from a nonexistent selection and could fabricate an invalid high sum.
- **Repeated edge operations:** Only parity matters; applying an edge any even number of times has no net effect, so unrestricted operation count does not create states beyond even node subsets.
