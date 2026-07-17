# Fancy Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1622 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Design, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fancy-sequence/) |

## Problem Description
### Goal
Implement a mutable `Fancy` sequence that starts empty. `append(val)` places a new value at the end. `addAll(inc)` adds `inc` to every value already present, and `multAll(m)` multiplies every value already present by `m`. Operations performed before an append do not affect the newly appended value.

`getIndex(idx)` returns the current zero-based value at `idx`, reduced modulo $10^9+7$; it returns `-1` when `idx` is outside the sequence. At most $10^5$ total method calls are made, so operations that rewrite every stored value cannot meet the required scaling.

### Function Contract
**Inputs**

- `operations`: a source-native trace beginning with `Fancy`, followed by method names `append`, `addAll`, `multAll`, or `getIndex`.
- `arguments`: one argument list for each operation. Constructor arguments are empty; other values satisfy $1 \le \texttt{val},\texttt{inc},m \le 100$, and $0 \le \texttt{idx} \le 10^5$.
- Let $Q \le 10^5$ be the number of trace operations, $A$ the number of appended values, and $M=10^9+7$.

**Return value**

Return the trace result list: `null` for construction and mutating calls, the current residue for a valid `getIndex`, and `-1` for an out-of-range index.

### Examples
**Example 1**

- Input: `operations = ["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]`, `arguments = [[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]`
- Output: `[null,null,null,null,null,10,null,null,null,26,34,20]`

**Example 2**

- Input: `operations = ["Fancy","getIndex"]`, `arguments = [[],[0]]`
- Output: `[null,-1]`

**Example 3**

- Input: `operations = ["Fancy","addAll","append","getIndex"]`, `arguments = [[],[5],[2],[0]]`
- Output: `[null,null,null,2]`

### Required Complexity
- **Time:** $O(Q\log M)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Represent all past bulk operations as one affine transform.** Store each appended item in a normalized form `base`. Maintain `multiplier` and `increment` so its current value is

$$
(\texttt{base}\cdot\texttt{multiplier}+\texttt{increment})\bmod M.
$$

Initially the transform is the identity. Because every legal multiplier $m$ is between 1 and 100 and $M$ is prime, `multiplier` is always invertible modulo $M$.

**Normalize new values against only future operations.** A newly appended `val` must appear as `val` now, without inheriting earlier bulk updates. Store `(val - increment) * inverse_multiplier mod M`. Applying the current affine transform to that base recovers `val`. Later bulk updates modify the shared transform and therefore affect this value along with all earlier values.

**Compose additions and multiplications.** `addAll(inc)` adds `inc` to the global increment. `multAll(m)` multiplies both global affine coefficients by `m`. It also multiplies `inverse_multiplier` by $m^{-1}\bmod M$, found with Fermat's little theorem. `getIndex` checks the boundary and applies the current affine transform to the stored base in constant time.

Every mutating operation composes exactly the transformation prescribed for all values that exist at that moment. Append algebraically cancels the accumulated transform, so earlier operations do not leak onto new items. Induction over the operation trace therefore gives the exact current residue at every valid index.

#### Complexity detail

`append`, `addAll`, and `getIndex` use $O(1)$ arithmetic. `multAll` performs modular exponentiation in $O(\log M)$ time, so $Q$ calls take $O(Q\log M)$ in the worst case. The normalized array stores one value per append, using $O(A)$ space.

#### Alternatives and edge cases

- **Rewrite the entire array:** Apply every addition or multiplication directly to all stored values. This is correct but can take $O(Q^2)$ total time.
- **Lazy segment tree:** Range-affine updates and point queries work in $O(\log A)$ per operation, but the global-update-only contract makes a single affine transform simpler.
- **Store operation histories per value:** Replaying later updates during `getIndex` shifts the quadratic risk to queries and requires extensive bookkeeping.
- Bulk operations on an empty sequence have no effect on values appended later.
- `getIndex(len(sequence))` is out of range and returns `-1`.
- Reduction modulo $M$ is required after chained additions and multiplications.
- The contract's positive `m` guarantee is essential: multiplication by zero would make the affine multiplier non-invertible and require epoch-reset handling.

</details>
