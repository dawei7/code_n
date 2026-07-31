## General

**Record the arithmetic runs that need no replacement**

For every index `i`, let `left[i]` be the length of the longest unchanged arithmetic subarray ending at `i`. Starting with lengths `1` and `2`, extend the previous run whenever

$$
\texttt{nums[i]}-\texttt{nums[i-1]}
=
\texttt{nums[i-1]}-\texttt{nums[i-2]}.
$$

Otherwise, the last two elements start a new length-two run. A symmetric right-to-left pass builds `right[i]`, the longest unchanged arithmetic subarray starting at `i`. The maximum `left` value covers the option of making no useful replacement.

**Use the changed element at an endpoint**

Suppose index `i` is replaced. It can always be assigned the value that continues the unchanged run ending at `i - 1`, producing `left[i - 1] + 1` elements. The same reasoning extends the run beginning at `i + 1` to length `right[i + 1] + 1`. These choices also handle replacing the first or last selected element, including either endpoint of the entire array.

**Bridge two sides only when one integer fits**

To include both neighbors of an interior replacement, its new value must lie exactly halfway between them. Therefore

$$
\texttt{nums[i+1]}-\texttt{nums[i-1]}=2d
$$

must hold for an integer common difference $d$. An odd neighbor gap cannot be bridged with an integer replacement.

When the gap is even, take $d$ as half of it. The left side can contribute its entire precomputed run only if its existing difference is $d$; otherwise only `nums[i - 1]` is compatible. Apply the same test to the right side. The resulting candidate length is the compatible left length, plus the changed element, plus the compatible right length. Every arithmetic subarray using one replacement falls into the unchanged, one-sided, or bridged case, so maximizing these candidates is exhaustive.

## Complexity detail

Each of the two preprocessing passes and the replacement-index pass visits $n$ positions once. The total time is $O(n)$. The `left` and `right` arrays use $O(n)$ auxiliary space.

The benchmark defines size as $n$ and uses already arithmetic arrays of lengths `16`, `64`, and `256`. The accepted source and an independently expressed difference-run implementation should preserve linear scaling. A correct control that rescans both sides for every replacement index performs $O(n^2)$ work on these full-length runs and should fail only the scaling verdict.

## Alternatives and edge cases

- **Recompute runs per replacement:** Scanning outward from every candidate index is correct but repeats the same work and can take $O(n^2)$ time.
- **Difference-array formulation:** Equal runs in the adjacent-difference array encode unchanged arithmetic subarrays and lead to the same $O(n)$ combination logic with shifted indices.
- **Odd neighbor gap:** If the elements around a replacement differ by an odd amount, no integer can be exactly halfway between them, though a one-sided extension may still be optimal.
- **Short compatible side:** When a neighboring side contains only one selected element, it imposes no pre-existing difference and can always participate in an even-gap bridge.
- **Endpoint replacement:** Changing the first or last element can extend the adjacent arithmetic run by one without any parity condition.
- **Constant arrays:** A common difference of zero is valid; an already constant array should retain its full length.
- **Optional operation:** An already optimal arithmetic subarray remains eligible because replacing an element is not required.
- **Unbounded new value:** The chosen replacement may be negative or exceed $10^5$, as demonstrated by the second source example's value `-2`.
