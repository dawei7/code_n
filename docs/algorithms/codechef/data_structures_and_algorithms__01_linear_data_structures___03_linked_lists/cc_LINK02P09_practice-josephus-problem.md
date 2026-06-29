# Practice - Josephus Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P09 |
| Difficulty Rating | 1200 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P09](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P09) |

---

## Problem Statement

You need to solve the famous Josephus problem using circular linked list in this section.

There are `N` people standing in a circle like 1->2->3...->N->1 and there is a knife. Whoever has the knife kills the person next to them and hands over the knife, i.e., if `2` has the knife in 1->2->3->1 then `2` kills `3` and hands over the knife to `1`. This process continues until there is only one person left, i.e., there is no one left to kill. This last person is deemed as the winner. Initially the knife is with person `1`.

For a given `N`, you need to determine the winner.

Note - You are given a circular linked list containing elements from `1` to `N` with head initially at `1`. In the `solution` function, you need to output a single integer denoting the winner.
**Do not make changes anywhere except the solveJosephus() function.**

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first and only line of each test case contains a single integer $N$, denoting the number of people

---

## Output Format

For each test case, output on a new line the winner of that game.

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
2
5
4
```

**Output**

```text
3
1
```

**Explanation**

For n=5, the moves are as followed (the person in bracket holds the knife):
(1)->2->3->4->5->1   (`1` kills `2` and hands knife to 3)
1->(3)->4->5->1   (`3` kills `4` and hands knife to 5)
1->3->(5)->1   (`5` kills `1` and hands knife to 3)
(3)->5   (`3` kills `5` and is the only person left)

Therefore, 3 is the winner.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Practice - Josephus Problem](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P09)

### [](#problem-statement-1)Problem Statement -

You need to solve the famous Josephus problem using circular linked list in this section.

There are `N` people standing in a circle like `1->2->3...->N->1` and there is a knife. Whoever has the knife kills the person next to them and hands over the knife, i.e., if `2` has the knife in `1->2->3->1` then `2` kills `3` and hands over the knife to `1`. This process continues until there is only one person left, i.e., there is no one left to kill. This last person is deemed as the winner. Initially the knife is with person `1`.

For a given `N`, you need to determine the winner.

### [](#approach-2)Approach:

The key idea of this solution is to use a **circular linked list** to efficiently simulate the process of eliminating every second person until one person remains.

-

**Node Structure**:

- A `Node` contains:

- **value**: The data of the node, representing a person.

- **next**: A pointer to the next node in the circular list.

-

**LinkedList Class**:

- **head**: A pointer to the first node in the list.

- **tail**: A pointer to the last node in the list.

-

**insertAtEnd(int value)**:

- This function adds a new node to the end of the circular linked list.

- If the list is empty, the new node becomes the head.

- If the list already has elements, the new node is added after the tail, and then the tail pointer is updated to the new node.

- The `next` pointer of the new tail is set to point back to the head, making the list circular.

-

**solveJosephus()**:

- This function simulates the elimination process.

- It continuously removes every second person until only one remains.

- The loop runs until there is only one node left in the list.

- It updates the `head` if the eliminated node is the current head and returns the value of the last remaining node.

### [](#time-complexity-3)Time Complexity:

-

**insertAtEnd**: **O(1)** as adding to the end of a circular linked list is a constant-time operation.

-

**solveJosephus**: **O(n)** where `n` is the number of people, as each person must be processed to determine the survivor.

### [](#space-complexity-4)Space Complexity:

- **O(n)** for storing n nodes in the circular linked list, each with one value and a pointer to the next node.

</details>
