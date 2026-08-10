
### Approach #1: Check Position [Accepted]

**Intuition**

If the rectangles do not overlap, then `rec1` must either be higher, lower, to the left, or to the right of `rec2`.

**Algorithm**

The answer for whether they *don't* overlap is `LEFT OR RIGHT OR UP OR DOWN`, where `OR` is the logical OR, and `LEFT` is a boolean that represents whether `rec1` is to the left of `rec2`.  The answer for whether they do overlap is the negation of this.

The condition "`rec1` is to the left of `rec2`" is $\text{rec1}[2] \le \text{rec2}[0]$, that is the right-most x-coordinate of `rec1` is left of the left-most x-coordinate of `rec2`.  The other cases are similar.

_Note: we should also check if either of the rectangle is actually a line._
If this is the case, then we cannot have any positive overlapping according to the definition.

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        # check if either rectangle is actually a line
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
            rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            # the line cannot have positive overlap
            return False

        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
```

**Complexity Analysis**

* Time and Space Complexity:  $O(1)$.

---
### Approach #2: Check Area [Accepted]

**Intuition**

If the rectangles overlap, they have positive area.  This area must be a rectangle where both dimensions are positive, since the boundaries of the intersection are axis aligned.

Thus, we can reduce the problem to the one-dimensional problem of determining whether two line segments overlap.

**Algorithm**

Say the area of the intersection is $width * height$, where `width` is the intersection of the rectangles projected onto the x-axis, and `height` is the same for the y-axis.  We want both quantities to be positive.

The `width` is positive when $min(\text{rec1}[2], \text{rec2}[2]) > max(\text{rec1}[0], \text{rec2}[0])$, that is when the smaller of (the largest x-coordinates) is larger than the larger of (the smallest x-coordinates).  The `height` is similar.

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0
```

**Complexity Analysis**

* Time and Space Complexity:  $O(1)$.