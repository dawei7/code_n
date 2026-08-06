## Examples

**Example 1**

- **Input:** `s = "abc", shift = [[0,1],[1,2]]`
- **Output:** `"cab"`
- **Explanation:** Operation `[0,1]` shifts left once, changing `"abc"` to `"bca"`. Operation `[1,2]` then shifts that result right twice, producing `"cab"`.

**Example 2**

- **Input:** `s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]`
- **Output:** `"efgabcd"`
- **Explanation:** The first right shift changes `"abcdefg"` to `"gabcdef"`, and the second changes it to `"fgabcde"`. Shifting left by two restores `"abcdefg"`; the final right shift by three yields `"efgabcd"`.
