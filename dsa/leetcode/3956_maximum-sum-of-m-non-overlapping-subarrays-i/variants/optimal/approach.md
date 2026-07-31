## General

Use a prefix sum `prefix`, so the sum of the half-open subarray from start `j` to endpoint `i` is `prefix[i] - prefix[j]`. For one DP layer, let `previous[j]` be the best total using exactly one fewer selected subarray among the first `j` elements. A new subarray ending at `i` may start at any `j` satisfying `l <= i - j <= r`, and its transition is

$$
\texttt{prefix[i]} + \max_j\bigl(\texttt{previous[j]} - \texttt{prefix[j]}\bigr).
$$

As `i` increases, the eligible starts form a sliding window `[i - r, i - l]`. Maintain their transition values in a decreasing deque. Insert the newly eligible start `i - l`, remove expired starts below `i - r`, and read the maximum from the deque front. Each start enters and leaves the deque at most once per DP layer.

The current layer represents exactly one more selected subarray than the previous layer. Besides taking a transition that ends at `i`, carry `current[i - 1]` forward so the final selected subarray may end earlier. Initialize the zero-subarray layer to zero at every prefix, compute exact counts from one through `min(m, floor(n / l))`, and take the best full-array value over all those layers. Keeping exact counts prevents the zero-subarray value from incorrectly winning when all sums are negative, while the final maximum implements “at most `m`.”

For correctness, every transition appends a length-valid subarray after a prefix containing the earlier non-overlapping choices, so it constructs a legal exact-count selection. Conversely, consider an optimal exact-count selection and its final subarray `[j, i)`. The preceding subarrays are represented by `previous[j]`, and `j` appears in the deque window for endpoint `i`, so the transition considers that optimum. Induction over the selected count proves every layer, and maximizing the completed layers yields the required answer.

## Complexity detail

Prefix sums take $O(n)$ time. For each of at most $m$ DP layers, every endpoint and deque index is processed a constant amortized number of times, giving $O(mn)$ total time. Prefix sums, two DP rows, and the deque use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan every legal length:** Evaluating all starts explicitly gives a correct $O(mnr)$ transition, but repeats the sliding-window maximum work that the deque shares across endpoints.
- **Full DP table:** Storing all $m + 1$ rows makes reconstruction easier but raises auxiliary space to $O(mn)$ when only the value is requested.
- **All-negative arrays:** The zero-subarray state must not be accepted as the final answer because the contract requires at least one selection.
- **At most `m`:** The optimum can use fewer than `m` subarrays, so compare the completed value after every exact-count layer.
- **Impossible exact counts:** No more than `floor(n / l)` legal subarrays can fit, allowing later DP layers to be skipped.
- **Large values:** Totals can exceed 32-bit integer range, so implementations must preserve wide integer arithmetic.
