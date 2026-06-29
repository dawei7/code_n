# Linked List - Add Two Numbers As Lists

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP57 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Linkedlist |
| Official Link | [PREP57](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_08/problems/PREP57) |

---

## Problem Statement

You are given heads of two **non-empty** linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.

Your task is add the two numbers and return the sum as a linked list.

Note:
- It is guaranteed that the list represents a number that does not have leading zeros except the number $0$ itself.
- In returned linked list digits should be stored in reverse order.

**Note:**

- For Java language, you need to:

Complete the function in the submit solution tab:
```
Node addTwoNumbers(Node l1, Node l2){...}
```
$\ $

- For C++ language, you need to:

Complete the function in the submit solution tab:
```
Node* addTwoNumbers(Node* l1, Node* l2){...}
```
$\ $

- For Python language, you need to:

Complete the function in the submit solution tab:
```
def addTwoNumbers(self, l1, l2):
```

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line contains two space separated integers $N$, $M$ — the length of two linked lists.
- The second line contains $N$ space separated digits $A_1, A_2, \ldots A_N$ — the value of the linked list nodes starting from the head for the first linked list.
- The third line contains $N$ space separated digits $B_1, B_2, \ldots B_M$ — the value of the linked list nodes starting from the head for the second linked list.

---

## Output Format

The function you complete should return the required answer.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N, M \leq 10^5$
- $0 \leq A_i, B_i \leq 9$

---

## Examples

**Example 1**

**Input**

```text
3
2 4
2 4
5 0 4 5
1 1
6
8
1 1
0
5
```

**Output**

```text
7 4 4 5 
4 1 
5
```

**Explanation**

**Test case $1$:** The two numbers will be $42$, $5405$. So the sum will be $5447$.

**Test case $2$:** The two numbers will be $6$, $8$. So the sum will be $14$.

**Test case $3$:** The two numbers will be $0$, $5$. So the sum will be $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 4
2 4
5 0 4 5
```

**Output for this case**

```text
7 4 4 5
```



#### Test case 2

**Input for this case**

```text
1 1
6
8
```

**Output for this case**

```text
4 1
```



#### Test case 3

**Input for this case**

```text
1 1
0
5
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this editorial, we will discuss the problem of adding two non-negative integers represented as linked lists. The digits are stored in reverse order, so the least significant digit comes first. Our goal is to add the two numbers and return the sum as a new linked list in the same reverse order.

We will explore **one correct approach** for solving this problem:

---

### Approach: Iterative Addition

In this approach, we traverse both linked lists simultaneously. At each step, we sum the digits from the two lists along with any carry from the previous addition. Mathematically, if we denote the digits by $a$ and $b$, and the carry by $c$, the current digit of the result is computed as:
$$
\text{digit} = (a + b + c) \mod 10
$$
and the new carry is updated as:
$$
c = \lfloor\frac{a + b + c}{10}\rfloor.
$$

The process continues until we have processed all digits and there is no remaining carry. This approach is efficient and runs in $O(\max(N, M))$, where $N$ and $M$ are the lengths of the two linked lists.

#### C++ Implementation:

```cpp
/* Linked List Node
struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
}; */

class Solution {
  public:
    Node* addTwoNumbers(Node* l1, Node* l2) {
        Node* dummy = new Node(0);
        Node* current = dummy;
        int carry = 0;
        while(l1 != NULL || l2 != NULL || carry != 0) {
            int x = (l1 != NULL) ? l1->data : 0;
            int y = (l2 != NULL) ? l2->data : 0;
            int sum = x + y + carry;
            carry = sum / 10;
            current->next = new Node(sum % 10);
            current = current->next;
            if(l1 != NULL) l1 = l1->next;
            if(l2 != NULL) l2 = l2->next;
        }
        return dummy->next;
    }
};
```

#### Python Implementation:

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.data if l1 is not None else 0
            y = l2.data if l2 is not None else 0
            total = x + y + carry
            carry = total // 10
            current.next = Node(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

---

### Summary

The **Iterative Addition** approach is the most straightforward technique that uses a loop to process both lists simultaneously. It efficiently handles the addition by using a dummy node to manage the result list, making it a reliable and efficient solution for adding two numbers represented as linked lists.

Happy coding and good luck with your DSA interviews!

</details>
