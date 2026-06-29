# Longest Common Prefix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LONGESPREFIX |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [LONGESPREFIX](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/LONGESPREFIX) |

---

## Problem Statement

You are given a list of $N$ strings. Your task is to find the **longest common prefix** shared by all the strings.

If there is **no common prefix**, return an empty string (`""`).

## Function Declaration

### Function Name

$longestCommonPrefix$ – This function finds the longest common prefix among a list of strings.

### Parameters

* $strs$ : A reference to a vector of strings containing $N$ strings.

### Return Value

* Returns a **string** representing the longest common prefix among all given strings.
* Returns an **empty string (`""`)** if no common prefix exists.

### Constraints

* $ 1 \leq N \leq 200 $
* $ 0 \leq |strs[i]| \leq 200 $
* Each string contains only lowercase English letters ($a – z$).

---

## Input Format

* The first line contains a single integer $N$, the number of strings.
* The next $N$ lines each contain one string.

---

## Output Format

* Print the **longest common prefix** among all strings.
* If no common prefix exists, print an empty string $""$.

---

## Constraints

- $1 \le N \le 200$
- $0 \le |S[i]| \le 200$
- $\text{Each string consists of lowercase English letters only.}$

---

## Examples

**Example 1**

**Input**

```text
4
interview
internet
internal
interval
```

**Output**

```text
inter
```

**Explanation**

All strings start with `"inter"`, which is the longest common prefix.

**Example 2**

**Input**

```text
3
apple
ape
april
```

**Output**

```text
ap
```

**Explanation**

All strings start with `"ap"` — that’s the longest common prefix.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Understanding

We are given **N strings**, and we need to find the **longest common prefix (LCP)** — the longest string that appears at the start of every given string.\
If there’s no such prefix, return an **empty string ("")**.

---

## Intuition

The **common prefix** must start from the **first character** of all strings.

If at any point a mismatch occurs between any two strings, the prefix ends there.

So, we can start with the **first string** as a potential prefix and **keep shortening** it until all strings share it.

---

## Algorithm

**Handle edge cases**:

- If the list is empty, return `""`.

**Initialize the prefix**:

- Let the first string be the initial prefix.

**Compare with other strings**:

- For each remaining string:

   - While the current string doesn’t start with the prefix, remove the last character from the prefix.

   - If the prefix becomes empty, return `""`.

**Return the prefix** after all comparisons — it’s the longest common prefix.

---

## Complexity Analysis

**Time Complexity**: O(N × M)

- N = number of strings

- M = length of the shortest string
Each character may be compared once for each string.

**Space Complexity**: O(1)

- Only a few variables are used (ignoring the input/output).

</details>
