# Frequency greater than k

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP59B |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Hashing |
| Official Link | [DSAAGP59B](https://www.codechef.com/learn/course/hashing/HASH04/problems/DSAAGP59B) |

---

## Problem Statement

Given a string S and an integer, K. Write a program to print characters with frequency greater than or equal to K in sorted order.

---

## Input Format

- The first line contains two integers: $N$ and $K$.
- The second line contains the string $S$.

---

## Output Format

Output the characters with frequency greater than or equal to $K$.

---

## Constraints

- $2 \leq length(S) \leq 10^5$
- $1 \leq K \leq 10^5$
- S can have both upper and lowercase letters

---

## Examples

**Example 1**

**Input**

```text
10 3
aaabbcdddd
```

**Output**

```text
ad
```

**Example 2**

**Input**

```text
10 2
aaAbBcdDdD
```

**Output**

```text
Dad
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem [Link](https://www.codechef.com/learn/course/hashing/HASH04/problems/DSAAGP59B)

### [](#problem-1)Problem:

Given a string S and an integer K, you need to output the characters with a frequency greater than or equal to K, sorted in **lexicographical** order.

### [](#approach-2)Approach:

We can use an **ordered map** (TreeMap in Java) to store the frequencies of all the characters in sorted order. After populating the frequency map, iterate through it and select characters with frequencies greater than or equal to K.

### [](#complexity-3)Complexity:

-

**Time Complexity:** `O(N)`, Traversed the whole string once to store the frequencies.

-

**Space Complexity:** `O(1)`, We store the frequency of each character in the map. Taking both lower and uppercase, the maximum space it can take is `O(52)` → `O(26)` for lowercase and `O(26)` for uppercase. As `O(52)` is a constant, the space complexity will be `O(1)`.

</details>
