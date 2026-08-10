
## Solution
---

### Overview ####

The problem is to sort the linked list in $\mathcal{O}(n \log n)$ time and using only constant extra space. If we look at various sorting algorithms, [Merge Sort](https://en.wikipedia.org/wiki/Merge_sort) is one of the efficient sorting algorithms that is popularly used for sorting the linked list. The merge sort algorithm runs in $\mathcal{O}(n \log n)$ time in all the cases. Let's discuss approaches to sort linked list using merge sort.

> [Quicksort](https://en.wikipedia.org/wiki/Quicksort) is also one of the efficient algorithms with the average time complexity of $\mathcal{O}(n \log n)$. But the worst-case time complexity is $\mathcal{O}(n ^{2})$. Also, variations of the quick sort like randomized quicksort are not efficient for the linked list because unlike arrays, random access in the linked list is not possible in $\mathcal{O}(1)$ time.
If we sort the linked list using quicksort, we would end up using the head as a pivot element which may not be efficient in all scenarios.
---

### Approach 1: Top Down Merge Sort

**Intuition**

Merge sort is a popularly known algorithm that follows the[ Divide and Conquer Strategy](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm). The divide and conquer strategy can be split into 2 phases:

 _Divide phase_: Divide the problem into subproblems.

_Conquer phase_: Repeatedly solve each subproblem independently and combine the result to form the original problem.

The Top Down approach for merge sort recursively splits the original list into sublists of equal sizes, sorts each sublist independently, and eventually merge the sorted lists.  Let's look at the algorithm to implement merge sort in Top Down Fashion.

**Algorithm**

- Recursively split the original list into two halves. The split continues until there is only one node in the linked list (Divide phase). To split the list into two halves, we find the middle of the linked list using the Fast and Slow pointer approach as mentioned in [Find Middle Of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/).

- Recursively sort each sublist and combine it into a single sorted list. (Merge Phase). This is similar to the problem [Merge two sorted linked lists](https://leetcode.com/problems/merge-two-sorted-lists/)

The process continues until we get the original list in sorted order.

For the linked list = `[10,1,60,30,5]`, the following figure illustrates the merge sort process using a top down approach.

![img](images/topDown_merge_sort.png)

If we have sorted lists, list1 = `[1,10]` and list2 = `[5,30,60]`. The following animation illustrates the merge process of both lists into a single sorted list.

![Slide 1](images/slideshow_148_sort_list_slide_1.png)

![Slide 2](images/slideshow_148_sort_list_slide_2.png)

![Slide 3](images/slideshow_148_sort_list_slide_3.png)

![Slide 4](images/slideshow_148_sort_list_slide_4.png)

![Slide 5](images/slideshow_148_sort_list_slide_5.png)

![Slide 6](images/slideshow_148_sort_list_slide_6.png)

![Slide 7](images/slideshow_148_sort_list_slide_7.png)

![Slide 8](images/slideshow_148_sort_list_slide_8.png)

![Slide 9](images/slideshow_148_sort_list_slide_9.png)

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the head or the entire list is none, return the head
        if not head or not head.next:
            return head
        # Get the middle node
        mid = self.getMid(head)
        # Split the list to left and right and sort them
        left = self.sortList(head)
        right = self.sortList(mid)
        # Merge the sorted lists
        return self.merge(left, right)

    def merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummyHead.next

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        midPrev = None
        while head and head.next:
            midPrev = head if not midPrev else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n \log n)$, where $n$ is the number of nodes in linked list.
The algorithm can be split into 2 phases, Split and Merge.

Let's assume that $n$ is power of $2$. For $n = 16$, the split and merge operation in  Top Down fashion can be visualized as follows

![img](images/top_down_time_complexity.png)

**_Split_**

The recursion tree expands in form of a complete binary tree, splitting the list into two halves recursively. The number of levels in a complete binary tree is given by $\log_{2} n$. For $n=16$, number of splits = $\log_{2} 16 = 4$

**_Merge_**

At each level, we merge n nodes which takes $\mathcal{O}(n)$ time.
For $n = 16$, we perform merge operation on $16$ nodes in each of the $4$ levels.

So the time complexity for split and merge operation is $\mathcal{O}(n \log n)$

* Space Complexity: $\mathcal{O}(\log n)$ , where $n$ is the number of nodes in linked list. Since the problem is recursive, we need additional space to store the recursive call stack. The maximum depth of the recursion tree is $\log n$

---

### Approach 2: Bottom Up Merge Sort

**Intuition**

The Top Down Approach for merge sort uses $\mathcal{O}(\log n)$ extra space due to recursive call stack. Let's understand how we can implement merge sort using constant extra space using Bottom Up Approach.

The Bottom Up approach for merge sort starts by splitting the problem into the smallest subproblem and iteratively merge the result to solve the original problem.
- First, the list is split into sublists of size 1 and merged iteratively in sorted order. The merged list is solved similarly.

- The process continues until we sort the entire list.

This approach is solved iteratively and can be implemented using constant extra space. Let's look at the algorithm to implement merge sort in Bottom Up Fashion.

**Algorithm**

Assume, $n$ is the number of nodes in the linked list.
- Start with splitting the list into sublists of size $1$. Each adjacent pair of sublists of size $1$ is merged in sorted order. After the first iteration, we get the sorted lists of size $2$. A similar process is repeated for a sublist of size $2$. In this way, we iteratively split the list into sublists of size $1,2,4,8 ..$ and so on until we reach $n$.

- To split the list into two sublists of given $\text{size}$ beginning from $\text{start}$, we use two pointers, $\text{mid}$ and $\text{end}$ that references to the start and end of second linked list respectively. The split process finds the middle of linked lists for the given $\text{size}$.

- Merge the lists in sorted order as discussed in  _Approach 1_

- As we iteratively split the list and merge, we have to keep track of the previous merged list using pointer $\text{tail}$ and the next sublist to be sorted using pointer $\text{nextSubList}$.

For the linked list = `[10,1,30,2,5]`, the following figure illustrates the merge sort process using a Bottom Up approach.

![img](images/bottom_up_merge_sort.png)

```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        n = self.getCount(head)
        start = head
        dummyHead = ListNode()
        size = 1
        while size < n:
            self.tail = dummyHead
            while start is not None:
                if start.next is None:
                    self.tail.next = start
                    break
                mid = self.split(start, size)
                self.merge(start, mid)
                start = self.nextSubList
            start = dummyHead.next
            size *= 2
        return dummyHead.next

    def split(self, start, size):
        midPrev = start
        end = start.next
        # Use fast and slow approach to find middle and end of second linked list
        for index in range(1, size):
            if end and end.next:
                end = end.next.next
            else:
                if end:
                    end = end.next
            if midPrev.next:
                midPrev = midPrev.next
        mid = midPrev.next
        midPrev.next = None
        self.nextSubList = end.next if end else None
        if end:
            end.next = None
        # Return the start of second linked list
        return mid

    def merge(self, list1, list2):
        dummyHead = ListNode()
        newTail = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                newTail.next = list1
                list1 = list1.next
            else:
                newTail.next = list2
                list2 = list2.next
            newTail = newTail.next
        newTail.next = list1 if list1 else list2
        # Traverse till the end of merged list to get the newTail
        while newTail.next:
            newTail = newTail.next
        # Link the old tail with the head of merged list
        self.tail.next = dummyHead.next
        # Update the old tail to the new tail of merged list
        self.tail = newTail

    def getCount(self, head):
        cnt = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            cnt += 1
        return cnt
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(n \log n)$, where $n$ is the number of nodes in linked list.
 Let's analyze the time complexity of each step:

1) Count Nodes - Get the count of number nodes in the linked list requires $\mathcal{O}(n)$ time.

2) Split and Merge - This operation is similar to _Approach 1_ and takes  $\mathcal{O}(n \log n)$ time.
For $n = 16$, the split and merge operation in Bottom Up fashion can be visualized as follows

![img](images/bottom_up_time_complexity.png)

This gives us total time complexity as
$\mathcal{O}(n) + \mathcal{O}(n \log n) = \mathcal{O}(n \log n)$

* Space Complexity: $\mathcal{O}(1)$ We use only constant space for storing the reference pointers  $\text{tail}$ , $\text{nextSubList}$ etc.