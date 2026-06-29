# Longest Substring Without Repeating Characters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLDW0103 |
| Difficulty Rating | 932 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SLDW0103](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0103) |

---

## Problem Statement

Given a string $S$ of length $N$, you have to output the length of the **longest substring** of $S$ with **non-repeating characters**.

A **substring** is a contiguous sequence of characters within the string.
The substring must not contain any character that appears more than once.

**Example:**

`S = "abcabcbb"`

* Longest substring without repeating characters: `"abc"`
* Output: `3`

## Function Declaration

### Function Name

$longestUniqueSubstring$ – This function computes the length of the longest contiguous substring of a given string that contains no repeating characters.

### Parameters

* $S$ : A string of length $N$ consisting of characters (typically lowercase English letters, but the logic is character-agnostic).

### Return Value

* Returns an integer representing the **maximum length** of a substring of $S$ such that **each character appears at most once** in that substring.

## Constraints

* $2 \leq N \leq 10^5$
* $S$ contains valid characters (no restriction on character set unless specified)
* The solution should be efficient enough to handle large input sizes

---

## Input Format

- The first and only line of input contains a single string $S$.

---

## Output Format

- Output the length of the longest substring with no repeating characters.

---

## Constraints

- $2 \leq N \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
abcabcbb
```

**Output**

```text
3
```

**Explanation**

The answer is "abc" with length 3.

**Example 2**

**Input**

```text
bbbb
```

**Output**

```text
1
```

**Example 3**

**Input**

```text
abcccdefg
```

**Output**

```text
5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Longest Substring Without Repeating Characters](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0103)

### [](#problem-statement-1)Problem Statement

Given a string ***S*** of length ***N***, output the length of the longest substring of ***S*** with non-repeating characters. This means no character in the substring should appear more than once. We can use the sliding window technique to solve this problem.

To implement this, we’ll use a frequency map to track the occurrences of characters. We’ll expand the window by adding characters until a duplicate is found. When a duplicate character is encountered, we’ll start shrinking the window from the left until each character in the window appears only once.

### [](#approach-2)Approach

The code uses a sliding window with two pointers, ***left*** and ***right***, to find the longest substring without repeating characters. Moving ***right*** over each character, we track character counts in a frequency map. When a duplicate is found (frequency > 1), ***left*** is moved forward to shrink the window until all characters are unique. After each adjustment, the window length is calculated, updating ***longest*** if this length is the largest so far. This continues until all characters are scanned, with ***longest*** holding the maximum length of a substring without repeats.

### [](#time-complexity-3)Time Complexity

O(N), where ***N*** is the length of the string, as each character is processed at most twice.

### [](#space-complexity-4)Space Complexity

O(K), where ***K*** is the number of unique characters, due to the frequency map used to store character counts.

</details>
