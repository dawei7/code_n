# Deletion in Circular Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P03 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P03](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P03) |

---

## Problem Statement

Let's learn how to delete an element given its value from a Circular Linked-list.

The steps to delete a node with value are very similar to that of Singly Linked-list.

There are two cases:

 - The list only contains one element (head = tail) and it is the element to be deleted: Assign both head and tail as null (Yes, that's it).

 - Otherwise :
    - Check if the first value is the value to be deleted
        - If yes, set head to second element and set tail's next to the new head
    - Now iterate over the linked list till you reach the tail
        - check if the next node is target
            - If it is, set current node's next to the next of the next node and break.

Note - Do consider when the element to be deleted is not present in the list. In that case, output the list as it is.

### Video Explanation

### Task
Study the function **deleteNode** in the IDE. After you have understood all the steps, delete the code and try to write it down yourself, to ensure that you have actually understood it. You can always check the solution if you are not able to figure something out.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of list.
- The second line of each test case contains $N$ space-separated integers denoting the elements of the list.
- The third line of each test case contains a single integer $K$, denoting the value of the node to be deleted.

---

## Output Format

For each test case, output on a new line the elements of the list after the deletion operation.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
5 2
1 2 3 4 5
```

**Output**

```text
1 3 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Deletion in Circular Linked List](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P03)

### [](#problem-statement-1)Problem Statement:

Study the function **deleteNode** in the IDE. After you have understood all the steps, delete the code and try to write it down yourself, to ensure that you have actually understood it. You can always check the solution if you are not able to figure something out.

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

- If the list is empty (`head == NULL`), the new node becomes both the head and `tail`.

- Otherwise, the new node is added after the current `tail`.

- The **tail** is updated to this new node.

- The new tail is then linked back to the head to maintain the circular structure.

### [](#time-complexity-3)Time Complexity:

- **insertAtEnd**: **O(1)** since we directly update the `tail` pointer and make the circular connection without needing to traverse the list.

### [](#space-complexity-4)Space Complexity:

- **O(n)** where `n` is the number of nodes, since we are storing `n` nodes in the linked list.

</details>
