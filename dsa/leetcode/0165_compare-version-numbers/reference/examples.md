## Examples

**Example 1**

- Input: `version1 = "1.2", version2 = "1.10"`
- Output: `-1`
- Explanation: The second revisions have integer values `2` and `10`. Because $2 < 10$, `version1 < version2`.

**Example 2**

- Input: `version1 = "1.01", version2 = "1.001"`
- Output: `0`
- Explanation: Ignoring leading zeroes, revisions `"01"` and `"001"` both have integer value `1`.

**Example 3**

- Input: `version1 = "1.0", version2 = "1.0.0.0"`
- Output: `0`
- Explanation: The missing revisions in `version1` are treated as zero, so they equal the trailing zero revisions in `version2`.
