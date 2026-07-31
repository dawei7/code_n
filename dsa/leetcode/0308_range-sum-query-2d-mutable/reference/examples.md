## Examples

**Example 1**

- Input: `["NumMatrix","sumRegion","update","sumRegion"], [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]`
- Output: `[null,8,null,10]`
- Explanation: Construct `NumMatrix` from the given matrix. `sumRegion(2,1,4,3)` initially returns `8`. Then `update(3,2,2)` changes the value at row `3`, column `2` from `0` to `2`. Repeating the same region query returns `10`.

The source illustration compares the queried rectangle before and after that update:

```text
before update        after update
3 0 1 4 2            3 0 1 4 2
5 6 3 2 1            5 6 3 2 1
1 [2 0 1] 5          1 [2 0 1] 5
4 [1 0 1] 7    ->    4 [1 2 1] 7
1 [0 3 0] 5          1 [0 3 0] 5

rectangle sum: 8     rectangle sum: 10
```
