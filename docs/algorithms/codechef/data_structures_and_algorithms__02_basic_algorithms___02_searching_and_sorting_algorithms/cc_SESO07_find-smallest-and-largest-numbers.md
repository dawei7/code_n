# Find smallest and largest numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO07 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO07](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO07) |

---

## Problem Statement

Write a program to find the **smallest** and **largest** elements in an array of integers.

### Input Format
- The first line contains an integer **n**, representing the number of elements in the array.
- The second line contains **n** integers separated by spaces, representing the elements of the **array**.

### Output Format
- Print the **smallest** and **largest** elements in the array on a single line, separated by a space.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of vertices and edges of the graph, respectively.
    - The next $M$ lines describe the edges. The $i$-th of these $M$ lines contains two space-separated integers $u_i$ and $v_i$, denoting an edge between $u_i$ and $v_i$.

---

## Output Format

For each test case, output on a new line the number of good subgraphs of $G$, modulo $10^9 + 7$.

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
10
4 3 53 13 2 44 55 35 56 34
```

**Output**

```text
2 56
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO07)

### [](#problem-explanation-1)Problem Explanation

The task is to find the smallest and largest elements in an array of integers. You are given an array of integers, and you need to determine the minimum and maximum values in this array and then print them.

### [](#approach-2)Approach

To find the smallest and largest elements in an array of integers, we can iterate through the array once while maintaining two variables: `smallest` and `largest`. Initially, we set `smallest` to `INT_MAX` and `largest` to `INT_MIN` to ensure any element in the array will update these values. As we traverse the array, we compare each element with `smallest` and `largest`, updating them accordingly if a smaller or larger element is found. After the loop, `smallest` will hold the minimum value, and `largest` will hold the maximum value, which we then print. This approach is efficient with a time complexity of O(n) and a space complexity of O(1).

### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of this solution is O(n), where `n` is the number of elements in the array. This is because we only traverse the array once to determine both the smallest and largest elements.

-

**Space Complexity**: The space complexity is O(1), as we are only using a fixed amount of extra space for the variables `smallest` and `largest`, regardless of the size of the input array.

</details>
