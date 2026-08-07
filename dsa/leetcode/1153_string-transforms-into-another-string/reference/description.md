## Description

Given two strings `str1` and `str2` of the same length, determine whether you can transform `str1` into `str2` by doing **zero or more** *conversions*.

In one conversion you can convert **all** occurrences of one character in `str1` to **any** other lowercase English character.

Return `true` if and only if you can transform `str1` into `str2`.
### Function Contract

**Inputs**

- `str1`: The starting string.
- `str2`: The desired target string.

Both strings have the same length $n$ and contain only lowercase English letters.

**Return value**

- `true` if zero or more global conversions can transform `str1` into `str2`; otherwise, `false`.

### Examples
#### Example 1

- **Input:** $str1 = "aabcc", str2 = "ccdee"$
- **Output:** `true`
- **Explanation:** Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
#### Example 2

- **Input:** $str1 = "leetcode", str2 = "codeleet"$
- **Output:** `false`
- **Explanation:** There is no way to transform str1 to str2.
### Constraints

- $1 \le \text{str1.length} = \text{str2.length} \le 10^{4}$

- `str1` and `str2` contain only lowercase English letters.