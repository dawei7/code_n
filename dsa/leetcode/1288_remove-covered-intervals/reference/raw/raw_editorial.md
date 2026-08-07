[TOC]

## Solution

---

### Approach 1: Greedy Algorithm

**Solution Pattern**

> The idea of the greedy algorithm is to pick the _locally_ optimal move at each step, which would lead to the _globally_ optimal solution.

Typical greedy solution has $$\mathcal{O}(N \log N)$$ time complexity and consists of two steps:

- Figure out how to sort the input data.
That would take $$\mathcal{O}(N \log N)$$ time and could be done directly by sorting or indirectly by using the heap data structure. Usually sorting is better than heap usage because of the gain in space.

- Parse the sorted input in $$\mathcal{O}(N)$$ time to construct a solution. 

In the case of already sorted input, the greedy solution could have $$\mathcal{O}(N)$$ time complexity, [here is an example](https://leetcode.com/articles/gas-station/).

**Intuition**

Let us figure out how to sort the input. The idea to sort by start point is pretty obvious because it simplifies further parsing:

![traversal](images/sort.png)

Let us consider two subsequent intervals after sorting. Since sorting ensures that `start1 < start2`, it's sufficient to compare the end boundaries:   

- If `end1 < end2`, the intervals won't completely cover one another, though they have some overlapping.

![traversal](images/dont_cover2.png) 

- If `end1 >= end2`, the interval 2 is covered by the interval 1.

![traversal](images/cover.png) 

**Edge case: How to treat intervals that share a start point**

> We've missed an important edge case in the previous discussion: what if two intervals share the start point, _i.e._ `start1 == start2`? 

The above algorithm will fail because it cannot distinguish these two situations as follows: 

![traversal](images/share.png) 

One of the intervals is covered by another, but if we sort only by the start point, we would not know which one. Hence, we need to sort by the endpoint as well.

> If two intervals share the same start point, one has to put the longer interval in front.

This way the above algorithm would work fine here as well. Moreover, it can deal with more complex cases, like the one below:

![traversal](images/complex.png)

**Algorithm**

- Sort in the ascending order by the start point. If two intervals share the same start point, put the longer one to be the first.

- Initiate the number of non-covered intervals: `count = 0`.

- Iterate over sorted intervals and compare end points. 
    
    - If the current interval is not covered by the previous one `end > prev_end`, increase the number of non-covered intervals. Assign the current interval to be previous for the next step.
    
    - Otherwise, the current interval is covered by the previous one. Do nothing.

- Return `count`.

**Implementation**



![Slide 1](images/slideshow_1288_LIS_1288_slide_1.png)

![Slide 2](images/slideshow_1288_LIS_1288_slide_2.png)

![Slide 3](images/slideshow_1288_LIS_1288_slide_3.png)

![Slide 4](images/slideshow_1288_LIS_1288_slide_4.png)

![Slide 5](images/slideshow_1288_LIS_1288_slide_5.png)

![Slide 6](images/slideshow_1288_LIS_1288_slide_6.png)




```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0
        
        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1    
                prev_end = end
        
        return count
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N \log N)$$ since the sorting dominates the complexity of the algorithm.
 
* Space complexity : $$\mathcal{O}(N)$$ or $$\mathcal{O}(\log{N})$$

  - The space complexity of the sorting algorithm depends on the implementation of each programming language.

  - For instance, the `sorted()` function in Python is implemented with the [Timsort](https://en.wikipedia.org/wiki/Timsort) algorithm whose space complexity is $$\mathcal{O}(N)$$.

  - In Java, the [Arrays.sort()](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-byte:A-) is implemented as a variant of quicksort algorithm whose space complexity is $$\mathcal{O}(\log{N})$$.


---