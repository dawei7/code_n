## Examples

**Example 1**

- Input: `nums = [20,10,30,30]`
- Output: `30`
- Explanation:
  - The value `20` occurs once.
  - The value `10` also occurs once.
  - The value `30` occurs twice.
  - Only `30` has frequency two, so its frequency is unique and it is the first qualifying element.

**Example 2**

- Input: `nums = [20,20,10,30,30,30]`
- Output: `20`
- Explanation:
  - The value `20` occurs twice.
  - The value `10` occurs once.
  - The value `30` occurs three times.
  - Frequencies two, one, and three each belong to exactly one distinct value. All three values therefore qualify, and `20` is encountered first in the array.

**Example 3**

- Input: `nums = [10,10,20,20]`
- Output: `-1`
- Explanation:
  - The value `10` occurs twice.
  - The value `20` also occurs twice.
  - Both distinct values share the same frequency, so neither frequency is unique and no element qualifies.
