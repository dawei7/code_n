# Rotate String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROTATESTRING |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ROTATESTRING](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/ROTATESTRING) |

---

## Problem Statement

You are given two strings $s$ and $goal$ of equal length. Determine whether string $s$ can be transformed into string $goal$ by performing a series of **left-shifts**.

A **left-shift** operation moves the first character of a string to the end of the string. For example, a left-shift on `"abcde"` results in `"bcdea"`.

If it is possible to transform $s$ into $goal$ using zero or more left-shifts, print `"Yes"`.\
 Otherwise, print `"No"`.

## Function Declaration

### Function Name
$canRotate$ – This function checks whether a string can be rotated using left-shift operations to match a target string.

### Parameters

* $s$ : A string representing the original string.
* $goal$ : A string representing the target string after rotations.

### Return Value

* Returns $true$ if string $s$ can be transformed into string $goal$ using zero or more left-shift operations.
* Returns $false$ otherwise.

## Constraints

- $1 \leq |s| = |goal| \leq 100$
- Strings $s$ and $goal$ consist of lowercase English letters.

---

## Input Format

- The first line contains the string $s$.
- The second line contains the string $goal$.

---

## Output Format

- Print `"Yes"` if $s$ can be rotated to become $goal$.
- Print `"No"` otherwise.

---

## Constraints

- $1 \le \text{length of } S, G \le 100$
- $\mathbf{S} \text{ and } \mathbf{G} \text{ consist of lowercase English letters.}$

---

## Examples

**Example 1**

**Input**

```text
hello
ohell
```

**Output**

```text
Yes
```

**Explanation**

`"hello"` left-shifted 4 times becomes `"ohell"`, so the answer is `"Yes"`.

**Example 2**

**Input**

```text
world
dlrow
```

**Output**

```text
No
```

**Explanation**

No sequence of left-shifts can transform `"world"` into `"dlrow"`, so the answer is `"No"`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

You are given two strings `S` and `G` of equal length.\
Your task is to determine whether `S` can be **rotated** (by performing a series of left-shifts) to become `G`.

A **left-shift** moves the first character of the string to the end.\
For example:\
`"abcde"` → `"bcdea"`

You can perform **zero or more left-shifts**, and if after some shifts `S` becomes equal to `G`, print **"YES"**, otherwise print **"NO"**.

---

# Example

Input:\
hello\
ohell

Output:\
YES

**Explanation**:
`"hello"` → `"elloh"` → `"lloeh"` → `"lohel"` → `"ohell"` ✅
After 4 left-shifts, we obtain `"ohell"`.

---

# Intuition

If you concatenate the string S with itself (i.e., form S + S),
every possible rotation of S will appear as a substring in that doubled string

Example:

S = "abcde"\
S + S = "abcdeabcde"

All rotations of "abcde":\
"abcde", "bcdea", "cdeab", "deabc", "eabcd"

All of them are substrings of "abcdeabcde"

So, instead of performing multiple shift operations, we can just check whether `G` exists as a substring in `S + S`.

---

# Algorithm

Check if `S` and `G` have the same length.\
If not, print `"NO"`.

Concatenate the string `S` with itself → `doubled = S + S``.

Check if `G` is a substring of `doubled`.
- If yes → print `"YES"`.
- Otherwise → print `"NO"`.

---

# Example Walkthrough

Example:

S = "hello"\
G = "ohell"

Step 1: `S + S = "hellohello"`

Step 2: Check if `"ohell"` is a substring of `"hellohello"`
✅ Found — Therefore, `"YES" `

---

# Complexity Analysis

| Type                 | Analysis                                                              |
| -------------------- | --------------------------------------------------------------------- |
| **Time Complexity**  | **O(N)** — substring search in doubled string (where N = length of S) |
| **Space Complexity** | **O(N)** — for the concatenated string `S + S`                        |

</details>
