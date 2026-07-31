## General

**Separate the input by parity**

There are only two possible kinds of legal input.

If every value already has the same parity, keep every value unchanged. This directly makes `nums2 = nums1`, so the required array exists.

Otherwise, the input contains at least one odd value. Fix any odd value `o` as an anchor. Keep every odd value unchanged. For every even value `e`, choose the subtraction assignment `e - o`. An even integer minus an odd integer is odd, so every constructed entry is now odd. The anchor always belongs to a different index from an even value, which satisfies the rule $j\ne i$.

These cases cover every non-empty input. Both produce a legal uniform-parity array, so the answer is always `true`; the implementation does not need to inspect the values.

## Complexity detail

The implementation returns the guaranteed result directly, using $O(1)$ time and $O(1)$ auxiliary space.

The benchmark defines size as $n$ and uses legal distinct arrays of lengths `4`, `20`, and `100`. The accepted source and an independently phrased constant-time implementation should remain flat. A correct but unnecessary parity scan performs $O(n)$ work and is the intended slower control.

## Alternatives and edge cases

- **Construct `nums2` explicitly:** Scanning the array and materializing the parity witness is correct, but takes $O(n)$ time and space even though only feasibility is requested.
- **Count odd and even values:** A full parity count also proves the two-case argument, but the result remains `true` for every possible count pair.
- **Single element:** Keeping the sole value already gives a uniform-parity array; no subtraction is needed.
- **All even or all odd:** Keeping every value is a valid construction.
- **Mixed parity:** Keep odd values and subtract one fixed odd anchor from every even value to make all results odd.
- **Distinctness and subtraction index:** An even value and the odd anchor cannot occupy the same index, so every constructed difference automatically uses $j\ne i$.
- **Negative constructed values:** Differences may be negative; parity is still well-defined, and the contract does not require `nums2` values to remain positive.
