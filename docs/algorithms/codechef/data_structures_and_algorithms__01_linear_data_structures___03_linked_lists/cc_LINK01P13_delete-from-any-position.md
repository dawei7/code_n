# Delete from any position

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK01P13 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Linked Lists |
| Official Link | [LINK01P13](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST03/problems/LINK01P13) |

---

## Problem Statement

Deletion from any position other than front is a little different.

For example, we have 1 -> 2 -> 3 and we want to remove 2.
For that, we have to point the next of 1 to 3 and delete 2.

### Video Explanation

### Task

Complete the function **deleteNode** to delete an element from any position.

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

Problem Link- [Delete from any position](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST03/problems/LINK01P13)

### [](#problem-statement-1)Problem Statement:

Deletion from any position other than front is a little different.

### [](#approach-2)Approach:

The **deleteNode** function removes a node with a specific value from a linked list:

-

**If the node to delete is the head**:

- Simply update the `head` pointer to the next node and delete the old `head`.

-

**If the node is elsewhere**:

- Traverse the list until you find the node whose next node has the target value.

- Then, skip over the target node by updating the `next` pointer.

Explanation of `iter -> next = iter -> next -> next`:

This line **removes** the target node by by passing it:

-

`iter -> next` is the node we want to remove.

-

`iter -> next -> next` is the node that comes **after** the one we want to remove.

-

By setting `iter -> next = iter -> next -> next`, we make the current node **skip** the node being deleted, linking directly to the next one. This effectively removes the target node from the list.

### [](#time-complexity-3)Time Complexity:

- **O(n)** because in the worst case, you may have to traverse the entire list to find the node to delete.

### [](#space-complexity-4)Space Complexity:

- **O(1)** since no additional space is used, only pointers are adjusted.

</details>
