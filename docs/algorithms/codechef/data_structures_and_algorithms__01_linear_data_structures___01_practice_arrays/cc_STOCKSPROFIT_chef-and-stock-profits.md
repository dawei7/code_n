# Chef and Stock Profits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STOCKSPROFIT |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [STOCKSPROFIT](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/STOCKSPROFIT) |

---

## Problem Statement

Chef is observing stock prices.\
You are given an array $prices$ where $prices[i]$ is the price of a given stock on the $i^{\text{th}}$ day.\
Chef wants to maximize his profit by choosing **one day to buy** and a **different future day to sell**.

Return the **maximum profit** Chef can achieve. If no profit is possible, return $0$.

## **Function Declaration**

### **Function Name**

$findMaxProfit$ – Computes the maximum achievable profit by buying on one day and selling on a later day.

### **Parameters**

* $prices$ : A list/array of integers where \
  $prices[i]$ = stock price on day $i$.

### **Return Value**

* Returns an **integer** — \
  the maximum profit Chef can make.
  If no profitable transaction is possible, return $0$.

## Constraints:

* $2 \leq n \leq 10^5$
* $0 \leq prices[i] \leq 10^4$

---

## Input Format

* $n$ → number of days
* Next line → **n integers** representing stock prices

---

## Output Format

Print the maximum profit Chef can achieve.

---

## Examples

**Example 1**

**Input**

```text
7
2 4 1 7 5 3 6
```

**Output**

```text
6
```

**Explanation**

**Buy** on day 3 (price = 1) and **sell** on day 4 (price = 7). Profit = 7 - 1 = 6.

**Example 2**

**Input**

```text
8
9 8 7 6 5 4 3 2
```

**Output**

```text
0
```

**Explanation**

Prices keep falling, so no profit can be made.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef is observing stock prices.\
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

Chef wants to maximize his profit by choosing **one day to buy** and a **different future day to sell**.

Return the **maximum profit** Chef can achieve. If no profit is possible, return `0`.

---

## Key Observations

- To maximize profit, Chef needs to **buy at the lowest price so far** and sell at a **later higher price**.

- At each day `i`, the potential profit is `prices[i] - minPrice`, where `minPrice` is the minimum price seen before day `i`.

- Keeping track of the smallest price up to each day and the maximum profit so far allows us to solve the problem in a single pass

---

## Approach

- Initialize two variables:
   - `minPrice = ∞` (to keep track of the lowest stock price seen so far).
   - `maxProfit = 0` (to store the maximum profit found).

- Traverse the array `prices`:
   - If the current price is smaller than `minPrice`, update `minPrice`.
   - Otherwise, compute `profit = prices[i] - minPrice`.
   - Update `maxProfit` if this profit is greater than the current `maxProfit`.
- After the traversal, `maxProfit` will contain the maximum achievable profit.
- If prices always decrease, no profit can be made → result will be `0`.

---

## Complexity Analysis

- **Time Complexity**: O(n) → single traversal of the array.

- **Space Complexity**: O(1) → only a few variables used.

</details>
