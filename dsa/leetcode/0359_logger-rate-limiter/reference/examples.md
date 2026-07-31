## Examples

**Example 1**

- Input: `operations = ["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"], arguments = [[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]`
- Output: `[null,true,true,false,false,false,true]`
- Explanation:
  1. Construct `Logger`.
  2. Printing `"foo"` at time `1` is allowed, so that message becomes eligible again at time `11`.
  3. Printing `"bar"` at time `2` is allowed, so it becomes eligible again at time `12`.
  4. The `"foo"` call at time `3` is rejected because $3 < 11$.
  5. The `"bar"` call at time `8` is rejected because $8 < 12$.
  6. The `"foo"` call at time `10` is rejected because $10 < 11$.
  7. The `"foo"` call at time `11` is allowed, and its next eligible time becomes `21`.
