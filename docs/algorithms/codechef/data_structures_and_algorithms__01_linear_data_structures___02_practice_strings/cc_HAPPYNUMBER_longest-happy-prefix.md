# Longest Happy Prefix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HAPPYNUMBER |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [HAPPYNUMBER](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/HAPPYNUMBER) |

---

## Problem Statement

A string is called a **happy prefix** if it is a non-empty prefix which is also a suffix of the string (excluding the string itself).

Given a string s, your task is to find the **longest happy prefix** of $s$. If no such prefix exists, print an empty string.

## Function Declaration

### Function Name

$longestHappyPrefix$ – This function finds the longest prefix of a string that is also its suffix.

### Parameters

* $s$ : A string consisting of lowercase English letters.

### Return Value

* Returns a string — the **longest happy prefix**.
* Returns an **empty string** if no happy prefix exists.

## Constraints

* $1 \leq T \leq 100$
* $1 \leq |s| \leq 10^5$
* $s$ contains only lowercase English letters

---

## Input Format

The first line contains an integer $T$ — the number of test cases.

Each of the next $T$ lines contains a string $s$ consisting of lowercase English letters.

---

## Output Format

* For each test case, print a single line containing the **longest happy prefix**.
* If no such prefix exists, print an **empty line**.

---

## Constraints

- $1 \le T \le 100$
- $1 \le |s| \le 10^{5}$
- $\texttt{s contains only lowercase English letters.}$

---

## Examples

**Example 1**

**Input**

```text
3
ababab
aaaa
abcd
```

**Output**

```text
abab
aaa
```

**Explanation**

* **Test Case 1 :**
  **Input:** `ababab`

  The prefix `abab` also appears as the suffix of the string and is the longest such match.
  **Output:** `abab`

* **Test Case 2 :**
  **Input:** `aaaa`

  The prefixes `a`, `aa`, and `aaa` are also suffixes of the string.
  The longest happy prefix is `aaa`.
  **Output:** `aaa`

* **Test Case 3 :**
  **Input:** `abcd`

  No non-empty prefix (excluding the full string) matches any suffix.
  **Output:** `""` (empty string)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Restatement

You are given a string s consisting of lowercase English letters.\
A **happy prefix** is a **non-empty prefix** of the string that is **also a suffix**, but **not equal to the entire string** itself.

Your task is to find the **longest happy prefix** of the given string.\
If no such prefix exists, print an **empty string**.

---

# Intuition

We are looking for the **longest prefix of the string that is also a suffix, excluding the entire string itself**.\
This is exactly what the **LPS (Longest Prefix Suffix)** array from the **KMP (Knuth-Morris-Pratt)** algorithm gives us!

- The **LPS array** stores for each position the **length of the longest prefix** which is also a **suffix** for the substring ending at that position.

- The **last value of the LPS array**, `lps[n-1]`, gives the **length of the longest happy prefix**.

---

# Approach

Initialize an LPS array of size `n` with all zeros.

Start iterating from index `1` to `n-1`:

- Maintain a pointer `len` that tracks the current longest prefix-suffix length.
- If `s[i] == s[len]`, increment `len` and assign `lps[i] = len`.
- If not equal, reduce `len` using previous lps[len - 1] until a match is found or `len = 0`.

The last **value of the LPS array**, `lps[n - 1]`, gives the **length of the longest happy prefix**.

---

# Complexity Analysis

**Time Complexity**: O(n) — each character is processed at most twice

**Space Complexity**: O(n) — for the LPS array

Return the substring s[0:lps[n - 1]].

</details>
