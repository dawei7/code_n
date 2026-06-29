# Count loop length in Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINKLP |
| Difficulty Rating | 1300 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [LINKLP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/LINKLP) |

---

## Problem Statement

Given a linked list, there may exist a single loop or no loop. If there are a total of **X** elements present in a loop, return **X-1** as your answer; otherwise, in case no loop exists, return **-1**.

To solve this problem, complete the function present in the submit solution tab.

---

## Input Format

- The first line will contain N, representing the elements in the linked list.

(For example, if N equals 5, the linked list looks like 1 -> 2 -> 3 -> 4 -> 5)

- The second line contains M, representing the last node's connection point. If the second line contains -1, then the last node will be connected to a null node; otherwise, it will be connected to one of the previous nodes.

(Example 1: If M equals -1 and N equals 5, the linked list looks like 1 -> 2 -> 3 -> 4 -> 5 -> NULL)

(Example 2: If M equals 2 and N equals 5, the linked list looks like 1 -> 2 -> 3 -> 4 -> 5 -> 2)

---

## Output Format

If your code is correct then the final code will print $-1$ if a loop doesn't exist, else the length of the loop.

---

## Constraints

Maximum elements in the linked list can be 10^5.

---

## Examples

**Example 1**

**Input**

```text
5
-1
```

**Output**

```text
-1
```

**Example 2**

**Input**

```text
5
2
```

**Output**

```text
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Linked List Cycle Detection and Cycle Length Calculation

In this lesson, we will solve a problem involving the detection of a cycle (loop) in a linked list and the calculation of its length. The goal is to return the number of nodes in the cycle if a cycle exists; otherwise, return $-1$. Although the problem description mentions returning $X-1$ (where $X$ is the number of nodes in the loop), the sample test cases and the reference solution indicate that we should instead return the full cycle length. We will discuss two important approaches to this problem.

## Approaches to the Problem

### Approach 1: Floyd’s Cycle Detection (Tortoise and Hare Algorithm)
This is the most common and efficient method to detect a cycle in a linked list:
- **Cycle Detection:**
  Use two pointers, **slow** and **fast**. The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time. If there is a cycle, these pointers will eventually meet.

  $$ \text{Time Complexity: } O(n) \quad \text{Space Complexity: } O(1) $$

- **Cycle Length Calculation:**
  Once a cycle is detected (i.e. the slow and fast pointers meet), keep one pointer fixed and move the other pointer until it comes back to the meeting point. Count the number of steps taken; this count gives the cycle length.

Below are the code implementations for this approach:

#### C++ Implementation (Floyd’s Cycle Detection)
```cpp
// Node is defined as
// struct Node{
//   int data=0;
//   Node* next;
//   Node(){
//         this->data = 0;
//         this->next = nullptr;
//   }
//   Node(int data){
//       this->data = data;
//       this->next = nullptr;
//   }
// };
int solve(Node* head){
    if (!head || !head->next) return -1;

    Node* slow = head;
    Node* fast = head;
    bool hasCycle = false;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            hasCycle = true;
            break;
        }
    }

    if (!hasCycle) return -1;

    int cycleLength = 1;
    fast = fast->next;
    while (fast != slow) {
        fast = fast->next;
        cycleLength++;
    }

    return cycleLength;
}
```

#### Python Implementation (Floyd’s Cycle Detection)
```python
# Node is defined as :
# class Node:
#    def __init__(self, val=0):
#        self.val = val
#        self.next = None

def solve(head):
    if not head or not head.next:
        return -1

    slow = head
    fast = head
    hasCycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            hasCycle = True
            break

    if not hasCycle:
        return -1

    cycleLength = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        cycleLength += 1

    return cycleLength
```

### Approach 2: Using a Visited Set (Hashing)
In this approach, we use extra memory to store the nodes we have already seen:
- **Cycle Detection:**
  Traverse the linked list and store each node’s address in a hash set (or Python set). If a node is already in the set, a cycle exists.

- **Cycle Length Calculation:**
  After detecting the cycle, starting from the first repeated node, traverse the cycle until you encounter the same node again. Count the number of nodes during this traversal.

  $$ \text{Time Complexity: } O(n) \quad \text{Space Complexity: } O(n) $$

Below are the code implementations for this approach:

#### C++ Implementation (Visited Set)
```cpp
// Node is defined as
// struct Node{
//   int data=0;
//   Node* next;
//   Node(){
//         this->data = 0;
//         this->next = nullptr;
//   }
//   Node(int data){
//       this->data = data;
//       this->next = nullptr;
//   }
// };
#include
int solve(Node* head){
    if (!head) return -1;

    std::unordered_set visited;
    Node* curr = head;

    while (curr != nullptr) {
        if (visited.find(curr) != visited.end()) {
            int cycleLength = 1;
            Node* runner = curr->next;
            while (runner != curr) {
                cycleLength++;
                runner = runner->next;
            }
            return cycleLength;
        }
        visited.insert(curr);
        curr = curr->next;
    }

    return -1;
}
```

#### Python Implementation (Visited Set)
```python
# Node is defined as :
# class Node:
#    def __init__(self, val=0):
#        self.val = val
#        self.next = None

def solve(head):
    visited = set()
    curr = head

    while curr:
        if curr in visited:
            cycleLength = 1
            runner = curr.next
            while runner != curr:
                cycleLength += 1
                runner = runner.next
            return cycleLength
        visited.add(curr)
        curr = curr.next

    return -1
```

## Conclusion
For beginners, the Floyd’s Cycle Detection algorithm (Approach 1) is highly recommended due to its efficiency in terms of space and time. However, understanding the visited set approach (Approach 2) is also valuable as it demonstrates an alternative method using extra space, which might be easier to grasp initially.

Both approaches correctly detect cycles and compute the cycle length. Remember that while the problem description mentioned returning $X-1$, the sample tests indicate that the full cycle length should be returned when a cycle exists.

</details>
