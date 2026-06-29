# Family Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FAMTREE |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [FAMTREE](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/FAMTREE) |

---

## Problem Statement

You are given a family tree with $N$ members numbered $1 ... N$. Every person $i$, except for the founder of the family (root) has a parent denoted by $P[i]$. $P[root]$ = -1 by definition. Person $i$ is a descendant of person $j$ if $i$ belongs to the subtree rooted at $j$.

The net worth (adjusted for inflation) is given for all the members of the family. Your task is to find the maximum difference in net worth's of two members where one member is a descendant of the other.

You can assume that no two members of this family married each other. So it remains a "family tree".

---

## Input Format

- First line will contain  an integer $N$, denoting the number of members.
- Second line contains N space seperated integers W[1], W[2] ... W[N] denoting the net_worth of the N members.
- Third line contains  N space seperated integers P[1], P[2] ... P[N] denoting the parents of the N members.

---

## Output Format

Output in a single line the maximum difference in net worth's of any two members where one member is a descendant of the other.

---

## Constraints

- $2 \leq N \leq 10^5$
- $-10^8 \leq W[i] \leq 10^8$
- $1 \leq P[i] \leq N$

---

## Examples

**Example 1**

**Input**

```text
4 
5 10 6 12 
2 -1 4 2
```

**Output**

```text
6
```

**Explanation**

This structure of the tree is:

            2
           / \
          1   4
             /
            3

The maximum difference occurs between the 3rd and 4th members. $W[3]-W[4] = 6$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Family Tree](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/FAMTREE)

### [](#problem-statement-1)Problem Statement:

You are given a family tree with N members numbered 1 ... N. Every person i, except for the founder of the family (root) has a parent denoted by P[i]. P[root] = -1 by definition. Person i is a descendant of person j if i belongs to the subtree rooted at j.

The net worth (adjusted for inflation) is given for all the members of the family. Your task is to find the maximum difference in net worth’s of two members where one member is a descendant of the other.

You can assume that no two members of this family married each other. So it remains a “family tree”.

### [](#approach-2)Approach:

To solve this, we perform a depth-first traversal `(DFS)` starting from the root of the tree. For each node, we calculate the minimum and maximum net worth in its subtree by recursively processing its children. During this traversal, we also compute the maximum difference in net worth between the current node and any of its descendants. At each node, the current node’s value is compared with the minimum and maximum values found in its children’s subtrees, and the maximum difference is updated accordingly. The result is the largest difference observed during the traversal.

### [](#time-complexity-3)Time Complexity:

The time complexity is O(N) because each node and its edges are processed once during the `DFS` traversal.

### [](#space-complexity-4)Space Complexity:

The space complexity is O(N) due to the storage required for the tree structure and the recursive call stack.

</details>
