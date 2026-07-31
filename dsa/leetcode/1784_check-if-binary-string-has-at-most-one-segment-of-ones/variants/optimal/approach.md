## General
**Express a second segment as a boundary**

Because `s[0]` is `'1'`, the string begins inside its first ones segment. That segment may continue to the end, or it may finish when the first `'0'` appears. A second ones segment exists exactly when some later adjacent pair changes from `'0'` to `'1'`.

Test whether the substring `"01"` occurs. If it does, a run of zeros is followed by another one and the answer is `false`; otherwise every one belongs to the initial segment and the answer is `true`.

Any detected `01` boundary starts a ones run after an earlier run has ended, proving that at least two segments exist. Conversely, if at least two segments exist, the first character of the second segment must immediately follow a zero and therefore creates a detected `01` boundary. The test is thus both necessary and sufficient.

## Complexity detail
The substring search examines the string in $O(n)$ time and uses $O(1)$ auxiliary space for this fixed two-character pattern.

## Alternatives and edge cases
- **Explicit adjacent-pair scan:** Comparing each position with its predecessor detects the same boundary in $O(n)$ time, but is more verbose than the fixed substring test.
- **Count segment starts:** Count positions containing `'1'` whose predecessor is absent or `'0'`, then test whether the count is at most one. This is more general but stores information that the Boolean decision does not need.
- **Split on zeros:** Splitting and counting nonempty pieces is correct, but it allocates substrings and uses $O(n)$ additional space.
- **Single character:** `"1"` contains one segment and has no adjacent pair to inspect.
- **All ones:** No segment boundary occurs, so the whole string is one valid segment.
- **Trailing zeros:** Once the initial segment ends, any number of zeros is allowed provided no later one appears.
- **No leading zero:** The guaranteed first `'1'` is what makes the presence of `"01"` equivalent to having a second segment.
