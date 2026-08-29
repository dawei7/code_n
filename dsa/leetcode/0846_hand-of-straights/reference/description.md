### 1. Description

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where $\text{hand}[i]$ is the value written on the $i^{\text{th}}$ card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

### 2. Function Contract

**Inputs**

- `hand`: Input parameter (`List[int]`).
- `groupSize`: Input parameter (`int`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** $hand = [1,2,3,6,2,3,4,7,8], groupSize = 3$
- **Output:** `true`
- **Explanation:** Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

#### Example 2

- **Input:** $hand = [1,2,3,4,5], groupSize = 4$
- **Output:** `false`
- **Explanation:** Alice's hand can not be rearranged into groups of 4.

### 4. Constraints

- $1 \le \text{hand.length} \le 10^{4}$

- $0 \le \text{hand}[i] \le 10^{9}$

- $1 \le groupSize \le \text{hand.length}$

### 5. Note

This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a>
