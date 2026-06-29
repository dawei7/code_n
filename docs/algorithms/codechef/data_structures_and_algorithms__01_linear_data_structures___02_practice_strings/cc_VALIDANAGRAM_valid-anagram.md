# Valid Anagram

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VALIDANAGRAM |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [VALIDANAGRAM](https://www.codechef.com/practice/course/strings/STRINGS/problems/VALIDANAGRAM) |

---

## Problem Statement

You are given two strings $s$ and $t$. Your task is to determine whether $t$ is an **anagram** of $s$.

An anagram is a word formed by rearranging the letters of another word, using **all the original letters exactly the number of times it is used**.

## Function Declaration

### Function Name

$isAnagram$ – This function checks whether one string is an anagram of another string.

### Parameters

* $s$ : A string representing the original word.
* $t$ : A string to be checked as an anagram of $s$.

### Return Value

* Returns $true$ if $t$ is an anagram of $s$.
* Returns $false$ otherwise.

### Constraints

* $ 1 \leq |s|, |t| \leq 5 \times 10^4 $
* Both $s$ and $t$ consist of **lowercase English letters** ($a – z$).

---

## Input Format

* The first line contains a single string $s$.
* The second line contains a single string $t$.

---

## Output Format

* Print $YES$ if $t$ is an anagram of $s$.
* Print $NO$ otherwise.

---

## Constraints

- $1 \le |s|,\ |t| \le 5 \times 10^{4}$
- $\texttt{s} \text{ and } \texttt{t} \text{ consist of lowercase English letters.}$

---

## Examples

**Example 1**

**Input**

```text
listen
silent
```

**Output**

```text
YES
```

**Explanation**

`"silent"` is an anagram of `"listen"`.

**Example 2**

**Input**

```text
hello
world
```

**Output**

```text
No
```

**Explanation**

`"world"` cannot be rearranged to form `"hello"`.

**Example 3**

**Input**

```text
aab
baa
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

We are given two strings `s` and `t`, and we must determine whether `t` is an **anagram** of `s`.\
An anagram means both strings contain exactly the same characters, with the same frequency, but possibly in a different order.

If `t` can be formed by rearranging the letters of `s`, we print `"YES"`, otherwise `"NO"`.

---

# Intuition

Two strings are anagrams if and only if they have identical frequency counts for every character.\
Since both strings consist of lowercase English letters, we can use an array of size 26 to store the count of each letter.

We increment counts for each character in `s` and decrement for each in `t`.
If all counts return to zero, the two strings are anagrams.

---

# Algorithm

- If lengths of `s` and `t` are not equal, return `"NO"`.
- Create an integer array `count[26]` initialized to 0.
- For every character `c` in `s`, increment `count[c - 'a']`.
- For every character `c` in `t`, decrement `count[c - 'a']`.
- Traverse the array; if any value is not zero, return `"NO"`.
- Otherwise, return `"YES"`.

---

# Complexity Analysis

**Time Complexity**: `O(N)` where `N` is the length of the strings.\
Each character is processed a constant number of times.

**Space Complexity**: `O(1)` since the frequency array size is fixed (26 letters).

---

# Key Takeaways

- The problem is efficiently solved using a constant-size frequency counter.
- Sorting both strings would also work but takes `O(N log N)` time, while the counting approach runs in linear time.
- The check relies entirely on balanced character frequencies — every increment in one string must have a matching decrement in the other.

</details>
