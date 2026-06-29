# Interleaving String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR31 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR31](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR31) |

---

## Problem Statement

Given three strings `s1`, `s2`, and `s3`, write a recursive function to determine if `s3` can be obtained by interleaving `s1` and `s2`. An interleaving of two strings `s1` and `s2` is a configuration where they are merged in such a way that maintains the left-to-right order of characters from each string.

---

## Input Format

- First line of input contains the string `s1`.
- Second line of input contains the string `s2`.
- Third line of input contains the string `s3`.

---

## Output Format

- Output `True` if `s3` can be obtained by interleaving `s1` and `s2`, else `False`.

---

## Constraints

- The length of `s1`, `s2`, and `s3` will be between 0 and 20.
- All strings consist of lowercase English letters only.

---

## Examples

**Example 1**

**Input**

```text
abc
def
adbcef
```

**Output**

```text
True
```

**Explanation**

s3 = s1[0] + s2[0] + s1[1] + s1[2] + s2[1] + s2[2]

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Interleaving String in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR31)

### [](#problem-statement-1)Problem Statement:

Given three strings `s1`, `s2`, and `s3`, write a recursive function to determine if `s3` can be obtained by interleaving `s1` and `s2`. An interleaving of two strings `s1` and `s2` is a configuration where they are merged in such a way that maintains the left-to-right order of characters from each string.

### [](#approach-2)Approach:

- **Base Case**:

- If `s1`, `s2`, and `s3` are all empty, return `true`. This means that we have successfully interleaved all characters from `s1` and `s2` to form `s3`.

- If `s3` is empty but either `s1` or `s2` still has characters, return `false`. This means we couldn’t completely interleave `s1` and `s2` to form `s3`.

- **Recursive Case**:

- Check the first character of `s1` with the first character of `s3`. If they match, recursively check the remaining parts of `s1`, `s3`, and `s2`.

- Similarly, check the first character of `s2` with `s3`. If they match, recursively check the remaining parts of `s2`, `s3`, and `s1`.

- If either recursive call returns `true`, we have found a valid interleaving.

### [](#complexity-3)Complexity:

- **Time Complexity:** For strings of length `n`, this approach can have an exponential time complexity, approximately `O(2^n)` in the worst case because each recursive call has two possible branches (one for `s1` and one for `s2`).

- **Space Complexity:** The space complexity is `O(n)` due to the depth of the recursive call stack.

</details>
