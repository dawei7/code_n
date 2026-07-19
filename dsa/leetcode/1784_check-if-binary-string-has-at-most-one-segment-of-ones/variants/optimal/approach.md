## General
**Express a second segment as a boundary**

Because `s[0]` is `'1'`, the string begins inside its first ones segment. That segment may continue to the end, or it may finish when the first `'0'` appears. A second ones segment exists exactly when some later adjacent pair changes from `'0'` to `'1'`.

Scan adjacent character pairs from left to right. If `s[index - 1] == "0"` and `s[index] == "1"`, return `false` immediately. If the scan finishes without that transition, no run of zeros was followed by another one, so every one belongs to the initial segment and the answer is `true`.

Any detected `01` boundary starts a ones run after an earlier run has ended, proving that at least two segments exist. Conversely, if at least two segments exist, the first character of the second segment must immediately follow a zero and therefore creates a detected `01` boundary. The test is thus both necessary and sufficient.

## Complexity detail
The scan examines at most $n-1$ adjacent pairs, taking $O(n)$ time. It keeps only the current index and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Substring search:** Testing whether `"01"` occurs expresses the same condition compactly and is also linear with a standard substring matcher.
- **Count segment starts:** Count positions containing `'1'` whose predecessor is absent or `'0'`, then test whether the count is at most one. This is more general but stores information that the Boolean decision does not need.
- **Split on zeros:** Splitting and counting nonempty pieces is correct, but it allocates substrings and uses $O(n)$ additional space.
- **Single character:** `"1"` contains one segment and has no adjacent pair to inspect.
- **All ones:** No segment boundary occurs, so the whole string is one valid segment.
- **Trailing zeros:** Once the initial segment ends, any number of zeros is allowed provided no later one appears.
- **No leading zero:** The guaranteed first `'1'` is what makes the presence of `"01"` equivalent to having a second segment.
