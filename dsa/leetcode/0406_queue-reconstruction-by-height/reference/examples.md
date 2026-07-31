## Examples

**Example 1**

- Input: `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
- Output: `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`
- Explanation: In the returned queue, the first two people of heights `5` and `7` each have no preceding person at least as tall. The next height-`5` person has the first two people ahead; height `6` has only the height-`7` person ahead; height `4` has the first four people ahead; and the final height-`7` person has the earlier height-`7` person ahead. These counts are respectively `0,0,2,1,4,1`, exactly matching the stored `k` values.

**Example 2**

- Input: `people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]`
- Output: `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`
