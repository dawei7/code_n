# Optimal insertion at the end

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK01P04 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Linked Lists |
| Official Link | [LINK01P04](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST01/problems/LINK01P04) |

---

## Problem Statement

The way we are doing insertion at the end is not really optimal. Every time we want to add an item at the end, we iterate through the complete list to reach the end.

The [time complexity](https://codechef.com/learn/course/time-complexity) of insertion at end is thus O(N) where N is the size of the linked list. But we can make it O(1).

How?

By maintaining a **tail** pointer, which will point to the last element of the linked list. Thus whenever we want to insert at the end, we can use **tail** for that.

### Task
Add a new **tail** pointer and update the current **insertAtEnd** to pass this exercise.

---

## Input Format

First line denotes 'n' the number of elements to be inserted in the list.
Second line consists of n space-separated integers denoting the elements to be added in the list.

---

## Output Format

Single line output of nodes in order from head to tail.

---

## Constraints

- $1 \leq N \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
2 32 23 53
```

**Output**

```text
2 32 23 53
```

**Explanation**

Initially we have an empty linked list. After each step:
1) 2
2) 2->32
3) 2->32->23
4) 2->32->23->53

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Optimal insertion at the end](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST01/problems/LINK01P04)

### [](#problem-statement-1)Problem Statement:

By maintaining a **tail** pointer, which will point to the last element of the linked list. Thus whenever we want to insert at the end, we can use **tail** for that.

***Task***

Add a new **tail** pointer and update the current **insertAtEnd** to pass this exercise.

### [](#approach-2)Approach:

The key idea of this solution is to **efficiently insert elements at the end** of the list using a **tail pointer**. By maintaining both the `head` and `tail` pointers, we can avoid traversing the entire list each time we want to add a new node, making the insertion process faster.

Here’s how the approach works:

-

**Node Structure**:

- A `Node` stores two things:

- **value**: The data of the node.

- **next**: A pointer that points to the next node in the list (or `nullptr` if it’s the last node).

-

**LinkedList Class**:

-

**head**: A pointer to the first node in the list.

-

**tail**: A pointer to the last node in the list.

-

**insertAtEnd(int value)**:

-

This function adds a new node to the end of the list.

-

If the list is empty (`head == nullptr`), the new node becomes both the head and tail.

-

Otherwise, the new node is linked to the `tail`, and then the `tail` is updated to point to this new node.

-

**printValues()**:

- This function prints all the values of the nodes in the list from the head to the tail.

The code uses this approach to efficiently manage the `linked list`.

### [](#time-complexity-3)Time Complexity:

-

**insertAtEnd**: **O(1)** since we directly update the `tail` pointer, avoiding traversal of the list.

-

**printValues**: **O(n)** where `n` is the number of nodes, as we need to traverse the entire list to print all elements.

### [](#space-complexity-4)Space Complexity:

- **O(n)** since we store n nodes in the linked list, with each node storing one value and a pointer to the next node.

</details>
