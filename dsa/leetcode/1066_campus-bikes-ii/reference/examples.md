## Examples

**Example 1**

- Input: `workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]`
- Output: `6`
- Explanation: Assign bike 0 to worker 0 and bike 1 to worker 1. Each assigned pair has Manhattan distance `3`, so their total is `6`.

The first source coordinate plot contains these labeled positions:

| Entity | Index | X | Y |
|---|---:|---:|---:|
| Worker | 0 | 0 | 0 |
| Worker | 1 | 2 | 1 |
| Bike | 0 | 1 | 2 |
| Bike | 1 | 3 | 3 |

**Example 2**

- Input: `workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]`
- Output: `4`
- Explanation: Assign bike 0 to worker 0. For the other two workers, either assign bike 1 to worker 1 and bike 2 to worker 2, or swap those two bike assignments. Both choices produce a total Manhattan distance of `4`.

The second source coordinate plot contains these labeled positions:

| Entity | Index | X | Y |
|---|---:|---:|---:|
| Worker | 0 | 0 | 0 |
| Worker | 1 | 1 | 1 |
| Worker | 2 | 2 | 0 |
| Bike | 0 | 1 | 0 |
| Bike | 1 | 2 | 2 |
| Bike | 2 | 2 | 1 |

**Example 3**

- Input: `workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]`
- Output: `4995`

**Additional Examples**

**Single worker**

- Input: `workers = [[0,0]], bikes = [[5,5]]`
- Output: `10`

The only assignment has Manhattan distance $\lvert 0-5\rvert+\lvert 0-5\rvert=10$.
