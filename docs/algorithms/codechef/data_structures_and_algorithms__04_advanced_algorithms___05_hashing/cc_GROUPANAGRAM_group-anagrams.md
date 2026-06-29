# Group Anagrams

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GROUPANAGRAM |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Hashing |
| Official Link | [GROUPANAGRAM](https://www.codechef.com/learn/course/hashing/HASH04/problems/GROUPANAGRAM) |

---

## Problem Statement

You are given $N$ strings. Your task is to group the strings that are anagrams of each other.
Complete the given function.

**Note**: An anagram is a string formed by rearranging the letters of a another string, using all the original letters exactly once. \
For example, **"listen"** and **"silent"** are anagrams of each other because they contain the same letters.

---

## Input Format

- The first line of input contains an integer $N$ — the number of strings.
- The next $N$ lines contain strings.

---

## Output Format

- Complete the function which return the vector of string vectors. each string vector are group of anagram strings.
- You can return the groups of anagrams in any order. You will get a text **Nicely Grouped!** if grouping is done correctly, otherwise **WA**.

---

## Constraints

- $1 \leq N \leq 100000$
- All strings are of lowercase latin letters.
- Size of each string is at most `10`.

---

## Examples

**Example 1**

**Input**

```text
5
abc
dba
acb
bda
cba
```

**Output**

```text
abc acb cba 
dba bda
```

**Explanation**

There could be multiple grouping, for eg, 1 valid grouping is: {abc, acb, cba}, {dba, bda}

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Group Anagrams in Hashing](https://www.codechef.com/learn/course/hashing/HASH04/problems/GROUPANAGRAM)

### [](#problem-1)Problem:

Given an array of strings, group the anagrams together. Anagrams are strings that can be rearranged to form each other, like “eat”, “tea”, and “ate”.

### [](#approach-2)Approach:

-

**Sort and Use as Key:** For each string in the input, sort the characters in lexicographical order. Since anagrams have the same characters in different orders, their sorted forms will be identical.

-

**Group Using Hash Map:** Use a hash map where the key is the sorted version of the string, and the value is a list of original strings (anagrams). If two strings are anagrams, they will have the same sorted key and will be grouped together in the same list.

-

**Build Result:** After processing all strings, the values of the map (lists of grouped anagrams) will be the final output.

### [](#complexity-3)Complexity:

-

**Time Complexity:** Sorting each string takes `O(M log M)`, where `M` is the length of the string. Iterating over all `N` strings results in a time complexity of `O(N * M log M)`.

-

**Space Complexity**: `O(N)` for storing the grouped anagrams in the hash map, where `N` is the total number of strings in the input.

</details>
