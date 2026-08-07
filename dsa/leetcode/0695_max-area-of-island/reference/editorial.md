[TOC]

### Approach #1: Depth-First Search (Recursive) [Accepted]

**Intuition and Algorithm**

We want to know the area of each connected shape in the grid, then take the maximum of these.

If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use `seen` to keep track of squares we haven't visited before. It will also prevent us from counting the same shape more than once.

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
```

**Complexity Analysis**

* Time Complexity: $O(R*C)$, where $R$ is the number of rows in the given `grid`, and $C$ is the number of columns.  We visit every square once.

* Space complexity: $O(R*C)$, the space used by `seen` to keep track of visited squares and the space used by the call stack during our recursion.

---
### Approach #2: Depth-First Search (Iterative) [Accepted]

**Intuition and Algorithm**

We can try the same approach using a stack-based, (or "iterative") depth-first search.

Here, `seen` will represent squares that have either been visited or are added to our list of squares to visit (`stack`). For every starting land square that hasn't been visited, we will explore 4-directionally around it, adding land squares that haven't been added to `seen` to our `stack`.

On the side, we'll keep a count `shape` of the total number of squares seen during the exploration of this shape. We'll want the running max of these counts.

```python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R*C)$, where $R$ is the number of rows in the given `grid`, and $C$ is the number of columns. We visit every square once.

* Space complexity: $O(R*C)$, the space used by `seen` to keep track of visited squares and the space used by `stack`.