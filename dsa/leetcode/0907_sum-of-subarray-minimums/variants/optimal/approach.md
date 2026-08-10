## General

Enumerating every subarray and finding its minimum would be quadratic or worse. The contribution method instead asks:

> For how many subarrays is `arr[i]` the chosen minimum?

If that count is known, index `i` contributes its value multiplied by the count. Summing over indices accounts for every subarray.

For each index `i`, the solution finds two boundaries:

- `left[i]` is the nearest index to the left whose value is strictly smaller than `arr[i]`, or `-1` if none exists.
- `right[i]` is the nearest index to the right whose value is smaller than or equal to `arr[i]`, or `n` if none exists.

The asymmetry—strict on one side and non-strict on the other—is essential for duplicate values.

**Count choices around one minimum.** A subarray in which `i` represents the minimum may start at any index from `left[i] + 1` through `i`. That gives

$$
i-\text{left}[i]
$$

start choices. It may end at any index from `i` through `right[i] - 1`, giving

$$
\text{right}[i]-i
$$

end choices. Every start can pair with every end, so the number of represented subarrays is their product.

The contribution is

$$
(i-\text{left}[i])
(\text{right}[i]-i)
\text{arr}[i].
$$

**Build strict-smaller left boundaries.** The first pass keeps indices in a stack whose values are strictly increasing. Before using the top as a boundary, it pops while `arr[top] >= v`. Equal values are removed along with greater ones, so a remaining top is strictly smaller. It is also nearest because any later index that could qualify would still be above it in the stack.

**Build smaller-or-equal right boundaries.** The reverse pass pops only while `arr[top] > arr[i]`. An equal value remains and becomes the boundary. Thus the retained nearest right value is less than or equal to the current value.

**Why duplicate ownership needs one strict side.** Consider `[1,1]`. The subarray containing both positions has minimum 1, but it must be counted once, not once for each occurrence. With the chosen boundaries, the first 1 stops at the equal value to its right, while the second 1 may extend left through the equal first value. The two-element subarray is assigned to the rightmost equal minimum.

If both sides used strict smaller boundaries, both equal occurrences could claim the shared subarray and double-count it. If both used smaller-or-equal boundaries, neither might claim the full interval. Either asymmetric convention works; this code chooses strict left and non-strict right.

**Why every subarray is counted exactly once.** Take any subarray and find its minimum value. Among occurrences of that value in the subarray, choose the rightmost one, at index `i`. No strictly smaller value lies between the subarray start and `i`, so its start lies after `left[i]`. No smaller-or-equal value lies between `i+1` and the subarray end, because `i` was the rightmost minimum, so its end lies before `right[i]`. The contribution range for `i` includes this subarray.

No other index can claim it under the boundary convention: a larger value is not a minimum, and an earlier equal minimum is blocked by the next equal value on its right. Thus contributions form an exact partition of all subarrays.

For `[3,1,2,4]`, value 1 has no smaller value on either side, so it represents $2\cdot3=6$ subarrays. Value 2 represents two, value 3 one, and value 4 one. Their weighted sum is $6+4+3+4=17$.

## Complexity detail

Let $n$ be the array length. Each index is pushed once and popped at most once in each monotonic-stack pass. Boundary construction is therefore linear, and the final contribution generator is linear.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(n)$ for `left`, `right`, and the stack.

The final sum is reduced modulo $10^9+7$. Python integers safely hold the unreduced products.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining a running minimum for every start costs $O(n^2)$ time.
- **Dynamic programming with a monotonic stack:** Compute the sum of minima for subarrays ending at each index. It also reaches $O(n)$ time.
- **Use strict comparisons on both sides:** Equal minima double-count shared subarrays.
- **Use non-strict comparisons on both sides:** Equal minima can leave shared subarrays unassigned.
- **All values increasing:** Left boundaries are immediate predecessors, while right boundaries are the sentinel.
- **All values decreasing:** Left boundaries are the sentinel, while right boundaries are immediate successors.
- **All values equal:** The asymmetric rule assigns each subarray to its rightmost element exactly once.
- **One element:** Its start and end choice counts are both one, so it contributes itself.
- **Boundary sentinels:** `-1` and `n` make formulas work without special cases at array ends.
- **Positive values:** The contract ensures every minimum is positive, though the contribution proof also works with other integers.
- **Modulo timing:** Reducing only after the sum is mathematically valid in Python; fixed-width languages may reduce during accumulation.
- **Store indices, not values:** Boundaries need distances, so stack entries must retain positions.
