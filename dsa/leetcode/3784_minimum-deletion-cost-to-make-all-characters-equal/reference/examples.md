## Examples

**Example 1**

- Input: `s = "aabaac", cost = [1,2,3,4,1,10]`
- Output: `11`
- Explanation:
  - Delete the characters at indices `0`, `1`, `2`, `3`, and `4`, leaving the one-character string `"c"`.
  - Those deletions cost `cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11`.

**Example 2**

- Input: `s = "abc", cost = [10,5,8]`
- Output: `13`
- Explanation:
  - Delete indices `1` and `2`, so only `"a"` remains.
  - The total deletion cost is `cost[1] + cost[2] = 5 + 8 = 13`.

**Example 3**

- Input: `s = "zzzzz", cost = [67,67,67,67,67]`
- Output: `0`
- Explanation:
  - Every character of `s` is already equal, so no deletion is necessary and the cost is `0`.
