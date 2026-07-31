## Examples

**Example 1**

- Input: `hp = 11, damage = [3,6,7], requirement = [4,2,5]`
- Output: `3`
- Explanation: The three run scores are `score(1) = 2`, `score(2) = 1`, and `score(3) = 0`, so their sum is `2 + 1 + 0 = 3`. In detail, the run starting at room 1 proceeds as follows:
  - It starts with 11 health.
  - Room 1 leaves `11 - 3 = 8`; because `8 >= 4`, this earns one point.
  - Room 2 leaves `8 - 6 = 2`; because `2 >= 2`, this earns another point.
  - Room 3 leaves `2 - 7 = -5`; because `-5 < 5`, it earns no point.

  Therefore `score(1) = 2`.

**Example 2**

- Input: `hp = 2, damage = [10000,1], requirement = [1,1]`
- Output: `1`
- Explanation: Here `score(1) = 0` and `score(2) = 1`, giving `0 + 1 = 1` in total.

  For the run from room 1:
  - It starts with 2 health.
  - Room 1 leaves `2 - 10000 = -9998`, which is below `1`, so no point is earned.
  - The run continues into room 2 and leaves `-9998 - 1 = -9999`, also below `1`, so this room earns no point either.

  For the run from room 2, health resets to 2. Entering that room leaves `2 - 1 = 1`, which meets `1 >= 1`; hence `score(2) = 1`.
