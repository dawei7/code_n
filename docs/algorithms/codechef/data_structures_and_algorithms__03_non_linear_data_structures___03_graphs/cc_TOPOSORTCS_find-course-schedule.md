# Find Course Schedule

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOPOSORTCS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Topological Sorting |
| Official Link | [TOPOSORTCS](https://www.codechef.com/learn/course/graphs/TOPOSORT/problems/TOPOSORTCS) |

---

## Problem Statement

You have to complete N courses. There are M requirements of the form "course a has to be completed before course b". Find an order in which you can complete the courses.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of courses and number of requirements.
- Courses are numbered from `1` to `N`.
- The subsequent `M` lines describe the requirements, each containing two integers, `a` and `b`, describing the requirements of the form course `a` has to be completed before course `b`.

---

## Output Format

- Output `N` space separated integers, describing the order of `N` courses which should be taken in order to complete all of them.
- If it's not possible to complete all the courses, output -1.

---

## Constraints

* $1 \leq N \leq 10^5$
* $0 \leq M \leq 2 \times 10^5$
* $1 \leq u_i, v_i \leq N$
* $u_i \neq v_i$

---

## Examples

**Example 1**

**Input**

```text
6 6
1 2
1 3
2 4
3 5
5 6
6 3
```

**Output**

```text
-1
```

**Explanation**

Courses 3, 5, and 6 are dependent on each other; hence, it is not possible to complete all the courses.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS/BFS, Topological order.

**Problem:** You have to complete N courses. There are M requirements of the form “course a has to be completed before course b”. Find an order in which you can complete the courses. Output N space separated integers, describing the order of N courses which should be taken in order to complete all of them. If it’s not possible to complete all the courses, output -1.

**Solution Approach:** We need to take the courses in an ordering which satisfies the prerequisite constraints. This means that any course can only be taken when all its prerequisite courses are already completed. We can visualize this problem as a graph where courses are nodes and edge from one course to the next means that 1st node is a prerequisite of the 2nd. Then, we can visit a node only when all of its previous connected nodes leading to it are already visited. This is nothing but Topological ordering. We have used BFS for topological ordering. Refer previous problem where we’ve discussed in detail how to find topological ordering using BFS.

**Time complexity:** O(N + M) as we are using BFS.

**Space complexity:** O(N) as we need to use a queue in BFS.

</details>
