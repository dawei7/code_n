### 1. Description

A magician has various spells.

You are given an array `power`, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of $\text{power}[i]$, they **cannot** cast any spell with a damage of $\text{power}[i] - 2$, $\text{power}[i] - 1$, $\text{power}[i] + 1$, or $\text{power}[i] + 2$.

Each spell can be cast **only once**.

Return the **maximum** possible *total damage* that a magician can cast.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** power = [1,1,3,4]

**Output:** 6

**Explanation:**

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

</div>
#### Example 2

<div class="example-block">
**Input:** power = [7,1,6,6]

**Output:** 13

**Explanation:**

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

</div>

### 4. Constraints

- $1 \le \text{power.length} \le 10^{5}$

- $1 \le \text{power}[i] \le 10^{9}$