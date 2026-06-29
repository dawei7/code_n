# Rotate the List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROTLIST |
| Difficulty Rating | 1300 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [ROTLIST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/ROTLIST) |

---

## Problem Statement

You are given the head of a singly linked list $A$ of length $N$. The values in the list are $A_1, A_2, \ldots, A_N$ respectively. You are also given a non-negative integer $R$. You need to rotate the list $R$ places to the right.

A single rotation to the right is an operation in which the last element of the list is moved to the first place in the list, while all the other elements are moved one place to the right.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains two space-separated integers $N$ and $R$.

- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Note:**
- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node rotateRight(Node head, int R){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* rotateRight(struct Node* head, int R){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def rotateRight(head, R):
```

---

## Output Format

- For each test case, the function you complete should return the head of the list which has been rotated to the right exactly $R$ times.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $0 \leq R \leq N-1$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
4 1
1 2 3 4
5 3
4 7 3 1 6
6 5
7 2 2 2 2 2
```

**Output**

```text
4 1 2 3
3 1 6 4 7
2 2 2 2 2 7
```

**Explanation**

**Example case 1:** After rotating the list once, the order of the elements is $[4,1,2,3]$.

**Example case 2:** After rotating the list $R=3$ times, the order of the elements is $[3,1,6,4,7]$.

**Example case 3:** After rotating the list $R=5$ times, the order of the elements is $[2,2,2,2,2,7]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1
1 2 3 4
```

**Output for this case**

```text
4 1 2 3
```



#### Test case 2

**Input for this case**

```text
5 3
4 7 3 1 6
```

**Output for this case**

```text
3 1 6 4 7
```



#### Test case 3

**Input for this case**

```text
6 5
7 2 2 2 2 2
```

**Output for this case**

```text
2 2 2 2 2 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Editorial: Rotating a Singly Linked List to the Right

In this lesson, we address the problem of rotating a singly linked list by $R$ places to the right. Put simply, a single right rotation moves the last node to the front, shifting all other nodes one position to the right.

We will explore **two approaches** that are essential for understanding and solving this problem:

---

#### **Approach 1: Two-Pointer / Circular List Approach (Efficient In-Place Method)**

**Overview:**
The idea here is to first compute the length of the list and then create a circular linked list by linking the tail back to the head. Once we have a circular structure, we find the point to break it such that the new head is achieved after performing right rotations.

**Steps:**

1. **Edge Cases:**
   Check if the list is empty, has only one node, or if $R$ is zero. In any of these cases, no rotation is needed.

2. **Determine the Length and Tail of the List:**
   Traverse the list to count the number of nodes ($L$) and to identify the tail (the last node).

3. **Normalize $R$:**
   Since rotating the list $L$ times results in the original list, update $R$ as:
   $$ R = R \mod L $$
   If $R$ becomes zero after this normalization, simply return the original list.

4. **Find the New Tail and New Head:**
   The new tail is the node at position
   $$ L - R - 1 $$
   (using 0-based indexing), and its next node (at index $L - R$) becomes the new head.

5. **Rotate the List:**
   - Break the list by setting the new tail's `next` to $nullptr$.
   - Connect the original tail's `next` to the original head to form the rotated list.

**C++ and Python Implementations:**

Below are the implementations using the above approach.

**C++ Code:**
```cpp
Node* rotateRight(Node* head, int R){
    if(head == nullptr || head->next == nullptr || R == 0)
        return head;
    int length = 1;
    Node* tail = head;
    while(tail->next){
        tail = tail->next;
        length++;
    }
    R = R % length;
    if(R == 0)
        return head;
    Node* newTail = head;
    for(int i = 0; i < length - R - 1; i++){
        newTail = newTail->next;
    }
    Node* newHead = newTail->next;
    newTail->next = nullptr;
    tail->next = head;
    return newHead;
}
```

**Python Code:**
```python
def rotateRight(head, R):
    if head is None or head.next is None or R == 0:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    R = R % length
    if R == 0:
        return head
    new_tail = head
    for _ in range(length - R - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
```

---

#### **Approach 2: Array Conversion Method (Using Extra Space)**

**Overview:**
In this approach, we convert the linked list into an array (or vector). Once the list is represented as an array, we can easily determine the new ordering of nodes using index calculations and then reconstruct the rotated linked list.

**Steps:**

1. **Edge Cases:**
   As before, handle cases where the list is empty, contains only one node, or where $R = 0$.

2. **Store the Nodes in an Array:**
   Traverse the linked list and store each node in an array. Let $L$ be the number of nodes.

3. **Normalize $R$:**
   Compute:
   $$ R = R \mod L $$
   If $R$ equals zero after normalization, return the original list.

4. **Reconstruct the List:**
   - The new head will be the node at index $L - R$.
   - Set the `next` pointer of the node at index $L - R - 1$ to $nullptr$.
   - Update the last node’s `next` to point to the original head.

**C++ and Python Implementations:**

Below is the code implementing the above logic.

**C++ Code:**
```cpp
#include
using namespace std;

Node* rotateRight(Node* head, int R){
    if(head == nullptr || head->next == nullptr || R == 0)
        return head;
    vector nodes;
    Node* cur = head;
    while(cur){
        nodes.push_back(cur);
        cur = cur->next;
    }
    int length = nodes.size();
    R = R % length;
    if(R == 0)
        return head;
    int newStart = length - R;
    Node* newHead = nodes[newStart];
    nodes[newStart - 1]->next = nullptr;
    nodes[length - 1]->next = head;
    return newHead;
}
```

**Python Code:**
```python
def rotateRight(head, R):
    if head is None or head.next is None or R == 0:
        return head
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    length = len(nodes)
    R %= length
    if R == 0:
        return head
    newStart = length - R
    nodes[newStart - 1].next = None
    nodes[length - 1].next = head
    return nodes[newStart]
```

---

### Conclusion

Both approaches solve the problem correctly:

- **Approach 1** is highly efficient and works in-place without using extra memory, making it ideal for interview situations where space optimization is critical.
- **Approach 2** utilizes an extra array to simplify the rotation logic by leveraging random access, which can be easier to understand and implement, though it uses additional space.

Understanding these methods deepens your grasp of linked list manipulations and reinforces different problem-solving strategies. Choose the method that best fits the constraints and requirements you face in your interview.

</details>
