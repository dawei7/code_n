## Examples

**Example 1**

- Input: `operations = ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"], arguments = [[],[1],[2],[2],[],[1],[2],[]]`
- Output: `[null,true,false,true,2,true,false,2]`
- Explanation:
  1. Construct an empty `RandomizedSet` and insert `1`, which returns `true`.
  2. Removing absent value `2` returns `false`.
  3. Insert `2`; the set is now `{1,2}`.
  4. The first `getRandom()` may return either `1` or `2`; the displayed run returns `2`.
  5. Remove `1`, leaving only `2`.
  6. Inserting `2` again returns `false`, and the final random call must return `2`.
