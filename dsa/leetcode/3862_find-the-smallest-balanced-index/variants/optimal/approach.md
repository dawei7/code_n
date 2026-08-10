## General

**Maintain the two quantities on opposite sides of the index**

For index `i`, define

$$
L_i=\sum_{j=0}^{i-1}\texttt{nums}[j]
$$

and

$$
R_i=\prod_{j=i+1}^{N-1}\texttt{nums}[j].
$$

The current element `nums[i]` belongs to neither side. The empty left sum at index zero is zero, while the empty right product at the last index is one.

The source scans from right to left. It begins with `s = sum(nums)` and `p = 1`. Before checking an index `i`, it subtracts `nums[i]` from `s`. At that moment:

- `s` is the sum of elements strictly left of `i`, so `s=L_i`; and
- `p` is the product of elements strictly right of `i`, so `p=R_i`.

It can therefore test the balance condition directly with `if s == p`.

After the test, `p *= nums[i]` prepares the product for the next index to the left. At index `i-1`, the elements strictly to the right begin with `nums[i]`, so the updated product is exactly `R_{i-1}`. Subtracting the next current value similarly updates the left sum.

**Why scanning from the right still returns the smallest index**

The method returns immediately when it finds a balanced index, which would normally make a right-to-left traversal return the largest matching index. Here the positivity constraint proves that there can be at most one balanced index.

As the index moves from left to right, the left sum strictly increases:

$$
L_{i+1}=L_i+\texttt{nums}[i]>L_i,
$$

because every array value is positive.

The right product is nonincreasing:

$$
R_i=\texttt{nums}[i+1]\cdot R_{i+1}\ge R_{i+1},
$$

because each factor is at least one.

Suppose two indices `i<j` were both balanced. Then `L_i<L_j`, while `R_i\ge R_j`. Equalities `L_i=R_i` and `L_j=R_j` would imply `L_i\ge L_j`, a contradiction. Thus zero or one balanced index exists. If the reverse scan finds one, it is automatically both the smallest and largest balanced index.

**Why the early break is safe**

After testing index `i`, the source multiplies `p` by `nums[i]`. This updated `p` is the right product for the next index `i-1`. It then checks `if p >= s: break`, where the current `s` is still `L_i`.

For any future index `j<i`:

- its left sum `L_j` is strictly smaller than `L_i=s` because at least one positive element is removed from the left-sum prefix; and
- its right product `R_j` is at least the updated `p` because it contains all factors already in `p` and possibly additional factors, each at least one.

Therefore, if

$$
p\ge s,
$$

then every future index satisfies

$$
R_j\ge p\ge s>L_j.
$$

Equality is impossible for all remaining indices, so terminating the loop cannot skip an answer. This is more than a performance heuristic; it is a consequence of positive inputs. If zero or negative values were allowed, products could decrease or change sign and this break would not be valid.

**Loop invariant**

At the point immediately after `s -= nums[i]` and before comparison:

- `s=L_i`;
- `p=R_i`;
- every index greater than `i` has already been checked and is not balanced; and
- if the loop has not broken, no monotonic dominance condition has yet ruled out all remaining indices.

The initialization works at `i=N-1`: subtracting the last value leaves the sum of all earlier elements, and `p=1` is the empty right product. The update steps transform the state exactly for `i-1`. Returning on equality identifies the unique answer. Breaking uses the dominance proof above. Exhausting the loop means every possible index was checked or safely ruled out, so minus one is correct.

**Trace the second example**

For `nums=[2,8,2,2,5]`, the scan begins at index four with right product one and left sum fourteen. They differ. Multiplying by five prepares the right product for index three. At index three, the left sum is twelve and the right product is five. After incorporating `nums[3]=2`, the next right product becomes ten.

At index two, subtracting the current two leaves `s=10`, while `p=10` represents `2\cdot5` to its right. Equality holds, so index two is returned.

For a one-element array, subtracting the sole value gives left sum zero and the initialized right product is one. They are unequal. After multiplication, the break condition holds, and the method returns minus one, matching the empty-sum and empty-product definitions.

**Why the product does not need a suffix array**

A suffix-product array would allow constant-time `R_i` lookup but require `O(N)` additional storage. The reverse traversal naturally accumulates the same product in one scalar. Similarly, subtracting from the total sum avoids a prefix-sum array.

The early break also prevents the Python product from growing through the entire array once it is already too large to meet any remaining left sum. The source does not cap the product to a sentinel value; it stops because further exact products are unnecessary.

## Complexity detail

Computing `sum(nums)` takes `O(N)` time. The reverse loop performs at most `N` iterations, each with constant-many arithmetic operations, so total time is `O(N)` under the standard unit-cost integer model. Early termination can make it faster on particular inputs but does not change the worst case.

Only `s`, `p`, `i`, and the existing input are stored, giving `O(1)` auxiliary space. These bounds match the manifest.

Python integers do not overflow. Under the stated limits, the early break also bounds practical product growth: while continuing, the prior product remains below a left sum of at most `10^{14}`, and one multiplication by a value at most `10^9` occurs before the break. In a fixed-width language, a saturating comparison or overflow-safe multiplication would still be prudent.

## Alternatives and edge cases

- **Prefix sums plus suffix products:** Precompute both sides for every index and scan for equality. This is straightforward but uses `O(N)` space that scalar accumulators avoid.
- **Recompute both sides at every index:** Directly summing and multiplying slices gives `O(N^2)` time. The rolling state reuses previous work.
- **Compute one total product and divide:** Positivity means division is defined, but values equal to one and enormous products still require care, and a full product can become huge before any useful comparison. Reverse accumulation with early stopping is safer.
- **Scan left to right:** A prefix sum is easy, but maintaining the right product by division needs the full product. The reverse direction builds the product naturally and uses a subtractive total sum.
- **Return the first reverse match without uniqueness:** In a generalized domain this could return the largest match. The source is safe specifically because positive values make `L_i` strictly increasing and `R_i` nonincreasing, allowing at most one equality.
- **Remove the current element from the wrong side:** At index `i`, `nums[i]` belongs to neither side. Subtract it before comparing and multiply it into `p` only after comparing.
- **Last index:** Its right product is the empty product one. It is balanced exactly when the sum of all preceding values is one.
- **First index:** Its left sum is zero, while its right product is positive under the contract, so index zero can never be balanced.
- **Length one:** Empty left sum zero differs from empty right product one, so the answer is minus one.
- **Values equal to one:** They leave the suffix product unchanged, making it nonincreasing rather than strictly decreasing from left to right. Uniqueness still follows because the left sum is strictly increasing.
- **Zero or negative values:** They are excluded. Allowing them would invalidate both the early-break inequality and potentially the uniqueness argument.
- **Product overflow:** Python is safe. Fixed-width implementations should compare before multiplication or saturate above the maximum possible left sum rather than permit overflow to reverse the inequality.
- **Break on `p >= s`:** Equality after the post-check multiplication does not indicate a balanced current index; `p` is already the next index's right product while `s` is still the current left sum. It only proves strict dominance for all farther-left indices.
