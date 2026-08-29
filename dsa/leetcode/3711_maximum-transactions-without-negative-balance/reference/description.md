### 1. Description

You are given an integer array `transactions`, where $\text{transactions}[i]$ represents the amount of the $i^{\text{th}}$ transaction:

- A positive value means money is **received**.

- A negative value means money is **sent**.

The account starts with a balance of 0, and the balance **must never become negative**. Transactions must be considered in the given order, but you are allowed to skip some transactions.

Return an integer denoting the **maximum number of transactions** that can be performed without the balance ever going negative.

### 2. Function Contract

**Inputs**

- `transactions`: An ordered array of signed transaction amounts.

The performed transactions form a subsequence of this array. Starting from zero, every prefix sum of that chosen subsequence must be at least zero; a later receipt cannot repair a balance that was negative earlier.

**Return value**

Return the largest possible number of performed transactions. The selected amounts themselves do not need to be returned.

### 3. Examples

#### Example 1

- **Input:** transactions = [2,-5,3,-1,-2]

- **Output:** 4

- **Explanation:** One optimal sequence is `[2, 3, -1, -2]`, balance: `0 → 2 → 5 → 4 → 2`.

#### Example 2

- **Input:** transactions = [-1,-2,-3]

- **Output:** 0

- **Explanation:** All transactions are negative. Including any would make the balance negative.

#### Example 3

- **Input:** transactions = [3,-2,3,-2,1,-1]

- **Output:** 6

- **Explanation:** All transactions can be taken in order, balance: `0 → 3 → 1 → 4 → 2 → 3 → 2`.

### 4. Constraints

- $1 \le \text{transactions.length} \le 10^{5}$

- $-10^{9} \le \text{transactions}[i] \le 10^{9}$
