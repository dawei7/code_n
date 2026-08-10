
## Solution

---
### Approach #1 Brute Force [Accepted]

The idea behind determining whether 4 given set of points constitute a valid square or not is really simple. Firstly, we need to determine if the sides of the quadrilateral formed by these 4 points are equal. But checking only this won't suffice. Since, this condition will be satisfied even in the case of a rhombus, where all the four sides are equal but the adjacent sides aren't perpendicular to each other. Thus, we also need to check if the lengths of the diagonals formed between the corners of the quadrilateral are equal. If both the conditions are satisfied, then only the given set of points can be deemed appropriate for constituting a square.

Now, the problem arises in determining which pairs of points act as the adjacent points on the square boundary. So, the simplest method is to consider every possible case. For the given 4 points, $[p_0, p_1, p_2, p_3]$, there are a total of 4! ways in which these points can be arranged to be considered as the square's boundaries. We can generate every possible permutation and check if any permutation leads to the valid square arrangement of points.

```python
class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def dist(p1, p2):
            return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

        def check(p1, p2, p3, p4):
            return (
                dist(p1, p2) > 0
                and dist(p1, p2) == dist(p2, p3)
                and dist(p2, p3) == dist(p3, p4)
                and dist(p3, p4) == dist(p4, p1)
                and dist(p1, p3) == dist(p2, p4)
            )

        def checkAllPermutations(p, l):
            if l == 4:
                return check(p[0], p[1], p[2], p[3])
            else:
                res = False
                for i in range(l, 4):
                    p[l], p[i] = p[i], p[l]
                    res |= checkAllPermutations(p, l + 1)
                    p[l], p[i] = p[i], p[l]
                return res

        p = [p1, p2, p3, p4]
        dis = [dist(p[i], p[(i + 1) % 4]) for i in range(4)]
        dis += [dist(p[i], p[(i + 2) % 4]) for i in range(4)]
        return (
            len(set(dis)) == 2 and min(dis) != 0 and checkAllPermutations(p, 0)
        )
```

**Complexity Analysis**

* Time complexity : $O(1)$. Constant number of permutations($4!$) are generated.

* Space complexity : $O(1)$. Constant space is required.

---
### Approach #2 Using Sorting [Accepted]

Instead of considering all the permutations of arrangements possible, we can make use of maths to simplify this problem a bit. If we sort the given set of points based on their x-coordinate values, and in the case of a tie, based on their y-coordinate value, we can obtain an arrangement, which directly reflects the arrangement of points on a valid square boundary possible.

Consider the only possible cases as shown in the figure below:

![Valid_Square](images/593_Valid_Square_1.PNG)

In each case, after sorting, we obtain the following conclusion regarding the connections of the points:

1. $p_0p_1$, $p_1p_3$, $p_3p_2$ and $p_2p_0$ form the four sides of any valid square.

2. $p_0p_3$ and $p_1p_2$ form the diagonals of the square.

Thus, once the sorting of the points is done, based on the above knowledge, we can directly compare $p_0p_1$, $p_1p_3$, $p_3p_2$ and $p_2p_0$ for equality of lengths(corresponding to the sides); and $p_0p_3$ and $p_1p_2$ for equality of lengths(corresponding to the diagonals).

```python
class Solution:
    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (
            p2[0] - p1[0]
        )

    def validSquare(self, p1, p2, p3, p4):
        p = [p1, p2, p3, p4]
        p.sort(key=lambda l: (l[0], l[1]))
        return (
            self.dist(p[0], p[1]) != 0
            and self.dist(p[0], p[1]) == self.dist(p[1], p[3])
            and self.dist(p[1], p[3]) == self.dist(p[3], p[2])
            and self.dist(p[3], p[2]) == self.dist(p[2], p[0])
            and self.dist(p[0], p[3]) == self.dist(p[1], p[2])
        )
```

**Complexity Analysis**

* Time complexity : $O(1)$. Sorting 4 points takes constant time.

* Space complexity : $O(1)$. Constant space is required.

---
### Approach #3 Checking every case [Accepted]

**Algorithm**

If we consider all the permutations descripting the arrangement of points as in the brute force approach, we can come up with the following set of 24 arrangements:

![Valid_Square](images/593_Valid_Square_2.PNG)

In this figure, the rows with the same shaded color indicate that the corresponding arrangements lead to the same set of edges and diagonals. Thus, we can see that only three unique cases exist. Thus, instead of generating all the 24 permutations, we check for the equality of edges and diagonals for only the three distinct cases.

```python
class Solution:
    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (
            p2[0] - p1[0]
        )

    def check(self, p1, p2, p3, p4):
        return (
            self.dist(p1, p2) > 0
            and self.dist(p1, p3) > 0
            and self.dist(p1, p2) == self.dist(p2, p3)
            and self.dist(p2, p3) == self.dist(p3, p4)
            and self.dist(p3, p4) == self.dist(p4, p1)
            and self.dist(p1, p3) == self.dist(p2, p4)
        )

    def validSquare(self, p1, p2, p3, p4):
        return (
            self.check(p1, p2, p3, p4)
            or self.check(p1, p3, p2, p4)
            or self.check(p1, p2, p4, p3)
        )
```

**Complexity Analysis**

* Time complexity : $O(1)$. A fixed number of comparisons are done.

* Space complexity : $O(1)$. No extra space required.