# Count Pairs of Equal Substrings With Minimum Difference

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/) |
| Frontend ID | 1794 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given two 0-indexed strings `firstString` and `secondString`, both containing only lowercase English letters. Consider every index quadruple $(i,j,a,b)$ satisfying

$$
0 \le i \le j < \lvert\texttt{firstString}\rvert
\quad\text{and}\quad
0 \le a \le b < \lvert\texttt{secondString}\rvert.
$$

The quadruple is eligible when the inclusive substring `firstString[i:j + 1]` equals `secondString[a:b + 1]`. Among all eligible quadruples, find the minimum possible value of $j-a$.

Return how many eligible quadruples attain that global minimum. If the two strings have no equal nonempty substrings, return zero.

### Function Contract

**Inputs**

- `firstString`: a lowercase English string of length $n$, where $1 \le n \le 2\cdot 10^5$.
- `secondString`: a lowercase English string of length $m$, where $1 \le m \le 2\cdot 10^5$.

**Return value**

- Return the number of equal-substring quadruples whose value $j-a$ is minimum over every eligible quadruple.

### Examples

**Example 1**

- Input: `firstString = "abcd", secondString = "bccda"`
- Output: `1`

The singleton match `(i, j, a, b) = (0, 0, 4, 4)` is the unique quadruple with minimum difference.

**Example 2**

- Input: `firstString = "ab", secondString = "cd"`
- Output: `0`

The strings share no character, so no equal nonempty substrings exist.

**Example 3**

- Input: `firstString = "abc", secondString = "abc"`
- Output: `3`

The three same-position singleton matches all have difference zero; longer equal substrings have a larger value.

### Required Complexity

- **Time:** $O(n+m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Prove that a minimum match has length one**

Suppose an eligible pair of equal substrings has length $L>1$. Their final characters, at indices $j$ and $b$, are equal. They alone form another eligible quadruple $(j,j,b,b)$ whose difference is $j-b$.

Because the second substring has $b=a+L-1>a$, this singleton has

$$
j-b < j-a.
$$

The longer quadruple therefore cannot minimize $j-a$. Every globally minimum quadruple must match one character, with $i=j$ and $a=b$. Conversely, each shared character occurrence pair gives such an eligible singleton.

**Choose the extreme occurrence for each character**

For a fixed character $c$, a singleton pair at indices $i$ and $a$ contributes $i-a$. This is minimized by taking the earliest occurrence of $c$ in `firstString` and the latest occurrence of $c$ in `secondString`.

Those two positions are unique. Any later first-string position adds a positive amount, and any earlier second-string position subtracts a smaller index, so no other occurrence pair of $c$ can tie its best difference.

**Count characters tied for the global minimum**

Scan `firstString` to retain the first index of each character, and scan `secondString` to retain the last index of each character. For every character present in both strings, compute

$$
d_c
=
\operatorname{first}_{\texttt{firstString}}(c)
-
\operatorname{last}_{\texttt{secondString}}(c).
$$

The smallest $d_c$ is the minimum possible $j-a$. Since each character contributes exactly one occurrence pair at its own minimum, the answer is the number of shared characters whose $d_c$ equals that smallest value. If there is no shared character, there is no eligible quadruple and the answer is zero.

#### Complexity detail

The two occurrence scans inspect $n+m$ characters. Comparing the resulting entries examines at most the 26 lowercase letters, so total time is $O(n+m)$. The occurrence tables have fixed alphabet size and therefore use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Compare every character pair:** Testing all $nm$ singleton pairs is correct after the length-one reduction, but it is unnecessarily quadratic.
- **Enumerate and compare all substrings:** This obscures the singleton proof and creates at least quadratic candidate sets in each string, with much worse comparison cost.
- **Store every occurrence:** Full position lists are unnecessary because only the earliest first-string and latest second-string occurrences can minimize the difference.
- **No shared character:** No equal nonempty substring exists, so return zero without taking a minimum of an empty collection.
- **Repeated occurrences:** Repetition changes the extreme indices but cannot create multiple best pairs for one character.
- **Ties across characters:** Different characters may have the same minimum difference; each contributes one quadruple and must be counted.
- **Negative differences:** They are valid and arise when the chosen second-string index is later than the chosen first-string index.
- **Minimum-length strings:** Two equal one-character strings yield one quadruple; two different characters yield zero.

</details>
