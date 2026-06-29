# Reverse a Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RTLL |
| Difficulty Rating | 1400 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [RTLL](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/RTLL) |

---

## Problem Statement

The Chef gives you a singly linked list $A$ integers and ask you to help him reverse the list.

Complete the function "listReverse" in the code snippet that takes a single argument: head of the linked list.

---

## Input Format

- The first line contains an integer $N$ - representing the number of elements of the linked list.
- The second line contains $N$ integers - representing the elements of the linked list.

---

## Output Format

For each testcase, output will be in a single line containing a list returned by the function listReverse.

---

## Constraints

- $1 \leq N \leq 10^5$
- $-10^9 \leq $ Node->value  $\leq 10^9$

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
5 4 3 2 1
```

**Example 2**

**Input**

```text
5
1 1 3 2 1
```

**Output**

```text
1 2 3 1 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Reversing a Singly Linked List

In this lesson, we will explore two different approaches to reverse a singly linked list. Reversing a linked list is a common interview problem that tests your understanding of pointers (or references) and linked list data structures. We will explain each remaining approach in detail and provide implementations in both C++ and Python. Let's begin!

---

## Approach 1: Iterative Reversal

### Explanation
The iterative approach uses three pointers to reverse the list in a single traversal:
- $prev$: Initially set to $NULL$. It will eventually become the new head.
- $current$: Starts at the head of the original list.
- $next$: Temporarily holds the next node during traversal.

At each step, we:
1. Save $current$’s next node in $next$.
2. Reverse the pointer of the $current$ node to point to $prev$.
3. Move $prev$ and $current$ one step forward.

This process continues until $current$ becomes $NULL$, indicating the end of the list. The final $prev$ will be the new head. This method has a time complexity of $O(n)$ and uses $O(1)$ extra space.

### C++ Code
```cpp
/*struct Node {
    int data;
    struct Node* next;
    Node(int data)
    {
        this->data = data;
        next = NULL;
    }
};*/

Node* reverseList(Node* head) {
    Node* prev = NULL;
    Node* curr = head;
    while (curr != NULL) {
        Node* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}
```

### Python Code
```python
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

---

## Approach 2: Using a Stack

### Explanation
This approach uses a stack to reverse the list by leveraging the Last-In-First-Out (LIFO) property:
1. Traverse the list and push each node onto a stack.
2. Pop nodes from the stack to rebuild the reversed list.

While this method maintains a time complexity of $O(n)$, it requires extra $O(n)$ space for the stack.

### C++ Code
```cpp
/*struct Node {
    int data;
    struct Node* next;
    Node(int data)
    {
        this->data = data;
        next = NULL;
    }
};*/

#include
Node* reverseList(Node* head) {
    if (!head) return head;
    std::stack nodeStack;
    Node* curr = head;
    while (curr) {
        nodeStack.push(curr);
        curr = curr->next;
    }
    Node* newHead = nodeStack.top();
    nodeStack.pop();
    curr = newHead;
    while (!nodeStack.empty()) {
        curr->next = nodeStack.top();
        nodeStack.pop();
        curr = curr->next;
    }
    curr->next = NULL;
    return newHead;
}
```

### Python Code
```python
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def reverse_list(head):
    if head is None:
        return head
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    new_head = stack.pop()
    curr = new_head
    while stack:
        curr.next = stack.pop()
        curr = curr.next
    curr.next = None
    return new_head
```

---

Each of these approaches has its own merits. The iterative method is most commonly used due to its space efficiency, while the stack-based approach provides a straightforward solution by leveraging an auxiliary data structure. Choose the method that best fits the constraints of your problem.

Happy coding and best of luck with your interviews!

</details>
