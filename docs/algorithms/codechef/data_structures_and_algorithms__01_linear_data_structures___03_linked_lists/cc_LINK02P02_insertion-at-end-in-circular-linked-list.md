# Insertion at end in Circular Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P02 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P02](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P02) |

---

## Problem Statement

Let's learn how to insert an element at the end of circular linked list.

Whenever inserting a new node, there can be two cases:

1) The list is empty (head = null) - Simply assign both head and tail as the new node and update the next pointer of tail.

2) The list is not empty
  - The new node is supposed to be added after tail, thus set next of tail to new node.
  - Update the tail to new node because now it is the last element.
  - Update the next of new tail to existing head.

### Video Explanation

Complete the **insertAtEnd** function in the IDE.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

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
5
1 2 3 4 5
```

**Output**

```text
1 2 3 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Insertion at end in Circular Linked List](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P02)

### [](#problem-statement-1)Problem Statement:

Whenever inserting a new node, there can be two cases:

-

The list is empty (head = null) - Simply assign both head and tail as the new node and update the next pointer of tail.

-

The list is not empty

- The new node is supposed to be added after tail, thus set next of tail to new node.

- Update the tail to new node because now it is the last element.

- Update the next of new tail to existing head.

Complete the **insertAtEnd** function in the IDE.

### [](#approach-2)Approach:

The key idea of this solution is to **maintain a circular linked list** where the last node’s `next` pointer connects back to the first node (`head`). This ensures that traversing the list can form a loop. The insertion of new elements is done efficiently using the **tail pointer**.

Here’s how the approach works:

-

**Node Structure**:

- A `Node` stores two things:

- **value**: The data of the node.

- **next**: A pointer that points to the next node in the list.

-

**insertAtEnd(int value)**:

- A new node is created using the provided `value`.

- If the list is empty (`head == NULL`), the new node becomes both the head and tail.

- Otherwise, the new node is added after the current `tail`.

- The **tail** is updated to this new node.

- The new tail is then linked back to the head to maintain the circular structure.

### [](#time-complexity-3)Time Complexity:

- **insertAtEnd**: **O(1)** since we directly update the tail pointer and make the circular connection without needing to traverse the list.

### [](#space-complexity-4)Space Complexity:

- **O(n)** where `n` is the number of nodes, since we are storing `n` nodes in the linked list.

</details>
