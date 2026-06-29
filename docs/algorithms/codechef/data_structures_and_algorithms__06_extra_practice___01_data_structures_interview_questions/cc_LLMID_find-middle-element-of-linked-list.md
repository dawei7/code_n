# Find Middle Element of Linked List

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LLMID |
| Difficulty Rating | 1200 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [LLMID](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/LLMID) |

---

## Problem Statement

You are given the head of a singly linked list $A$ of length $N$. The values in the list are $A_1, A_2, \ldots, A_N$ respectively. You need to find the value of the middle element of the linked list.

The middle element of a linked list of length $N$ is the $(\lfloor \frac{N}{2} \rfloor + 1)$-th element from the head of the list.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, the function you complete should return the value of the middle element of the list.

**Note:**
You need to complete the function `getMiddleElement` to solve the problem.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
1 2 3 4 5
6
1 2 3 4 5 6
4
10 1 6 12
```

**Output**

```text
3
4
6
```

**Explanation**

**Example case 1:** The value of the middle element is $A_3=3$.

**Example case 2:** The value of the middle element is $A_4=4$.

**Example case 3:** The value of the middle element is $A_3=6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
6
1 2 3 4 5 6
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4
10 1 6 12
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to find the middle element of a singly linked list. The middle element is defined as the $(\lfloor \frac{N}{2} \rfloor + 1)$-th node when counting from the head (using one-indexing). For example, in a list with 5 nodes, the 3rd node is the middle element.

We will cover three different approaches to solve this problem:

---

### **Approach 1: Two-Pointer (Slow-Fast) Technique**

**Idea:**
We use two pointers, `slow` and `fast`. The `slow` pointer moves one node at a time while the `fast` pointer moves two nodes at a time. When the `fast` pointer reaches the end (or goes past it), the `slow` pointer will be at the middle of the linked list.

**Why It Works:**
Since the `fast` pointer moves twice as fast as the `slow` pointer, by the time the `fast` pointer has traversed the entire list, the `slow` pointer will have reached half the list’s length.

**Time Complexity:**
$O(N)$, where $N$ is the number of nodes in the list.

**Space Complexity:**
$O(1)$, since we use only two extra pointers.

**C++ Code:**

```cpp
int getMiddleElement(Node* head){
    if (head == NULL) return -1;  // Check for empty list

    Node* slow = head;
    Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow->val;
}
```

**Python Code:**

```python
def getMiddleElement(head):
    if head is None:
        return -1  # Check for an empty list

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data
```

---

### **Approach 2: Two-Pass Counting Method**

**Idea:**
In this approach, we first traverse the linked list to count the total number of nodes. After obtaining the count, we calculate the middle index as $midIndex = \lfloor \frac{N}{2} \rfloor$ (using zero-indexing). Then, we traverse the list again until we reach the middle node.

**Why It Works:**
By counting nodes first, we accurately determine the middle index, which allows a straightforward second pass to locate the middle element.

**Time Complexity:**
$O(N)$, but with two passes through the list.

**Space Complexity:**
$O(1)$, as only a few extra variables are used.

**C++ Code:**

```cpp
int getMiddleElement(Node* head){
    if (head == NULL) return -1;

    int count = 0;
    Node* current = head;
    while (current != NULL) {
        count++;
        current = current->next;
    }

    int midIndex = count / 2;  // Zero-indexed position for the middle element
    current = head;
    for (int i = 0; i < midIndex; i++) {
        current = current->next;
    }

    return current->val;
}
```

**Python Code:**

```python
def getMiddleElement(head):
    if head is None:
        return -1

    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    midIndex = count // 2  # Zero-indexed middle position
    current = head
    for _ in range(midIndex):
        current = current.next

    return current.data
```

---

### **Approach 3: Using Auxiliary Array**

**Idea:**
In this method, we traverse the linked list, storing each node’s value in an array. Once the traversal is complete, the middle element can be accessed directly using the index $midIndex = \lfloor \frac{N}{2} \rfloor$.

**Why It Works:**
Storing node values in an array makes it simple to access any index, including the middle. However, this approach uses extra space for the array.

**Time Complexity:**
$O(N)$ to traverse the list and build the array.

**Space Complexity:**
$O(N)$ due to the additional array used for storing node values.

**C++ Code:**

```cpp
int getMiddleElement(Node* head){
    if (head == NULL) return -1;

    vector values;
    Node* current = head;
    while (current != NULL) {
        values.push_back(current->val);
        current = current->next;
    }

    return values[values.size() / 2];
}
```

**Python Code:**

```python
def getMiddleElement(head):
    if head is None:
        return -1

    values = []
    while head:
        values.append(head.data)
        head = head.next

    return values[len(values) // 2]
```

---

### **Summary**

- **Approach 1 (Two-Pointer Technique):**
  Efficient with one pass and constant extra space. Ideal for time-critical applications.

- **Approach 2 (Two-Pass Counting):**
  Simple and easy to understand, working in two passes with constant space. Good for beginners.

- **Approach 3 (Using Auxiliary Array):**
  Utilizes extra space for simplicity. Although not as space efficient, it is straightforward to implement.

Each approach has its merits, and understanding multiple methods is essential for tackling various linked list problems in interviews. The two-pointer technique is the most popular due to its efficiency, but knowing alternative methods is beneficial for a deeper understanding of algorithm design.

Happy coding and best of luck with your DSA interview preparation!

</details>
