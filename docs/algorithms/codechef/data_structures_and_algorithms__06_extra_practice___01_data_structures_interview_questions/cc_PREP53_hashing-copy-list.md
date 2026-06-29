# Hashing - Copy List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP53 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Hashing |
| Official Link | [PREP53](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_13/problems/PREP53) |

---

## Problem Statement

You are given head of the **non-empty** linked list of length $N$ where the value of the $i^{th}$ node will be $A_i$. Each node contains an additional random pointer, which could point to any node in the list, or NULL.

Construct a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly $N$ brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

Your task is to return the head of the copied linked list.

Note:
- After you will return the node of the copied linked list the system will automatically check if the copied linked list is correct or not. It will output $1$ if the output linked list is perfectly copied otherwise will output $0$.
- The random pointer points to NULL if it does not point to any node.

### Input:

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line contains one integer $N$ — the length of the linked list.
- The next line contains $N$ space-separated integers $A_1, A_2, \ldots A_N$ — the value of the linked list nodes starting from the head for the linked list.
- The next line contains one integer $M$ — the number of random pointers.
- The next $M$ lines contains two space separated integers $X$, $Y$ — the random pointer of node $X$ point to node $Y$.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node copyRandomList(Node head){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* copyRandomList(Node* head){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def Node copyRandomList(self, head):
```
### Output:
The function you complete should return the required answer.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N, A_i \leq 10^5$
- $1 \leq M \leq N$
- $1 \leq X, Y \leq N$
- $X \neq Y$

### Sample Input:
```
2
5
1 6 4 8 15
2
1 3
4 5
3
5 10 15
2
1 3
2 3
```

### Sample Output:
```
1
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we tackle the problem of deep copying a linked list where each node contains a next pointer and an additional random pointer. The goal is to create a completely independent copy of the list such that every node in the new list has the same value, next, and random pointers as the original, but none of the new nodes point back to nodes of the original list.

We'll discuss **two primary approaches** to solve this problem.

---

### Approaches to the Problem

#### **Approach 1: Interleaving (In-Place) Method**

In this approach, we reduce extra space usage by interleaving the copied nodes along with the original nodes. The algorithm comprises three main steps:

1. **Interleaving Copy Nodes:**

   Traverse the original list. For each node, create a new node with the same data and insert it immediately after the original node. After this step, the list will alternate between original and copied nodes.

   For example, if the original list is:
   $$\text{A}_1 \rightarrow \text{A}_2 \rightarrow \text{A}_3$$
   it becomes:
   $$\text{A}_1 \rightarrow \text{A}_1' \rightarrow \text{A}_2 \rightarrow \text{A}_2' \rightarrow \text{A}_3 \rightarrow \text{A}_3'$$

2. **Assigning Random Pointers:**

   Traverse the modified list. For each original node, if its random pointer is not $NULL$, then set the random pointer of its copy (which is the next node) to the node immediately after the original node’s random pointer. This is because each copied node follows its original, making the assignment straightforward.

3. **Separating the Lists:**

   Finally, restore the original list by skipping over the copied nodes and extract the copied nodes to form the new list. This step requires iterating through the modified list and resetting the next pointers accordingly.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(1)$ (apart from the space for the new nodes)

This approach is optimal in terms of space since it makes use of the original list structure during the copy process.

---

#### **Approach 2: Hash Map (Dictionary) Method**

This is a more straightforward method in which we use a hash map (or dictionary) to maintain a mapping from each original node to its corresponding copied node. The algorithm follows these steps:

1. **Create Copies and Mapping:**

   Traverse the original list, create a copy for each node, and store the mapping from the original node to the new node in a hash map.

2. **Assign Next and Random Pointers:**

   Traverse the list again, and for each node, set:
   - The next pointer of its copy to the mapping of the original node’s next.
   - The random pointer of its copy to the mapping of the original node’s random.

3. **Return the Copied Head:**

   Return the new head from the mapping corresponding to the original head.

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$ (due to the extra hash map)

Although this approach uses extra space, it is conceptually simpler and easier to implement, especially for beginners.

---

### Code Implementations

Below, we provide both the C++ and Python implementations for each approach. Note that you should only complete the `template_code` section in the provided templates.

---

#### **Approach 1: Interleaving (In-Place) Method**

**C++ Code:**
```cpp
/* Linked List Node
struct Node {
    int data;
    struct Node *next;
    struct Node *random;
    Node(int x) {
        data = x;
        next = NULL;
        random = NULL;
    }
}; */

class Solution {
  public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr)
            return nullptr;

        // Step 1: Interleave copy nodes with original nodes.
        Node* curr = head;
        while (curr) {
            Node* copy = new Node(curr->data);
            copy->next = curr->next;
            curr->next = copy;
            curr = copy->next;
        }

        // Step 2: Copy random pointers.
        curr = head;
        while (curr) {
            if (curr->random)
                curr->next->random = curr->random->next;
            curr = curr->next->next;
        }

        // Step 3: Separate the copy from the original.
        Node* newHead = head->next;
        curr = head;
        while (curr) {
            Node* copy = curr->next;
            curr->next = copy->next;
            if (copy->next)
                copy->next = copy->next->next;
            curr = curr->next;
        }
        return newHead;
    }
};
```

**Python Code:**
```python
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        # Step 1: Create cloned nodes interleaved with original nodes.
        curr = head
        while curr:
            new_node = Node(curr.data)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers for the cloned nodes.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the cloned list from the original list.
        new_head = head.next
        curr = head
        while curr:
            clone = curr.next
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            curr = curr.next
        return new_head
```

---

#### **Approach 2: Hash Map (Dictionary) Method**

**C++ Code:**
```cpp
/* Linked List Node
struct Node {
    int data;
    struct Node *next;
    struct Node *random;
    Node(int x) {
        data = x;
        next = NULL;
        random = NULL;
    }
}; */

#include
class Solution {
  public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr)
            return nullptr;

        // Creating a map to store original node -> copied node mapping.
        std::unordered_map nodeMap;
        Node* curr = head;

        // Step 1: Create a copy for each node and store in the map.
        while (curr) {
            nodeMap[curr] = new Node(curr->data);
            curr = curr->next;
        }

        // Step 2: Assign next and random pointers using the map.
        curr = head;
        while (curr) {
            nodeMap[curr]->next = curr->next ? nodeMap[curr->next] : nullptr;
            nodeMap[curr]->random = curr->random ? nodeMap[curr->random] : nullptr;
            curr = curr->next;
        }
        return nodeMap[head];
    }
};
```

**Python Code:**
```python
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        # Create a dictionary to map original nodes to their copies.
        old_to_new = {}
        curr = head

        # Step 1: Copy the nodes.
        while curr:
            old_to_new[curr] = Node(curr.data)
            curr = curr.next

        # Step 2: Set the next and random pointers.
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next, None)
            old_to_new[curr].random = old_to_new.get(curr.random, None)
            curr = curr.next

        return old_to_new[head]
```

---

### Conclusion

Both approaches solve the problem in $O(N)$ time, but they differ in their space complexity. The interleaving method uses $O(1)$ extra space (excluding the space for the new nodes) and is optimal for space, while the hash map approach, though simpler to understand and implement, requires $O(N)$ extra space. Depending on the constraints and the importance of space optimization, you may choose either method.

Happy coding and best of luck with your DSA interviews!

</details>
