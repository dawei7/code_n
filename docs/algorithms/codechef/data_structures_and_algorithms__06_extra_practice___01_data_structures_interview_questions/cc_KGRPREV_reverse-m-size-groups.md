# Reverse m size groups

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KGRPREV |
| Difficulty Rating | 1600 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [KGRPREV](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/KGRPREV) |

---

## Problem Statement

You are given a linked list with $N$ nodes. You have to perform following commands -
- Make groups of size $M$ from the head node to the last node.
- Assuming $x$ groups are created, you have to reverse the order of nodes in each group.
- Relative order of the groups in the final linked list must remain the same i.e after reversing, all the elements of group $1$ should appear before group $2$ and so on.

In order to solve this problem, you just have to complete the function

Node* reverseMSizeGroups(Node* head, int M) by returning the head node of the linked list

It is guaranteed that $N$ is divisible by $M$ for all test cases.

---

## Input Format

- First line will contain $T$, the number of testcases. Then the testcases follow.
- The first line of each test case contains 2 integers $N$ - length of linked list and $M$-group size
- Second line of each test case contains $N$ space separated integers $val_1, val_2,.... val_i,... val_n$ where $val_i$ is the value stored at ith node starting from the head node.

**Note:**

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* reverseMSizeGroups(Node* head, int M)
```
$\ $

---

## Output Format

Using the function you complete, for each testcase linked list generated must be the required linked list.

- For each test case N space separated integers $nval_1, nval_2, .., nval_i , ... nval_N$ will be outputted, where $nval_i$ is the new value stored at ith node starting from the head node.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$, $N$ is divisible by $M$
- $1 \leq val_i \leq 10^5$

Sum of $N$ over all test cases will not exceed 10^5

---

## Examples

**Example 1**

**Input**

```text
2
9 3
1 2 3 4 5 6 7 8 9
10 2
100 102 99 98 10 232 12 45 123 43
```

**Output**

```text
3 2 1 6 5 4 9 8 7
102 100 98 99 232 10 45 12 43 123
```

**Explanation**

**Testcase 1** : Given Linked List - 1 $\rightarrow$ 2 $\rightarrow$  3 $\rightarrow$  4 $\rightarrow$  5 $\rightarrow$  6 $\rightarrow$  7 $\rightarrow$  8 $\rightarrow$  9

We need to make groups of 3 and reverse them. So, final linked list will be

3 $\rightarrow$ 2 $\rightarrow$ 1   $\rightarrow$   6 $\rightarrow$ 5 $\rightarrow$ 4   $\rightarrow$  9 $\rightarrow$ 8 $\rightarrow$ 7

**Testcase 2** : Given Linked List - 100 $\rightarrow$ 102 $\rightarrow$  99 $\rightarrow$  98 $\rightarrow$  10 $\rightarrow$  232 $\rightarrow$  12 $\rightarrow$  45 $\rightarrow$ 123 $\rightarrow$ 43

We need to make groups of 2 and reverse them. So, final linked list will be

102 $\rightarrow$ 100   $\rightarrow$    98 $\rightarrow$ 99   $\rightarrow$  232 $\rightarrow$ 10   $\rightarrow$    45 $\rightarrow$ 12   $\rightarrow$   43 $\rightarrow$ 123

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9 3
1 2 3 4 5 6 7 8 9
```

**Output for this case**

```text
3 2 1 6 5 4 9 8 7
```



#### Test case 2

**Input for this case**

```text
10 2
100 102 99 98 10 232 12 45 123 43
```

**Output for this case**

```text
102 100 98 99 232 10 45 12 43 123
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on Reversing ${M}$-Size Groups in a Linked List

In this lesson, we discuss various approaches to reverse nodes in a linked list in groups of ${M}$. Given a linked list of ${N}$ nodes, our goal is to perform the following steps:
- **Group Formation:** Divide the list into groups of size ${M}$.
- **Group Reversal:** Reverse the order of nodes in each group.
- **Group Connection:** Maintain the overall order of the groups in the final list.

We will explore two different approaches to solve this problem.

---

## 1. Iterative Approach with Pointer Manipulation

### Methodology
In this approach, we iterate through the linked list and reverse nodes in groups of ${M}$ using pointer manipulation. We use a loop to reverse each segment of ${M}$ nodes and then connect the reversed groups together.

### Explanation
- **Grouping:** Start with a pointer `current` at the head of the list.
- **Reversal:** For each group, use a loop to reverse the next ${M}$ nodes. We maintain three pointers: one to traverse (`curr`), one for the previous node (`prev`), and one to store the next node (`nextNode`).
- **Connecting Groups:** After reversing a group, connect it with the tail of the previous group.
- **Complexity:** This approach works in $O({N})$ time and uses $O(1)$ extra space.

### Code Implementation

#### C++ Code
```cpp
// C++ Iterative Approach
Node* reverseMSizeGroups(Node* head, int M) {
    if (!head || M == 1)
        return head;
    Node* current = head;
    Node* newHead = nullptr;
    Node* prevTail = nullptr;
    while (current) {
        Node* groupHead = current;
        Node* prev = nullptr;
        Node* curr = current;
        for (int i = 0; i < M; i++) {
            Node* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        if (newHead == nullptr)
            newHead = prev;
        if (prevTail != nullptr)
            prevTail->next = prev;
        prevTail = groupHead;
        current = curr;
    }
    return newHead;
}
```

#### Python Code
```python
# Python Iterative Approach
def reverse_m_size_groups(head, M):
    if head is None or M == 1:
        return head
    current = head
    newHead = None
    prevTail = None
    while current:
        groupHead = current
        prev = None
        curr = current
        for _ in range(M):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        if newHead is None:
            newHead = prev
        if prevTail is not None:
            prevTail.next = prev
        prevTail = groupHead
        current = curr
    return newHead
```

---

## 2. Stack-Based Approach

### Methodology
In the stack-based approach, we use a stack to temporarily store nodes of each group. By pushing ${M}$ nodes onto the stack and then popping them, we obtain the nodes in reversed order.

### Explanation
- **Stack Usage:** For each group, push the ${M}$ nodes into a stack.
- **Reversal:** Pop nodes from the stack to reverse the order.
- **Group Connection:** Connect the reversed nodes to the previously processed section of the list.
- **Complexity:** This approach works in $O({N})$ time and uses $O({M})$ extra space due to the stack.

### Code Implementation

#### C++ Code
```cpp
// C++ Stack-Based Approach
#include
Node* reverseMSizeGroups(Node* head, int M) {
    if (!head || M == 1)
        return head;
    std::stack s;
    Node* current = head;
    Node* newHead = nullptr;
    Node* prev = nullptr;
    while (current) {
        int count = 0;
        Node* temp = current;
        while (temp && count < M) {
            s.push(temp);
            temp = temp->next;
            count++;
        }
        while (!s.empty()) {
            Node* node = s.top();
            s.pop();
            if (newHead == nullptr) {
                newHead = node;
                prev = node;
            } else {
                prev->next = node;
                prev = node;
            }
        }
        prev->next = temp;
        current = temp;
    }
    return newHead;
}
```

#### Python Code
```python
# Python Stack-Based Approach
def reverse_m_size_groups(head, M):
    if head is None or M == 1:
        return head
    stack = []
    current = head
    newHead = None
    prev = None
    while current:
        count = 0
        temp = current
        while temp and count < M:
            stack.append(temp)
            temp = temp.next
            count += 1
        while stack:
            node = stack.pop()
            if newHead is None:
                newHead = node
                prev = node
            else:
                prev.next = node
                prev = node
        prev.next = temp
        current = temp
    return newHead
```

---

## Summary

We discussed two effective approaches to reverse ${M}$-sized groups in a linked list:

1. **Iterative Approach:** Uses pointer manipulation with $O({N})$ time and $O(1)$ extra space.
2. **Stack-Based Approach:** Utilizes an auxiliary stack to reverse nodes in a group with $O({N})$ time and $O({M})$ extra space.

Each approach offers its own advantages and trade-offs, allowing you to choose the one that best fits the constraints of the problem at hand. These methods provide valuable insights into linked list manipulation, which is a frequent topic in technical interviews.

</details>
