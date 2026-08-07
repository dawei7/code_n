[TOC]

## Solution

---
### Approach #1 Single Scan [Accepted]

The solution is very simple. We can find out the extra maximum number of flowers, $$count$$, that can be planted for the given $$flowerbed$$ arrangement. To do so, we can traverse over all the elements of the $$flowerbed$$ and find out those elements which are 0(implying an empty position). For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower at the current position without violating the no-adjacent-flowers-rule. For the first and last elements, we need not check the previous and the next adjacent positions respectively.

If the $$count$$ obtained is greater than or equal to $$n$$, the required number of flowers to be planted, we can plant $$n$$ flowers in the empty spaces, otherwise not.

**Implementation**


```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n
```



**Complexity Analysis**

* Time complexity: $$O(n)$$. A single scan of the $$flowerbed$$ array of size $$n$$ is done.

* Space complexity: $$O(1)$$. Constant extra space is used.

---
### Approach #2 Optimized [Accepted]

**Algorithm**

Instead of finding the maximum value of $$count$$ that can be obtained, as done in the last approach, we can stop the process of checking the positions for planting the flowers as soon as $$count$$ becomes equal to $$n$$. Doing this leads to an optimization of the first approach. If $$count$$ never becomes equal to $$n$$, $$n$$ flowers can't be planted at the empty positions.

**Implementation**


```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n
```


**Complexity Analysis**

* Time complexity: $$O(n)$$. A single scan of the $$flowerbed$$ array of size $$n$$ is done.

* Space complexity: $$O(1)$$. Constant extra space is used.