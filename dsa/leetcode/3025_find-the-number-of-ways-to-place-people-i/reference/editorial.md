### Approach 1: Triple Loop Enumeration

#### Intuition

Since the data scale is $2 \leq n \leq 50$, we can consider a naive approach to solve: first, use a double loop to traverse all pairs of points. For each pair, if they are not on the main diagonal of the rectangle they form, then check whether there are any other points inside the rectangle (including the boundary). If there are none, then the pair of points satisfies the conditions of the problem.

To determine whether a point lies within a given rectangle, we only need to check if its coordinates $(x, y)$ fall within the horizontal and vertical limits of the rectangle. Checking $x$ and $y$ separately is sufficient. Additionally, since the problem specifies that the rectangle includes its boundaries, we should use closed intervals in our checks.

When there are only two points, the third loop is never entered, so we need to handle this case as a special case directly.

#### Implementation

```python
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)

        for i in range(n):
            pointA = points[i]
            for j in range(n):
                pointB = points[j]
                if i == j or not (
                    pointA[0] <= pointB[0] and pointA[1] >= pointB[1]
                ):
                    continue
                if n == 2:
                    ans += 1
                    continue

                illegal = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    pointTmp = points[k]
                    isXContained = (
                        pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    )
                    isYContained = (
                        pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    )
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{points}$.

- Time complexity: $O(n^3)$.

  We use a double loop to traverse all point pairs, and then a single loop to check whether any points lie inside the rectangle formed by the pair.

- Space complexity: $O(1)$.

  Only a few additional variables are needed.

---

### Approach 2: Sorting + Monotonic Scan

#### Intuition

The brute-force triple-loop method has a time complexity of $O(n^3)$, which is acceptable for $n \leq 50$, but we can do better by leveraging sorting and a single forward scan.

We start by sorting all points in ascending order of their $x$-coordinate. When two points have the same $x$-coordinate, we sort them in descending order of their $y$-coordinate. This ensures that for any later point in the sorted order, the $x$-coordinate is always greater or equal to the earlier point, while the $y$-coordinate is potentially smaller.

Now, for each point `i`, we consider it as the top-left corner of the rectangle and look for valid points `j` to its right (i.e., with larger $x$ values). To avoid counting pairs that have other points within the rectangle, we maintain a running minimum `minh` (the lowest $y$-value encountered so far).

For each next point `j`, if its $y$-coordinate is greater than `minh` and not above point `i`, it forms a valid pair. We then update `minh` to this $y$-coordinate to ensure we don’t count future rectangles overlapping this one vertically.

#### Implementation

```python
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort points by x ascending, and for ties by y descending
        points.sort(key=lambda p: (p[0], -p[1]))

        n = len(points)
        ans = 0

        # For each left point
        for i in range(n - 1):
            pi2 = points[i][1]
            min_h = float("-inf")

            # Scan right-side points
            for j in range(i + 1, n):
                if points[j][1] > min_h and points[j][1] <= pi2:
                    ans += 1
                    min_h = points[j][1]

        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{points}$.

- Time complexity: $O(n^3)$.

  Sorting takes $O(n \log n)$, and the nested scan takes $O(n^2)$. Hence, the total time complexity is $O(n^2)$, which is significantly better than the triple-loop $O(n^3)$ approach.

- Space complexity:

  Apart from a few local variables, the algorithm operates in-place, so its auxiliary space usage is minimal.
  However, we must account for the additional space used by the sorting operation ($S$), which depends on the language implementation:

  * In **Java**, `Arrays.sort()` for primitive arrays uses a variant of Dual-Pivot Quick Sort, which requires $O(\log n)$ stack space.
  * In **C++**, `std::sort()` is typically implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worst-case space complexity of $O(\log n)$.
  * In **Python**, the built-in `sort()` method uses Timsort, a hybrid of Merge Sort and Insertion Sort, which requires $O(n)$ auxiliary space in the worst case.

  Hence, the space complexity varies by language:

  $$[
  $\mathcal{O}(\\log n)$ \text{ for C++ and Java}, \quad $\mathcal{O}(n)$ \text{ for Python.}
  ]$$

---