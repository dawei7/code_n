# Critical points in a Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CRITLIST |
| Difficulty Rating | 1000 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [CRITLIST](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/CRITLIST) |

---

## Problem Statement

Given the head of a linked list, Find the number of critical points. (The starting and end are not considered critical points).

Local minima or maxima are called critical points.

A Node is called a local minima if both next and previous elements are greater than the current element.

A Node is called a local maxima if both next and previous elements are smaller than the current element.

---

## Input Format

- The first line contains $N$, the number of elements in the linked list.
- The second line contains a number $m$ which denotes where the loop will be made from the tail of the linked list. $0 \le m \lt n $ (i.e the first node is called $0^{th}$ node).
- (Naturally the Linked list has connections from $i^{th}$ node to $i+1^{th}$ node).
- (Note.  Node values will be zero)

$\ $
- For C++ language, you need to:

Complete the function in the submit solution tab:
```
int solve(Node* head){}
```
$\ $

---

## Output Format

-1 if a loop doesnt exist, else the length of the loop.

---

## Constraints

- $1 \leq$ Number of elements in the linked list  , $N$ $\leq 10^5$
- $1 \leq Node.data \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
8
1 2 3 3 3 5 1 3
```

**Output**

```text
2
```

**Explanation**

1 is a minima and 5 is a maxima hence there are 2 critical points

**Example 2**

**Input**

```text
7
1 2 3 2 1 3 2
```

**Output**

```text
3
```

**Explanation**

3rd node, 5th node and 6th node are the critical nodes, hence the answer is 3

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we are going to solve a problem where we need to count the number of critical points in a linked list. A node (except the first and last) is considered a critical point if it is either a local maximum or a local minimum. Formally, for a linked list with elements
$$\{l_0, l_1, \dots, l_{n-1}\},$$
a node at index $i$ (with $1 \leq i \leq n-2$) is critical if either

$$l_i > l_{i-1} \text{ and } l_i > l_{i+1},$$

or

$$l_i < l_{i-1} \text{ and } l_i < l_{i+1}.$$

We will discuss two common approaches to solve this problem.

### Approach 1: Iterative Pointer Traversal
In this approach, we traverse the linked list using three pointers:
- **prev** — points to the previous node.
- **curr** — points to the current node.
- **next** — points to the node following the current node.

At every step (starting from the second node and ending at the second last node), we compare the `data` of the current node with its adjacent nodes. If the condition for a local maximum or a local minimum holds, we increment our counter.

**Time Complexity:** $O(n)$
**Space Complexity:** $O(1)$

Below are the implementations for this approach in both C++ and Python.

#### C++ Implementation (Approach 1)
```cpp
/*
Node is defined as:
class Node{
  public:
  int data;
  Node* next;
  Node(int data){
      this->data = data;
      this->next = nullptr;
  }
}
*/
int solve(Node* head){
    if (!head || !head->next || !head->next->next) {
        return 0;
    }
    int criticalPoints = 0;
    Node* prev = head;
    Node* curr = head->next;
    Node* next = head->next->next;
    while (next) {
        if ((curr->data > prev->data && curr->data > next->data) ||
            (curr->data < prev->data && curr->data < next->data)) {
            criticalPoints++;
        }
        prev = curr;
        curr = next;
        next = next->next;
    }
    return criticalPoints;
}
```

#### Python Implementation (Approach 1)
```python
# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    # Return the number of critical points (integer)
    if not head or not head.next or not head.next.next:
        return 0
    critical = 0
    prev = head
    curr = head.next
    nxt = head.next.next
    while nxt:
        if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
            critical += 1
        prev = curr
        curr = nxt
        nxt = nxt.next
    return critical
```

---

### Approach 2: Converting Linked List to Array
In this approach, we first extract all the node values into an array. Once we have the array, we can easily access the neighboring elements using indices. For every element at index $i$ (with $1 \leq i \leq \text{len(array)} - 2$), we check if it satisfies either the local maximum or local minimum condition.

**Time Complexity:** $O(n)$
**Space Complexity:** $O(n)$ (due to auxiliary array)

This method may be conceptually simpler, especially for beginners, because array indexing makes checking neighbors straightforward.

Below are the implementations for this approach in both C++ and Python.

#### C++ Implementation (Approach 2)
```cpp
/*
Node is defined as:
class Node{
  public:
  int data;
  Node* next;
  Node(int data){
      this->data = data;
      this->next = nullptr;
  }
}
*/
int solve(Node* head){
    vector arr;
    Node* curr = head;
    while(curr){
        arr.push_back(curr->data);
        curr = curr->next;
    }
    if(arr.size() < 3) return 0;
    int count = 0;
    for (int i = 1; i < arr.size() - 1; i++){
        if ((arr[i] > arr[i-1] && arr[i] > arr[i+1]) ||
            (arr[i] < arr[i-1] && arr[i] < arr[i+1])){
            count++;
        }
    }
    return count;
}
```

#### Python Implementation (Approach 2)
```python
# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    # Return the number of critical points (integer)
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    if len(arr) < 3:
        return 0
    count = 0
    for i in range(1, len(arr) - 1):
        if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
            count += 1
    return count
```

### Summary and Intuition
- **Approach 1** uses constant extra space and directly traverses the linked list with three pointers. It’s efficient and avoids extra memory usage.
- **Approach 2** converts the list into an array, which may be easier for beginners to work with due to simpler index-based access. However, it uses additional space proportional to the number of nodes.

Both approaches have a time complexity of $O(n)$, making them suitable within the problem constraints. Choose the approach that best fits your familiarity with pointer manipulation or array operations.

Happy coding and best of luck with your DSA interviews!

</details>
