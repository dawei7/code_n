## General

**Forward search branches, but backward search is almost forced**

From `(x, y)`, one move produces either `(x, x + y)` or `(x + y, y)`. A forward search has two choices at every point, and coordinates can grow toward $10^9$, so enumerating descendants is impractical.

Work backward from `(tx, ty)` instead. All coordinates are positive. If `tx > ty`, the last forward move could only have added `ty` to the first coordinate, so the preceding point must be `(tx - ty, ty)`. The other operation would have made the second coordinate larger, contrary to `tx > ty`.

Similarly, if `ty > tx`, the unique possible parent is `(tx, ty - tx)`. This turns a branching forward process into a deterministic reverse process.

**Bundle repeated subtractions with modulo**

Repeatedly subtracting the smaller coordinate is correct but can be too slow. If `tx` is much larger than `ty`, several reverse steps will keep `ty` fixed:

`tx, tx - ty, tx - 2 * ty, ...`.

Modulo performs all those subtractions at once. Therefore:

- When `tx > ty`, replace `tx` with `tx % ty`.
- When `ty > tx`, replace `ty` with `ty % tx`.

This is the same acceleration used by the Euclidean algorithm.

**Why the main loop keeps both coordinates strictly above the start**

The loop continues only while `tx > sx` and `ty > sy` and the target coordinates differ. While both are still above their respective starting values, bundling all possible same-direction reverse steps cannot skip the only remaining form of a solution that must be checked separately.

Once one target coordinate equals its starting coordinate, that coordinate must remain fixed for the rest of the forward journey. Applying modulo again could jump below the boundary or to zero and lose the information needed to test how many repeated additions remain.

The loop also stops if `tx == ty`. For equal positive coordinates, subtracting one from the other would make a coordinate zero. Positive starting coordinates cannot reach such a parent. Equality is useful only if the complete target already equals the start, which is tested afterward.

**Understand the fixed-coordinate finish**

Suppose reverse reduction stops with `tx == sx`. The first coordinate has reached its required starting value. From this point, a valid forward suffix cannot use the operation that increases `x`, because coordinates never decrease in forward time and `x` would overshoot `tx`.

The only remaining operation keeps `x` fixed and adds it to `y`:

$$
(sx, y) \longrightarrow (sx, y + sx).
$$

After some nonnegative number `q` of such operations,

$$
ty = sy + q \cdot sx.
$$

The exact equality case `ty == sy` was already handled. Otherwise a valid positive number of remaining steps exists exactly when `ty > sy` and `(ty - sy) % tx == 0`. Since `tx == sx` in this branch, using `tx` as the divisor is the same condition.

The symmetric case `ty == sy` requires `tx > sx` and `(tx - sx) % ty == 0`.

**Why the other stopped states are impossible**

If neither target coordinate equals its corresponding start coordinate after the loop, no valid fixed-coordinate suffix exists.

One coordinate may have fallen below its starting boundary because a modulo produced a small remainder. Forward operations never decrease coordinates, so such a point cannot be the start's descendant.

Alternatively, coordinates may be equal while they are not the exact start. As explained above, their only reverse subtraction would create zero, so there is no positive-coordinate ancestor continuing toward the given start.

The final `False` covers all these cases.

**Trace a reachable example**

For `(sx, sy) = (1, 1)` and `(tx, ty) = (3, 5)`, both target coordinates exceed the start and `ty > tx`, so reverse reduction makes `ty = 5 % 3 = 2`.

Now `tx > ty`, so `tx = 3 % 2 = 1`. The main loop stops because `tx == sx`.

The remaining difference is `ty - sy = 2 - 1 = 1`, which is divisible by `tx = 1`. Thus the method returns true. Reversing these parent steps corresponds to the valid forward chain `(1,1) -> (1,2) -> (3,2) -> (3,5)`.

**Trace an unreachable equal target**

For start `(1,1)` and target `(2,2)`, the main loop does not perform modulo because `tx == ty`. The point is not exactly the start, neither coordinate is paired with the other correct start coordinate in a valid finish, and the method returns false.

**Why modulo preserves reachability during the loop**

Assume `tx > ty` while both coordinates remain above their starting bounds. Every possible parent must repeatedly subtract the unchanged `ty` from `tx` until the ordering changes or the first coordinate approaches its boundary. All intermediate first coordinates are congruent to `tx` modulo `ty`.

Replacing `tx` by the remainder reaches the endpoint of precisely this forced run of parents in one operation. It neither chooses among multiple parents nor removes a possible alternative route. The symmetric argument applies when `ty > tx`.

Consequently the loop preserves whether the start is an ancestor. The exact-match and divisibility finish checks characterize all cases where batching must stop at a starting boundary, so the returned Boolean is correct.

## Complexity detail

Each loop iteration performs the larger coordinate modulo the smaller coordinate, matching Euclid's algorithm. The coordinate scale decreases geometrically over successive iterations in the standard amortized analysis, giving $O(\log(\max(tx, ty)))$ time under constant-time integer arithmetic.

The algorithm mutates four scalar parameters and allocates no collection or recursion stack. Its auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Repeated reverse subtraction:** It follows the same unique-parent proof, but cases such as a huge `tx` with small `ty` can require nearly $10^9$ iterations.

- **Forward breadth-first or depth-first search:** Each point has two children and the reachable tree grows too quickly for the coordinate limits.

- **Memoized forward search:** Avoiding duplicate states does not solve the enormous two-dimensional search-space problem.

- **Start equals target:** The post-loop exact equality check returns true without requiring an operation.

- **One coordinate reaches its start first:** Use divisibility to represent all remaining identical additions instead of applying another modulo.

- **Modulo remainder zero:** Zero is below every valid positive start coordinate, so the loop stops and the final checks correctly reject it unless an earlier boundary case already proved reachability.

- **Equal target coordinates:** They cannot be reversed while remaining positive, unless the entire point is already the start.

- **Target coordinate below start:** Forward moves only increase one coordinate and never decrease either, so the final result is false.

- **Strict inequality in finish checks:** The zero-step equality case is handled first; `ty > sy` or `tx > sx` ensures the divisibility branches represent at least one remaining move.
