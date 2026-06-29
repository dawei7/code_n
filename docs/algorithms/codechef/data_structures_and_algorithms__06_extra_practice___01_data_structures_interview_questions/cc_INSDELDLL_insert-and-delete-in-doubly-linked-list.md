# Insert and Delete in Doubly Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSDELDLL |
| Difficulty Rating | 1300 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [INSDELDLL](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/INSDELDLL) |

---

## Problem Statement

You are given the head of a doubly linked list $A$ of length $N$. The values in the list are $A_1, A_2, \ldots, A_N$ respectively. You need to complete a function that inserts a node with a given value at the given position and a function that deletes a node at the given position. The positions are numbered from $1$ to $N$.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains two space-separated integers $N$ and $Q$.

- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

- $Q$ lines follow. The $i$-th of these lines starts with an integer $T_i$ denoting the type of the query. If $T_i=1$, the $i$-th lines contains two space-separated integers $P_i$ and $V_i$ denoting the position and the value of the node that should be inserted respectively. If $T_i=2$, the $i$-th line contains a single integer $P_i$ denoting the position of the node that should be deleted. It is guaranteed that it will be possible to insert a node at the given position or delete the node at the given position.

**Note:**
- For Java language, you need to:

Complete the functions in the submit solution tab:
```
Node insertNode(Node head, int position, int value){...}

Node deleteNode(Node head, int position){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* insertNode(struct Node* head, int position, int value){...}

Node* deleteNode(struct Node* head, int position){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def insertNode(head, position, value):

def deleteNode(head, position):
```

---

## Output Format

- For each query in each test case, the appropriate function you completed will be called and it should return the head of the doubly-linked list on which the appropriate operation has been performed.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 1000$
- $1 \leq Q \leq 100$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- $1 \leq T_i \leq 2$ for each valid $i$
- when deleting a node, $P_i$ is between $1$ and the **current size of the list** for each valid $i$
- when inserting a node, $P_i$ is between $1$ and the **current size of the list plus one** for each valid $i$
- the list will not become empty after any query
- the size of the list will be at most $1008$ after each query
- $1 \leq V_i \leq 10^9$
- the sum of $N$ over all test cases does not exceed $1000$

---

## Examples

**Example 1**

**Input**

```text
1
5 3
1 2 3 4 5
2 2
1 2 6
2 5
```

**Output**

```text
1 6 3 4
```

**Explanation**

**Example case 1:** After deleting the node at position $2$, the order of the values is $[1,3,4,5]$. After inserting a node with value $6$ at the position $2$, the order of the values is $[1,6,3,4,5]$. Finally, after deleting the node at position $5$, the order of the values is $[1,6,3,4]$.

**Example 2**

**Input**

```text
1
3 4
1 2 3
1 4 4
1 5 1
2 1
2 4
```

**Output**

```text
2 3 4
```

**Explanation**

**Example case 1:** After inserting a node with value $4$ at the end of the list, the order of the values is $[1,2,3,4]$. After inserting a node with value $1$ at the end of the list, the order of the values is $[1,2,3,4,1]$. After deleting the first node of the list, the order of the values is $[2,3,4,1]$. Finally, after deleting the last node of the list, the order of the values is $[2,3,4]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to perform insertion and deletion operations on a doubly linked list. A doubly linked list is a data structure where each node has a pointer to both its next and previous nodes. This allows bidirectional traversal, which is very useful when handling operations near both ends of the list.

In our problem, we are required to:
- **Insert** a new node with a given value at a specified position.
- **Delete** a node from a specified position.

We will discuss the main approach used to solve this problem, walk through the logic step by step, and finally present the code implementation for both C++ and Python.

---

### Approach 1: Direct Traversal Method

This approach involves the following key steps:

1. **Insertion Operation:**

   To insert a new node at position $p$:
   - **Edge Case (Insertion at Head):**
     If $p = 1$, the new node becomes the head of the list. We update the new node's `next` pointer to point to the current head. If the list is not empty, ensure that the current head's `prev` pointer is updated to reference the new node.

   - **General Case (Insertion in Middle/End):**
     If $p > 1$, we traverse the list from the head until reaching the node at position $p - 1$. This is done with a simple loop that advances a pointer along the list. Once the $(p-1)\text{-th}$ node is found, we set:
     $$
     \begin{aligned}
     \text{newNode.next} &= (\text{p-1 node}).\text{next} \\
     \text{newNode.prev} &= (\text{p-1 node})
     \end{aligned}
     $$
     If the $(p-1)\text{-th}$ node’s `next` is not NULL, update that node’s `prev` pointer to point back to the new node. Finally, update the `(p-1)` node’s `next` pointer to the new node.

2. **Deletion Operation:**

   To delete a node at position $p$:
   - **Edge Case (Deletion at Head):**
     When $p = 1$, we update the head pointer to reference the node after the head. If the new head is not NULL, its `prev` pointer is set to NULL.

   - **General Case (Deletion in Middle/End):**
     For $p > 1$, traverse the list until reaching the $p\text{-th}$ node. Then:
     $$
     \begin{aligned}
     (\text{p-th node.prev}).\text{next} &= (\text{p-th node}).\text{next} \\
     (\text{p-th node.next}).\text{prev} &= (\text{p-th node}).\text{prev} \quad \text{(if it exists)}
     \end{aligned}
     $$
     Finally, free (or delete) the $p\text{-th}$ node.

The time complexity for both insertion and deletion is $O(p)$ per operation, where $p$ is the position of the node. Given that the maximum list size is small ($\leq 1008$), this approach is efficient.

---

### Code Implementation

Below are the detailed implementations for this approach in both C++ and Python. The code strictly follows the given template.

---

#### C++ Code

```cpp
/*struct Node {
	int val;
	struct Node* next;
	struct Node* prev;
	Node(int x){
		val = x;
		next = NULL;
		prev = NULL;
	}
};*/

Node* insertNode(Node* head, int position, int value){
    Node* newNode = new Node(value);
    if (position == 1) {
        newNode->next = head;
        if(head) head->prev = newNode;
        return newNode;
    }
    Node* current = head;
    for (int i = 1; i < position - 1 && current; i++){
        current = current->next;
    }
    if(!current) return head;
    newNode->next = current->next;
    newNode->prev = current;
    if(current->next) current->next->prev = newNode;
    current->next = newNode;
    return head;
}

Node* deleteNode(Node* head, int position){
    if(!head) return NULL;
    if(position == 1) {
        Node* newHead = head->next;
        if(newHead) newHead->prev = NULL;
        delete head;
        return newHead;
    }
    Node* current = head;
    for (int i = 1; i < position && current; i++){
        current = current->next;
    }
    if(!current) return head;
    current->prev->next = current->next;
    if(current->next) current->next->prev = current->prev;
    delete current;
    return head;
}
```

---

#### Python Code

```python
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
"""

def insertNode(head, position, value):
    newNode = Node(value)
    if position == 1:
        newNode.next = head
        if head:
            head.prev = newNode
        return newNode
    current = head
    curr_pos = 1
    while curr_pos < position - 1 and current is not None:
        current = current.next
        curr_pos += 1
    if current is None:
        return head
    newNode.next = current.next
    newNode.prev = current
    if current.next is not None:
        current.next.prev = newNode
    current.next = newNode
    return head

def deleteNode(head, position):
    if head is None:
        return None
    if position == 1:
        newHead = head.next
        if newHead is not None:
            newHead.prev = None
        return newHead
    current = head
    curr_pos = 1
    while curr_pos < position and current is not None:
        current = current.next
        curr_pos += 1
    if current is None:
        return head
    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
    return head
```

---

### Summary

In conclusion, the **Direct Traversal Method** is both intuitive and efficient for this problem. By carefully handling edge cases (insertion/deletion at the head) and updating the `next` and `prev` pointers of adjacent nodes, we ensure that the doubly linked list remains valid after every operation. Both C++ and Python implementations follow this logic, making it a versatile approach for managing doubly linked lists in various programming languages.

</details>
