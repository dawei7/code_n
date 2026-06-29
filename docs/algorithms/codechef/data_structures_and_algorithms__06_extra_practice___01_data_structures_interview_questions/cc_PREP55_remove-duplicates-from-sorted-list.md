# Remove Duplicates from Sorted List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP55 |
| Difficulty Rating | 900 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [PREP55](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/PREP55) |

---

## Problem Statement

You are given head of the **non-empty** sorted linked list where the value of the $i^{th}$ node will be $A_i$.

Your task is to delete all duplicates such that each element appears only once and return the linked list sorted.

### Input:

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line contains one integer $N$ — the length of the linked list.
- The second line contains $N$ space separated integers $A_1, A_2, \ldots A_N$ — the value of the linked list nodes starting from the head for the linked list.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node removeDuplicates(Node head){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* removeDuplicates(Node* head){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def Node removeDuplicates(self, head):
```
### Output:
The function you complete should return the required answer.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N, A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
1 1 6 8 8
5
1 2 3 4 5
4
5 5 5 5
```

**Output**

```text
1 6 8 
1 2 3 4 5 
5
```

**Explanation**

**Test case $1$:** We will remove duplicate entry of $1$, $8$. So the sorted linked list will be $1 \rightarrow 6 \rightarrow 8$.

**Test case $2$:** There is no duplicate entry. So the sorted linked list will be $1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5$.

**Test case $3$:** We will remove duplicate entry of $5$. So the sorted linked list will be $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 1 6 8 8
```

**Output for this case**

```text
1 6 8
```



#### Test case 2

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
1 2 3 4 5
```



#### Test case 3

**Input for this case**

```text
4
5 5 5 5
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Removing Duplicates from a Sorted Linked List

In this lesson, we explore a common linked list problem where you are given a sorted linked list and must remove any duplicate elements so that each element appears only once. Since the list is sorted, duplicates occur consecutively, which simplifies our task.

Below, we describe two approaches to solve this problem and provide code implementations for each in both C++ and Python.

---

## Approaches to the Problem

### 1. Iterative Approach (Two-Pointer Technique)
Since the linked list is sorted, we can use an iterative approach with a pointer (or two-pointer technique) to traverse the list. At each node, we check if its next node has the same value. If it does, we remove the next node by adjusting the pointer. This method runs in $O(n)$ time and requires only $O(1)$ extra space.

**C++ Explanation:**
- Initialize a pointer `curr` to the head.
- Iterate as long as `curr` and `curr->next` are not null.
- If `curr->data` equals `curr->next->data`, delete the duplicate node and adjust the `next` pointer.
- Otherwise, move to the next node.

**Python Explanation:**
- Use a similar iterative loop.
- Check if `curr.data` equals `curr.next.data` and then bypass `curr.next` by linking it to the node after the duplicate.

---

### 2. Using Extra Space (Hash Set Method)
While the list is sorted, an alternative approach uses a hash set. This method is more general and can work even for unsorted lists:
- Use a hash set to keep track of seen values as you traverse the linked list.
- For each node, if its next node's value is already in the set, remove that node.
- Otherwise, add the value to the set and move forward.

**C++ Explanation:**
- Utilize the C++ STL `unordered_set` to store values.
- Iterate through the list. If the next node's value is in the `unordered_set`, remove it; otherwise, insert the value.

**Python Explanation:**
- Use Python’s `set` to hold seen values.
- Traverse the list. If the next node’s data is already seen, bypass the duplicate; otherwise, add the value and continue.

---

## Code Implementation

Below are the implementations for the two correct approaches in C++ and Python. Remember, when submitting in your environment, you only need to complete the `template_code` section, leaving the provided prefix and suffix intact.

### Approach 1: Iterative Approach

**C++ Code:**
```cpp
class Solution {
  public:
    Node* removeDuplicates(Node* head) {
        Node* curr = head;
        while (curr != nullptr && curr->next != nullptr) {
            if (curr->data == curr->next->data) {
                Node* temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
            } else {
                curr = curr->next;
            }
        }
        return head;
    }
};
```

**Python Code:**
```python
class Solution:
    def removeDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

---

### Approach 2: Using a Hash Set

**C++ Code:**
```cpp
#include
class Solution {
  public:
    Node* removeDuplicates(Node* head) {
        if (!head) return head;
        std::unordered_set seen;
        Node* curr = head;
        seen.insert(curr->data);
        while (curr->next != nullptr) {
            if (seen.find(curr->next->data) != seen.end()) {
                Node* temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
            } else {
                seen.insert(curr->next->data);
                curr = curr->next;
            }
        }
        return head;
    }
};
```

**Python Code:**
```python
class Solution:
    def removeDuplicates(self, head):
        if head is None:
            return head
        seen = set()
        curr = head
        seen.add(curr.data)
        while curr.next:
            if curr.next.data in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.data)
                curr = curr.next
        return head
```

---

## Summary

- **Iterative Approach:** Utilizes a straightforward loop and pointer manipulation to remove duplicates in $O(n)$ time and $O(1)$ space.
- **Hash Set Approach:** Leverages extra space by using a hash set to track seen values. This is more general and works even if the list were unsorted, though it requires additional memory.

Each approach has its merits, and choosing one depends on the constraints and specific requirements of the problem at hand.

Happy Coding!

</details>
