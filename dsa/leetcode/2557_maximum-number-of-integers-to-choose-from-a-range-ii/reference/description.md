### 1. Description

You are given an integer array `banned` and two integers `n` and `maxSum`. You are choosing some number of integers following the below rules:

- The chosen integers have to be in the range `[1, n]`.

- Each integer can be chosen **at most once**.

- The chosen integers should not be in the array `banned`.

- The sum of the chosen integers should not exceed `maxSum`.

Return *the **maximum** number of integers you can choose following the mentioned rules*.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** $banned = [1,4,6], n = 6, maxSum = 4$
- **Output:** `1`
- **Explanation:** You can choose the integer 3.
3 is in the range [1, 6], and do not appear in banned. The sum of the chosen integers is 3, which does not exceed maxSum.

#### Example 2

- **Input:** $banned = [4,3,5,6], n = 7, maxSum = 18$
- **Output:** `3`
- **Explanation:** You can choose the integers 1, 2, and 7.
All these integers are in the range [1, 7], all do not appear in banned, and their sum is 10, which does not exceed maxSum.

### 4. Constraints

- $1 \le \text{banned.length} \le 10^{5}$

- $1 \le \text{banned}[i] \le n \le 10^{9}$

- $1 \le maxSum \le 10^{15}$
