### 1. Description

You are given an integer array `deck` where $\text{deck}[i]$ represents the number written on the $$i^{\text{th}}$$ card.

Partition the cards into **one or more groups** such that:

- Each group has **exactly** `x` cards where `x > 1`, and

- All the cards in one group have the same integer written on them.

Return `true`* if such partition is possible, or *`false`* otherwise*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $deck = [1,2,3,4,4,3,2,1]$
- **Output:** `true`
**Explanation**: Possible partition [1,1],[2,2],[3,3],[4,4].
#### Example 2

- **Input:** $deck = [1,1,1,2,2,2,3,3]$
- **Output:** `false`
**Explanation**: No possible partition.

### 4. Constraints

- $1 \le \text{deck.length} \le 10^{4}$

- $0 \le \text{deck}[i] < 10^{4}$