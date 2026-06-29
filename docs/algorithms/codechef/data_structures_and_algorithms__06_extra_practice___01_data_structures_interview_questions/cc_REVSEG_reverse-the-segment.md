# Reverse the Segment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REVSEG |
| Difficulty Rating | 1500 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [REVSEG](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/REVSEG) |

---

## Problem Statement

You are given the head of a singly linked list $A$ of length $N$. The values in the list are $A_1, A_2, \ldots, A_N$ respectively. You are also given two integers $L$ and $R$. You need to reverse the nodes of the list from position $L$ to position $R$.

#### **Function Description**

You are given a function named **`reverseSegment`** that you must complete.

The function receives the following parameters:

* **`head`** – the head pointer of a singly linked list
* **`L`** – the starting position of the segment to be reversed (1-indexed)
* **`R`** – the ending position of the segment to be reversed (1-indexed)

The linked list contains `N` nodes, and you need to reverse only the nodes from position **L** to **R**, while keeping the rest of the list unchanged.

The function must **return the head** of the linked list **after reversing the segment** between positions `L` and `R`.

The input and output formats given below are only if you want to test using custom inputs

#### Constraints:
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq L \leq R \leq N$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains three space-separated integers $N$, $L$ and $R$.

- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, the function you complete should return the head of the list in which the nodes from the appropriate segment are reversed.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq L \leq R \leq N$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
6 2 5
1 2 3 4 5 6
4 1 3
1 2 3 4
5 3 5
10 4 3 6 7
3 1 3
5 6 4
```

**Output**

```text
1 5 4 3 2 6
3 2 1 4
10 4 7 6 3
4 6 5
```

**Explanation**

**Example case 1:** After reversing the segment $[2,5]$ of the list, the order of the values is $1,5,4,3,2,6$.

**Example case 2:** After reversing the segment $[1,3]$ of the list, the order of the values is $3,2,1,4$.

**Example case 3:** After reversing the segment $[3,5]$ of the list, the order of the values is $10,4,7,6,3$.

**Example case 4:** After reversing the whole list, the order of the values is $4,6,5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 2 5
1 2 3 4 5 6
```

**Output for this case**

```text
1 5 4 3 2 6
```



#### Test case 2

**Input for this case**

```text
4 1 3
1 2 3 4
```

**Output for this case**

```text
3 2 1 4
```



#### Test case 3

**Input for this case**

```text
5 3 5
10 4 3 6 7
```

**Output for this case**

```text
10 4 7 6 3
```



#### Test case 4

**Input for this case**

```text
3 1 3
5 6 4
```

**Output for this case**

```text
4 6 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial for Reversing a Sublist in a Singly Linked List

In this lesson, we focus on the problem of reversing a segment of a singly linked list between positions $L$ and $R$. Given a linked list with nodes containing values $A_1, A_2, \dots, A_N$, our goal is to reverse the nodes from position $L$ to $R$ while keeping the remaining nodes intact. This problem is very common in DSA interviews and helps you understand pointer manipulation, recursion, and alternative strategies using extra space.

Below, we discuss three important approaches to solve this problem.

---

## Approach 1: Iterative In-Place Reversal

### Explanation

The iterative approach uses constant extra space, making it both time-efficient and space-efficient. The procedure is as follows:

1. **Dummy Node Creation:** Create a dummy node to simplify edge-case handling (e.g., when $L = 1$).
2. **Traverse to Sublist Start:** Walk through the list to reach the node immediately before the $L^\text{th}$ node.
3. **Iterative Reversal:** Reverse the segment between $L$ and $R$ by re-linking the pointers. A typical method is by repeatedly removing the node right after the start of the segment and inserting it immediately after the node preceding the segment.

The overall time complexity is $O(N)$ with $O(1)$ extra space.

### Code Implementation

**C++ Implementation:**
```cpp
Node* reverseSegment(Node* head, int L, int R){
    if (!head || L == R) return head;
    Node dummy(0);
    dummy.next = head;
    Node* prev = &dummy;
    for (int i = 1; i < L; i++) {
        prev = prev->next;
    }
    Node* start = prev->next;
    Node* then = start->next;
    for (int i = L; i < R; i++) {
        start->next = then->next;
        then->next = prev->next;
        prev->next = then;
        then = start->next;
    }
    return dummy.next;
}
```

**Python Implementation:**
```python
def reverseSegment(head, L, R):
    if not head or L == R:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    for _ in range(1, L):
        prev = prev.next
    start = prev.next
    then = start.next
    for _ in range(L, R):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next
    return dummy.next
```

---

## Approach 2: Recursive Reversal

### Explanation

This approach uses recursion to reverse the segment by breaking the problem into two parts:
1. **Reverse First $n$ Nodes:** Create a helper function (often named `reverseN`) that reverses the first $n$ nodes of the list and returns both the new head and the successor node (the node following the reversed segment).
2. **Adjust for Offset $L$:** For the overall sublist reversal from $L$ to $R$, recursively move the head pointer until the $L^\text{th}$ node is reached, and then apply the `reverseN` function for $R$ nodes. The recursion naturally adjusts the pointers back.

This method provides an elegant solution and helps build a deeper understanding of recursion with linked lists.

### Code Implementation

**C++ Implementation:**
```cpp
Node* reverseN(Node* head, int n, Node*& successor) {
    if(n == 1){
        successor = head->next;
        return head;
    }
    Node* last = reverseN(head->next, n - 1, successor);
    head->next->next = head;
    head->next = successor;
    return last;
}

Node* reverseSegment(Node* head, int L, int R){
    if(L == 1) {
        Node* successor = nullptr;
        return reverseN(head, R, successor);
    }
    head->next = reverseSegment(head->next, L - 1, R - 1);
    return head;
}
```

**Python Implementation:**
```python
def reverseN(head, n):
    if n == 1:
        return head, head.next
    last, successor = reverseN(head.next, n - 1)
    head.next.next = head
    head.next = successor
    return last, successor

def reverseSegment(head, L, R):
    if L == 1:
        new_head, _ = reverseN(head, R)
        return new_head
    head.next = reverseSegment(head.next, L - 1, R - 1)
    return head
```

---

## Approach 3: Using an Auxiliary Array

### Explanation

The auxiliary array approach simplifies the problem by decoupling node storage from pointer manipulation. The steps involved are:

1. **Store Nodes in an Array:** Traverse the list and store pointers to each node in an array.
2. **Reverse the Subarray:** Reverse the part of the array corresponding to indices $L-1$ to $R-1$.
3. **Re-link the Nodes:** Iterate through the array to update the `next` pointers of each node to rebuild the list with the reversed segment.

This approach uses $O(N)$ extra space, which can be acceptable based on problem constraints.

### Code Implementation

**C++ Implementation:**
```cpp
#include
Node* reverseSegment(Node* head, int L, int R){
    if (!head) return head;
    std::vector nodes;
    Node* curr = head;
    while(curr){
        nodes.push_back(curr);
        curr = curr->next;
    }
    int start = L - 1, end = R - 1;
    while(start < end){
        std::swap(nodes[start], nodes[end]);
        start++;
        end--;
    }
    for(size_t i = 0; i < nodes.size() - 1; i++){
        nodes[i]->next = nodes[i+1];
    }
    nodes.back()->next = nullptr;
    return nodes[0];
}
```

**Python Implementation:**
```python
def reverseSegment(head, L, R):
    if not head:
        return head
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    i, j = L - 1, R - 1
    while i < j:
        nodes[i], nodes[j] = nodes[j], nodes[i]
        i += 1
        j -= 1
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = None
    return nodes[0]
```

---

## Conclusion

Each of the three approaches presented has its merits:

- The **Iterative In-Place Reversal** is optimal when you want to minimize extra memory usage, working in $O(N)$ time and $O(1)$ space.
- The **Recursive Reversal** approach offers a mathematically elegant solution with minimal code, though care must be taken with recursion depths.
- The **Auxiliary Array** method provides simplicity in implementation by leveraging extra space, making it easier to understand and implement for beginners.

Choose the approach that best fits your understanding and the constraints of your problem.

</details>
