# Linked List - Intersection of Linked Lists

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP56 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [PREP56](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/PREP56) |

---

## Problem Statement

You are given heads of $2$ linked lists.

Find the point where these two linked lists **intersect** with each other and return the node data at the intersection.

### Input:

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of four lines of input.
- First line contains two space separated integers $N, M,$ and $X$, length of linked list $A$, $B$, and length of linked list after Merge Point.
- Second line contains $A_1, A_2, \ldots A_N$, value of the linked list nodes starting from the head for the first linked list.
- Third line contains $B_1, B_2, \ldots B_M$, value of the linked list nodes starting from the head for the second linked list.
- Fourth line contains $C_1, C_2, \ldots C_X$, value of the linked list nodes after the merge point of two linked lists.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node intersectPoint(Node head1, Node head2){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* intersectPoint(Node* head1, Node* head2){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def intersectPoint(headA, headB):
```
### Output:
The function you complete should return the required answer.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N, M, X \leq 5\cdot 10^4$
- $1 \leq A_i, B_i, C_i \leq 10^9$

### Sample Input:
```
3
3 3 3
2 12 17
26 35 38
43 49 55
2 1 2
3 9
12
20 27
1 1 3
5
8
11 13 20
```

### Sample Output:
```
43
20
11
```

### Sample Explanation:
**Test case $1$:** The first node of intersection has value $43$.

**Test case $2$:** The first node of intersection has value $20$.

**Test case $3$:** The first node of intersection has value $11$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Intersection Point of Two Linked Lists

In this lesson, we discuss how to find the intersection point of two linked lists. This is a classic problem in data structures and algorithms and is frequently asked in technical interviews. The intersection point is defined as the node at which the two linked lists merge into a single linked list.

There are several approaches to solve this problem. We will discuss three approaches:

---

## Approach 1: Two-Pointer (Pointer Switching) Technique

### Concept:
We use two pointers, one starting at the head of each list. The idea is to traverse both lists simultaneously. When a pointer reaches the end of a list, it is redirected to the head of the other list. Eventually, the two pointers will either meet at the intersection node or both reach the end (i.e., `NULL`) if there is no intersection. This works because the pointers traverse a total length of $$L_1 + L_2,$$ where $$L_1$$ and $$L_2$$ are the lengths of the two lists respectively.

### Complexity:
- **Time Complexity:** $$O(m+n)$$, where $$m$$ and $$n$$ are the lengths of the two lists.
- **Space Complexity:** $$O(1)$$, as we do not use any extra space.

### Code Explanation:
- **C++:** We initialize two pointers, `ptr1` and `ptr2`. In a loop, we advance each pointer. If a pointer reaches the end of a list, we redirect it to the head of the other list. When the pointers meet, we return the intersection node’s data.
- **Python:** The logic is identical to the C++ version. We check for `None` to handle the end of the list and then return the data of the intersection node.

Below are the code implementations for this approach.

```cpp
/* Template Code for C++ */
int intersectPoint(Node* head1, Node* head2)
{
    if (!head1 || !head2)
        return -1;

    Node* ptr1 = head1;
    Node* ptr2 = head2;

    while (ptr1 != ptr2) {
        ptr1 = ptr1 ? ptr1->next : head2;
        ptr2 = ptr2 ? ptr2->next : head1;
    }

    return (ptr1) ? ptr1->data : -1;
}
```

```python
# Template Code for Python
def intersetPoint(head1, head2):
    if head1 is None or head2 is None:
        return -1
    a, b = head1, head2
    while a is not b:
        a = a.next if a else head2
        b = b.next if b else head1
    return a.data if a is not None else -1
```

---

## Approach 2: Hashing Method

### Concept:
This approach involves using a hash set to store the nodes of the first linked list, and then traversing the second linked list. The first node we encounter in the second list that already exists in the set is the intersection node.

### Complexity:
- **Time Complexity:** $$O(m+n)$$.
- **Space Complexity:** $$O(m)$$ (or $$O(n)$$), which is the size of the hash set storing nodes from one list.

### Code Explanation:
- **C++:** We use an unordered set to store pointers from the first list. As we traverse the second list, we check if the node has been seen before.
- **Python:** We use a set to store nodes from the first list. Then, we iterate over the second list to find the intersecting node.

Below are the code implementations for this approach.

```cpp
/* Template Code for C++ */
#include

int intersectPoint(Node* head1, Node* head2)
{
    std::unordered_set nodes;
    while (head1 != nullptr) {
        nodes.insert(head1);
        head1 = head1->next;
    }
    while (head2 != nullptr) {
        if (nodes.find(head2) != nodes.end())
            return head2->data;
        head2 = head2->next;
    }
    return -1;
}
```

```python
# Template Code for Python
def intersetPoint(head1, head2):
    nodes = set()
    temp = head1
    while temp:
        nodes.add(temp)
        temp = temp.next
    temp = head2
    while temp:
        if temp in nodes:
            return temp.data
        temp = temp.next
    return -1
```

---

## Approach 3: Length Difference Method

### Concept:
In this method, we first calculate the lengths of both linked lists, denoted as $$L_1$$ and $$L_2$$. The difference $$d = |L_1 - L_2|$$ indicates how many extra nodes the longer list has. By advancing the pointer of the longer list by $$d$$ nodes, we align the start of the traversal for both lists. Then, we move both pointers one step at a time until they meet at the intersection.

### Complexity:
- **Time Complexity:** $$O(m+n)$$.
- **Space Complexity:** $$O(1)$$.

### Code Explanation:
- **C++:** We compute the lengths of the two lists. Then, we advance the pointer of the longer list by the difference in lengths before traversing both lists simultaneously.
- **Python:** We define a helper function to compute the length of a list. After computing the lengths, we align both pointers and then traverse until we find the intersection.

Below are the code implementations for this approach.

```cpp
/* Template Code for C++ */
int intersectPoint(Node* head1, Node* head2)
{
    int len1 = 0, len2 = 0;
    Node* ptr1 = head1;
    Node* ptr2 = head2;

    while (ptr1 != nullptr) {
        len1++;
        ptr1 = ptr1->next;
    }
    while (ptr2 != nullptr) {
        len2++;
        ptr2 = ptr2->next;
    }

    ptr1 = head1;
    ptr2 = head2;

    int diff = abs(len1 - len2);
    if (len1 > len2) {
        while (diff--) {
            ptr1 = ptr1->next;
        }
    } else {
        while (diff--) {
            ptr2 = ptr2->next;
        }
    }

    while (ptr1 && ptr2) {
        if (ptr1 == ptr2)
            return ptr1->data;
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    return -1;
}
```

```python
# Template Code for Python
def intersetPoint(head1, head2):
    def get_length(node):
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt

    len1 = get_length(head1)
    len2 = get_length(head2)

    diff = abs(len1 - len2)
    p, q = head1, head2

    if len1 > len2:
        for _ in range(diff):
            p = p.next
    else:
        for _ in range(diff):
            q = q.next

    while p and q:
        if p == q:
            return p.data
        p = p.next
        q = q.next
    return -1
```

---

## Final Thoughts

Each approach has its merits:

- **Two-Pointer Technique (Approach 1):** It is elegant and uses constant extra space.
- **Hashing Method (Approach 2):** It is straightforward to implement but requires extra space.
- **Length Difference Method (Approach 3):** It uses the concept of list lengths to align the pointers and also uses constant space.

For interview scenarios, the two-pointer technique is often preferred because of its simplicity and constant space requirements. However, understanding all three approaches provides a comprehensive grasp of the problem-solving strategies for linked list problems.

</details>
