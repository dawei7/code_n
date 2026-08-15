# Account Balance After Rounded Purchase

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2806 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/account-balance-after-rounded-purchase/) |

## Problem Description

### Goal

You begin with a bank-account balance of $100$ dollars and make one purchase whose price is `purchaseAmount` dollars. Before deducting the price, round it to the nearest multiple of $10$. Zero counts as a multiple of $10$, and an amount exactly halfway between two multiples is rounded upward: for example, $5$ becomes $10$ and $15$ becomes $20$.

Subtract this rounded amount from the initial balance and return the number of dollars that remain.

### Function Contract

**Inputs**

- `purchaseAmount`: An integer purchase price satisfying $0 \leq \texttt{purchaseAmount} \leq 100$.

**Return value**

Return the integer balance after rounding the purchase price to the nearest multiple of $10$ with half-way values rounded upward, then subtracting it from $100$.

### Examples

#### Example 1

- **Input:** `purchaseAmount = 9`
- **Output:** `90`
- **Explanation:** The nearest multiple of $10$ is $10$, leaving `100 - 10 = 90`.

#### Example 2

- **Input:** `purchaseAmount = 15`
- **Output:** `80`
- **Explanation:** A half-way value rounds upward, so $15$ becomes $20$.

#### Example 3

- **Input:** `purchaseAmount = 10`
- **Output:** `90`
- **Explanation:** The price is already a multiple of $10$ and does not change before subtraction.
