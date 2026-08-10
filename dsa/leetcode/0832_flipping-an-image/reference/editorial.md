
---
### Approach #1: Direct [Accepted]

**Intuition and Algorithm**

We can do this in place.  In each row, the `i`th value from the left is equal to the inverse of the `i`th value from the right.

We use $(C+1) / 2$ (with floor division) to iterate over all indexes `i` in the first half of the row, including the center.

```python
class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                """
                In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                """
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where `N` is the total number of elements in `A`.

* Space Complexity: $O(1)$ in *additional* space complexity.