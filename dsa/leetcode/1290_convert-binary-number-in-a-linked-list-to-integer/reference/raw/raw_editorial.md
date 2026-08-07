[TOC]

## Solution

---

### Overview

Here we have two subproblems:

- To parse a non-empty linked list and to retrieve the digit sequence that represents a binary number.

- To convert this sequence into the number in decimal representation. 

The first subproblem is easy because the linked list is guaranteed to be non-empty.


```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        while head.next:
            head = head.next
            # TODO
```


The second subproblem is to convert $$(101)_2$$ into $$1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 5$$. It could be solved in two ways. Using classical arithmetic is more straightforward

![img](images/try1.png)
*Figure 1. Approach 1: num = num * 2 + x*


and to use bitwise operators is faster

![img](images/try2.png)
*Figure 2. Approach 2: num = (num << 1) | x*


<br />
<br />


---
### Approach 1: Binary Representation

![img](images/try1.png)
*Figure 3. Approach 1: num = num * 2 + x.*


- Initialize the result number to be equal to the head value: `num = head.val`. This operation is safe because the list is guaranteed to be non-empty.

- Parse linked list starting from the head: `while head.next`:

    - The current value is `head.next.val`. Update the result by shifting it by one to the left and adding the current value: `num = num * 2 + head.next.val`.
    
- Return `num`.

**Implementation**


```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$. 

* Space complexity: $$\mathcal{O}(1)$$. 
<br />
<br />


---
### Approach 2: Bit Manipulation

![img](images/try2.png)
*Figure 4. Approach 2: num = (num << 1) | x*


- Initialize the result number to be equal to the head value: `num = head.val`. This operation is safe because the list is guaranteed to be non-empty.

- Parse linked list starting from the head: `while head.next`:

    - The current value is `head.next.val`. Update the result by shifting it by one to the left and adding the current value using logical OR: `num = (num << 1) | head.next.val`.
    
- Return `num`.

**Implementation**


```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$. 

* Space complexity: $$\mathcal{O}(1)$$. 
<br />
<br />

---