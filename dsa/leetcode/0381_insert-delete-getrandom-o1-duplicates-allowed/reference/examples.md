## Examples

**Example 1**

- Input: `operations = ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"], arguments = [[],[1],[1],[2],[],[1],[]]`
- Output: `[null,true,false,true,2,true,1]`
- Explanation:
  1. Construct the collection, then insert `1`; because it was absent, the call returns `true`.
  2. Insert another `1`; the call returns `false`, but the occurrence is still added, producing `[1,1]`.
  3. Insert `2`, which returns `true` and produces `[1,1,2]`.
  4. A random draw returns `1` with probability $2/3$ and `2` with probability $1/3$; the shown run returns `2`.
  5. Remove one `1`, leaving `[1,2]`.
  6. The final draw chooses `1` or `2` with equal probability; the shown run returns `1`.
