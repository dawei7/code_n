# Insert Remove Nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NODEAD |
| Difficulty Rating | 1300 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [NODEAD](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/NODEAD) |

---

## Problem Statement

You are given a singly linked list. Complete two functions first for deleting the node with the given value and second for inserting the value.

Node* delete(Node* head, int position)

Node* insert(Node* head, int position, int value)

---

## Input Format

- The first line of input contains 2 integers $N$ - length of linked list and $Q$ - number of queries
- Second line contains $N$ space separated integers $val_1, val_2,.... val_i,... val_n$ where $val_i$ is the value stored at ith node starting from the head node.
- Each of the next $Q$ lines contains either
  - 2 integers $0$ and $pos$, where $0$ denotes delete operation and pos is the position of node to be deleted.
  - or 3 integers $1$ , $pos$ and $value$, where $1$ denotes insert operation, pos is the position where node should be inserted and value is the value of the inserted node.

**Note:**

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* remove(Node* head, int position){..}

Node* insert(Node* head, int position, int value){..}
```
For both the functions return pointer to the head of the linked list.

---

## Output Format

Using the functions you have completed, the linked list generated after each query should be correct.
- For each query $K$ space separated integer $val_1, val_2,.... val_i,... val_k$ after executing the query will be outputted. Here $val_i$ is the value of stored at ith node starting from head and $K$ is the length of linked list after executing the query.

---

## Constraints

- $1 \leq N \leq 10^4$
- $1 \leq Q \leq 100$
- $1 \leq val \leq 10^5$

For delete operation
- $1 \leq pos \leq N_{current}$

For insert operation
- $1 \leq pos \leq N_{current} + 1$
- $1 \leq value \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3 5
10 20 5
0 2
1 3 12
1 2 11
1 1 13
0 5
```

**Output**

```text
10 5
10 5 12
10 11 5 12
13 10 11 5 12
13 10 11 5
```

**Explanation**

Initial Linked List : 10 $\rightarrow$ 20 $\rightarrow$ 5

Query 1 : 0 2
Delete $2^{nd}$ node, so new linked list : 10 $\rightarrow$ 5

Query 2 : 1 3 12
Add node with value 12 at $3^{rd}$ position, so new linked list : 10 $\rightarrow$ 5 $\rightarrow$ 12

Query 3 : 1 2 11
Add node with value 11 at $2^{nd}$  position, so new linked list : 10 $\rightarrow$ 11 $\rightarrow$ 5 $\rightarrow$ 12

Query 4 : 1 1 13
Add node with value 13 at $1^{st}$ position, so new linked list : 13 $\rightarrow$ 10 $\rightarrow$ 11 $\rightarrow$ 5 $\rightarrow$ 12

Query 5 : 0 5
Delete last node, so new linked list : 13 $\rightarrow$ 10 $\rightarrow$ 11 $\rightarrow$ 5
