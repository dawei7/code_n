# Biggest Friend Group

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSU14 |
| Difficulty Band | Disjoint Set Union |
| Path | Data Structures and Algorithms |
| Lesson | DSU |
| Official Link | [DSU14](https://www.codechef.com/learn/course/dsu/LDSU02/problems/DSU14) |

---

## Problem Statement

The are $N$ people on a social networking app. You are given $M$ connections containing two integers $a$, $b$ where $a$ is a friend of $b$. Output the size of the largest friend group.

---

## Input Format

- The first line of input contains two integers $N$ and $M$, denoting the number of people and the number of connections.
- Next $M$ lines contain two integers $a$ and $b$ denoting that $a$ is a friend of $b$.

---

## Output Format

For each test case, output on a new line the size of the largest friend group.

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
10 5
0 1
1 2
2 3
3 4
4 5
```

**Output**

```text
6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#biggest-friend-group-1)Biggest Friend Group

## [](#problem-explanation-2)Problem Explanation

In this problem you are given the number of nodes and M number of connections. You have to find the size of the largest connected component.

## [](#logic-3)Logic

If we enter all the nodes in a DSU. All the nodes in the same connected component will have the same leader. So we can count the number of nodes with the same leader in the array. We can do this by taking an array of size n. We can initialize this array with 0. And increment the index of the leader every time it is encountered in and array. After this we end up with the size of all the connected components. Now we can find out the max size from this array.

</details>
