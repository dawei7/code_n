[TOC]

## Solution

--- 

### Approach 1: 

**Intuition**

The nodes in the list are already linked, and hence the rotation basically means 

- To close the linked list into the ring.

- To break the ring after the new tail and just in front of the new head.

![rotate](images/rotate.png)

> Where is the new head?

In the position `n - k`, where `n` is the number of nodes in the list. The new tail is just before, in the position `n - k - 1`. 

> We were assuming that `k < n`. What about the case of `k >= n`?

`k` could be rewritten as a sum `k = (k // n) * n + k % n`, where the first term doesn't result in any rotation. Hence one could simply replace `k` with `k % n` to always have a number of rotation places smaller than `n`.

**Algorithm**

The algorithm is quite straightforward :

* Find the old tail and connect it with the head `old_tail.next = head` to close the ring. Compute the length of the list `n` at the same time.

* Find the new tail, which is `(n - k % n - 1)`th node from the `head`, and the new head, which is `(n - k % n)`th node.

* Break the ring `new_tail.next = None` and return `new_head`.

**Implementation**



![Slide 1](images/slideshow_61_LIS_61_slide_1.png)

![Slide 2](images/slideshow_61_LIS_61_slide_2.png)

![Slide 3](images/slideshow_61_LIS_61_slide_3.png)

![Slide 4](images/slideshow_61_LIS_61_slide_4.png)

![Slide 5](images/slideshow_61_LIS_61_slide_5.png)

![Slide 6](images/slideshow_61_LIS_61_slide_6.png)

![Slide 7](images/slideshow_61_LIS_61_slide_7.png)

![Slide 8](images/slideshow_61_LIS_61_slide_8.png)

![Slide 9](images/slideshow_61_LIS_61_slide_9.png)

![Slide 10](images/slideshow_61_LIS_61_slide_10.png)

![Slide 11](images/slideshow_61_LIS_61_slide_11.png)

![Slide 12](images/slideshow_61_LIS_61_slide_12.png)

![Slide 13](images/slideshow_61_LIS_61_slide_13.png)

![Slide 14](images/slideshow_61_LIS_61_slide_14.png)




```python
class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N)$$ where $$N$$ is a number of elements in the list.
 
* Space complexity : $$\mathcal{O}(1)$$ since it's a constant space solution.