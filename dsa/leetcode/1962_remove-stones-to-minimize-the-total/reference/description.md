### 1. Description

You are given a **0-indexed** integer array `piles`, where $\text{piles}[i]$ represents the number of stones in the $$i^{\text{th}}$$ pile, and an integer `k`. You should apply the following operation **exactly** `k` times:

- Choose any $\text{piles}[i]$ and **remove** $floor(\text{piles}[i] / 2)$ stones from it.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Notice

that you can apply the operation on the **same** pile more than once.

Return *the **minimum** possible total number of stones remaining after applying the *`k`* operations*.

`floor(x)` is the **largest** integer that is **smaller** than or **equal** to `x` (i.e., rounds `x` down).

### 4. Examples

#### Example 1

- **Input:** $piles = [5,4,9], k = 2$
- **Output:** `12`
- **Explanation:** Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,<u>5</u>].
- Apply the operation on pile 0. The resulting piles are [<u>3</u>,4,5].
The total number of stones in [3,4,5] is 12.
#### Example 2

- **Input:** $piles = [4,3,6,7], k = 3$
- **Output:** `12`
- **Explanation:** Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,<u>3</u>,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,<u>4</u>].
- Apply the operation on pile 0. The resulting piles are [<u>2</u>,3,3,4].
The total number of stones in [2,3,3,4] is 12.

### 5. Constraints

- $1 \le \text{piles.length} \le 10^{5}$

- $1 \le \text{piles}[i] \le 10^{4}$

- $1 \le k \le 10^{5}$