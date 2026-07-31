## General

**The operation preserves every bit inventory.** Fix one bit position and inspect that bit in the chosen pair. AND and OR transform `00` into `00`, `01` or `10` into `01`, and `11` into `11`. The number of set occurrences at that bit is therefore unchanged. Repeated operations can move those occurrences among array elements, but cannot create or destroy them.

Count how many input values contain each bit. The optimization can now be viewed as distributing each bit's conserved copies among the selected values, with at most one copy of a bit per value.

**Square convexity rewards concentration.** Suppose $A\ge B$, a bit of value $w$ is absent from $A$, and that bit is present in $B$. Moving the occurrence from $B$ to $A$ changes the two-square total by

$$
(A+w)^2+(B-w)^2-A^2-B^2
=2w(A-B)+2w^2>0.
$$

Thus an optimal arrangement stacks available bits onto already-large values instead of spreading them evenly. For each of the `k` values in order, take one remaining copy of every bit that is still available. Equivalently, a bit with count $c$ belongs to the first $\min(c,k)$ constructed values. Their set-bit collections are nested, producing the most concentrated reachable distribution.

The AND/OR operation can realize this redistribution: whenever a desired recipient lacks a bit held by another element, using the recipient as the OR side transfers that bit while the AND side retains exactly the bits common to both. Since the per-bit counts match, repeated transfers reach the greedy inventories.

Square each constructed value, add it to the answer modulo $10^9+7$, and decrement every bit occurrence used for that value.

## Complexity detail

There are $O(\log V)$ relevant bit positions. Counting inventories costs $O(n\log V)$ time, and constructing `k` values costs $O(k\log V)$. Because $k\le n$, the total is $O(n\log V)$ time. The bit-count array uses $O(\log V)$ auxiliary space.

## Alternatives and edge cases

- **Simulate transfers among source elements:** Repeatedly scanning all array elements to assemble each selected value is correct but can take $O(kn\log V)$ time.
- **Sort the original numbers:** Their initial numeric order does not capture the better values reachable by moving individual bit occurrences.
- **Spread each bit evenly:** This works against the convex square objective; aligning bits in the same values yields a greater or equal total.
- **Choose one element:** All available distinct bit positions can be concentrated into that single selected value.
- **Choose all elements:** Operations may still improve the sum by creating large values and zeros, even though every final element is selected.
- **Modulo arithmetic:** Construct and square the full integer value, then reduce each accumulated contribution modulo $10^9+7$.
