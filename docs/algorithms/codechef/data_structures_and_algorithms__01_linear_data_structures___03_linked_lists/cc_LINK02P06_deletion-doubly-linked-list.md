# Deletion - Doubly Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P06 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P06](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P06) |

---

## Problem Statement

In this section, we will learn how to do the deletion operation in a doubly linked list.

Let's suppose you need to delete the node `target` between node `A` and node `B`, the pointers we need to update are:
 - next pointer of `A`
 - prev pointer of `B`
 - head pointer if `target` is the head

Complete the function delete(int val) where `val` denotes the value of the node to be deleted.

### Video Explanation

***Do not make changes anywhere else in the code except this function***

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of list.
- The second line of each test case contains $N$ space-separated integers denoting the elements of the list.
- The third line consists of a single integer denoting $val$.

---

## Output Format

For each test case, output on a new line the elements of the list after the deletion operation.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
5 3
1 2 3 4 5
```

**Output**

```text
1 2 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Deletion - Doubly Linked List](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P06)

### [](#problem-statement-1)Problem Statement:

Let’s suppose you need to delete the node `target` between node `A` and node `B`, the pointers we need to update are:

- `next` pointer of `A`

- `prev` pointer of `B`

- `head` pointer if `target` is the head

Complete the function delete(int val) where `val` denotes the value of the node to be deleted.

### [](#approach-2)Approach:

The key idea of this function is to **find the target node** with the specified value and then **adjust the pointers** of its neighboring nodes (if they exist) to remove it from the list.

Here’s how the approach works:

-

**Finding the Target Node**:

- Start from the `head` and traverse the list until you find the node that contains the specified value.

-

**Updating Pointers**:

-

Once the target node is found, identify its previous node (A) and next node (B).

-

Update the `next` pointer of node A to point to node B.

-

Update the `prev` pointer of node B to point to node A.

-

If the target node is the `head`, update `head` to point to node B.

-

**Handling Edge Cases**:

- Ensure to check if node A is `NULL` (which means the `target` node was the `head`) or if node B is `NULL` (which means the `target` node was the `tail`).

This approach efficiently removes the node while ensuring the list remains connected.

### [](#time-complexity-3)Time Complexity:

- **O(n)** in the worst case, where `n` is the number of nodes in the list, as we may need to traverse the entire list to find the target node.

### [](#space-complexity-4)Space Complexity:

- **O(1)** since we are only using a constant amount of space for pointers and do not require additional data structures.

</details>
