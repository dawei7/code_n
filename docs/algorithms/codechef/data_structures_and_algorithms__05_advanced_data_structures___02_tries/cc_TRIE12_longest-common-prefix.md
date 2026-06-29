# Longest Common Prefix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIE12 |
| Difficulty Band | Tries |
| Path | Data Structures and Algorithms |
| Lesson | Learn Tries |
| Official Link | [TRIE12](https://www.codechef.com/learn/course/tries/LTRIE02/problems/TRIE12) |

---

## Problem Statement

Complete the lcp function to return the Longest Common Prefix among all the strings in the trie.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of string.
- Following $N$ lines contain $N$ strings.

---

## Output Format

Output the Longest Common Prefix for all the strings.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
4
call
cat
caller
camera
```

**Output**

```text
ca
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem explanation

In this problem, we have to find the Longest Common Prefix among all the strings using trie. The Longest Common Prefix is the longest substring that is common in all the strings where the first character of the substring is the first character of the string.

For example in the strings

longest

long

longitude

lonely

The longest common prefix will be “lon”.

## [](#solution-2)Solution

To find the longest common prefix using a trie, we traverse the trie until a it branches. We can check for branch by checking whether two or more characters have pointers to other nodes. If two or more characters in the children array have pointers then we will end the traversal and return the substring formed.

## [](#algorithm-3)Algorithm

- Start from root and set a variable current as the pointer to the root.

- Initialize the prefix with an empty string.

- Iterate over the trie until current is NULL or EndOfWord is True.

- Iterate over the children array and check how many indexes contain a pointer i.e. don’t contain NULL.

- If count is 1

- append the character of index containing a pointer to the prefix.

- set current to the pointer in the children array.

- else break

- return prefix

</details>
