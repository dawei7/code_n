## General

**Turn the inequalities into alternating roles.**

The required pattern is

$$
\text{nums}[0] < \text{nums}[1] > \text{nums}[2] < \text{nums}[3] > \cdots.
$$

Even indices are valleys and odd indices are peaks. It is therefore natural to reserve the smaller half of the values for even positions and the larger half for odd positions. Sorting first makes those two groups explicit.

The exact optimal source creates `arr = sorted(nums)`. This is a new ascending copy; all later reads come from `arr`, while assignments overwrite the original `nums`. Keeping a separate copy prevents early writes from destroying values that have not yet been placed.

**Split the sorted values into lower and upper halves.**

Let $n$ be the array length. The index

$$
i = \left\lfloor\frac{n-1}{2}\right\rfloor
$$

is the final index of the lower half, and `j = n - 1` is the final index of the upper half.

For an even length $n=2q$, the lower and upper halves each contain $q$ values:

$$
\text{lower} = \text{arr}[0:q],
\qquad
\text{upper} = \text{arr}[q:2q].
$$

For an odd length $n=2q+1$, there are $q+1$ even positions but only $q$ odd positions. Accordingly, the lower half contains $q+1$ values and the upper half contains $q$:

$$
\text{lower} = \text{arr}[0:q+1],
\qquad
\text{upper} = \text{arr}[q+1:2q+1].
$$

This size difference is why the formula uses `(n - 1) >> 1`, which is integer division of $n-1$ by two. The extra value for an odd-length array belongs in a valley position, including the unpaired final even index.

**Read both halves backward.**

The loop visits destination index `k` from left to right. At an even `k`, it writes `arr[i]` and decrements `i`; at an odd `k`, it writes `arr[j]` and decrements `j`. The resulting arrangement has the form

$$
L_0, U_0, L_1, U_1, L_2, U_2, \ldots,
$$

where $L_0,L_1,\ldots$ are the lower-half values in descending order and $U_0,U_1,\ldots$ are the upper-half values in descending order.

Using descending order inside each half is essential when duplicates exist. If both halves were read from left to right, equal values near the split could land next to each other. For the sorted array `[1,2,2,2,3,3]`, ascending interleaving would begin `[1,2,2,3,...]`, which already fails at `2 > 2`. Reversing the halves separates the equal values: lower descending is `[2,2,1]`, upper descending is `[3,3,2]`, and their interleaving is `[2,3,2,3,1,2]`.

The reversal places the largest lower value first, but it also pairs it with the largest upper value. As the lower choices decrease, the upper choices decrease in step. Duplicate values around the median are pushed apart instead of being aligned across an early peak boundary.

**Walk through the first example.**

For `nums = [1,5,1,1,6,4]`, sorting gives

$$
[1,1,1,4,5,6].
$$

The length is six, so `i = 2` and `j = 5`. Even destinations receive `arr[2]`, `arr[1]`, and `arr[0]`, all equal to `1`. Odd destinations receive `arr[5]`, `arr[4]`, and `arr[3]`, namely `6`, `5`, and `4`. The overwritten input becomes

$$
[1,6,1,5,1,4],
$$

and every strict inequality holds.

For an odd-length illustration, suppose the sorted values are `[1,2,3,4,5]`. The lower half is `[1,2,3]`, the upper half is `[4,5]`, and reversed interleaving produces `[3,5,2,4,1]`. The lower half supplies the extra final valley.

**Why every odd position is greater than its neighbors.**

Consider the peak placed at destination `2t + 1`. It receives

$$
U_t = \text{arr}[n-1-t].
$$

Its left valley receives

$$
L_t = \text{arr}\!\left[\left\lfloor\frac{n-1}{2}\right\rfloor-t\right],
$$

and, if a right valley exists, that valley receives the even earlier sorted value

$$
L_{t+1} = \text{arr}\!\left[\left\lfloor\frac{n-1}{2}\right\rfloor-t-1\right].
$$

The sorted index used for $U_t$ is to the right of both indices used for its neighboring lower values, so $U_t$ is at least as large as each neighbor. The only concern is equality. Reading both halves backward maximizes the sorted-index separation for values placed next to each other. If equality still spanned one of these paired ranges, there would be too many copies of that value, or too few strictly larger values, to place all copies into a strict valley-peak arrangement. That would contradict the contract's guarantee that a valid answer exists.

The odd-length boundary is the subtle case. If a value occupied the entire sorted interval from a paired lower index through its upper index, it could occur as many as the $q+1$ valley slots of an array of length $2q+1$. Then every one of the $q$ peaks separating those valleys would have to be strictly larger. But the equality interval leaves fewer than $q$ larger elements, so a valid strict arrangement would be impossible. Thus the existence guarantee rules out equality for every neighboring pair produced by this construction.

Consequently, each peak is strictly greater than both adjacent valleys. Those local comparisons are exactly all inequalities in the required pattern, proving the final permutation is valid.

**Why the result is still a permutation and why mutation is correct.**

The lower and upper index ranges are disjoint and together cover every index of `arr`. Each loop iteration consumes one value by decrementing the corresponding pointer. There are exactly as many lower-half values as even destinations and as many upper-half values as odd destinations. Hence every original occurrence, including every duplicate occurrence, is written exactly once. No value is lost or invented.

The function intentionally returns nothing. Its contract is fulfilled by replacing every entry of the original list `nums`. The separate sorted copy is only temporary working storage.

## Complexity detail

Let $n$ be the number of elements. Creating `arr = sorted(nums)` takes $O(n\log n)$ time. The placement loop visits every destination once and takes $O(n)$ time, so the exact implementation's total time complexity is $O(n\log n)$.

The sorted copy contains $n$ elements and therefore uses $O(n)$ auxiliary space. The pointer variables use only $O(1)$ additional space beyond that copy.

The variant manifest currently describes a median quickselect plus virtual-index three-way partition with $O(n)$ time and $O(1)$ space. That algorithm is not present in the checked-in optimal source. The source calls `sorted` and keeps the resulting array, so its actual bounds are $O(n\log n)$ time and $O(n)$ space. It mutates the required output list in place in the API sense, but it does not satisfy the follow-up's $O(1)$ auxiliary-space target.

## Alternatives and edge cases

- **Quickselect plus virtual indexing:** Select the median in expected $O(n)$ time, then three-way partition values through the index mapping that visits odd positions before even positions. This can meet the expected $O(n)$-time and $O(1)$-space follow-up, but it is considerably more intricate and is not the exact source shown here.

- **Sort and interleave halves in ascending order:** This looks similar but fails with duplicates around the median, because equal boundary values can become adjacent. Reversing both halves is the detail that spreads duplicates safely.

- **Sort without a separate copy:** Rearranging `nums` while also using it as the unread sorted source risks overwriting values before they are consumed. The copied `arr` cleanly separates reads from writes.

- **Length one:** `i` and `j` both start at zero. The only value is written to even index zero, and there are no inequalities to violate.

- **Odd length:** The lower half deliberately has one extra value because there is one extra even position. The last write is a valley with no right-hand peak requirement.

- **Many duplicates:** Duplicate values are allowed, but the inequalities are strict. The reversed-half construction handles every input for which the promised valid answer exists. An input with too many copies in an incompatible rank distribution would have no valid strict wiggle, but such an input is excluded by the contract.

- **Already wiggled input:** The method still sorts and reconstructs it. Preserving an existing order is unnecessary; any valid permutation is accepted.

- **Negative values:** The contract uses values from `0` through `5000`, but the reasoning depends only on ordering. The same construction would work for any comparable numeric values under the same existence guarantee.
