# First Occurrence of Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ZFUNCTION |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ZFUNCTION](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/ZFUNCTION) |

---

## Problem Statement

You are given two strings:
- $text$ (also called **haystack**)
- $pattern$ (also called **needle**)

Your task is to determine the **index of the first occurrence** of $pattern$ in $text$.

If $pattern$ does not appear in $text$, return **-1**.

## Function Declaration

### Function Name
$Search$ – This function finds the **index of the first occurrence** of a substring within a given string.

### Parameters

* $text$ : The main string (haystack) in which the pattern is searched.
* $pattern$ : The substring (needle) to search for.

### Return Value

* Returns an integer representing the **0-based index** of the first occurrence of $pattern$ in $text$.
* Returns **-1** if the pattern does not exist in the text.

## Constraints

- $1 \leq |text|, |pattern| \leq 10^5$
- Both strings consist of **lowercase English letters** (`'a'`–`'z'`) only

---

## Input Format

* The first line contains a string $text$.
* The second line contains a string $pattern$.

---

## Output Format

* Print a single integer — the index of the first occurrence of $pattern$ in $text$.
* If the pattern is not present, print **-1**.

---

## Constraints

- $1 \le |haystack|,\ |needle| \le 10^{4}$
- $\texttt{Both strings consist of only lowercase English letters ('a'–'z')}$

---

## Examples

**Example 1**

**Input**

```text
programmingisfun
ming
```

**Output**

```text
7
```

**Explanation**

The substring `"ming"` first appears in `"programmingisfun"` starting at index `7`.

**Example 2**

**Input**

```text
datastructures
tree
```

**Output**

```text
-1
```

**Explanation**

The substring `"tree"` is not present in `"datastructures"`, so the output is `-1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# problem Understanding

You are given two strings:

- **haystack** → The main text

- **needle** → The substring to search

Your task is to return the 0-based index at which the first occurrence of `needle` appears in `haystack`.

If `needle` does not exist inside `haystack` → return -1.

---

# Intuition

A straightforward solution would check for a match starting from every index in the string → **O(n × m)** time.
This becomes too slow for strings up to **10⁴ characters**.

To optimize, we can use **Knuth–Morris–Pratt (KMP Algorithm)** 🎯

---

# Approach

**Step 1: Build LPS (Longest Prefix Suffix) Array**

For the `needle`, compute repeating prefix-suffix patterns.

Example:\
pattern = `"ababaca"`
lps = `[0,0,1,2,3,0,1]`

**Step 2: Pattern Matching**

Traverse `haystack`:

- If characters match → move both pointers

- On mismatch → use LPS to jump needle pointer efficiently

✅ First full match → return starting index\
❌ No match by end → return -1

---

# Complexity Analysis

| Operation                 | Complexity           |
| ------------------------- | -------------------- |
| LPS Construction          | **O(m)**             |
| Pattern Search            | **O(n)**             |
| **Total Time Complexity** | ✅ **O(n + m)**       |
| Space Complexity          | **O(m)** (LPS array) |

</details>
