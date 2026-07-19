## General
**Keep the smallest tail for every attainable length**

Maintain an array `tails` where `tails[length - 1]` is the smallest final value found for any strictly increasing subsequence of that length in the processed prefix. Smaller tails are always at least as useful as larger ones: they leave more future values able to extend the subsequence.

For each value, binary-search the first tail that is greater than or equal to it. Replacing that tail improves an existing length without changing the maximum length. If no such tail exists, append the value because it extends the longest attainable subsequence.

**Lower bound enforces strict increase**

Using the first position with `tail >= value` is essential. An equal value replaces the same-length tail rather than extending it, so duplicates cannot create a strictly increasing step. A value larger than every tail appends only after proving it can follow the representative of the longest length.

For `[10,9,2,5,3,7,101,18]`, the tails evolve through `[10]`, `[9]`, `[2]`, `[2,5]`, `[2,3]`, `[2,3,7]`, `[2,3,7,101]`, and `[2,3,7,18]`. The final array is not necessarily an actual subsequence, but its length is four.

**Tail replacement preserves exactly the attainable lengths**

Before processing a value, each tails entry witnesses an attainable subsequence length, and the entries are strictly increasing. Replacing the lower-bound position preserves that length by attaching the value to the previous shorter tail, while making its endpoint no larger. Appending witnesses one new longer length.

Conversely, if some processed prefix has an increasing subsequence of length $L$, consider its elements in order. The lower-bound updates can place each successive element no later than its position in that subsequence, so `tails` reaches length at least $L$. Every stored length is attainable and every attainable length is represented; therefore `len(tails)` is exactly the LIS length.

## Complexity detail
Each of the `n` values performs one binary search over at most `n` tails, giving $O(n \log n)$ time. The tails array contains at most `n` integers and uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Dynamic programming over every earlier index:** is correct and useful for reconstruction, but takes $O(n^2)$ time.
- **Sort the values:** destroys original index order and solves a different problem.
- Equal values never extend a subsequence. A decreasing or all-equal array has answer one; negative values require no special handling.
