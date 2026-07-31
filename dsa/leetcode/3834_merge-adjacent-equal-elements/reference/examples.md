## Examples

**Example 1**

- Input: `nums = [3,1,1,2]`
- Output: `[3,4]`
- Explanation: The equal middle values merge first, changing the array to `[3,2,2]`. The new equal pair of `2` values then merges to produce `[3,4]`. No equal neighbors remain, so that array is final.

**Example 2**

- Input: `nums = [2,2,4]`
- Output: `[8]`
- Explanation: Merging the first pair gives `[4,4]`. Those two equal values merge again, leaving the single value `[8]`.

**Example 3**

- Input: `nums = [3,7,5]`
- Output: `[3,7,5]`
- Explanation: The input has no adjacent equal values, so the process performs no operation and returns the array unchanged.

