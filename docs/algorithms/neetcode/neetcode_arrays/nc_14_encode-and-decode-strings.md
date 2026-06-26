## Problem Description & Examples
### Goal
Design an algorithm to encode a list of strings to a single string and decode it back to the original list of strings. No restrictions on characters in the strings.

Implement `solve(strs)` which encodes, then decodes, and returns the final list.

### Function Contract
**Inputs**

- `strs`: List[str]

**Return value**

List[str] - same as input after encode+decode roundtrip

### Examples
**Example 1**

- Input: `strs = ["neet", "code"]`
- Output: `["neet", "code"]`

**Example 2**

- Input: `strs = ['.GpPE;uLW{Os']`
- Output: `['.GpPE;uLW{Os']`

**Example 3**

- Input: `strs = ['U=6b', 'LBkM`CY/(q=Xav']`
- Output: `['U=6b', 'LBkM`CY/(q=Xav']`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
