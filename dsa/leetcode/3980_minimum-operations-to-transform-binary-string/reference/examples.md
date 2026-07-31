## Examples

**Example 1**

- Input: `s1 = "11", s2 = "00"`
- Output: `1`
- **Explanation:** Apply the adjacent-pair operation to indices `0` and `1`. Both characters change from `'1'` to `'0'`, so `"11"` becomes `"00"` in one operation.

**Example 2**

- Input: `s1 = "01", s2 = "10"`
- Output: `3`
- **Explanation:** First change index `0` from `'0'` to `'1'`, producing `"11"`. Next clear indices `0` and `1` together, producing `"00"`. Finally change index `0` from `'0'` to `'1'`, producing `"10"`. These three operations are minimum.

**Example 3**

- Input: `s1 = "1", s2 = "0"`
- Output: `-1`
- **Explanation:** The single-position operation cannot turn `'1'` into `'0'`, while the pair operation needs two adjacent characters. The target is therefore unreachable.
