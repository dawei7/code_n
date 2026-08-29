## General

Computer zero is the only initially unlocked computer. The decisive question is whether its complexity is strictly smaller than every other computer’s complexity.

- If yes, computer zero can directly unlock every other computer, so they may appear in any order.
- If no, at least one minimum-complexity non-root computer can never be unlocked, so no complete order exists.

This turns an apparently dependency-heavy permutation problem into one linear check plus a factorial.

**Why every later complexity must exceed complexity[0]**

To unlock computer `i>0`, some already unlocked computer `j` must satisfy both:

$$
j<i
\quad\text{and}\quad
complexity[j] < complexity[i].
$$

Suppose some non-root computer has complexity at most `complexity[0]`. Consider a non-root computer with globally minimum complexity among all such problematic computers and, more broadly, among the array’s minimum values.

If its complexity is below the root’s, no computer has a strictly smaller complexity available anywhere, so it cannot be unlocked.

If its complexity equals the root’s and this is the global minimum, computer zero is not strictly lower, and no other computer is strictly lower either. It also cannot be unlocked.

Index restrictions cannot rescue either case; they only reduce the possible helpers further. Therefore the existence of any later value `<= complexity[0]` implies answer zero.

The source detects exactly this condition during the loop and returns immediately.

**Why the condition is sufficient**

Now suppose every `complexity[i]` for `i>0` is strictly greater than `complexity[0]`.

For every such computer:

- helper computer zero has label `0<i`;
- its complexity is strictly lower;
- it is already decrypted from the beginning.

So every non-root computer is eligible immediately, independently of which other computers have been unlocked. No dependency among computers one through `n-1` remains.

**Counting valid orders**

Computer zero must be the initially unlocked root, so it occupies the first position in every represented unlocking order. The remaining `n-1` distinct labels can be arranged arbitrarily.

The number of orders is

$$
(n-1)!.
$$

The source initializes `ans=1` and, for loop indices `i=1` through `n-1`, multiplies `ans` by `i`. The product is exactly `1\cdot2\cdots(n-1)`.

Modulo `10^9+7` is applied after every multiplication. The identity

$$
(ab)\bmod M
= ((a\bmod M)(b\bmod M))\bmod M
$$

ensures this produces the required factorial residue without building the enormous exact factorial.

**Why the permutation does not mean “whatever is first becomes root”**

The note fixes computer label zero as the decrypted root. It is not merely the first arbitrary element of a proposed permutation.

This is why the count is `(n-1)!` rather than `n!`: zero is fixed first, and only the other labels are permuted.

**Example**

For `complexity=[1,2,3]`, root complexity one is strictly smallest. Both computers one and two can use computer zero immediately. The remaining labels can appear as `[1,2]` or `[2,1]`, giving two orders.

For `[3,3,3,4,4,4]`, computer one has complexity equal to the root. No lower-complexity computer exists to unlock it, so a complete order is impossible and the source returns zero.

**Why no detailed dependency graph is needed**

The rule permits **any** lower-index, lower-complexity unlocked helper. Once root zero is strictly lower than everyone, it is a universal helper satisfying the index condition for all labels. If root zero is not uniquely smallest, a global-minimum problematic node has no possible lower-complexity chain.

These two cases are exhaustive, so sorting, graph construction, and topological-order counting are unnecessary.

## Complexity detail

The loop visits each non-root complexity once. It performs a comparison and, if valid, one modular multiplication. Time complexity is `O(n)`.

Only `mod`, `ans`, and the loop index are stored. Auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Sort by complexity:** Sorting can reveal whether the root is uniquely smallest, but costs `O(n\log n)` and loses the simplicity of a direct scan.
- **Build dependency edges:** Explicitly connecting each computer to eligible helpers can create quadratic work. The root-minimum observation makes the graph unnecessary.
- **Topological permutation DP:** General dependency-order counting is difficult, but this instance collapses to either no order or all orders of the non-root labels.
- **Root tied for minimum:** Strict inequality is required, so any later equal minimum makes the answer zero.
- **A later value below the root:** Some global-minimum non-root computer has no lower-complexity helper and blocks all complete permutations.
- **Root uniquely smallest:** Every later computer is available from the start, even if their complexities are equal to one another.
- **Later duplicate complexities:** They do not conflict when all exceed the root; each can independently use computer zero.
- **Index condition:** Root label zero is less than every non-root label, which is why it serves universally.
- **Smallest valid n:** With two computers and a valid root minimum, `(n-1)!=1`, so only order `[0,1]` exists.
- **Early failure:** Returning on the first bad complexity is safe because one impossible computer already prevents a full permutation.
- **Modulo:** Applying it incrementally preserves the factorial residue and bounds intermediate values.
- **Computer zero fixed first:** It is pre-unlocked by label, not chosen dynamically from the permutation.
- **Unique passwords:** Password identity does not alter the count; only complexity comparisons and labels matter.
