## General

**Precompute the non-decreasing run on both sides of every index**

If index `i` is replaced, all unchanged elements included to its left must already form a non-decreasing run ending at `i-1`. Likewise, included elements to its right must form a non-decreasing run starting at `i+1`.

`left[i]` stores the length of the longest non-decreasing subarray ending exactly at `i`. It starts at one and extends `left[i-1]` when `nums[i] >= nums[i-1]`.

`right[i]` symmetrically stores the longest non-decreasing subarray starting exactly at `i`. A reverse scan extends it when `nums[i] <= nums[i+1]`.

These arrays let the solution evaluate a proposed replacement position in constant time instead of rescanning its surrounding runs.

**Preserve the best zero-replacement answer**

The operation is optional. `max(left)` is the longest non-decreasing subarray already present, so `ans` begins with that value. This protects cases where changing an element offers no improvement or the entire array is already valid.

**Try each index as the replaced position**

For index `i`, let `a` be `left[i-1]` when a left neighbor exists, otherwise zero. Let `b` be `right[i+1]` when a right neighbor exists, otherwise zero.

If one side is absent, an arbitrary replacement value can always extend the existing run by one. The general expression `a+b+1` handles both boundaries.

When both neighbors exist, one replacement can bridge both runs exactly when some integer `v` satisfies

$$
\texttt{nums}[i-1]\le v\le\texttt{nums}[i+1].
$$

Such a value exists precisely when `nums[i-1] <= nums[i+1]`. Then the combined candidate length is

$$
a+1+b.
$$

The neighboring runs already satisfy their internal inequalities, and the chosen `v` supplies the two missing boundary inequalities.

If `nums[i-1] > nums[i+1]`, no value can be simultaneously at least the left neighbor and at most the right neighbor. Both sides cannot be joined. The replacement can still extend the left run by choosing a sufficiently large value, giving `a+1`, or extend the right run with a sufficiently small value, giving `b+1`. The source takes both maxima.

For `[1,2,3,1,2]` at index three, the left run length is three and the right-side run length is one. Since left neighbor three is greater than right neighbor two, both cannot be bridged. Choosing replacement three extends the left run to length four, which is optimal.

As a compatible example, consider `[1,2,9,4,5]` and replace the nine at index two. The left run ending at index one has length two, and the right run beginning at index three also has length two. Since `nums[1]=2<=4=nums[3]`, choose any integer from two through four, such as three. The complete array becomes `[1,2,3,4,5]`, and the formula returns `2+1+2=5`.

The formulas cannot exceed `n`. The left and right runs occupy disjoint positions on opposite sides of `i`, and adding one accounts for the replacement position itself.

**Why checking only immediate neighbors is enough**

The precomputed runs already guarantee every inequality farther inside each side. Replacing `nums[i]` affects only comparisons `(i-1,i)` and `(i,i+1)`. Therefore the immediate neighbor relation completely determines whether both intact runs can be connected.

Every result using one replacement has some replaced index `i`. Its unchanged left and right pieces cannot exceed `a` and `b`, and the compatibility test gives the exact maximum way to combine them. Scanning every `i` therefore considers every possible optimal replacement, while `max(left)` covers using none.

## Complexity detail

Let `n` be the array length. Building `left` and `right` requires two $O(n)$ scans. Testing all replacement positions is another $O(n)$ scan with constant work per index. Total time is $O(n)$.

The two length arrays each contain `n` integers, so auxiliary space is $O(n)$. The remaining variables use constant space. A more intricate streaming formulation might reduce memory, but it is not the exact source.

## Alternatives and edge cases

- **Try many replacement values:** The chosen integer domain is unbounded, so enumeration is impossible and unnecessary. Neighbor inequalities reduce feasibility to one interval test.
- **Recompute runs for every index:** This gives $O(n^2)$ time. Prefix/suffix run lengths reuse the same information.
- **Always combine both sides:** When the left neighbor exceeds the right neighbor, no replacement can satisfy both inequalities.
- **Use strict inequalities:** The required order is non-decreasing, so equal neighboring and replacement values are valid.
- **No replacement:** Initializing from `max(left)` preserves an already optimal original run.
- **First or last index:** Only one neighboring run exists, and replacing the endpoint can extend it by one.
- **Single-element array:** Both side lengths are zero, and the answer remains one.
- **Entire array non-decreasing:** The initial answer is `n`; candidate lengths cannot exceed it.
- **One sharp drop:** Replacing an endpoint of the drop may join runs only if the two outer neighbor values are compatible.
- **Negative values:** Comparisons, not magnitude, drive the algorithm; arbitrary signed integers work unchanged.
- **Replacement outside input bounds:** The contract allows any integer, which guarantees one-sided extension is always possible.
