## General
**Represent all past bulk operations as one affine transform.** Store each appended item in a normalized form `base`. Maintain `multiplier` and `increment` so its current value is

$$
(\texttt{base}\cdot\texttt{multiplier}+\texttt{increment})\bmod M.
$$

Initially the transform is the identity. Because every legal multiplier $m$ is between 1 and 100 and $M$ is prime, `multiplier` is always invertible modulo $M$.

**Normalize new values against only future operations.** A newly appended `val` must appear as `val` now, without inheriting earlier bulk updates. Store `(val - increment) * inverse_multiplier mod M`. Applying the current affine transform to that base recovers `val`. Later bulk updates modify the shared transform and therefore affect this value along with all earlier values.

**Compose additions and multiplications.** `addAll(inc)` adds `inc` to the global increment. `multAll(m)` multiplies both global affine coefficients by `m`. It also multiplies `inverse_multiplier` by $m^{-1}\bmod M$, found with Fermat's little theorem. `getIndex` checks the boundary and applies the current affine transform to the stored base in constant time.

Every mutating operation composes exactly the transformation prescribed for all values that exist at that moment. Append algebraically cancels the accumulated transform, so earlier operations do not leak onto new items. Induction over the operation trace therefore gives the exact current residue at every valid index.

## Complexity detail
`append`, `addAll`, and `getIndex` use $O(1)$ arithmetic. `multAll` performs modular exponentiation in $O(\log M)$ time, so $Q$ calls take $O(Q\log M)$ in the worst case. The normalized array stores one value per append, using $O(A)$ space.

## Alternatives and edge cases
- **Rewrite the entire array:** Apply every addition or multiplication directly to all stored values. This is correct but can take $O(Q^2)$ total time.
- **Lazy segment tree:** Range-affine updates and point queries work in $O(\log A)$ per operation, but the global-update-only contract makes a single affine transform simpler.
- **Store operation histories per value:** Replaying later updates during `getIndex` shifts the quadratic risk to queries and requires extensive bookkeeping.
- Bulk operations on an empty sequence have no effect on values appended later.
- `getIndex(len(sequence))` is out of range and returns `-1`.
- Reduction modulo $M$ is required after chained additions and multiplications.
- The contract's positive `m` guarantee is essential: multiplication by zero would make the affine multiplier non-invertible and require epoch-reset handling.
