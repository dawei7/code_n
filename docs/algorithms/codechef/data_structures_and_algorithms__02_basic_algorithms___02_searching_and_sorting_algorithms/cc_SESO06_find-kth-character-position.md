# Find Kth Character Position

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO06 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Searching |
| Official Link | [SESO06](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO06) |

---

## Problem Statement

Given a string **s1**, a character **c1**, and an integer **k**, find and print the position of the $k$th occurrence of the character **c1** in the string **s1**. If the $k$th occurrence does not exist, print **-1**.

### Input Format
- The first line contains the string **s1**, the character **c1**, and the integer **k** separated by spaces.
### Output Format
- An integer representing the position of the $k$th occurrence of **c1** in **s1**.
- If the $k$th occurrence does not exist, print **-1**.

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
HelloHowyoudoing H 2
```

**Output**

```text
5
```

**Example 2**

**Input**

```text
funny n 3
```

**Output**

```text
-1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH2/problems/SESO06)

You are given a string `s1`, a character `c1`, and an integer `k`. The task is to find the position of the `k`th occurrence of the character `c1` in the string `s1`. If the `k`th occurrence does not exist in the string, the program should output `-1`.

### [](#approach-1)Approach

The approach to solving this problem involves iterating through the string and counting occurrences of the character `c1`. As you traverse the string, each time you encounter `c1`, you increment a counter. When the counter reaches `k`, you print the current index, which corresponds to the `k`th occurrence of `c1`. If you finish iterating through the string without the counter reaching `k`, you print `-1` to indicate that the `k`th occurrence does not exist.

### [](#complexity-analysis-2)Complexity Analysis

-

**Time Complexity**: The time complexity is O(n), where `n` is the length of the string `s1`. The string is traversed once to find the `k`th occurrence.

-

**Space Complexity**: The space complexity is O(1), as only a few integer variables are used regardless of the size of the input.

</details>
