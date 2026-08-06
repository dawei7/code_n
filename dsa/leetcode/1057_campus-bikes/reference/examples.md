## Examples

**Example 1**

- Input: `workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]`
- Output: `[1,0]`
- Explanation: Worker 1 and bike 0 form the uniquely closest available pair, so they are assigned first. Worker 0 then receives bike 1, producing `[1,0]` in worker-index order.

The source coordinate plot contains the following labeled positions:

| Entity | Index | X | Y |
|---|---:|---:|---:|
| Worker | 0 | 0 | 0 |
| Worker | 1 | 2 | 1 |
| Bike | 0 | 1 | 2 |
| Bike | 1 | 3 | 3 |

**Example 2**

- Input: `workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]`
- Output: `[0,2,1]`
- Explanation: Worker 0 receives bike 0 first. Worker 1 and worker 2 are then equally far from bike 2, so the smaller worker index gives bike 2 to worker 1. Worker 2 receives bike 1, yielding `[0,2,1]`.

The source coordinate plot contains the following labeled positions:

| Entity | Index | X | Y |
|---|---:|---:|---:|
| Worker | 0 | 0 | 0 |
| Worker | 1 | 1 | 1 |
| Worker | 2 | 2 | 0 |
| Bike | 0 | 1 | 0 |
| Bike | 1 | 2 | 2 |
| Bike | 2 | 2 | 1 |
