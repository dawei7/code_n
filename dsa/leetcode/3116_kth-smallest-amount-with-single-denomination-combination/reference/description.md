### 1. Description

You are given an integer array `coins` representing coins of different denominations and an integer `k`.

You have an infinite number of coins of each denomination. However, you are **not allowed** to combine coins of different denominations.

Return the $k^{\text{th}}$ **smallest** amount that can be made using these coins.

### 2. Function Contract

**Inputs**

- `coins`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** coins = [3,6,9], k = 3

- **Output:** 9

- **Explanation:** The given coins can make the following amounts:

Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.

Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.

Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.

All of the coins combined produce: 3, 6, <u>**9**</u>, 12, 15, etc.

#### Example 2

- **Input:** coins = [5,2], k = 7

- **Output:** 12

- **Explanation:** The given coins can make the following amounts:

Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.

Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.

All of the coins combined produce: 2, 4, 5, 6, 8, 10, <u>**12**</u>, 14, 15, etc.

### 4. Constraints

- $1 \le \text{coins.length} \le 15$

- $1 \le \text{coins}[i] \le 25$

- $1 \le k \le 2 * 10^{9}$

- `coins` contains pairwise distinct integers.
