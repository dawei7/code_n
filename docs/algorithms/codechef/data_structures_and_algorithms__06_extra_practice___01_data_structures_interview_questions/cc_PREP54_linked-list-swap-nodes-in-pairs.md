# Linked List - Swap nodes in pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP54 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [PREP54](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/PREP54) |

---

## Problem Statement

You are given a linked list $A$ of size $N$.

Considering the first node as the head of the linked list, you need to swap the $i^{th}$ node with the $(i+1)^{th}$ node in the linked list, such that:
- The index $i$ is **odd**;
- $(i+1) \le N$.

Return the new head after making the swaps.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node pairWiseSwap(Node head){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* pairWiseSwap(Node* head){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def pairWiseSwap(headA):
```

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- First line contains an integer $N$, length of the linked list $A$.
- Second line contains $A_1, A_2, \ldots A_N$, the value of the linked list nodes starting from the head for the linked list.

---

## Output Format

The function you complete should return the required answer.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
8 15 1
6
5 19 19 3 5 6
2
2 8
```

**Output**

```text
15 8 1 
19 5 3 19 6 5 
8 2
```

**Explanation**

**Test case $1$:** We swap the first and second nodes, having values $8$ and $15$ respectively. The third node would not be swapped with any node.

**Test case $2$:** We swap the following pair of nodes: $(1, 2), (3, 4), (5, 6)$.

**Test case $3$:** We swap the first and second node.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
8 15 1
```

**Output for this case**

```text
15 8 1
```



#### Test case 2

**Input for this case**

```text
6
5 19 19 3 5 6
```

**Output for this case**

```text
19 5 3 19 6 5
```



#### Test case 3

**Input for this case**

```text
2
2 8
```

**Output for this case**

```text
8 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to perform a pairwise swap of nodes in a linked list. The goal is to swap every adjacent pair of nodes. For example, given a linked list like:

$$ A_1 \rightarrow A_2 \rightarrow A_3 \rightarrow A_4 \rightarrow \ldots $$

After swapping, it should become:

$$ A_2 \rightarrow A_1 \rightarrow A_4 \rightarrow A_3 \rightarrow \ldots $$

In this updated lesson, we will focus on a single, effective approach to solve this problem.

---

### Approach 1: Iterative Swapping Using a Dummy Node

**Concept:**

In this approach, we use a dummy node to simplify the edge cases (especially when swapping the first pair). The dummy node points to the head of the list. We then iterate through the list using two pointers, swapping every pair of nodes as we go.

**Steps:**

1. **Check Base Cases:**
   If the list is empty or contains only one node, return the head as no swap is required.
2. **Initialization:**
   - Create a dummy node and set its next pointer to the head of the linked list.
   - Use a pointer called `prev` to keep track of the node preceding the current pair.
   - Use a pointer `curr` to refer to the first node of the current pair.
3. **Swapping Mechanism:**
   - For the current two nodes (i.e. `curr` and `curr->next`):
     - Store the pointer to the node after the pair as `nextPair`.
     - Point the second node's next to the first node.
     - Connect the `prev` node to the second node.
     - Point the first node's next to `nextPair`.
   - Move both `prev` and `curr` forward in the list to process subsequent pairs.
4. **Return the New Head:**
   After processing all nodes, the new head of the list is `dummy->next`.

**C++ Code:**

```cpp
class Solution
{
    public:
    Node* pairWiseSwap(struct Node* head)
    {
        // If the list is empty or has only one node, return as is.
        if (head == NULL || head->next == NULL)
            return head;

        Node* dummy = new Node(0);
        dummy->next = head;
        Node* prev = dummy;
        Node* curr = head;

        while (curr && curr->next) {
            Node* nextPair = curr->next->next;
            Node* second = curr->next;

            // Swapping the nodes.
            second->next = curr;
            curr->next = nextPair;
            prev->next = second;

            // Reposition the pointers for the next pair.
            prev = curr;
            curr = nextPair;
        }
        head = dummy->next;
        delete dummy;
        return head;
    }
};
```

**Python Code:**

```python
class Solution:
    def pairWiseSwap(self, head):
        # Base case: if there are less than two nodes, no swap is needed.
        if head is None or head.next is None:
            return head

        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next

            # Swapping nodes.
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # Moving prev and curr pointers forward.
            prev = curr
            curr = nextPair

        return dummy.next
```

---

### Final Remarks

The iterative approach provided above efficiently swaps nodes in pairs and handles edge cases using a dummy node. Its time complexity is $ O(N) $, where $ N $ is the number of nodes in the linked list.

In an interview setting, explaining the rationale behind using a dummy node to simplify pointer management and discussing trade-offs between iterative and recursive approaches can strengthen your solution presentation.

Happy Coding!

</details>
