[TOC]

## Solution

---

### Approach 1: Binary Search

**Intuition**

Given an array `colors` and a series of queries, each of which contains two integers `i` and `c`, we want to find the shortest distance between `i` and the target color `c`.
The most straightforward approach would be: For each query containing index `i` and color `c`, find all occurrences of `c` in the array. For each occurrence, calculate the distance between it and index `i`. Return the shortest distance found.

However, the above approach wastes time going through colors that are not `c`.
To solve this, we could begin by initializing three lists; one for each color. We could then iterate over `colors`, putting each index into its respective color list. Then when we go through the list of queries, we only need to look at the list that corresponds with `c`. The cleanest way of storing these lists would be to use a hashmap; the keys are colors, and the values are lists.



![Slide 1](images/slideshow_1182_approach_1_1182-Page-1.png)

![Slide 2](images/slideshow_1182_approach_1_1182-Page-2.png)

![Slide 3](images/slideshow_1182_approach_1_1182-Page-3.png)

![Slide 4](images/slideshow_1182_approach_1_1182-Page-4.png)



We've made a big improvement - but don't stop here - we can make it even better! The fact is, we don't have to scan an entire list for the given query containing `i` and `c`;
the values in each list are sorted, because we inserted the indexes in order, from `0` to `n`.
Therefore, we can use a binary search to find the value nearest to `i`. Using binary search improves the time complexity from linear to logarithmic.

**Algorithm**

- Initialize a hashmap to map each color to a list of indexes.
- Iterate over `colors` and put each index into its corresponding list of the hashmap.
- For each query containing `i` and `c`:
  - if `c` is not one of the keys in the hashmap, then we know that `colors` does not contain `c` and therefore should return `-1` as stated in the problem description;
  - else, we want to find the position of `i` in its corresponding color list `indexList` to maintain the sorted order:
    - if `i` is smaller than all elements in `indexList`, then `i - indexList[0]` is the shortest distance;
    - else if `i` is larger than all elements in the color list, then `indexList[indexList.size() - 1] - i` is the shortest distance;
    - else, the nearest occurrence of `c` to `i` is either at the insertion index, or the one before it, and so we calculate the distance from `i` to each of them, and return the smallest.

> **Interview Tip:** It can be challenging to know whether you should implement the binary search algorithm yourself, or whether you should use the built-in one. Some interviewers will want you to implement it, as that is a part of what they're evaluating you on. Others might expect you to use the built-in one, as writing your own is often seen as poor *software engineering* practice.
To be on the safe side, we recommend that you ask your interviewer *whether or not it's okay for you to use the built-in* binary search. If they say it's your choice, then we recommend using the built-in binary search, as that is considered best practice in software engineering.
To learn more about implementing binary search, [check out our explore card](https://leetcode.com/explore/learn/card/binary-search/)


```python
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list)
        for i,c in enumerate(colors):
            hashmap[c].append(i)

        query_results = []
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                query_results.append(-1)
                continue

            index_list = hashmap[color]
            # use bisect from Python standard library
            # more details: https://docs.python.org/3/library/bisect.html
            insert = bisect.bisect_left(index_list, target)

            # compare the index on the left and right of insert
            # make sure it will not fall out of the index_list
            left_nearest = abs(index_list[max(insert - 1, 0)] - target)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - target)
            query_results.append(min(left_nearest, right_nearest))

        return query_results
```


**Complexity Analysis**

* Time Complexity : $$\mathcal{O}(Q \log N + N)$$, where $Q$ is the length of `queries` and $N$ is the length of `colors`.

  Going through the input array `colors` and storing each `color - index` pair take $$\mathcal{O}(N)$$ time. When iterating `queries` and generating results, we apply binary search once for each query, and each binary search takes $$\mathcal{O}(\log N)$$, which results in $$\mathcal{O}(Q \log N)$$. Putting them together and ignoring constants for Big O notation, we have $$\mathcal{O}(Q \log N + N)$$.
* Space Complexity : $$\mathcal{O}(N)$$.
This is because we store the indexes of each `color - index` pair in a hashmap.

<br/>

---

### Approach 2: Pre-computed

**Intuition**

Another approach is to pre-compute and store the shortest distance between each index `i` and each color `c` so that, for each query, we can then return the answer in constant time.

To find the shortest distance between `i` and `c`, we divide it into two steps: firstly find the nearest `c` on `i`'s left; secondly, find the nearest `c` on `i`'s right.
The minimum of these is the shortest distance.


An important fact is that, if `color[i]` and `color[j]` are `c` when `i<j` and there's no `c` between `i` and `j`, then for each index `k` between `i` and `j`:
- the shortest distance between `k` and `c` on its *left* is `k-i`.
- the shortest distance between `k` and `c` on its *right* is `j-k`.

![Nearest color to the index.](images/1182-5.png)


*Figure 1. Find the nearest color on the left and right.*


Therefore, we can find the nearest target color in two separate phases:
- Iterating **from left to right** and looking **forwards** to find the nearest target color on the **left**.
- Iterating **from right to left** and looking **backwards** to find the nearest target color on the **right**.

Please don't hesitate to look at the visualizations below. Looking left (forwards) and right (backwards) are quite similar therefore I've put them sequentially for your reference.



![Slide 1](images/slideshow_1182_approach_2_1182-Page-7.png)

![Slide 2](images/slideshow_1182_approach_2_1182-Page-8.png)

![Slide 3](images/slideshow_1182_approach_2_1182-Page-9.png)

![Slide 4](images/slideshow_1182_approach_2_1182-Page-10.png)

![Slide 5](images/slideshow_1182_approach_2_1182-Page-11.png)

![Slide 6](images/slideshow_1182_approach_2_1182-Page-12.png)

![Slide 7](images/slideshow_1182_approach_2_1182-Page-14.png)

![Slide 8](images/slideshow_1182_approach_2_1182-Page-15.png)

![Slide 9](images/slideshow_1182_approach_2_1182-Page-16.png)

![Slide 10](images/slideshow_1182_approach_2_1182-Page-17.png)

![Slide 11](images/slideshow_1182_approach_2_1182-18.png)

![Slide 12](images/slideshow_1182_approach_2_1182-19.png)

![Slide 13](images/slideshow_1182_approach_2_1182-20.png)

![Slide 14](images/slideshow_1182_approach_2_1182-21.png)

![Slide 15](images/slideshow_1182_approach_2_1182-22.png)

![Slide 16](images/slideshow_1182_approach_2_1182-23.png)

![Slide 17](images/slideshow_1182_approach_2_1182-24.png)

![Slide 18](images/slideshow_1182_approach_2_1182-25.png)



**Algorithm**


```python
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # initializations
        n = len(colors)
        rightmost = [0, 0, 0]
        leftmost = [n - 1, n - 1, n - 1]

        distance = [[-1] * n for _ in range(3)]

        # looking forward
        for i in range(n):
            color = colors[i] - 1
            for j in range(rightmost[color], i + 1):
                distance[color][j] = i - j
            rightmost[color] = i + 1

        # looking backward
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(leftmost[color], i - 1, -1):
                # if the we did not find a target color on its right
                # or we find out that a target color on its left is
                # closer to the one on its right
                if distance[color][j] == -1 or distance[color][j] > j - i:
                    distance[color][j] = j - i
            leftmost[color] = i - 1

        return [distance[color - 1][index] for index,color in queries]
```



**Complexity Analysis**

* Time Complexity : $$\mathcal{O}(N + Q)$$, where $N$ is the length of `colors` and $Q$ is the length of `queries`.

  This is because we use iterations to fill `distance` which is a matrix of 3 rows and  $N$ columns taking $$\mathcal{O}(N)$$ time. Afterwards, we generate the answer for each query in `queries` in $$\mathcal{O}(1)$$.
* Space Complexity : $$\mathcal{O}(N)$$.
This is because we initialize two arrays of size 3 and one 2D array of 3 rows and $N$ columns.
<br/>

---