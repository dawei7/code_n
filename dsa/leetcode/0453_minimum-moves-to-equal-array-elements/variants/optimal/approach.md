## General

Simulating the stated operation is deceptive. One move increments exactly `n - 1` elements, so nearly the entire array changes every time, and the largest element may change from step to step. The optimal solution uses a change of perspective that turns each complicated move into one simple decrement.

**Equality is unchanged by a uniform shift**

Suppose one move increments every element except the element at index `j`. Immediately after that move, imagine subtracting `1` from every array element. This imaginary uniform subtraction does not affect whether the elements are equal: adding or subtracting the same amount from all values preserves every pairwise difference.

The combined effect is:

- Every incremented element receives `+1` and then `-1`, for a net change of zero.
- The excluded element receives no increment and then `-1`, for a net change of `-1`.

Thus, up to an irrelevant uniform shift, “increment `n - 1` elements by one” is exactly equivalent to “decrement one chosen element by one.” Every sequence of original moves corresponds to the same number of single-element decrements, and conversely each chosen decrement tells us which element to exclude from the corresponding original move.

The transformed problem is much easier: how many single-element decrements are needed to make all values equal?

**The transformed target must be the minimum**

Decrements can only lower values. Therefore a common target `t` cannot exceed the original minimum value `m = min(nums)`, because an element already equal to `m` cannot be increased in the transformed view.

For a chosen target $t\le m$, element `nums[i]` needs exactly

$$
\texttt{nums}[i]-t
$$

decrements. The total is

$$
\sum_{i=0}^{n-1}(\texttt{nums}[i]-t).
$$

Choosing a smaller target increases the required decrement count for every element. The largest legal target, and therefore the one requiring the fewest moves, is exactly the original minimum `m`.

The minimum number of moves is consequently

$$
\sum_{i=0}^{n-1}(\texttt{nums}[i]-m).
$$

Distributing the sum gives the formula used by the code:

$$
\sum_{i=0}^{n-1}\texttt{nums}[i] - n\cdot m.
$$

That is `sum(nums) - min(nums) * len(nums)`.

**A direct example**

For `nums = [1,2,3]`, the minimum is `1`. In the decrement view:

- `1` needs zero decrements.
- `2` needs one decrement.
- `3` needs two decrements.

The total is $0+1+2=3$. The formula agrees: $1+2+3-3\cdot1=3$.

Mapping those three decrements back to the original operation yields a valid three-move sequence. Decrementing `3` in the transformed view means incrementing the other two original elements; decrementing it again repeats that exclusion, and decrementing `2` corresponds to excluding its position. Uniform shifts make the absolute intermediate numbers look different, but the pairwise gaps close in exactly the same way.

For `[1,1,1]`, every value already equals the minimum. Each difference is zero, so the result is zero.

**Why no smaller number of moves can work**

In the equivalent decrement problem, an element at value `x` must lose at least `x - m` units before it can equal the original minimum. Choosing a target below `m` only adds more required decrements; choosing one above `m` is impossible using decrements. Since one transformed move decreases only one element by one, at least the sum of all gaps from `m` moves is necessary.

Performing exactly those decrements—lower each element until it reaches `m`—uses that many moves and succeeds. The lower bound is therefore achievable, proving the formula is minimal rather than merely sufficient.

**Why negative values cause no difficulty**

The reasoning depends on differences, not on values being positive. For `[-3,-1,2]`, the minimum is `-3`, and the gaps are `0`, `2`, and `5`, for seven moves. The formula computes `(-3-1+2) - 3*(-3) = -2+9 = 7`. Uniform shifts and decrement counts remain valid across zero.

The input is guaranteed nonempty, so `min(nums)` is always defined. Python integers also grow as needed, so the intermediate sum and product cannot overflow even when individual values are large.

## Complexity detail

Let $n$ be the array length. `sum(nums)` scans all $n$ values once, and `min(nums)` scans them once again. Multiplication, subtraction, and `len(nums)` are constant-time operations under the standard fixed-width arithmetic model. The total time is therefore $O(n)$.

Only aggregate integer values are stored. The input is not copied, sorted, or modified, so auxiliary space is $O(1)$.

In a strict arbitrary-precision bit-cost model, arithmetic cost grows with integer width. The customary problem analysis uses the fixed-width model, and the final answer is guaranteed to fit in a 32-bit integer. In a fixed-width language, however, the intermediate sum and `min * n` should still be computed in a sufficiently wide type because they can exceed an individual input value even if their final difference fits.

## Alternatives and edge cases

- **Sum individual gaps:** First find `m`, then accumulate `x - m` for each `x`. It has the same $O(n)$ time and $O(1)$ space and may reduce intermediate-overflow risk in fixed-width languages.
- **Sort the array:** After sorting, sum every difference from the first value. This is correct but wastes $O(n\log n)$ time merely to discover the minimum.
- **Simulate one move at a time:** Repeatedly incrementing `n - 1` elements can require an enormous number of operations and touches many array positions per move.
- **Raise everything to the maximum:** That reasoning fits an operation that increments one element, not this operation. Incrementing all but one is relatively equivalent to lowering the excluded element.
- **All values equal:** Every gap from the minimum is zero, so no moves are needed.
- **One-element array:** A move would increment zero elements, but the sole value is already equal to every array element. The formula returns zero.
- **Repeated minimum values:** Each minimum contributes zero; only elements above the minimum require transformed decrements.
- **Negative values:** Subtraction from the minimum still produces nonnegative gaps and the same formula remains valid.
- **Large magnitudes:** Use wide accumulation in fixed-width languages even though the promised final answer fits 32 bits.
- **Input preservation:** The one-line calculation only reads `nums`, leaving its order and values unchanged.
