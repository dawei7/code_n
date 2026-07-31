## General

For every index, first determine the length of the non-decreasing run ending there. These left-run lengths identify how far a candidate subarray can extend before a replaced position. A backward scan similarly maintains the length of the non-decreasing run beginning immediately after the current position.

Consider replacing `nums[i]`. The replacement can always extend only the run on the left by one, or only the run on the right by one. It can join both runs when `nums[i - 1] <= nums[i + 1]`: in that case an integer between those boundary values, inclusive, can be placed at index `i`, so the complete left run, replacement position, and complete right run form one non-decreasing subarray.

If the two neighboring values have the opposite order, no single replacement value can be simultaneously at least the left neighbor and at most the right neighbor. The two runs cannot then be joined through `i`, although either side can still be extended by one. Taking the best of all such choices and the original runs covers both one replacement and the allowed no-replacement outcome.

## Complexity detail

The forward and backward scans each process all $n$ positions once, giving $O(n)$ time. The array of left-run lengths uses $O(n)$ auxiliary space; the backward run length and answer use constant additional storage.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Storing both left- and right-run lengths gives the same $O(n)$ time and $O(n)$ space with a more symmetric implementation.
- **Try every replacement and rescan:** Testing neighboring replacement values at each index is correct but takes $O(n^2)$ time.
- **No replacement needed:** The longest original run remains a candidate because the operation is optional.
- **Equal neighbors:** The non-decreasing comparisons are inclusive, so equal boundary values can be bridged.
- **First or last position:** Replacing an endpoint can extend only the single adjacent run, and the result cannot exceed $n$.
- **Single-element array:** Its only subarray already has length `1` and is non-decreasing.
- **Arbitrary replacement value:** Only the ordering interval between neighboring values matters; no enumeration over the numeric range is required.
