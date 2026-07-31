## Examples

**Example 1**

- Input: `words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]`
- Output: `"rij"`
- Explanation:
  - The weight of `"abcd"` is `5 + 3 + 12 + 14 = 34`. Its residue is `34 % 26 = 8`, which maps to `'r'`.
  - The weight of `"def"` is `14 + 1 + 2 = 17`. Its residue is `17 % 26 = 17`, which maps to `'i'`.
  - The weight of `"xyz"` is `7 + 7 + 2 = 16`. Its residue is `16 % 26 = 16`, which maps to `'j'`.

Thus, concatenating the mapped characters produces `"rij"`.

**Example 2**

- Input: `words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]`
- Output: `"yyy"`
- Explanation: Every word has weight 1. The residue `1 % 26 = 1` maps to `'y'`.

Thus, concatenating the mapped characters produces `"yyy"`.

**Example 3**

- Input: `words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]`
- Output: `"g"`
- Explanation: The weight of `"abcd"` is `7 + 5 + 3 + 4 = 19`. Its residue is `19 % 26 = 19`, which maps to `'g'`.

Thus, concatenating the mapped characters produces `"g"`.
