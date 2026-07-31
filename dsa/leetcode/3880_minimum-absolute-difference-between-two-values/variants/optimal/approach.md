## General

**Only the nearest earlier opposite value can improve the answer**

Suppose the scan reaches a `1` at index `i`. Among all earlier indices containing `2`, the latest one has the smallest value of `i - j`; every older `2` is farther away. The same argument holds when the current value is `2` and the earlier candidates contain `1`.

Maintain `last_one` and `last_two`, initially absent. At a `1`, compare its index with `last_two` when available, then replace `last_one`. At a `2`, compare with `last_one`, then replace `last_two`. A zero changes neither state. Keep the smallest distance observed and return `-1` if no comparison ever became possible.

For any valid pair, consider its later endpoint. When that endpoint is scanned, the algorithm compares it with the latest earlier occurrence of the opposite value. That comparison is no larger than the pair's distance. Conversely, every comparison made by the algorithm is itself a valid `1`-to-`2` pair. The minimum recorded comparison therefore equals the minimum over all valid pairs.

## Complexity detail

The scan visits each of the $n$ entries once, taking $O(n)$ time. It stores two indices and one best distance, so the auxiliary space is $O(1)$.

The benchmark defines size as $n$ and uses alternating `1`, `2` arrays of lengths `16`, `64`, and `256`. The accepted last-index scan and an independent adjacent-nonzero scan should scale linearly. A correct implementation that compares every `1` index with every array position performs $O(n^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every valid pair:** Checking each `1` against every `2` is direct but takes $O(n^2)$ time in the worst case.
- **Store both position lists:** Two sorted index lists can be merged in linear time, but they require $O(n)$ additional space that the running last indices avoid.
- **Adjacent nonzero values:** The optimum also occurs across a transition between consecutive nonzero entries of different values; tracking that filtered predecessor is an equivalent one-pass view.
- **Missing value:** If either `1` or `2` never occurs, no comparison is recorded and the answer is `-1`.
- **Reverse order:** A `2` before a `1` is handled symmetrically because distance uses an absolute difference.
- **Zeros:** Any number of zeros may separate the two useful values; their indices contribute to the distance even though zeros do not update the remembered positions.
- **Immediate neighbors:** Adjacent `1` and `2` values produce the smallest possible answer, `1`.
