# Longest Palindromic Substring

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LONGESTPALIN |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [LONGESTPALIN](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/LONGESTPALIN) |

---

## Problem Statement

Chef has a string **S** consisting of letters and digits.\
He wants to find the **longest palindromic substring**.

A **palindromic substring** is a contiguous sequence of characters that reads the same forward and backward. Due to case sensitivity 'A' != 'a' in a palindrome.

The function searches for all possible palindromic substrings in $s$ and returns the one with the maximum length.
If there is a tie, priority is given to the substring with the **smallest starting index**.

## Function Declaration

### Function Name
$findLongestPalindrome$ – This function finds the longest palindromic substring in a given string.

### Parameters

* $s$ : A string consisting of English letters (uppercase and lowercase) and digits.

### Return Value

* Returns a string representing the **longest palindromic substring** in $s$.
* If multiple palindromic substrings of the same maximum length exist, the one that appears **first** in $s$ is returned.

## Constraints

- $1 \leq |s| \leq 1000$
- String $s$ consists of:
  - English letters (uppercase and lowercase)
  - Digits (`0`–`9`)

---

## Input Format

- A single line containing the string $s$.

---

## Output Format

- Print the longest palindromic substring.
- If multiple answers exist, print the one that appears first in the string.

---

## Constraints

- $1 \le |S| \le 1000$
- $\texttt{S consists of only English letters (uppercase/lowercase) and digits.}$

---

## Examples

**Example 1**

**Input**

```text
racecar12321
```

**Output**

```text
racecar
```

**Explanation**

"racecar" and "12321" are both palindromes.

Both have length 7 and 5 respectively.

"racecar" length is larger so it is printed.

**Example 2**

**Input**

```text
abaxyzzyxf
```

**Output**

```text
xyzzyx
```

**Explanation**

The longest palindromic substring is "xyzzyx" (length 6).

Even though "aba" is a palindrome, it is shorter than "xyzzyx".

**Example 3**

**Input**

```text
121323
```

**Output**

```text
121
```

**Explanation**

121 and 323 are both palindrome.

Both have length of 3.

Thus for tie breaker the palindrome with the smaller starting index will be printed.

121 starting index=0.
323 starting index=3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

You are given a string `S` consisting of English letters (uppercase/lowercase) and digits.
Your task is to find the **longest contiguous substring** of `S` that is a **palindrome**.

A substring is palindromic if it reads the same forward and backward.

If multiple palindromic substrings have the same maximum length, you must return the one that appears **first** in the string.

---

## Key Observations

1. A palindrome is symmetric around its center.
2. Palindromes can be:

   * **Odd-length** (single center character)
   * **Even-length** (center between two characters)
3. The maximum length of the string is 1000, which allows solutions up to `O(n²)`.

---

## Possible Approaches

### 1. Brute Force Approach

**Idea**

* Generate all possible substrings.
* Check each substring to see if it is a palindrome.
* Track the longest valid palindrome.

**Steps**

1. Iterate over all start indices.
2. Iterate over all end indices.
3. Check if `S[start..end]` is a palindrome.
4. Update the result if a longer palindrome is found.

**Time Complexity**

* Substring generation: `O(n²)`
* Palindrome check: `O(n)`
* Total: `O(n³)`

**Space Complexity**

* `O(1)` (ignoring substring storage)

**Drawbacks**

* Too slow for large inputs.
* Repeated palindrome checks cause inefficiency.

---

### 2. Dynamic Programming Approach

**Idea**

* Use a 2D DP table where `dp[i][j]` indicates whether substring `S[i..j]` is a palindrome.

**Recurrence**

* `dp[i][j] = true` if:

  * `S[i] == S[j]`
  * and either `j - i <= 2` or `dp[i+1][j-1] == true`

**Steps**

1. Initialize single-character palindromes.
2. Fill the DP table by increasing substring length.
3. Track the longest palindrome found.

**Time Complexity**

* `O(n²)`

**Space Complexity**

* `O(n²)`

**Drawbacks**

* Uses extra memory.
* More complex to implement and reason about.

---

### 3. Expand Around Center Approach (Used in Given Code)

**Idea**
Every palindrome has a center from which it expands outward.

There are two types of centers:

1. **Odd-length palindrome** → center at index `i`
2. **Even-length palindrome** → center between indices `i` and `i+1`

For each index, expand outward while characters match.

---

## Approach Used in the Given Code

### Core Concept

Instead of checking all substrings, the solution:

* Treats each character (and each pair of characters) as a potential center.
* Expands outward to find the longest palindrome at that center.
* Keeps track of the longest palindrome found so far.

---

### Helper Function: Expand Around Center

**Purpose**

* Given two indices (`left` and `right`), expand outward as long as characters match.

**Logic**

1. While `left >= 0` and `right < n` and `s[left] == s[right]`:

   * Move `left` one step left.
   * Move `right` one step right.
2. When expansion stops, extract the valid palindrome substring.

This function handles both:

* Odd-length palindromes (`left == right`)
* Even-length palindromes (`right == left + 1`)

---

### Main Function Logic

1. Initialize an empty string `longest`.
2. Iterate through each index `i` in the string.
3. For each index:

   * Expand around `(i, i)` to find odd-length palindrome.
   * Expand around `(i, i+1)` to find even-length palindrome.
4. Compare each result with `longest` and update if longer.
5. Return `longest`.

---

### Why This Works Well

* Every palindrome must expand from a center.
* Checking both odd and even centers ensures all palindromes are covered.
* First occurrence is preserved naturally since updates only happen when a strictly longer palindrome is found.

---

### Time Complexity

* There are `n` centers.
* Each expansion takes up to `O(n)` in the worst case.
* Total time complexity: `O(n²)`

---

### Space Complexity

* `O(1)` extra space (excluding the output string).

---

## 4. Manacher’s Algorithm (Advanced)

**Idea**

* Transform the string to handle even and odd palindromes uniformly.
* Use symmetry to avoid redundant expansions.

**Time Complexity**

* `O(n)`

**Space Complexity**

* `O(n)`

**Drawbacks**

* Complex to implement.
* Harder to debug and explain.
* Overkill for constraints up to 1000.

</details>
