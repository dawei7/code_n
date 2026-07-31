## Examples

**Example 1**

- Input: `nums = [4,5,4]`
- Output: `[4,4,5]`
- Explanation: The reflection trace for each occurrence is:
  - `4` -> binary `100` -> reversed `001` -> `1`
  - `5` -> binary `101` -> reversed `101` -> `5`
  - `4` -> binary `100` -> reversed `001` -> `1`

  Ordering these reflected values produces `[4,4,5]`.

**Example 2**

- Input: `nums = [3,6,5,8]`
- Output: `[8,3,6,5]`
- Explanation: The reflections are:
  - `3` -> binary `11` -> reversed `11` -> `3`
  - `6` -> binary `110` -> reversed `011` -> `3`
  - `5` -> binary `101` -> reversed `101` -> `5`
  - `8` -> binary `1000` -> reversed `0001` -> `1`

  Sorting by reflection yields `[8,3,6,5]`. Values `3` and `6` tie at reflection `3`, so their original values put `3` before `6`.
