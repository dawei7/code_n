## Examples

**Example 1**

- Input: `l = 8, r = 10`
- Output: `3`

- **Explanation:** Both `8` and `9` are one-digit integers, so they are good and therefore fancy. The digits of `10` are `[1,0]`; because `1 > 0`, they are strictly decreasing, making `10` good and fancy as well. All three values in the range qualify, so the result is `3`.

**Example 2**

- Input: `l = 12340, r = 12341`
- Output: `1`

- **Explanation:** The digits `[1,2,3,4,0]` of `12340` are not strictly monotone. Its digit sum is `1 + 2 + 3 + 4 + 0 = 10`, whose digits `[1,0]` are strictly decreasing. Thus `12340` is fancy. The digits `[1,2,3,4,1]` of `12341` are also not strictly monotone, while its digit sum is `1 + 2 + 3 + 4 + 1 = 11`; the equal digits `[1,1]` are not strictly monotone. Thus `12341` is not fancy, leaving exactly one qualifying integer.

**Example 3**

- Input: `l = 123456788, r = 123456788`
- Output: `0`

- **Explanation:** The digits of `123456788` are not strictly monotone because the final two digits are equal. Its digit sum is `1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8 = 44`, and `[4,4]` is not strictly monotone either. The range's only value is therefore not fancy, so the result is `0`.
