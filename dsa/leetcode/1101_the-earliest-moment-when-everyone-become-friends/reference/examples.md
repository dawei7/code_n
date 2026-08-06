## Examples

**Example 1**

- **Input:** `logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6`
- **Output:** `20190301`
- **Explanation:** The chronological group changes are:
  1. At `20190101`, people 0 and 1 join, leaving `[0,1]`, `[2]`, `[3]`, `[4]`, and `[5]`.
  2. At `20190104`, people 3 and 4 join, leaving `[0,1]`, `[2]`, `[3,4]`, and `[5]`.
  3. At `20190107`, the friendship between 2 and 3 forms `[2,3,4]`, so the groups are `[0,1]`, `[2,3,4]`, and `[5]`.
  4. At `20190211`, the friendship between 1 and 5 forms `[0,1,5]`, leaving that group and `[2,3,4]`.
  5. At `20190224`, people 2 and 4 are already acquainted, so the groups do not change.
  6. At `20190301`, the friendship between 0 and 3 merges the final two groups, and everyone is acquainted.

**Example 2**

- **Input:** `logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4`
- **Output:** `3`
- **Explanation:** At timestamp `3`, all four people—0, 1, 2, and 3—belong to one acquaintance group.
