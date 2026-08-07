### 1. Description

You are given a **0-indexed** 2D integer array `brackets` where $\text{brackets}[i] = [\text{upper}_{i}, \text{percent}_{i}]$ means that the $$i^{\text{th}}$$ tax bracket has an upper bound of $\text{upper}_{i}$ and is taxed at a rate of $\text{percent}_{i}$. The brackets are **sorted** by upper bound (i.e. $\text{upper}_{i}-1 < \text{upper}_{i}$ for `0 < i < brackets.length`).

Tax is calculated as follows:

- The first $\text{upper}_{0}$ dollars earned are taxed at a rate of $\text{percent}_{0}$.

- The next $\text{upper}_{1} - \text{upper}_{0}$ dollars earned are taxed at a rate of $\text{percent}_{1}$.

- The next $\text{upper}_{2} - \text{upper}_{1}$ dollars earned are taxed at a rate of $\text{percent}_{2}$.

- And so on.

You are given an integer `income` representing the amount of money you earned. Return *the amount of money that you have to pay in taxes.* Answers within $10^{-5}$ of the actual answer will be accepted.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $brackets = [[3,50],[7,10],[12,25]], income = 10$
- **Output:** `2.65000`
- **Explanation:**
Based on your income, you have 3 dollars in the 1^st tax bracket, 4 dollars in the 2^nd tax bracket, and 3 dollars in the 3^rd tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50\% +$4 * 10% + $3 * 25\% =$2.65 in taxes.
#### Example 2

- **Input:** $brackets = [[1,0],[4,25],[5,50]], income = 2$
- **Output:** `0.25000`
- **Explanation:**
Based on your income, you have 1 dollar in the 1^st tax bracket and 1 dollar in the 2^nd tax bracket.
The tax rate for the two tax brackets is 0% and 25%, respectively.
In total, you pay $1 * 0\% +$1 * 25% = $0.25 in taxes.
#### Example 3

- **Input:** $brackets = [[2,50]], income = 0$
- **Output:** `0.00000`
- **Explanation:**
You have no income to tax, so you have to pay a total of $0 in taxes.

### 4. Constraints

- $1 \le \text{brackets.length} \le 100$

- $1 \le \text{upper}_{i} \le 1000$

- $0 \le \text{percent}_{i} \le 100$

- $0 \le income \le 1000$

- $\text{upper}_{i}$ is sorted in ascending order.

- All the values of $\text{upper}_{i}$ are **unique**.

- The upper bound of the last tax bracket is greater than or equal to `income`.