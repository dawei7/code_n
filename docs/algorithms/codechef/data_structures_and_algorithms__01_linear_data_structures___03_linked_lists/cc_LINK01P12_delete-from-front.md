# Delete from front

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK01P12 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Linked Lists |
| Official Link | [LINK01P12](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST03/problems/LINK01P12) |

---

## Problem Statement

Before deleting a node, we will need to find it by value. To find a value, we can traverse the linked list and see if node of any value matches the value we want to delete.

Once the **targetNode** is found, we can then delete it.

### Video Explanation

### Task

Complete the function **deleteNode** to delete an element from the front of the linked list. In the next lesson, we will learn how to delete an element from any other position.

---

## Input Format

- The first line of input will contain a single integer T, denoting the number of test cases. The description of the test cases follows.
- The second line of each test case contains a single integer N, denoting the length of list.
- The third line of each test case contains the value of the linked list
- The fourth line of each test case contains a single integer X, the value of the node to be deleted from the list.

---

## Output Format

For each test case, output on a new line the elements of list in order from head to tail.

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
5 1
1 2 3 4 5
```

**Output**

```text
2 3 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Delete from front](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST03/problems/LINK01P12)

### [](#problem-statement-1)Problem Statement:

Complete the function **deleteNode** to delete an element from the front of the linked list. In the `next` lesson, we will learn how to delete an element from any other position.

### [](#approach-2)Approach:

The key idea of this solution is to **delete the node** that matches a given value and update the **head** if the node being deleted is the first node.

Here’s how the approach works:

-

**Check if the node to delete is the head**: If the node to be deleted is the **head** (i.e., the node at the start of the list), we need to update the head to the `next` node in the list.

-

**Update the head pointer**: The head is updated to point to the `next` node in the list.

-

**Delete the target node**: After updating the `head`, the old head (which contains the value to be deleted) is removed from memory using `delete`.

### [](#time-complexity-3)Time Complexity:

- **O(1)** because the function only checks the head node and updates the `head` pointer.

### [](#space-complexity-4)Space Complexity:

- **O(1)** since no additional data structures are used.

</details>
