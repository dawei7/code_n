# Sort a linked list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SRTLL |
| Difficulty Rating | 1800 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [SRTLL](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/SRTLL) |

---

## Problem Statement

You are given a linked list.
Your task is to sort the linked list in ascending order.

**Note**:
- Input is already handled
- You only need to complete the function `rearrange`

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line of every test case contains an integer $N$ - the length of array.
- The second line of every test case contains $N$ integers - $ A_1,A_2,..,A_N$ denoting the integers in the linked list.
- You don't need to read or print anything. Just complete the function sort() which takes the head of the linked list as input.

---

## Output Format

Return the head of the sorted linked list.

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
1
1
3
5 2 7
4
4 1 2 2
```

**Output**

```text
1
2 5 7
1 2 2 4
```

**Explanation**

**Test Case 1:** The is only a single value in the entire linked list

**Test Case 3:** It is easy to see that the linked list after sorting is $[1, 2, 2, 4]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
5 2 7
```

**Output for this case**

```text
2 5 7
```



#### Test case 3

**Input for this case**

```text
4
4 1 2 2
```

**Output for this case**

```text
1 2 2 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Editorial: Sorting a Linked List

In this lesson, we explore the problem of sorting a singly linked list. We will discuss two effective approaches so that you can understand various techniques and choose the one best suited for a given scenario.

---

### Approach 1: Convert to Array and Sort

In this method, we traverse the linked list to copy its elements into an array. We then use an efficient built-in sort function to sort the array. Finally, we traverse the linked list again to update the node values with the sorted elements.

#### **Methodology:**
1. **Traverse and Store:** Start at the head of the linked list and collect each node's value into a linear array.
2. **Sort the Array:** Use a built-in sorting algorithm (typically $O(N \log N)$ complexity) to sort the array.
3. **Reassign Values:** Iterate through the linked list again, updating each node’s value with the sorted values from the array.

#### **Complexity:**
- **Time Complexity:** $O(N \log N)$ (due to sorting)
- **Space Complexity:** $O(N)$ (extra space for the array)

#### **When to Use:**
This approach is very intuitive and easy to implement for beginners. However, it requires extra space proportional to the size of the list.

---

### Approach 2: Merge Sort on the Linked List

Merge sort is ideally suited for sorting linked lists because it does not require random access and works in a divide and conquer manner. The main idea here is to split the list into two halves, recursively sort each half, and finally merge the sorted halves.

#### **Key Functions:**
- **getMid:** Finds the middle node to split the list.
- **merge:** Merges two sorted lists into one sorted list.

#### **Methodology:**
1. **Base Case:** If the list is empty or has a single node, it is already sorted.
2. **Divide:** Use the `getMid` function to split the list into two halves.
3. **Conquer:** Recursively sort each half using merge sort.
4. **Combine:** Merge the two sorted halves with the `merge` function.

#### **Complexity:**
- **Time Complexity:** $O(N \log N)$.
- **Space Complexity:** $O(\log N)$ (used by the recursion stack).

#### **When to Use:**
Merge sort is efficient and works in-place (ignoring recursion stack space) without needing extra memory for an array. It is the most common method for sorting linked lists.

---

### Code Implementations

Below, you can find the implementations in both C++ and Python for each approach. **Remember:** You should only complete the `template_code` section in your submissions as per the provided template.

---

#### **Approach 1: Convert to Array and Sort**

**C++ Implementation:**
```cpp
/*struct Node {
    int val;
    Node *next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node *n) : val(x), next(n) {}
  };
  */
class Solution{
    public:
    Node* rearrange(Node* head)
    {
        if(!head) return head;
        vector vals;
        Node* curr = head;
        while(curr){
            vals.push_back(curr->val);
            curr = curr->next;
        }
        sort(vals.begin(), vals.end());
        curr = head;
        for(auto v : vals){
            curr->val = v;
            curr = curr->next;
        }
        return head;
    }
};
```

**Python Implementation:**
```python
class Solution:
    def rearrange(self, head):
        if not head:
            return head
        # Extract values from linked list into list
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        # Sort the values
        vals.sort()
        # Reconstruct linked list with sorted values
        curr = head
        for v in vals:
            curr.val = v
            curr = curr.next
        return head
```

---

#### **Approach 2: Merge Sort on the Linked List**

**C++ Implementation:**
```cpp
/*struct Node {
    int val;
    Node *next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node *n) : val(x), next(n) {}
  };
  */
class Solution{
    public:

    // Function to merge two sorted lists
    Node* merge(Node* l1, Node* l2) {
        Node dummy(0);
        Node* curr = &dummy;
        while(l1 && l2){
            if(l1->val <= l2->val){
                curr->next = l1;
                l1 = l1->next;
            } else{
                curr->next = l2;
                l2 = l2->next;
            }
            curr = curr->next;
        }
        if(l1) curr->next = l1;
        if(l2) curr->next = l2;
        return dummy.next;
    }

    // Function to find the middle of the list
    Node* getMid(Node* head) {
        Node* slow = head;
        Node* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    Node* rearrange(Node* head)
    {
        if(!head || !head->next)
            return head;
        Node* mid = getMid(head);
        Node* right = mid->next;
        mid->next = nullptr;
        Node* left = rearrange(head);
        right = rearrange(right);
        return merge(left, right);
    }
};
```

**Python Implementation:**
```python
class Solution:
    def merge(self, l1, l2):
        dummy = Node(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next

    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def rearrange(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None
        left = self.rearrange(head)
        right = self.rearrange(right)
        return self.merge(left, right)
```

---

### Final Remarks

- **Intuition:**
  - **Approach 1** is simple and leverages the efficiency of array sorting, but uses extra space.
  - **Approach 2 (Merge Sort)** is optimal for linked lists, sorting in $O(N \log N)$ without the need for extra array space.

- **Recommendations:**
  For general and large inputs, **Approach 2 (Merge Sort)** is highly recommended due to its efficiency and in-place merging. Approach 1 is a great option when extra space is not a concern.

Each approach is implemented according to the provided template; only the `template_code` sections were modified, ensuring the prefix and suffix remain unchanged.

</details>
