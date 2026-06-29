# Duplicate Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DR |
| Difficulty Rating | 1200 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [DR](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/DR) |

---

## Problem Statement

The Chef is celebrating his birthday! His best friend gifted him a sorted singly linked list. But there is a catch - Chef hates duplicates, so he wants to remove every element that occurs more than once (he wants to remove all of the occurrences). However, he is very busy with his birthday party, he asks you to help him.

Complete the function "duplicateRemoval" in the code snippet that takes a single argument: a head of the sorted singly linked list. The function should return the head of the singly linked list that is the modification of the original one, but the duplicates are completely erased. The function will be called multiple times.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains an integer $N$ - representing the length of the linked list
- The second line of each test case contains $N$ space-separated integers - representing the elements of the list

Note: You need to complete the functions in the submit solution tab.

---

## Output Format

For each testcase, output will be in a single line containing a list passed by the function duplicateRemoval.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$
- $1 \leq A_i \leq 10^9$ - elements of the linked list

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 3 4
7
1 1 5 6 6 6 10
```

**Output**

```text
1 2 4
5 10
```

**Explanation**

In the first test case the only duplicate value is 3, while in the second test case the only duplicate values are 1 and 6.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 3 4
```

**Output for this case**

```text
1 2 4
```



#### Test case 2

**Input for this case**

```text
7
1 1 5 6 6 6 10
```

**Output for this case**

```text
5 10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this editorial, we discuss an effective approach to solve the problem of removing all nodes from a sorted linked list that are duplicates (i.e. any element that appears more than once is completely removed). Our goal is to produce a final list that contains only unique elements from the original list.

Below is the approach that we will cover:

---

### Approach 1: Iterative Dummy Node Method (Two-Pointer Technique)

**Intuition:**
Since the linked list is sorted, duplicates (if any) will appear consecutively. We can use a dummy node to handle edge cases (for example, when the first few nodes are duplicates) and maintain two pointers:
- **`prev` pointer:** Points to the last node known to be unique.
- **`curr` pointer:** Used to traverse the list.

**Methodology:**
1. Initialize a dummy node whose `next` pointer points to the head of the list.
2. Start iterating using the `curr` pointer.
3. If the current node’s value is the same as its next node, then mark a duplicate and skip all nodes with that duplicate value.
4. Connect the `prev` pointer to the first node that is different (i.e. the next unique node).
5. Otherwise, simply move both pointers forward.
6. Continue this process until all nodes have been processed.

This approach works in $O(n)$ time with $O(1)$ extra space (apart from the dummy node). It is optimal for in-place manipulation.

---

Below are the code implementations for the above approach in **C++** and **Python**.

#### Approach 1: Iterative Dummy Node Method

**C++ Implementation:**

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

Node* duplicateRemoval(Node* head) {
    Node dummy(0);
    dummy.next = head;
    Node* prev = &dummy;
    Node* curr = head;
    while (curr != NULL) {
        // Check if current node has duplicates
        bool duplicate = false;
        while (curr->next != NULL && curr->data == curr->next->data) {
            duplicate = true;
            curr = curr->next;
        }
        if (duplicate) {
            // Skip all duplicates
            prev->next = curr->next;
        } else {
            // No duplicate; move the prev pointer
            prev = prev->next;
        }
        curr = curr->next;
    }
    return dummy.next;
}
```

**Python Implementation:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeDuplicates(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr is not None:
        if curr.next is not None and curr.data == curr.next.data:
            duplicate_val = curr.data
            # Skip all nodes with the duplicate value
            while curr is not None and curr.data == duplicate_val:
                curr = curr.next
            prev.next = curr
        else:
            prev = curr
            curr = curr.next
    return dummy.next
```

---

### Summary
- **Approach 1** uses a dummy node and two pointers to remove consecutive duplicates in a single pass with constant extra space. This is the optimal solution for a sorted linked list where duplicates appear consecutively.

Happy coding and best of luck with your DSA interviews!

</details>
