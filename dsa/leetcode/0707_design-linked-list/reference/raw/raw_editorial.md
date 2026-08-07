[TOC]

## Solution

---

### Interview Strategy

[Linked List](https://en.wikipedia.org/wiki/Linked_list#Basic_concepts_and_nomenclature) is a data structure with zero or several elements. Each element contains a value and link(s) to the other element(s). Depending on the number of links, that could be a singly linked list, doubly linked list or multiply linked list.  

A singly linked list is the simplest one, it provides `addAtHead` in a constant time, and `addAtTail` in a linear time. Though the doubly linked list is the most used one, because it provides both `addAtHead` and `addAtTail` in a constant time, and optimizes the insert and delete operations.

A doubly linked list is implemented in Java as [LinkedList](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html). Since these structures are quite well-known, a good interview strategy would be to mention them during the discussion but not to base the code on them. Better to use the limited interview time to work with two ideas:
 
- [Sentinel nodes](https://leetcode.com/articles/remove-linked-list-elements/)

>Sentinel nodes are widely used in the trees and linked lists as _pseudo-heads_, _pseudo-tails_, _etc_. They serve as the guardians, as the name suggests, and usually, they do not hold any data.

Sentinel nodes will be used here to simplify insert and delete. We would apply this in both of the following approaches.

- Bidirectional search for a doubly-linked list

Rather than starting from the head, we could search the node in a doubly-linked list from both head and tail.

If you are familiar with the concepts, you can start directly from the Approach #2. By the way, Approach #2 is 90% of what you need to solve the problem of [LRU Cache](https://leetcode.com/articles/lru-cache/).

### Approach 1: Singly Linked List

Let's start with the simplest possible MyLinkedList, which contains just a structure size and a sentinel head.

![bla](images/singly4.png)


```python
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
```


Note, that the sentinel node is used as a pseudo-head and is always present. This way the structure could never be empty, it will contain at least a sentinel head. All nodes in MyLinkedList have a type ListNode: value + link to the next element.


```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```


**Add at Index, Add at Head, and Add at Tail**

Let's first discuss insert at index operation, because thanks to the sentinel node addAtTail and addAtHead operations could be reduced to this operation as well. 

The idea is straightforward:

- Find the predecessor of the node to insert. If the node is to be inserted at the head, its predecessor is a sentinel head. If the node is to be inserted at the tail, its predecessor is the last node.

- Insert the node by changing the link to the next node.


```python
to_add.next = pred.next
pred.next = to_add
```


![bla](images/singly_insert.png)

---

![bla](images/singly_insert_head.png)

**Delete at Index**

Basically, the same as insert:

- Find the predecessor.

- Delete the node by changing the links to the next node.


```python
# delete pred.next 
pred.next = pred.next.next
```


![bla](images/singly_delete.png)

**Get**            

Get is a very straightforward: start from the sentinel node and do `index + 1` steps


```python
# index steps needed 
# to move from sentinel node to wanted index
for _ in range(index + 1):
    curr = curr.next
return curr.val
```


![bla](images/singly_get.png)

**Implementation**


```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        # index steps needed 
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(1)$$ for addAtHead. $$\mathcal{O}(k)$$ for get, addAtIndex, and deleteAtIndex, where $$k$$ is an index of the element to get, add or delete. $$\mathcal{O}(N)$$ for addAtTail.
 
* Space complexity: $$\mathcal{O}(1)$$ for all operations.
<br />
<br />


---
### Approach 2: Doubly Linked List

Time to implement DLL MyLinkedList, which is much faster (twice as fast on the test case set here) though a bit more complex. It contains size, sentinel head, and sentinel tail.

![bla](images/dll.png)


```python
class MyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
```


Note, that the sentinel head and tail are always present. All nodes in MyLinkedList have a type ListNode: value + two links: to the next and to the previous elements.


```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
```


**Add at Index, Add at Head, and Add at Tail**

The idea is simple:

- Find the predecessor and the successor of the node to insert. If the node is to be inserted at head, its predecessor is a sentinel head. If the node is to be inserted at the tail, its successor is a sentinel tail.

> Use bidirectional search to perform faster.

- Insert the node by changing the links to the next and previous nodes.


```python
to_add.prev = pred
to_add.next = succ
pred.next = to_add
succ.prev = to_add
```


![bla](images/dll_insert2.png)

**Delete at Index**

Basically, the same as insert:

- Find the predecessor and successor.

- Delete the node by changing the links to the next and previous nodes.


```python
pred.next = succ
succ.prev = pred
```


![bla](images/dll_delete2.png)

**Get**            

Get is very straightforward: 

- Compare `index` and `size - index` to define the fastest way: starting from the head, or starting from the tail.

- Go to the wanted node.


```python
# Choose the fastest way: to move from the head
# or to move from the tail
if index + 1 < self.size - index:
    curr = self.head
    for _ in range(index + 1):
        curr = curr.next
else:
    curr = self.tail
    for _ in range(self.size - index):
        curr = curr.prev
```


![bla](images/dll_get2.png)

**Implementation**


```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
                
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length, 
        # the node will not be inserted.
        if index > self.size:
            return
        
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        
        # Find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        # Insertion itself
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # If the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        # Find the predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        # Delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(1)$$ for addAtHead and addAtTail. $$\mathcal{O}(\min(k, N - k))$$ for get, addAtIndex, and deleteAtIndex, where $$k$$ is an index of the element to get, add or delete. 
 
* Space complexity: $$\mathcal{O}(1)$$ for all operations.