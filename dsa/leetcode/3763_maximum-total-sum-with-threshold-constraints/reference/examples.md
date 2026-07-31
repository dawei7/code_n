## Examples

**Example 1**

- Input: `nums = [1,10,4,2,1,6], threshold = [5,1,5,5,2,2]`
- Output: `17`
- Explanation:
  - At `step = 1`, choose `i = 1` because `threshold[1] <= step`. The total becomes `10`, index `1` is marked, and the step advances.
  - At `step = 2`, choose `i = 4`; the total becomes `11` and index `4` is marked.
  - At `step = 3`, choose `i = 5`; the total becomes `17` and index `5` is marked.
  - At `step = 4`, indices `0`, `2`, and `3` all have thresholds greater than `4`, so none can be chosen and the process ends.

**Example 2**

- Input: `nums = [4,1,5,2,3], threshold = [3,3,2,3,3]`
- Output: `0`
- Explanation: At `step = 1`, no index has `threshold[i] <= 1`. The process therefore ends immediately with total `0`.

**Example 3**

- Input: `nums = [2,6,10,13], threshold = [2,1,1,1]`
- Output: `31`
- Explanation:
  - At `step = 1`, choose `i = 3`; the total becomes `13` and index `3` is marked.
  - At `step = 2`, choose `i = 2`; the total becomes `23` and index `2` is marked.
  - At `step = 3`, choose `i = 1`; the total becomes `29` and index `1` is marked.
  - At `step = 4`, choose `i = 0`; the total becomes `31` and index `0` is marked.
  - All indices have now been chosen, so the process ends after step `4`.
