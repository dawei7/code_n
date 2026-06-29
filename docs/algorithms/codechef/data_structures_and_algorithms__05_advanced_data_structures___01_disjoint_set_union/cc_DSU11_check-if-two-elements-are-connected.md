# Check if two elements are connected

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSU11 |
| Difficulty Band | Disjoint Set Union |
| Path | Data Structures and Algorithms |
| Lesson | DSU |
| Official Link | [DSU11](https://www.codechef.com/learn/course/dsu/LDSU02/problems/DSU11) |

---

## Problem Statement

In the previous MCQ you noticed that the elements in the same connected component return the same leader on calling the find() function. Based on this solve the following question.
The are $N$ people on a social networking app. You are given $M$ connections containing two integers $a$, $b$ where $a$ is a friend of $b$. You are given $Q$ queries. Each query contains two integers $x$, $y$. Check if $x$ and $y$ are in the same friends group or not(whether they are directly or indirectly connected to each other).
Print "yes" if they are connected. Otherwise print "No".

---

## Input Format

- The first line of input contains two integers $N$ and $M$, denoting the number of people and the number of connections.
- Next $M$ lines contain two integers $a$ and $b$ denoting that $a$ is a friend of $b$.
- Next line contains a single integer $Q$ denoting the number of queries.
- Next $Q$ contain two integers $x$ and $y$ asking whether $x$ and $y$ are connected or not.

---

## Output Format

For each queries print "yes" if they are connected. Otherwise print "No".

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
10 4
1 2
2 3
3 4
4 5
8
5 1
1 2
2 3
4 5
0 1
0 9
9 8
8 7
```

**Output**

```text
Yes
Yes
Yes
Yes
No
No
No
No
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#check-if-two-elements-are-connected-1)Check if two elements are connected

## [](#problem-explanation-2)Problem Explanation

In this problem we are given N number of nodes and M number of connections between these nodes. We have to answer Q queries asking if two nodes are connected.

## [](#logic-3)Logic

If we insert all the nodes with their connections into a DSU. Then, the elements in the same connected component will have the same leader. So, we can use the find function to find the leader of the two elements in the query and if they have the same leader, they will belong to the same connected component.

</details>
