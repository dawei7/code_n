# Miscellaneous Linear Search

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO05 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO05](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO05) |

---

## Problem Statement

Given **n** pairs of integers, write a program to check if there exists any pair that contains both integers **a** and **b** in any order.

---

## Input Format

- The first line contains an integer $n$, the number of pairs.
- The next $n$ lines each contain two space-separated integers representing a pair.
- The last line contains two integers $a$ and $b$.

---

## Output Format

- Print **"Yes"** if there exists any pair that contains both integers a and b in any order.
- Print **"No"** if no such pair exists.

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
2 3
4 5
3 5
1 7
5 3
```

**Output**

```text
Yes
```

**Example 2**

**Input**

```text
4
2 3
4 5
3 5
1 7
5 9
```

**Output**

```text
No
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH1/problems/SESO05)

### [](#problem-explanation-1)Problem Explanation

You are given `n` pairs of integers, and the task is to check if there exists any pair among these that contains both integers `target_x` and `target_y` in any order. If such a pair exists, the program should output “Yes”; otherwise, it should output “No”.

### [](#approach-2)Approach

The approach to solving this problem is straightforward. First, we read the number of pairs `n` and then store each pair in two separate vectors, `a` and `b`. These vectors represent the two elements of each pair. After reading all the pairs, we take the target integers `target_x` and `target_y` as input.

Next, we iterate through all the pairs and check if any pair matches the target integers in either of the two possible orders:

- If the first integer of the pair is equal to `target_x` and the second is equal to `target_y`.

- If the first integer of the pair is equal to `target_y` and the second is equal to `target_x`.

If we find such a pair, we set a boolean flag `found` to `true`. After checking all the pairs, we simply output “Yes” if the flag is `true`, otherwise “No”.

### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of this solution is O(n), where `n` is the number of pairs. This is because we need to check each pair to see if it matches the target integers.

-

**Space Complexity**: The space complexity is O(n) due to the storage of the pairs in the two vectors `a` and `b`.

### [](#edge-cases-4)Edge Cases

- If `n` is `0`, the program will immediately output “No” since there are no pairs to check.

- The program correctly handles cases where `target_x` and `target_y` are the same number, as it checks both possible orders within the pair.

</details>
