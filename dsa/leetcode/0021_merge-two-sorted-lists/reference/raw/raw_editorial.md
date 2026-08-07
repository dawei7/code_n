[TOC]

## Video Solution

---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/657657566" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>&nbsp;
</div>

## Solution Article

### Approach 1: Recursion

**Intuition**

We can recursively define the result of a `merge` operation on two lists as
the following (avoiding the corner case logic surrounding empty lists):

$$
\left\{
\begin{array}{ll}
      list1[0] + merge(list1[1:], list2) & list1[0] < list2[0] \\
      list2[0] + merge(list1, list2[1:]) & otherwise
\end{array}
\right.
$$

Namely, the smaller of the two lists' heads plus the result of a `merge` on
the rest of the elements.

**Algorithm**

We model the above recurrence directly, first accounting for edge cases.
Specifically, if either of `l1` or `l2` is initially `null`, there is no
merge to perform, so we simply return the non-`null` list. Otherwise, we
determine which of `l1` and `l2` has a smaller head, and recursively set the
`next` value for that head to the next merge result. Given that both lists
are `null`-terminated, the recursion will eventually terminate.


```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```


**Complexity Analysis**

* Time complexity : $$O(n + m)$$

    Because each recursive call increments the pointer to `l1` or `l2` by one (approaching the dangling `null` at the end of each list), there will be exactly one call to `mergeTwoLists` per element in each list. Therefore, the time complexity is linear in the combined size of the lists.

* Space complexity : $$O(n + m)$$

    The first call to `mergeTwoLists` does not return until the ends of both `l1` and `l2` have been reached, so $$n + m$$ stack frames consume $$O(n + m)$$ space.

<br />

---

### Approach 2: Iteration

**Intuition**

We can achieve the same idea via iteration by assuming that `l1` is entirely
less than `l2` and processing the elements one-by-one, inserting elements of
`l2` in the necessary places in `l1`.

**Algorithm**

First, we set up a false "`prehead`" node that allows us to easily return the
head of the merged list later. We also maintain a `prev` pointer, which
points to the current node for which we are considering adjusting its `next`
pointer. Then, we do the following until at least one of `l1` and `l2` points
to `null`: if the value at `l1` is less than or equal to the value at `l2`,
then we connect `l1` to the previous node and increment `l1`. Otherwise, we
do the same, but for `l2`. Then, regardless of which list we connected, we
increment `prev` to keep it one step behind one of our list heads.

After the loop terminates, at most one of `l1` and `l2` is non-`null`.
Therefore (because the input lists were in sorted order), if either list is
non-`null`, it contains only elements greater than all of the
previously-merged elements. This means that we can simply connect the
non-`null` list to the merged list and return it.

To see this in action on an example, check out the animation below:



![Slide 1](images/slideshow_21_Merge_Two_Sorted_Lists_Slide1.PNG)

![Slide 2](images/slideshow_21_Merge_Two_Sorted_Lists_Slide2.PNG)

![Slide 3](images/slideshow_21_Merge_Two_Sorted_Lists_Slide3.PNG)

![Slide 4](images/slideshow_21_Merge_Two_Sorted_Lists_Slide4.PNG)

![Slide 5](images/slideshow_21_Merge_Two_Sorted_Lists_Slide5.PNG)

![Slide 6](images/slideshow_21_Merge_Two_Sorted_Lists_Slide6.PNG)

![Slide 7](images/slideshow_21_Merge_Two_Sorted_Lists_Slide7.PNG)

![Slide 8](images/slideshow_21_Merge_Two_Sorted_Lists_Slide8.PNG)

![Slide 9](images/slideshow_21_Merge_Two_Sorted_Lists_Slide9.PNG)

![Slide 10](images/slideshow_21_Merge_Two_Sorted_Lists_Slide10.PNG)

![Slide 11](images/slideshow_21_Merge_Two_Sorted_Lists_Slide11.PNG)

![Slide 12](images/slideshow_21_Merge_Two_Sorted_Lists_Slide12.PNG)

![Slide 13](images/slideshow_21_Merge_Two_Sorted_Lists_Slide13.PNG)

![Slide 14](images/slideshow_21_Merge_Two_Sorted_Lists_Slide14.PNG)

![Slide 15](images/slideshow_21_Merge_Two_Sorted_Lists_Slide15.PNG)

![Slide 16](images/slideshow_21_Merge_Two_Sorted_Lists_Slide16.PNG)

![Slide 17](images/slideshow_21_Merge_Two_Sorted_Lists_Slide17.PNG)

![Slide 18](images/slideshow_21_Merge_Two_Sorted_Lists_Slide18.PNG)

![Slide 19](images/slideshow_21_Merge_Two_Sorted_Lists_Slide19.PNG)

![Slide 20](images/slideshow_21_Merge_Two_Sorted_Lists_Slide20.PNG)

![Slide 21](images/slideshow_21_Merge_Two_Sorted_Lists_Slide21.PNG)

![Slide 22](images/slideshow_21_Merge_Two_Sorted_Lists_Slide22.PNG)

![Slide 23](images/slideshow_21_Merge_Two_Sorted_Lists_Slide23.PNG)

![Slide 24](images/slideshow_21_Merge_Two_Sorted_Lists_Slide24.PNG)

![Slide 25](images/slideshow_21_Merge_Two_Sorted_Lists_Slide25.PNG)

![Slide 26](images/slideshow_21_Merge_Two_Sorted_Lists_Slide26.PNG)

![Slide 27](images/slideshow_21_Merge_Two_Sorted_Lists_Slide27.PNG)

![Slide 28](images/slideshow_21_Merge_Two_Sorted_Lists_Slide28.PNG)

![Slide 29](images/slideshow_21_Merge_Two_Sorted_Lists_Slide29.PNG)

![Slide 30](images/slideshow_21_Merge_Two_Sorted_Lists_Slide30.PNG)

![Slide 31](images/slideshow_21_Merge_Two_Sorted_Lists_Slide31.PNG)

![Slide 32](images/slideshow_21_Merge_Two_Sorted_Lists_Slide32.PNG)

![Slide 33](images/slideshow_21_Merge_Two_Sorted_Lists_Slide33.PNG)

![Slide 34](images/slideshow_21_Merge_Two_Sorted_Lists_Slide34.PNG)

![Slide 35](images/slideshow_21_Merge_Two_Sorted_Lists_Slide35.PNG)




```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
```


**Complexity Analysis**

* Time complexity : $$O(n + m)$$

    Because exactly one of `l1` and `l2` is incremented on each loop
    iteration, the `while` loop runs for a number of iterations equal to the
    sum of the lengths of the two lists. All other work is constant, so the
    overall complexity is linear.

* Space complexity : $$O(1)$$

    The iterative approach only allocates a few pointers, so it has a
    constant overall memory footprint.