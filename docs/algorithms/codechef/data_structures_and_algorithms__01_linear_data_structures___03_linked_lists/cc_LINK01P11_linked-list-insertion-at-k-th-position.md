# Linked List - Insertion at k-th position

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK01P11 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Linked Lists |
| Official Link | [LINK01P11](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST01/problems/LINK01P11) |

---

## Problem Statement

In the last two lessons, we saw how to insert at the start and end of a linked list. How about inserting after some k-th node in the linked list?

The approach is similar to inserting at the end, but rather than going to the end of the list, we will just iterate to the k-th node.

To insert a node in between the k and k+1 node, we will have to change the next pointer of both the k-th node and new Node.
1. Set next of new Node to next of current
2. Set next of current to new Node

### Task
Complete the function **insertAfterK** in IDE to insert an element after k-th node.

---

## Input Format

First line denotes 'n' the number of elements in the list.
Second line consists of two space separated integers, $x$ - the value to be added and $k$ - the position after which the value is added.
Third line consists of n space-separated integers denoting the elements in the list.

---

## Output Format

The complete list after insertion.

---

## Constraints

- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
3 2
2 32 23 53
```

**Output**

```text
2 32 3 23 53
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link: [Linked List - Insertion at k-th position](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST01/problems/LINK01P11)

### [](#problem-solution-1)Problem Solution:

To insert a node in between the `k` and `k+1` node, we will have to change the `next` pointer of both the `k-th` node and new Node.

- Set next of new Node to next of current

- Set next of current to new Node

### [](#approach-2)Approach:

The code snippet defines the function `insertAfterK` which inserts a new node with a given value after the **k-th** node in a linked list.

-

**Creating a New Node**: A new node is created using `newNode = new Node(value)` which stores the given value.

-

**Handling an Empty List**: If the linked list is empty (`head == NULL`), the new node becomes the head of the list, and the function returns.

-

**Traversing to the k-th Node**: The function traverses the list until it reaches the k-th node using a loop.

-

**Inserting the New Node**:

-

**Setting the Next Pointer**: The line `newNode -> next = current -> next;` connects the newly created node (`newNode`) to the node that comes after the k-th node. This ensures that the new node is inserted correctly between the k-th node and its next node.

-

**Updating the k-th Node**: The line `current -> next = newNode;` makes the k-th node point to the newly created node (`newNode`), thereby completing the insertion.

This process ensures that the new node is inserted right after the `k-th` node, maintaining the correct structure of the `linked list`.

### [](#time-complexity-3)Time Complexity:

- **O(k)** since the function traverses the list up to the `k-th` node.

### [](#space-complexity-4)Space Complexity:

- **O(1)** as no extra space is used apart from the new node.

</details>
