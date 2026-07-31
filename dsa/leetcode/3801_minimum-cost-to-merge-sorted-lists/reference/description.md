## Description

You are given a 2D integer array `lists`. Every `lists[i]` is nonempty and sorted in non-decreasing order.

Repeatedly choose two different current lists `a = lists[i]` and `b = lists[j]`, merge their elements into one sorted list, remove `a` and `b`, and insert the merged list at any position. The cost of that merge is

$$
\operatorname{len}(a)+\operatorname{len}(b)
+ \lvert\operatorname{median}(a)-\operatorname{median}(b)\rvert.
$$

Continue until only one sorted list remains. Return the minimum total cost among all possible merge orders.

For this problem, the median of a sorted list is its middle element. When the length is even, use the left of the two middle elements.
