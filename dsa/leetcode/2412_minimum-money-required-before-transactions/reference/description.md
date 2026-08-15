### 1. Description

You are given a **0-indexed** 2D integer array `transactions`, where $\text{transactions}[i] = [\text{cost}_{i}, \text{cashback}_{i}]$.

The array describes transactions, where each transaction must be completed exactly once in **some order**. At any given moment, you have a certain amount of `money`. In order to complete transaction `i`, $money \ge \text{cost}_{i}$ must hold true. After performing a transaction, `money` becomes $money - \text{cost}_{i} + \text{cashback}_{i}$.

Return* the minimum amount of *`money`* required before any transaction so that all of the transactions can be completed **regardless of the order** of the transactions.*

### 2. Function Contract

**Inputs**

- `transactions`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $transactions = [[2,1],[5,0],[4,2]]$
- **Output:** `10`
- **Explanation:** 
**Starting with money = 10, the transactions can be performed in any order.
It can be shown that starting with money < 10 will fail to complete all transactions in some order.

#### Example 2

- **Input:** $transactions = [[3,0],[0,3]]$
- **Output:** `3`
- **Explanation:** 
- If transactions are in the order [[3,0],[0,3]], the minimum money required to complete the transactions is 3.
- If transactions are in the order [[0,3],[3,0]], the minimum money required to complete the transactions is 0.
Thus, starting with money = 3, the transactions can be performed in any order.

### 4. Constraints

- $1 \le \text{transactions.length} \le 10^{5}$

- $\text{transactions}[i].length = 2$

- $0 \le \text{cost}_{i}, \text{cashback}_{i} \le 10^{9}$
