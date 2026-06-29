# Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAAGP1094 |
| Difficulty Rating | 932 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSAAGP1094](https://www.codechef.com/learn/course/binary-search/LIBSDSA01/problems/DSAAGP1094) |

---

## Problem Statement

Given a sorted array of **distinct** integers $A$ and a target value $K$, return the index if the target is found. If not, return the index where it would be if inserted in order.

Complete the function and use Binary Search to solve this Problem.

### Video Explanation

**Note:** Do not write anything outside the function.

---

## Input Format

- The first line of input contains two space-separated integers $N$ and $Q$  denoting the number of elements in the array $A$ and Q queries to search the given target element.
- The second line contains $N$ space-separated integers denoting the elements in the array $A$.
- The next $Q$ lines contain the elements for which we need to find the search index positions

---

## Output Format

- For each query Q: Output position of $K$ or the position where $K$ is to be inserted.

---

## Constraints

- $2 \leq N \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
9 1
1 3 6 7 10 13 20 25 27 
7
```

**Output**

```text
3
```

**Explanation**

$7$ is present at the index $3$.

**Example 2**

**Input**

```text
9 1
1 3 6 7 10 13 20 25 27 
9
```

**Output**

```text
4
```

**Explanation**

$9$ when inserted, would be present at index $4$.
