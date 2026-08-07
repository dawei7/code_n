## Examples

**Example 1**

- Input: `["TwoSum", "add", "add", "add", "find", "find"]`, `[[], [1], [3], [5], [4], [7]]`
- Output: `[null, null, null, null, true, false]`
- Explanation:
  TwoSum twoSum = new TwoSum();
  twoSum.add(1);   // [] --> [1]
  twoSum.add(3);   // [1] --> [1,3]
  twoSum.add(5);   // [1,3] --> [1,3,5]
  twoSum.find(4);  // 1 + 3 = 4, return true
  twoSum.find(7);  // No two integers sum up to 7, return false
