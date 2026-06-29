# Check Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS276 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSCPPAS276](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/DSCPPAS276) |

---

## Problem Statement

You are given a string $(S)$. Your task is to determine if the string can be a palindrome after deleting at most one character from it.

---

## Input Format

- The first line contains one integer $n$, the size of the string                                                                                                               - Next line contains string $S$.

---

## Output Format

- Print whether $S$ can be made palindrome after deleting at most one character.

---

## Constraints

- $1 \leq |S| \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
abca
```

**Output**

```text
true
```

**Explanation**

We can delete b or c to make it palindrome.
after deleting b the S will be aca which is palindrome.

**Example 2**

**Input**

```text
4
batr
```

**Output**

```text
false
```

**Explanation**

There is no way to make S palindrome after deleting at most 1 character.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

You are given a string `S`. The task is to determine if the string can be transformed into a palindrome by deleting at most one character.

#### [](#approach-2)Approach:

To determine if the string can be a palindrome after deleting at most one character, we can use a two-pointer technique. The key idea is to check the string from both ends towards the center and identify the first mismatch. When a mismatch is found, there are two possible ways to potentially fix the string:

- Skip the character at the left pointer.

- Skip the character at the right pointer.

If either of these modifications results in a valid palindrome, the original string can be considered a valid palindrome after deleting one character.

### [](#step-by-step-explanation-3)Step-by-Step Explanation:

-

**Two-Pointer Technique:**

- Use two pointers, `left` starting at the beginning of the string and `right` starting at the end.

- Move the `left` pointer forward and the `right` pointer backward towards the center, comparing the characters at each position.

-

**Handling Mismatch:**

- If the characters at `left` and `right` are the same, move both pointers closer to the center.

- If the characters are different, check two scenarios:

- Skip the character at `left` and check if the remaining substring (from `left + 1` to `right`) is a palindrome.

- Skip the character at `right` and check if the remaining substring (from `left` to `right - 1`) is a palindrome.

-

**Checking Substring for Palindrome:**

- Use a helper function `isPalindrome` to check if a given substring (bounded by `left` and `right` indices) is a palindrome.

-

**Return Result:**

- If either scenario (skipping left or right) results in a palindrome, return `true`.

- If no mismatches are found during the initial comparison (i.e., the string is already a palindrome), return `true`.

-

**Edge Case:**

- A single character string or an empty string is trivially a palindrome.

### [](#complexity-4)Complexity:

-

**Time Complexity:** The time complexity is `O(N)`, where `N` is the length of the string. This is because each character is checked at most twice.

-

**Space Complexity:** The space complexity is `O(1)` since no additional space is required beyond a few variables.

</details>
