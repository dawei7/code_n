## Examples

**Example 1**

- Input: `n = 4, costs = [1,2,3,4]`
- Output: `13`
- Explanation: One minimum-cost route is `0 -> 1 -> 2 -> 4`.

| Jump | Cost calculation | Cost |
|---|---|---:|
| $0 \to 1$ | `costs[1] + (1 - 0)^2 = 1 + 1` | $2$ |
| $1 \to 2$ | `costs[2] + (2 - 1)^2 = 2 + 1` | $3$ |
| $2 \to 4$ | `costs[4] + (4 - 2)^2 = 4 + 4` | $8$ |

The route therefore costs `2 + 3 + 8 = 13`, which is the minimum total.

**Example 2**

- Input: `n = 4, costs = [5,1,6,2]`
- Output: `11`
- Explanation: One minimum-cost route is `0 -> 2 -> 4`.

| Jump | Cost calculation | Cost |
|---|---|---:|
| $0 \to 2$ | `costs[2] + (2 - 0)^2 = 1 + 4` | $5$ |
| $2 \to 4$ | `costs[4] + (4 - 2)^2 = 2 + 4` | $6$ |

The two jumps contribute `5 + 6 = 11` in total, which is optimal.

**Example 3**

- Input: `n = 3, costs = [9,8,3]`
- Output: `12`
- Explanation: Jumping directly from step $0$ to step $3$ costs `costs[3] + (3 - 0)^2 = 3 + 9 = 12`, and no other route is cheaper.
