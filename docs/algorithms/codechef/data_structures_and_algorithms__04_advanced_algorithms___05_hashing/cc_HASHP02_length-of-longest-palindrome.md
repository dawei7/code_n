# Length of Longest Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HASHP02 |
| Difficulty Rating | 1696 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Hashing |
| Official Link | [HASHP02](https://www.codechef.com/learn/course/hashing/HASH04/problems/HASHP02) |

---

## Problem Statement

Given a string $s$ which consists of lowercase latin letters, return the length of the **longest palindrome** that can be built with those letters.

---

## Input Format

- The first and only line of input contains the string `s`.

---

## Output Format

- Output on a single line, the length of the longest palindrome that can be format using the letters of `s`.

---

## Constraints

- $1 \leq s.length \leq 10^5$
- s consists of lowercase English letters only.

---

## Examples

**Example 1**

**Input**

```text
bbd
```

**Output**

```text
3
```

**Explanation**

- Longest palindromic string: bdb

**Example 2**

**Input**

```text
aabdcd
```

**Output**

```text
5
```

**Explanation**

- Longest possible palindromic strings: adbda, adcda, dabad, dacad

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Length of Longest Palindrome in Hashing](https://www.codechef.com/learn/course/hashing/HASH04/problems/HASHP02)

### [](#problem-1)Problem:

Given a string S which consists of lowercase Latin letters, return the length of the longest palindrome that can be built with those letters.

### [](#approach-2)Approach:

-

**Understand Palindrome Properties**: A palindrome reads the same forwards and backward. In a palindrome, characters must appear in pairs, except for one character that can appear in the center.

-

**Count Character Frequencies**: Use a hash map (or unordered map) to count the occurrences of each character in the string.

-

**Calculate Maximum Palindrome Length**:

- Keep track of the total length of the palindrome.

- Check if there’s at least one character with an odd count.

- For each character count:

- If the count is even, add it directly to the total length.

- If the count is odd, add the largest even part of it (i.e., `count - 1`) to the total length and mark that an odd count has been found.

- **Handle Center Character**: If there is at least one character with an odd frequency, add `1` to the total length to account for the center character of the palindrome.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)`, where `N` is the length of the string (for counting characters).

- **Space Complexity**: `O(1)`, as the maximum number of unique characters is constant (`26` lowercase letters).

</details>
