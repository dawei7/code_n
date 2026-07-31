## Examples

**Example 1**

- Input: `nums = [3,3,3]`
- Output: `3`
- Explanation: At length one, `[3]` appears three times. At length two, `[3,3]` appears twice. The length-three sequence `[3,3,3]` is the complete array and appears once, so the minimum unique length is `3`.

**Example 2**

- Input: `nums = [2,1,2,3,3]`
- Output: `1`
- Explanation: Among the singleton subarrays, `[2]` appears twice, `[1]` appears once, and `[3]` appears twice. Since `[1]` is already unique, no length smaller than `1` is possible and the answer is `1`.

**Example 3**

- Input: `nums = [1,1,2,2,1]`
- Output: `2`
- Explanation: At length one, `[1]` appears three times and `[2]` appears twice, so neither sequence is unique. At length two, the four subarrays are `[1,1]`, `[1,2]`, `[2,2]`, and `[2,1]`; each appears exactly once. Therefore at least one unique subarray has length `2`, and no unique singleton exists, making `2` the minimum.
