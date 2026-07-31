## Examples

**Example 1**

- Input: `towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2`
- Output: `[3,1]`
- Explanation:
  - Tower `[1, 2, 5]` has Manhattan distance `|1 - 1| + |2 - 1| = 1`, so it is reachable.
  - Tower `[2, 1, 7]` has Manhattan distance `|2 - 1| + |1 - 1| = 1`, so it is reachable.
  - Tower `[3, 1, 9]` has Manhattan distance `|3 - 1| + |1 - 1| = 2`, so it is reachable.

All three towers are reachable. Quality factor `9` is the maximum, and it belongs to the tower at `[3, 1]`.

**Example 2**

- Input: `towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5`
- Output: `[1,3]`
- Explanation:
  - Tower `[1, 3, 4]` has Manhattan distance `|1 - 0| + |3 - 0| = 4`, so it is reachable.
  - Tower `[2, 2, 4]` has Manhattan distance `|2 - 0| + |2 - 0| = 4`, so it is reachable.
  - Tower `[4, 4, 7]` has Manhattan distance `|4 - 0| + |4 - 0| = 8`, so it is not reachable.

The maximum quality among the reachable towers is `4`. Both `[1, 3]` and `[2, 2]` have that quality, and `[1, 3]` is the lexicographically smaller coordinate.

**Example 3**

- Input: `towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1`
- Output: `[-1,-1]`
- Explanation:
  - Tower `[5, 6, 8]` has Manhattan distance `|5 - 1| + |6 - 2| = 8`, so it is not reachable.
  - Tower `[0, 3, 5]` has Manhattan distance `|0 - 1| + |3 - 2| = 2`, so it is not reachable.

Neither tower lies within the radius, so the result is `[-1, -1]`.
