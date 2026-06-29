# Linear Search in string

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO04 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO04](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO04) |

---

## Problem Statement

Given a string and a character as input, print the first position of the character in the string if it is present. If the character does not exist in the string, print "**-1**".

---

## Input Format

- The first line contains a string.
- The second line contains a single character.

---

## Output Format

- Print the **first position** (0-based index) of the character in the string if it is present.
- Print "**-1**" if the character is not present in the string.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
HelloHowYouDoing
w
```

**Output**

```text
7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO04)

#### [](#problem-understanding-1)Problem Understanding

The problem requires us to determine the first position of a specified character in a given string. If the character exists in the string, we need to print its index (0-based). If the character does not exist in the string, we should print `-1`.

#### [](#approach-2)Approach

To solve the problem, we use a simple linear search approach. We iterate through each character in the string, comparing it to the target character. If we find a match, we immediately record the index of the first occurrence and break out of the loop. If no match is found after checking all characters, we output `-1` to indicate that the character is not present in the string. This method ensures we efficiently find the first occurrence with a time complexity of O(n), where n is the length of the string.

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of this solution is O(n), where `n` is the length of the input string. In the worst case, the algorithm might need to check each character of the string to determine if the `searchChar` is present.

-

**Space Complexity**: The space complexity is O(1), as the solution only uses a few extra variables (`position` and loop counters) regardless of the input size.

#### [](#edge-cases-4)Edge Cases

- If the input string is empty, the algorithm will immediately output `-1`, as there are no characters to search through.

- If the `searchChar` is the first character in the string, the algorithm will quickly find it and output `0`.

- If the `searchChar` does not exist in the string, the algorithm will correctly output `-1`.

</details>
