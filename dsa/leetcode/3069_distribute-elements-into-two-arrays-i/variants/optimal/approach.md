## General

**Preserve the two evolving arrays.** Initialize the first array with `nums[0]` and the second with `nums[1]`, which are the language-native counterparts of the statement's first two one-indexed operations. Both arrays are now nonempty, so their last values are always defined.

Process the remaining values from left to right. Before appending each value, compare `first[-1]` with `second[-1]`. Append to the first array only when its last value is strictly greater; otherwise append to the second. Finally, concatenate the two arrays in the required order.

After initialization, each maintained array exactly matches the corresponding array after the first two operations. For every later value, the simulation observes the same two last elements as the prescribed process and applies the same strict comparison, so it chooses the same destination. By induction, both arrays are correct after every operation, and their concatenation is the required result.

## Complexity detail

Let $n$ be the length of `nums`. Each value is appended exactly once, and concatenating the two completed arrays copies $n$ values, so total time is $O(n)$. The two arrays together store $n$ values, giving $O(n)$ space for the returned construction.

## Alternatives and edge cases

- **Track destinations then rebuild:** Recording one destination flag per value and reconstructing both arrays later is also $O(n)$ but adds an unnecessary intermediate representation.
- **Repeated list concatenation:** Replacing append operations with `array = array + [value]` copies an entire partial array each time and can degrade to $O(n^2)$ time.
- **In-place partitioning:** The decision depends on the evolving last values and the output preserves order within each destination, so a simple partition cannot replace the simulation.
- **Minimum length:** With three values, exactly one comparison occurs after initialization.
- **Strict comparison:** A value joins the first array only for `first[-1] > second[-1]`; the `else` branch owns every other case. Legal inputs are distinct, so the two last values cannot be equal.
- **Concatenation order:** The final answer always places all first-array values before all second-array values, regardless of the chronological interleaving of appends.
- **Boundary values:** Only comparisons matter, so values at `1` and `100` require no special arithmetic handling.
