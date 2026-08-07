## Description

You are given an integer array `daysLate` where $\text{daysLate}[i]$ indicates how many days late the $$i^{\text{th}}$$ book was returned.

The penalty is calculated as follows:

- If $\text{daysLate}[i] = 1$, penalty is 1.

- If $2 \le \text{daysLate}[i] \le 5$, penalty is $2 * \text{daysLate}[i]$.

- If $\text{daysLate}[i] > 5$, penalty is $3 * \text{daysLate}[i]$.

Return the total penalty for all books.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** daysLate = [5,1,7]

**Output:** 32

**Explanation:**

- $\text{daysLate}[0] = 5$: Penalty is $2 * \text{daysLate}[0] = 2 * 5 = 10$.

- $\text{daysLate}[1] = 1$: Penalty is `1`.

- $\text{daysLate}[2] = 7$: Penalty is $3 * \text{daysLate}[2] = 3 * 7 = 21$.

- Thus, the total penalty is $10 + 1 + 21 = 32$.

</div>
#### Example 2

<div class="example-block">
**Input:** daysLate = [1,1]

**Output:** 2

**Explanation:**

- $\text{daysLate}[0] = 1$: Penalty is `1`.

- $\text{daysLate}[1] = 1$: Penalty is `1`.

- Thus, the total penalty is $1 + 1 = 2$.

</div>
### Constraints

- $1 \le \text{daysLate.length} \le 100$

- $1 \le \text{daysLate}[i] \le 100$