# Maximum Number of Balls in a Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1742 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/) |

## Problem Description

### Goal

A factory has one ball for every integer label from `lowLimit` through `highLimit`, inclusive. There are infinitely many numbered boxes. Each ball is placed into the box whose number equals the sum of the decimal digits in that ball's label; for example, ball `321` goes into box $3+2+1=6$.

After assigning every ball by this rule, return the greatest number of balls held by any one box. If several boxes tie for the largest occupancy, return that shared occupancy rather than a box number.

### Function Contract

**Inputs**

- `lowLimit`: the smallest ball label.
- `highLimit`: the largest ball label, with $1 \le \texttt{lowLimit} \le \texttt{highLimit} \le 10^5$.

Let $R=\texttt{highLimit}-\texttt{lowLimit}+1$ and let $D$ be the number of decimal digits in `highLimit`.

**Return value**

- Return the maximum frequency of any decimal digit sum among all $R$ labels.

### Examples

**Example 1**

- Input: `lowLimit = 1, highLimit = 10`
- Output: `2`
- Explanation: Labels `1` and `10` both have digit sum $1$, while every other box receives at most one ball.

**Example 2**

- Input: `lowLimit = 5, highLimit = 15`
- Output: `2`
- Explanation: Boxes $5$ and $6$ each receive two balls, which is the maximum occupancy.

**Example 3**

- Input: `lowLimit = 19, highLimit = 28`
- Output: `2`
- Explanation: Labels `19` and `28` both have digit sum $10$.

### Required Complexity

- **Time:** $O(RD)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Reduce each label to its box number**

Visit every integer in the inclusive range. Repeatedly take its last decimal digit with remainder by $10$, add that digit to a running sum, and remove it with integer division by $10$. The resulting sum is exactly the destination box.

**Count occupancies as balls arrive**

Maintain a frequency array indexed by digit sum. A $D$-digit positive integer has digit sum at most $9D$, so only $9D+1$ slots are needed even though the problem describes infinitely many boxes. Increment the selected slot for each ball.

**Track the maximum incrementally**

After updating a box, compare its new occupancy with the best seen so far. Every ball contributes to exactly one box and every box count is updated for all of its balls, so the largest recorded count after the final label is precisely the requested maximum.

#### Complexity detail

Computing one digit sum examines at most $D$ digits for each of the $R$ labels, giving $O(RD)$ time. The frequency array has $9D+1$ entries and therefore uses $O(D)$ auxiliary space. Under the stated upper bound, $D \le 6$, so this storage is also constant in the legal domain.

#### Alternatives and edge cases

- **String conversion:** Summing the characters of each decimal representation has the same $O(RD)$ bound but allocates a temporary string per label.
- **Recount every digit sum:** Storing all sums and calling a linear count for each one is correct but can take $O(R^2)$ time.
- **Single label:** Exactly one box receives one ball, so the answer is one.
- **One-digit interval:** Distinct one-digit labels go to distinct boxes.
- **Powers of ten:** Zero digits still participate in the representation but add nothing to the box number.
- **Tied boxes:** Only the occupancy is returned, so no tie-breaking box identifier is needed.
- **Inclusive upper endpoint:** The ball labeled `highLimit` must be counted.

</details>
