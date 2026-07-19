## General
**Remove absolute values using the sorted order**

At index `i`, every element to the left is at most `nums[i]`. If their sum is $L$, their combined contribution is therefore

$$
i \cdot \texttt{nums[i]} - L.
$$

Every element to the right is at least `nums[i]`. If their sum is $R$, and there are $n-i-1$ such elements, their contribution is

$$
R - (n-i-1) \cdot \texttt{nums[i]}.
$$

Adding these two expressions gives the desired value at `i`. Equal values cause no difficulty: subtracting equal quantities contributes zero on whichever side they occur.

**Maintain both side sums in one traversal**

Compute the total array sum once. Before processing an index, keep `left_sum` for all earlier values. The right sum is then `total - left_sum - nums[i]`. Form the two contributions, append their sum, and add the current value to `left_sum` before advancing.

For each index, sortedness proves that the left and right formulas equal the corresponding absolute differences term by term. Those sides partition every other index, so their sum is exactly the required result. Updating `left_sum` preserves its meaning for the next position, establishing every output in order.

## Complexity detail
Computing the total and traversing the array each take $O(n)$ time. Apart from the required output list, the algorithm stores only the total, running left sum, current index, and a few arithmetic values, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Compare every pair directly:** summing `abs(nums[i] - nums[j])` for each output is straightforward but repeats work and takes $O(n^2)$ time.
- **Prefix-sum array:** storing every prefix also gives $O(n)$ time, but it uses $O(n)$ extra space when one running sum is sufficient.
- **Unsorted input:** the sign simplification depends on non-decreasing order; sorting an arbitrary input would change index identities and require additional mapping.
- **Duplicate values:** equal elements contribute zero distance and can produce identical result entries at adjacent positions.
- **Two elements:** each result is simply the absolute difference between the pair.
- **Large totals:** implementations in fixed-width languages should use an integer width capable of holding the summed differences.
