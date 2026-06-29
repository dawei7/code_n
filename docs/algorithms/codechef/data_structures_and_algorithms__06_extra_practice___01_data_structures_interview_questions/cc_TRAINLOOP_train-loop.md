# Train Loop 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRAINLOOP |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [TRAINLOOP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/TRAINLOOP) |

---

## Problem Statement

You are given a linked-list with $N$ nodes. It might be possible that the tail of the linked-list points to the head of the linked-list; If this is the case, then we call the linked-list to be **circular**.

You have to tell if a given linked list is circular or not.

Each node (except the tail node) points to exactly one node, denoted by the pointer **next**. Each node has a value associated with itself, denoted by the field **val**.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space separated integers N and M.
- The following $M$ lines contain two space separated integers u and v, denoting that there is a connection directed from compartment u to compartment v.
- For C++ language, you need to:
Complete the function in the submit solution tab:

bool isCircular(Node* engine){ .  .  . }

---

## Output Format

For each test case, the function you complete should return a boolean. “true” if the train forms a loop, “false” otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- The value of the field "val" of each node is less than or equal to $N$.
- The value of the field "val" is different for each node.
It is guaranteed that the sum of $N$ over all the test cases won't exceed $3*10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5 4
1 2
2 3
3 4
4 5
5 5
1 3 
3 2
2 4
4 5
5 3
5 5
5 1
1 2
4 3
2 4
4 5
```

**Output**

```text
NO
NO
YES
```

**Explanation**

**Test-Case 3** : One can see that the linked-list formed by making the given connections forms a circular loop!

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

Given a linked list, We have to tell if it is a circular linked list or not.

## [](#approach-2)Approach

We can take a make to track the visited nodes, and if the revisit a visited node we can check if it is the head or not. If the revisited node is the head, then the linked list is circular else it is just a linked list with a cycle in between.

</details>
