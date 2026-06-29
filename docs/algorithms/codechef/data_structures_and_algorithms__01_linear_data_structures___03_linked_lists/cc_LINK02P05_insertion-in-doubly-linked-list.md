# Insertion in Doubly Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P05 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P05](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P05) |

---

## Problem Statement

In this section, we will learn how to do the insertion operation in a doubly linked list.

Let's suppose you need to insert a node `newNode` between node `A` and node `B`, the pointers we need to update are:
 - next pointer of `A`
 - prev pointer of `B`
 - next and prev pointer of `newNode`

Complete the function **insertAtIndex(int index, int value)** where `index` denotes that you need to insert a new node after the `index-1`th element, i.e., at the `index`th position.

Note: In case of `index`, 0-based indexing is used, i.e., for **insertAtIndex(0, k)** node with value `k` is to be inserted in the beginning.

### Video Explanation

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of list.
- The second line of each test case contains $N$ space-separated integers denoting the elements of the list.
- The third line consists of two integers denoting $index$ and $val$ respectively.

---

## Output Format

For each test case, output on a new line the elements of the list after the insertion operation.

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
5 2 99
1 2 3 4 5
```

**Output**

```text
1 2 99 3 4 5
```

**Explanation**

Original linkedlist if lenght 5: 1 2 3 4 5 \
Inserting 99 at the index 2 results in linkedlist: 1 2 99 3 4 5

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Insertion in Doubly Linked List](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P05)

### [](#problem-statement-1)Problem Statement:

Let’s suppose you need to insert a node `newNode` between node `A` and node `B`, the pointers we need to update are:

- next pointer of `A`

- prev pointer of `B`

- next and prev pointer of `newNode`

Complete the function **insertAtIndex(int index, int value)** where `index` denotes that you need to insert a new node after the `index-1` th element, i.e., at the `index` th position.

### [](#approach-2)Approach:

The key idea of this solution is to **insert a new node at a specific index** in a doubly linked list. Depending on the position, the new node will either:

Here’s how the approach works:

-

**Inserting at Index 0 (Head)**:

-

If the index is `0`, the new node will become the new **head**.

-

The existing head node will shift, and the new node will be linked to it by updating the pointers.

-

**Inserting at Other Positions**:

-

First, we traverse the list to find the node after which we need to insert (the node at `index - 1`).

-

Once located, we update the **next** and **prev** pointers of the surrounding nodes to insert the new node.

-

This ensures that the new node is properly linked between its neighbors.

-

**printValues()**:

- This function prints all the values in the linked list, starting from the head and moving to the tail.

### [](#time-complexity-3)Time Complexity:

-

**insertAtIndex**: **O(n)** because, in the worst case, we might need to traverse the entire list to reach the position before inserting.

-

**printValues**: **O(n)** where `n` is the number of nodes, as it requires traversing the list to print all elements.

### [](#space-complexity-4)Space Complexity:

- **O(1)** for insertion, as the operation modifies pointers but does not use extra space beyond the new node.

</details>
