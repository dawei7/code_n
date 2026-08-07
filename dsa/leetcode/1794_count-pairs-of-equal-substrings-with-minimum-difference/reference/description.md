## Description

You are given two strings `firstString` and `secondString` that are **0-indexed** and consist only of lowercase English letters. Count the number of index quadruples `(i,j,a,b)` that satisfy the following conditions:

- $0 \le i \le j < \text{firstString.length}$

- $0 \le a \le b < \text{secondString.length}$

- The substring of `firstString` that starts at the $$i^{\text{th}}$$character and ends at the$$j^{\text{th}}$$character (inclusive) is **equal** to the substring of `secondString` that starts at the$$a^{\text{th}}$$character and ends at the$$b^{\text{th}}$$ character (inclusive).

- $j - a$ is the **minimum** possible value among all quadruples that satisfy the previous conditions.

Return *the **number** of such quadruples*.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

- **Input:** $firstString = "abcd", secondString = "bccda"$
- **Output:** `1`
- **Explanation:** The quadruple (0,0,4,4) is the only one that satisfies all the conditions and minimizes j - a.
#### Example 2

- **Input:** $firstString = "ab", secondString = "cd"$
- **Output:** `0`
- **Explanation:** There are no quadruples satisfying all the conditions.
### Constraints

- $1 \le \text{firstString.length}, \text{secondString.length} \le 2 * 10^{5}$

- Both strings consist only of lowercase English letters.