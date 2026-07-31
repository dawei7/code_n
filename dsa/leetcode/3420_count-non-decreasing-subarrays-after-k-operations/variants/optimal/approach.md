## General

For a fixed subarray, the cheapest non-decreasing result is forced from left to right. Keep the first value, then raise each later value only when it is below the greatest original value seen earlier. Its final value is therefore the prefix maximum, and the required operations equal the sum of `prefix_max - nums[index]`.

Process possible left endpoints from right to left while maintaining the largest feasible right endpoint. Represent the raised values in the current window as constant-height blocks. Their start indices are stored in a deque: the back is the leftmost block and the front contains the block covering the current right endpoint. When a new `nums[left]` exceeds one or more adjacent block heights, those blocks must all be raised to `nums[left]`. Pop them from the back and add `(block length) * (height increase)` to the cost, then append the new left endpoint.

If the cost exceeds `k`, move `right` leftward. The removed element currently has the height of the deque's front block, so subtract that height minus its original value. Remove the front block marker when its start is the deleted index. Cost cannot decrease when a fixed-left window extends rightward, so after this contraction every endpoint from `left` through `right` is valid and every later endpoint is invalid. Add `right - left + 1` to the answer.

The deque exactly partitions the window by equal prefix-maximum height, so its block-area updates preserve the minimum required increment cost. The right boundary never moves right, and the feasibility monotonicity proves that the counted endpoints are precisely all valid subarrays for each left endpoint.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each index is appended once, removed at most once from the back during a merge, and removed at most once from the front during contraction. Both pointers also move only across the array. The total time is $O(n)$, and the deque uses $O(n)$ auxiliary space in the worst case.

The benchmark defines `size` as $n$ and uses descending arrays of 32, 96, and 256 values. Every subarray is legal under the large budget, so a direct method that recomputes the prefix-maximum cost for every start and end performs $\Theta(n^2)$ work. The accepted block-deque scan must remain linear.

## Alternatives and edge cases

- **Enumerate every subarray:** Incrementally extending each start gives correct costs but examines $\Theta(n^2)$ start/end pairs.
- **Sum adjacent drops:** Raising one low element can force several later elements upward; only prefix maxima, not independent adjacent differences, give the true minimum cost.
- **Decrement earlier elements:** The contract permits increments only, so lowering a peak is not an available repair.
- **Binary search every left endpoint:** A range-cost data structure can test endpoints, but it adds logarithmic factors and substantially more machinery.
- **Already non-decreasing input:** Every block has its original height, the maintained cost stays zero, and all $n(n+1)/2$ subarrays count.
- **Single element:** It is already non-decreasing and always contributes one valid subarray.
- **Repeated values:** Equality needs no operation and remains within the same non-decreasing block relationship.
- **Large values and budget:** The total cost and answer can exceed 32-bit integer range, so arithmetic must retain full integer precision.
