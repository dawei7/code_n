# Longest Palindromic Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR32 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR32](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR32) |

---

## Problem Statement

Given a string `s`, your task is to find the length of the longest subsequence that is a palindrome.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A **palindrome** is a string/sequence that reads the same backwards as forwards, e.g. *madam*.

---

## Input Format

- The only line of input contains a string `s`.

---

## Output Format

- Output the length of longest palindromic subsequence of `s`.

---

## Constraints

- The length of `s` will be at most 20.
- All strings consist of lowercase English letters only.

---

## Examples

**Example 1**

**Input**

```text
agbdba
```

**Output**

```text
5
```

**Explanation**

The longest palindromic subsequence is "abdba".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Longest Palindromic Subsequence in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR32)

### [](#problem-statement-1)Problem Statement:

Given a string `s`, your task is to find the length of the longest subsequence that is a palindrome.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A **palindrome** is a string/sequence that reads the same backward as forwards, e.g. *madam*.

### [](#approach-2)Approach:

We are using two pointers, `start` and `end`, where `start` denotes the character at the 0th position, and `end` denotes the character at the (n-1)th position.

- **Base Cases**:

- If the start index is greater than the end index, return 0 (no valid subsequence).

- If the start index equals the end index, return 1 (a single character is a palindrome).

- **Matching Characters**:

- If the characters at the start and end indices match, add 2 to the result and recurse on the substring between these indices.

- **Non-Matching Characters**:

- If the characters do not match, recursively explore two options:

- Exclude the start character.

- Exclude the end character.

- Return the maximum length of the subsequences from both options.

- **Recursion** continues until all possible subsequences are explored.

### [](#complexity-3)Complexity:

- **Time Complexity:** The time complexity of this approach is `O(2^n)` because every recursive call branches into two subproblems (exploring the start and end characters)

- **Space Complexity:** `O(n)` due to the depth of the recursion stack, where `n` is the length of the string.

</details>
