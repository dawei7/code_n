# Flatten a Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRANGELIST |
| Difficulty Rating | 1600 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [STRANGELIST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/STRANGELIST) |

---

## Problem Statement

Alice has a **strange singly-linked list**. A usual singly linked-list or a *not-strange linked list* consist of nodes pointing to exactly one node ( except for the the tail node which points to null ). However, in case of a **strange singly-linked list**, instead of pointing towards a single linked-list node, some nodes of the linked-list are pointing towards two nodes! Each node in the strange linked-list has two pointers named :
- **next**
- **child**

The “child” pointer of a node may again point towards a strange singly linked list.

Alice wants to restructure this linked-list into a *not-strange linked list*. While doing so, she must follow the following rules.

Let **cur** be a node in restructured linked-list, then
- **cur.next** must occur after cur in the restructured linked-list.
- All the nodes ( if any ) which are part of **cur.child** linked list must occur after the node cur and before the node **cur.next** in the restructured linked list.
- Let **cur** be a node in the restructured linked-list, then **cur.child** must be “null”.

**NOTE** : Refer to sample case for a visual depiction.

---

## Input Format

- The first line of the input contains a single integer T - the number of test cases. The description of T test cases follows.

- The first line of each test case contains a single integer $N$.

- The following $N - 1$ lines contain three space separated integers $u, v$ and $type$.
If the value of $type$ is equal to 0, then the next pointer of node with value equal to $u$ points towards the node with value equal to $v$.
If the value of type is equal to 1, then the child pointer of node with value equal to $u$ points towards the node with value equal to $v$.

- For C++ language, you need to:

Complete the function in the submit solution tab:

bool flatten(Node* head){ .  .  . }

---

## Output Format

For each test case, the function you complete should return the restructured linked-list.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2*10^5$
- It is guaranteed that the sum of $N$ over all test cases is less than or equal to $3*10^5$.

---

## Examples

**Example 1**

**Input**

```text
1
9
4 7 1
1 2 0
2 3 0
6 9 0
3 6 0
2 4 1
4 8 0
6 5 1
```

**Output**

```text
1 2 4 7 8 3 6 5 9
```

**Explanation**

![Alt text](https://s3.amazonaws.com/codechef_shared/download/Images/Internal+problems_images/strange_list.JPG "a title")

![Alt text](https://s3.amazonaws.com/codechef_shared/download/Images/Internal+problems_images/not_strange_list.JPG "a title")

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore the problem of flattening a **strange singly-linked list**. In this list, every node has two pointers:
- **next**: pointing to the immediate next node,
- **child**: pointing to the head of another linked list.

The objective is to flatten the list so that every node’s child list is inserted between the node and its original next node, and all child pointers are set to `null`.

In simpler terms, given a node
$$ \text{cur} $$
with a child list, we must restructure the list so that all nodes in
$$ \text{cur.child} $$
appear between
$$ \text{cur} $$
and
$$ \text{cur.next} $$. The final flattened list should have every node’s child pointer set to `null`.

The main challenge is to achieve this efficiently given the constraint that the total number of nodes (across test cases) can be as high as
$$ 3 \times 10^5, $$
which calls for an algorithm with time complexity of
$$ O(n). $$

Below, we discuss **two approaches** to solve the problem.

---

### **Approach 1: Recursive Depth-First Flattening**

**Idea:**

We recursively flatten the child sublist and then merge it with the main list. For each node:
1. **If the node has a child:**
   - Recursively flatten the child list.
   - Set the node's `child` pointer to `null`.
   - Insert the flattened child list between the current node and its next node.
   - Traverse the flattened child list to its end and attach the stored `next` pointer.
2. **Else:**
   - Simply move to the next node.

Because each node is processed only once, the overall time complexity is
$$ O(n). $$

**Example Walkthrough:**

Consider a node `cur` with a link to its child list. After flattening, the list order is modified from:

$$ \text{cur} \rightarrow \text{cur.child} \rightarrow \ldots \rightarrow \text{tail of child} \rightarrow \text{cur.next} $$

This approach guarantees that all nodes from the child list appear between `cur` and `cur.next`.

**Code Implementation:**

Below is the code implementation using recursion in both C++ and Python.

---

### **Approach 2: Iterative Flattening Using a Stack**

**Idea:**

In the iterative approach, we simulate the recursion with an explicit stack:
1. Start with the head of the list.
2. For the current node:
   - **If it has a child:**
     - If `cur.next` exists, push it onto the stack.
     - Set `cur.next` to `cur.child` and set `cur.child` to `null`.
   - **If there is no next node and the stack is not empty:**
     - Pop the top node from the stack and assign it as `cur.next`.
3. Continue this process until the end of the list is reached.

This method is efficient and avoids the overhead of recursive calls, while still ensuring a depth-first order in flattening.

**Example Walkthrough:**

Imagine processing a node with a child pointer. We store `cur.next` (if any) on the stack, process the child list, and then resume by popping from the stack when needed. This maintains the desired order:

$$ \text{cur} \rightarrow \text{cur.child} \rightarrow \ldots \rightarrow \text{tail of child} \rightarrow \text{stored } \text{cur.next} $$

**Code Implementation:**

Below is an iterative solution using a stack in both C++ and Python.

---

### **Summary**

Both approaches ensure the flattened list respects the rules:
- Every `cur.child` is set to `null`.
- The child list is inserted directly between the node and its original `next` pointer.
- The overall order follows a depth-first sequence.

While **Approach 1 (Recursive)** is conceptually simple and leverages the call stack, **Approach 2 (Iterative with a Stack)** is a good alternative if you want to avoid recursion limits. Both have a time complexity of
$$ O(n) $$
and are effective for this problem.

Below, you will find the complete code implementations for both approaches in the prescribed format.

Happy coding!

</details>
