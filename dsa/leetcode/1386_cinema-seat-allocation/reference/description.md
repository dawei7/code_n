## Description

![](images/cinema_seats_1.png)

A cinema has `n` rows of seats, numbered from 1 to `n`. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array `reservedSeats`, where $\text{reservedSeats}[i] = [\text{row}_{i}, \text{seat}_{i}]$ means that seat $\text{seat}_{i}$ in row $\text{row}_{i}$ is already reserved.

A four-person group must be assigned to four seats in the **same** row. The group can be seated in one of the following seat blocks:

- seats `2, 3, 4, 5`

- seats `4, 5, 6, 7`

- seats `6, 7, 8, 9`

A block can be used only if **none** of its seats are reserved. Each seat can be assigned to **at most **one group.

Return an integer denoting the **maximum** number of four-person groups that can be assigned.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/cinema_seats_3.png)

- **Input:** $n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]$
- **Output:** `4`
- **Explanation:** The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
#### Example 2

- **Input:** $n = 2, reservedSeats = [[2,1],[1,8],[2,6]]$
- **Output:** `2`
#### Example 3

- **Input:** $n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]$
- **Output:** `4`
### Constraints

- $1 \le n \le 10^{9}$

- $1 \le \text{reservedSeats.length} \le min(10 * n, 10^{4})$

- $\text{reservedSeats}[i] = [\text{row}_{i}, \text{seat}_{i}]$

- $1 \le \text{row}_{i} \le n$

- $1 \le \text{seat}_{i} \le 10$

- All $\text{reservedSeats}[i]$ are distinct.