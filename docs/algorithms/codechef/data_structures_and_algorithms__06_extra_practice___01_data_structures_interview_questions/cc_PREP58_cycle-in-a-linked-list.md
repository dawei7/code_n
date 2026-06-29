# Cycle in a linked list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP58 |
| Difficulty Rating | 1100 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [PREP58](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/PREP58) |

---

## Problem Statement

You are given a linked list $A$ of size $N$.

Return the node where the cycle begins in the linked list. If there is no cycle, return NULL.

### Input:

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains three lines of input.
- First line contains an integer $N$, length of the linked list $A$.
- Second line contains $A_1, A_2, \ldots A_N$, the value of the linked list nodes starting from the head for the linked list.
- Third line contains an integer denoting the index of the node where the cycle starts.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node detectCycle(Node head){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* detectCycle(Node* head){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def detectCycle(head):
```
### Output:
The function you complete should return the required answer.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2
8 5
1
2
5 9
1
3
5 6 8
2
```

**Output**

```text
8
5
6
```

**Explanation**

**Test case $1$:** The list is of the form $8 \rightleftharpoons 5$, where $8$ is the head. Thus, the cycle starts from $8$.

**Test case $2$:** The list is of the form $5 \rightleftharpoons 9$, where $5$ is the head. Thus, the cycle starts from $5$.

**Test case $3$:** The list is of the form $5\rightarrow 6 \rightleftharpoons 8$, where $5$ is the head. Thus, the cycle starts from $6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
8 5
1
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
2
5 9
1
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
3
5 6 8
2
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Editorial: Detecting the Start of a Cycle in a Linked List

In this lesson, we explore the problem of identifying the node at which a cycle begins in a linked list. Understanding and solving this problem is essential for interviews in data structures and algorithms.

---

### Problem Overview

Given a linked list, our goal is to detect if there is a cycle and, if so, return the node where the cycle starts. If there is no cycle, we return `NULL` (or `None` in Python).

---

### Approach 1: Floyd's Cycle Detection (Tortoise and Hare)

The **Floyd's Cycle Detection** algorithm is a two-pointer technique where:
- A **slow pointer** moves one step at a time.
- A **fast pointer** moves two steps at a time.

If there is a cycle, these pointers will eventually meet inside the cycle. Once they meet, we reset one pointer to the head and then move both pointers one step at a time. The point where they meet again is the starting node of the cycle.

**Mathematical Insight:**

Let $L$ be the distance from the head to the start of the cycle, $C$ be the cycle's length, and $x$ be the distance from the cycle start to the meeting point. At the meeting point:
$$
\text{Distance of slow pointer} = L + x
$$
$$
\text{Distance of fast pointer} = L + x + k \cdot C
$$
Since the fast pointer travels twice as fast:
$$
2(L + x) = L + x + k \cdot C \implies L + x = k \cdot C \implies L = k \cdot C - x
$$
Thus, by resetting one pointer to the head and advancing both one step at a time, they meet at the starting node of the cycle.

**Time Complexity:** $O(n)$
**Space Complexity:** $O(1)$

#### Code Implementation

**C++:**

```cpp
class Solution
{
    public:
    Node* detectCycle(Node* head)
    {
        if (!head || !head->next)
            return NULL;

        Node* slow = head;
        Node* fast = head;
        Node* entry = head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
            {
                while (slow != entry)
                {
                    slow = slow->next;
                    entry = entry->next;
                }
                return entry;
            }
        }
        return NULL;
    }
};
```

**Python:**

```python
class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        entry = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None
```

---

### Approach 2: Hashing (Using a Set for Visited Nodes)

Another approach uses a hash set to store visited nodes:
- As you traverse the linked list, store each node in a set.
- If you encounter a node that is already in the set, that node marks the start of the cycle.

This method is straightforward to implement at the expense of extra space.

**Time Complexity:** $O(n)$
**Space Complexity:** $O(n)$

#### Code Implementation

**C++:**

```cpp
#include
class Solution
{
    public:
    Node* detectCycle(Node* head)
    {
        std::unordered_set visited;
        while (head)
        {
            if (visited.find(head) != visited.end())
                return head;
            visited.insert(head);
            head = head->next;
        }
        return NULL;
    }
};
```

**Python:**

```python
class Solution:
    def detectCycle(self, head):
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
```

---

### Conclusion

- **Floyd's Cycle Detection** is preferred due to its optimal space usage ($O(1)$) and is an essential technique to grasp for interviews.
- The **Hashing Approach** offers a simpler, more intuitive solution but requires extra memory.

Understanding both methods improves your problem-solving toolkit and prepares you for various interview scenarios in the domain of linked lists and cycle detection.

Happy Coding!

</details>
