# Find Next Smaller value in Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NSELL |
| Difficulty Rating | 1600 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [NSELL](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/NSELL) |

---

## Problem Statement

Chef gave you the $head$ of a linked list and challenged you to find the next smaller value for every node in the linked list. Can you solve the challenge?

**Note:** If for some value, there is no next smaller value then assume the next smaller value for this number to be $-1$.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the array.
- You don't need to read or print anything. Just complete the function nextSmallerValue() which takes the head of the linked list as input.

---

## Output Format

Return the head of the linked list which contains next smaller value for every node.

---

## Constraints

- $ 1\leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $\sum N \leq 5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
9 19
6
19 18 16 12 8 8
6
14 9 14 5 2 1
```

**Output**

```text
-1 -1 
18 16 12 8 -1 -1 
9 5 5 2 1 -1
```

**Explanation**

**Test Case 1:** There is no next smaller value for both the elements.

**Test Case 3:** Next smaller values can easily be verified.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
9 19
```

**Output for this case**

```text
-1 -1
```



#### Test case 2

**Input for this case**

```text
6
19 18 16 12 8 8
```

**Output for this case**

```text
18 16 12 8 -1 -1
```



#### Test case 3

**Input for this case**

```text
6
14 9 14 5 2 1
```

**Output for this case**

```text
9 5 5 2 1 -1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Finding Next Smaller Value in a Linked List

In this problem, we are given the head of a linked list and asked to replace each node’s value with the next node’s value that is strictly smaller than the current node’s value. If no such node exists, we assign $-1$ to that position.

We explore two efficient approaches to solve this problem.

---

## Approach 1: Monotonic Stack Approach (Optimal)

### Explanation

This efficient approach uses a monotonic stack. The idea is to traverse the list only once while maintaining a stack of nodes that haven't yet found their next smaller value.

The algorithm steps are:
1. **Initialize an empty stack.**
2. **Traverse the linked list from left to right.**
3. **For each current node,** while the stack is not empty and the top node’s value is greater than the current node's value, update the top node’s value with the current node's value and pop it from the stack.
4. **Push the current node onto the stack.**
5. **After the traversal,** assign $-1$ to the value of any nodes left in the stack (since no smaller element was found).

This procedure has a time complexity of
$$ O(n) $$
because every node is pushed and popped at most once.

### C++ Code
```cpp
class Solution{
    public:
    Node* nextSmallerValue(Node* head) {
        if (!head) return head;
        std::stack st;
        Node* curr = head;
        while (curr) {
            while (!st.empty() && st.top()->val > curr->val) {
                st.top()->val = curr->val;
                st.pop();
            }
            st.push(curr);
            curr = curr->next;
        }
        while (!st.empty()) {
            st.top()->val = -1;
            st.pop();
        }
        return head;
    }
};
```

### Python Code
```python
class Solution:
    def next_smaller_value(self, head):
        if not head:
            return head
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val > curr.val:
                stack[-1].val = curr.val
                stack.pop()
            stack.append(curr)
            curr = curr.next
        while stack:
            stack[-1].val = -1
            stack.pop()
        return head
```

---

## Approach 2: Array Conversion with Monotonic Stack

### Explanation

In this method, we first convert the linked list into an array of nodes. Then, we use a monotonic stack on this array to determine the next smaller value for each node. Finally, we update the original linked list based on the results from the array.

The detailed steps are:
1. **Traverse the linked list** and store pointers (or references) to the nodes in an array.
2. **Use a stack (storing indices)** to compute the next smaller values by comparing the elements.
3. **Update the linked list** based on the computed results.

Though this approach utilizes additional space
$$ O(n) $$
it can be easier to implement and debug, particularly if you are more comfortable with array manipulations.

### C++ Code
```cpp
class Solution{
    public:
    Node* nextSmallerValue(Node* head) {
        if (!head) return head;
        std::vector nodes;
        Node* curr = head;
        while (curr) {
            nodes.push_back(curr);
            curr = curr->next;
        }
        std::stack st;
        std::vector result(nodes.size(), -1);
        for (int i = 0; i < nodes.size(); i++) {
            while (!st.empty() && nodes[st.top()]->val > nodes[i]->val) {
                result[st.top()] = nodes[i]->val;
                st.pop();
            }
            st.push(i);
        }
        for (int i = 0; i < nodes.size(); i++) {
            nodes[i]->val = result[i];
        }
        return head;
    }
};
```

### Python Code
```python
class Solution:
    def next_smaller_value(self, head):
        if not head:
            return head
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        stack = []
        result = [-1] * len(nodes)
        for i in range(len(nodes)):
            while stack and nodes[stack[-1]].val > nodes[i].val:
                result[stack.pop()] = nodes[i].val
            stack.append(i)

        for i in range(len(nodes)):
            nodes[i].val = result[i]
        return head
```

---

## Conclusion

We explored two efficient approaches to tackle the challenge:

1. **Monotonic Stack Approach (Approach 1):** This method processes the linked list in a single pass with a time complexity of $ O(n) $, utilizing minimal extra space.
2. **Array Conversion with Monotonic Stack (Approach 2):** Although it requires additional space, this approach can be simpler to implement if you feel more comfortable working with arrays.

For optimal performance, the Monotonic Stack Approach is highly recommended.

</details>
