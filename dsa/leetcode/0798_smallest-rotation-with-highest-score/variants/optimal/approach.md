## General

**Follow one element across every rotation**

Let an element `v = nums[i]` start at index `i` in an array of length `n`. After a left rotation by `k`, its new index is:

$$
j(k)=(i-k+n)\bmod n.
$$

The element contributes one point exactly when:

$$
v \le j(k).
$$

Computing this condition for every pair of element and rotation would cost $O(n^2)$. The optimization is to describe, for each element, the whole interval of rotations where it scores and add all intervals with a difference array.

**Understand how the new index changes**

As `k` increases by one, the element's new index decreases by one. When it would go below zero, it wraps to `n-1`.

For a positive value `v`, the element is good while its index runs through:

`n-1, n-2, ..., v`.

It is bad while its index is:

`v-1, v-2, ..., 0`.

Thus its scoring rotations form one consecutive interval on the circular rotation axis.

**Find where the good circular interval begins**

At rotation `k = i`, the element has moved to index zero. At the next rotation it wraps to index `n-1`, which is always at least `v` because `v < n`.

Therefore the first rotation in its good interval is:

$$
l=(i+1)\bmod n.
$$

This is the code's `l`.

**Find where the interval stops**

Starting from new index `n-1` at rotation `l`, the element remains good until its index has fallen through `v`. The following rotation gives new index `v-1` and becomes bad.

Solving for that rotation gives:

$$
r=(i+1-v)\bmod n.
$$

The implementation writes an equivalent nonnegative expression:

`r = (n + i + 1 - v) % n`.

The element therefore scores on the half-open circular interval `[l,r)`.

**Special case `v = 0`**

Zero is no greater than any array index, so a zero-valued element scores for every rotation.

The formulas give `l == r`, representing a full circular interval rather than an empty scoring set. Since this element contributes the same one point to every candidate rotation, it cannot affect which rotation is best. The difference representation deliberately records no change for it.

Ignoring a constant contribution to all candidates is safe when only the maximizing index is requested.

**Record interval changes in `d`**

For each element, the code applies:

`d[l] += 1`

and:

`d[r] -= 1`.

For an ordinary nonwrapping interval with `l < r`, prefix sums gain one from `l` through `r-1` and return to the prior level at `r`. This is the usual difference-array range addition.

A circular interval may wrap through rotation zero, producing `l > r`. A conventional range update would add one to `[l,n)` and `[0,r)`. The exact code omits the extra initial baseline. Its prefix contribution is instead negative one on the bad complement `[r,l)` and zero on the good wrapped interval.

That representation differs from the true zero/one contribution by negative one at every rotation—a constant offset for this element. Constants do not change the maximizing rotation.

**Why all prefix sums represent scores up to one global constant**

Each element contributes one of three difference patterns:

- A nonwrapping good interval contributes its exact indicator: one when good and zero when bad.
- A wrapping good interval contributes its exact indicator minus one everywhere.
- A zero-valued always-good element contributes zero, also its exact indicator minus one everywhere.

After summing all elements:

$$
s(k)=\operatorname{score}(k)-C,
$$

where `C` is the number of element intervals represented with the constant-minus-one form. `C` does not depend on `k`.

Therefore:

$$
\arg\max_k s(k)=\arg\max_k \operatorname{score}(k).
$$

The algorithm can compare `s` values without ever reconstructing the discarded baseline.

**Build every shifted score with a prefix sum**

The second loop scans `d` from rotation zero upward. Running value `s` accumulates:

`s += d[k]`.

After that update, `s` is the shifted score for rotation `k`. All $n$ rotation scores are obtained in one pass.

The difference entries sum to zero because every element adds one and subtracts one. Hence the final running value is zero, so at least one scanned `s` is nonnegative. Initialization `mx = -1` is therefore safely improved, and `ans` cannot remain at its temporary value `n`.

**Choose the smallest index among ties**

Rotations are scanned in increasing order. The code updates the answer only when:

`s > mx`.

It deliberately does not update on equality. Once the first rotation with a particular maximum is stored, later tied rotations leave it unchanged. This implements the required smallest-index tie break automatically.

**Trace one element**

Let `n = 5`, `i = 0`, and `v = 2`. Its new indices for rotations zero through four are:

`0, 4, 3, 2, 1`.

It scores at rotations one, two, and three. The formulas give `l = 1` and `r = 4`, so adding one on half-open interval `[1,4)` is exact.

If instead `i = 3` and `v = 2`, the good interval may wrap around rotation zero. The difference contribution uses zero on the wrapped good part and negative one on its bad complement. Although values are shifted, comparisons with other rotations remain correct.


For every element, the derived circular interval contains exactly the rotations where its new index is at least its value. Difference updates encode that indicator either exactly or with an element-wide constant removed.

Prefix sums therefore equal actual total scores minus one rotation-independent constant. Maximizers are unchanged. The ascending scan records the first strictly best shifted score, so it returns the smallest rotation having the true maximum score.

## Complexity detail

The first pass processes each of the $n$ elements once and performs constant arithmetic and two difference updates. The second pass takes $O(n)$ time to recover all shifted scores. Total time is $O(n)$.

The difference array has length $n$, requiring $O(n)$ auxiliary space. All other state is scalar.

## Alternatives and edge cases

- **Recompute every score:** Applying each of $n$ rotations to all $n$ elements costs $O(n^2)$ time.

- **Explicit circular range updates:** Add the missing baseline for wrapped intervals and initialize the score exactly. It is easier to interpret numerically but not necessary for finding the argmax.

- **Event sweep from rotation zero's actual score:** Compute score zero, then record which elements gain or lose as rotation advances. This gives another $O(n)$ difference formulation.

- **Value zero:** It scores for every rotation and is safely omitted as a constant.

- **Value `n - 1`:** It scores only when placed at the final index, so its good interval has length one.

- **Wrapped interval:** The exact difference representation may be negative on the complement, but only a global score offset is removed.

- **All rotations tied:** Strict-improvement updates preserve answer zero.

- **Single-element array:** Its value must be zero, the difference sum is zero, and rotation zero is returned.

- **Temporary answer `n`:** The zero final prefix sum guarantees some rotation improves `mx = -1`.
