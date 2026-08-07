[TOC]

### Approach #1: Depth-First Search [Accepted]

**Intuition**

We perform the algorithm explained in the problem description: paint the starting pixels, plus adjacent pixels of the same color, and so on.

**Algorithm**

Say `color` is the color of the starting pixel. Let's flood fill the starting pixel: we change the color of that pixel to the new color, then check the 4 neighboring pixels to make sure they are valid pixels of the same `color`, and of the valid ones, we flood fill those, and so on.

We can use a function `dfs` to perform a flood fill on a target pixel.


```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image
```



**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of pixels in the image. We might process every pixel.

* Space Complexity: $$O(N)$$, the size of the implicit call stack when calling `dfs`.