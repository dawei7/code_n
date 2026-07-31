## Examples

**Example 1**

- Input: `data = [197,130,1]`
- Output: `true`
- Explanation: The bytes are `11000101 10000010 00000001`, which encode one valid two-byte character followed by one valid one-byte character.

**Example 2**

- Input: `data = [235,140,4]`
- Output: `false`
- Explanation: The bytes are `11101011 10001100 00000100`. The leader requests a three-byte character, and the first continuation begins with `10`, but the second continuation does not, so the sequence is invalid.
