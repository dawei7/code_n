## Examples

**Example 1**

- Input: `s = "0234567890112"`
- Output: `[0,11,12]`
- Explanation:

  - At index `0`, the index is written as `"0"`, and `s[0]` is also `"0"`; therefore, index `0` is good.
  - At index `11`, the representation is `"11"`. The ending substring `s[10..11]` is `"11"`, so index `11` is good.
  - At index `12`, the representation is `"12"`. The ending substring `s[11..12]` is `"12"`, so index `12` is good.

  No other index has a matching substring ending at that position. Hence the answer is `[0, 11, 12]`.

**Example 2**

- Input: `s = "01234"`
- Output: `[0,1,2,3,4]`
- Explanation:

  Every index `i` from `0` through `4` has a one-digit decimal representation, and the one-character substring `s[i]` equals that digit.

  A matching ending substring therefore exists at every position, so all five indices are good.

**Example 3**

- Input: `s = "12345"`
- Output: `[]`
- Explanation:

  There is no index whose decimal representation matches a substring ending at that index.

  Consequently, the string has no good indices and the returned array is empty.
