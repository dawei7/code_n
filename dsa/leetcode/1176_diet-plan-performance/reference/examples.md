## Examples

**Example 1**

- Input: `calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3`
- Output: `0`

- Explanation: Because `k = 1`, each entry forms its own window. The totals `1` and `2` each lose a point, `3` is neutral, and `4` and `5` each gain a point, so the losses and gains cancel.

**Example 2**

- Input: `calories = [3,2], k = 2, lower = 0, upper = 1`
- Output: `1`

- Explanation: There is one length-two window. Its total is `3 + 2 = 5`, which is greater than `upper`, so the dieter gains one point.

**Example 3**

- Input: `calories = [6,5,0,0], k = 2, lower = 1, upper = 5`
- Output: `0`

- Explanation: The first total, `6 + 5 = 11`, is above `upper` and gains one point. The next total, `5 + 0 = 5`, lies within the inclusive neutral interval. The final total, `0 + 0 = 0`, is below `lower` and loses one point, leaving a score of zero.
