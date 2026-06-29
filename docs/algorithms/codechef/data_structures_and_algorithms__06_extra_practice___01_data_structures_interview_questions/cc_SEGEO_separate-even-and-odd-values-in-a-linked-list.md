# Separate Even and Odd values in a linked list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEGEO |
| Difficulty Rating | 1300 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [SEGEO](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/SEGEO) |

---

## Problem Statement

Chef has a linked list. He wants to modify the linked list such that all the even values appear before the odd values without changing their relative order. But he's too busy now and asked you to do the job for him.

Can you do it?

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the linked list.
- You don't need to read or print anything. Just complete the function rearrange() which takes the head of the linked list as input.

---

## Output Format

Return the head of the linked list after rearrangement.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $\sum N \leq 5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 3
4 
1 7 6 8
4
2 1 4 3
```

**Output**

```text
2 1 3
6 8 1 7
2 4 1 3
```

**Explanation**

**Test Case 1:** It is easy to see that the linked list after rearrangement will be $[2, 1, 3]$

**Test Case 2:** It is easy to see that the linked list after rearrangement will be $[6, 8, 1, 7]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
2 1 3
```



#### Test case 2

**Input for this case**

```text
4
1 7 6 8
```

**Output for this case**

```text
6 8 1 7
```



#### Test case 3

**Input for this case**

```text
4
2 1 4 3
```

**Output for this case**

```text
2 4 1 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we address the problem of rearranging a linked list so that all nodes containing even values appear before those with odd values while preserving their relative order. In this editorial, we discuss two approaches to solve the problem and provide corresponding implementations in both **C++** and **Python**.

---

## Approach 1: Two-List Partitioning

### Explanation

The idea behind this approach is to traverse the original linked list once and create two separate lists:
- One for nodes with even values.
- One for nodes with odd values.

After the traversal, we connect the even list to the odd list. This way, the relative order within the even and odd groups is maintained.

**Methodology:**

1. **Initialization:**
   Set up four pointers:
   - `evenHead` and `evenTail` for the even-valued nodes.
   - `oddHead` and `oddTail` for the odd-valued nodes.

2. **Traversal:**
   Iterate through the linked list. For each node:
   - If the node’s value is even (i.e., the remainder when divided by 2 is zero), append it to the even list.
   - Otherwise, append it to the odd list.

3. **Combining Lists:**
   After the traversal:
   - If the even list is not empty, link the last node of the even list (`evenTail`) to the head of the odd list (`oddHead`).
   - Ensure that the last node in what becomes the reordered list has its `next` pointer set to `nullptr` (or `None` in Python).

4. **Edge Cases:**
   If there are no even nodes, simply return the odd list. If there are no odd nodes, return the even list.

**Complexity:**

- **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the linked list.
- **Space Complexity:** $O(1)$ auxiliary space.

### Code Implementation

#### C++ Code:
```cpp
class Solution{
	public:
	Node* rearrange(Node* head)
	{
		if (!head || !head->next) return head;
		Node* evenHead = nullptr;
		Node* evenTail = nullptr;
		Node* oddHead = nullptr;
		Node* oddTail = nullptr;
		Node* current = head;
		while (current) {
			if (current->val % 2 == 0) {
				if (!evenHead) {
					evenHead = evenTail = current;
				} else {
					evenTail->next = current;
					evenTail = current;
				}
			} else {
				if (!oddHead) {
					oddHead = oddTail = current;
				} else {
					oddTail->next = current;
					oddTail = current;
				}
			}
			current = current->next;
		}
		if (evenHead) {
			evenTail->next = oddHead;
			if (oddTail) oddTail->next = nullptr;
			return evenHead;
		} else {
			if (oddTail) oddTail->next = nullptr;
			return oddHead;
		}
	}
};
```

#### Python Code:
```python
class Solution:
    def rearrange(self, head):
        if not head or not head.next:
            return head
        evenHead = evenTail = None
        oddHead = oddTail = None
        current = head
        while current:
            if current.val % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = current
                else:
                    evenTail.next = current
                    evenTail = current
            else:
                if not oddHead:
                    oddHead = oddTail = current
                else:
                    oddTail.next = current
                    oddTail = current
            current = current.next
        if evenHead:
            evenTail.next = oddHead
            if oddTail:
                oddTail.next = None
            return evenHead
        else:
            if oddTail:
                oddTail.next = None
            return oddHead
```

---

## Approach 2: Array-Based Grouping

### Explanation

In this approach, we create two arrays (or dynamic lists) to store pointers to even and odd nodes separately while traversing the linked list. After this, we reconstruct the linked list by linking all even nodes first, followed by all odd nodes.

**Methodology:**

1. **Traversal and Collection:**
   Traverse the linked list and for every node:
   - Detach the node from the original list (by setting its `next` pointer to `nullptr` or `None`).
   - Append the node to the corresponding array based on whether its value is even or odd.

2. **Reconstruction:**
   Create a new linked list by iterating over the even array first (maintaining the order) and then appending the odd array.

3. **Return the New Head:**
   The head of the new linked list is the first node in the even array if it is non-empty; otherwise, it is the first node in the odd array.

**Complexity:**

- **Time Complexity:** $O(n)$, where $n$ is the number of nodes.
- **Space Complexity:** $O(n)$ additional space is used to store the nodes.

### Code Implementation

#### C++ Code:
```cpp
class Solution{
	public:
	Node* rearrange(Node* head)
	{
		if (!head || !head->next) return head;
		vector evenNodes, oddNodes;
		Node* current = head;
		while (current) {
			Node* nxt = current->next;
			current->next = nullptr;
			if (current->val % 2 == 0) {
				evenNodes.push_back(current);
			} else {
				oddNodes.push_back(current);
			}
			current = nxt;
		}
		Node* newHead = nullptr;
		Node* tail = nullptr;
		auto appendNodes = [&](vector &nodes) {
			for (auto node : nodes) {
				if (!newHead) {
					newHead = tail = node;
				} else {
					tail->next = node;
					tail = node;
				}
			}
		};
		appendNodes(evenNodes);
		appendNodes(oddNodes);
		return newHead;
	}
};
```

#### Python Code:
```python
class Solution:
    def rearrange(self, head):
        if not head or not head.next:
            return head
        evenNodes = []
        oddNodes = []
        current = head
        while current:
            nxt = current.next
            current.next = None
            if current.val % 2 == 0:
                evenNodes.append(current)
            else:
                oddNodes.append(current)
            current = nxt
        newHead = None
        tail = None
        def append_nodes(nodes, newHead, tail):
            for node in nodes:
                if newHead is None:
                    newHead = node
                    tail = node
                else:
                    tail.next = node
                    tail = node
            return newHead, tail
        newHead, tail = append_nodes(evenNodes, newHead, tail)
        newHead, tail = append_nodes(oddNodes, newHead, tail)
        return newHead
```

---

## Conclusion

Both approaches solve the problem in $O(n)$ time:
- **Approach 1 (Two-List Partitioning):**
  This is the more space-efficient method, requiring only $O(1)$ extra space. It is ideal when memory usage is a concern.

- **Approach 2 (Array-Based Grouping):**
  This approach is simple and intuitive but uses additional $O(n)$ space due to the use of dynamic arrays (or lists).

For most practical scenarios, **Approach 1** is preferred due to its optimal space usage while maintaining linear time complexity.

</details>
