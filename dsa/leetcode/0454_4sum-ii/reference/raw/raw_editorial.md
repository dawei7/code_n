[TOC]

## Solution

### Overview

This problem is a variation of [4Sum](https://leetcode.com/articles/4sum/), and we recommend checking that problem first. The main difference is that here we pick each element from a different array, while in 4Sum all elements come from the same array. For that reason, we cannot use the [Two Pointers](https://leetcode.com/articles/4sum/#approach-1-two-pointers) approach, where elements must be in the same sorted array.

On the bright side, we do not need to worry about using the same element twice - we pick one element at a time from each array. As you will see later, this help reduce the time complexity.

Finally, we do not need to return actual values and ensure they are unique; we just count each combination of four elements that sums to zero.

---

### Approach 1: Hashmap

A brute force solution will be to enumerate all combinations of elements using four nested loops, which results in $\mathcal{O}(n^4)$ time complexity. A faster approach is to use three nested loops, and, for each sum `a + b + c`, search for a complementary value `d == -(a + b + c)` in the fourth array. We can do the search in $\mathcal{O}(1)$ if we populate the fourth array into a hashmap.

> Note that we need to track the frequency of each element in the fourth array. If an element is repeated multiple times, it will form multiple quadruples. Therefore, we will use hashmap values to store counts.

Building further on this idea, we can observe that `a + b == -(c + d)`. First, we will count sums of elements `a + b` from the first two arrays using a hashmap. Then, we will enumerate elements from the third and fourth arrays, and search for a complementary sum `a + b == -(c + d)` in the hashmap.



![Slide 1](images/slideshow_454_4Sum_II_454-1.png)

![Slide 2](images/slideshow_454_4Sum_II_454-2.png)

![Slide 3](images/slideshow_454_4Sum_II_454-3.png)

![Slide 4](images/slideshow_454_4Sum_II_454-4.png)

![Slide 5](images/slideshow_454_4Sum_II_454-5.png)

![Slide 6](images/slideshow_454_4Sum_II_454-6.png)

![Slide 7](images/slideshow_454_4Sum_II_454-7.png)

![Slide 8](images/slideshow_454_4Sum_II_454-8.png)



#### Algorithm

1. For each `a` in `A`.
    - For each `b` in `B`.
        - If `a + b` exists in the hashmap `m`, increment the value.
        - Else add a new key `a + b` with the value `1`.

2. For each `c` in `C`.
    - For each `d` in `D`.
        - Lookup key `-(c + d)` in the hashmap `m`.
        - Add its value to the count `cnt`.

3. Return the count `cnt`.

#### Implementation


```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = 0
        m = collections.defaultdict(int)
        for a in A:
            for b in B:
                m[a + b] += 1
                
        for c in C:
            for d in D:
                cnt += m[-(c + d)]
                
        return cnt
```


#### Complexity Analysis

- Time Complexity: $\mathcal{O}(n^2)$. We have 2 nested loops to count sums, and another 2 nested loops to find complements.

- Space Complexity: $\mathcal{O}(n^2)$ for the hashmap. There could be up to $\mathcal{O}(n^2)$ distinct `a + b` keys.

---

### Approach 2: kSum II

After you solve 4Sum II, an interviewer can follow-up with 5Sum II, 6Sum II, and so on. What they are really expecting is a generalized solution for `k` input arrays. Fortunately, the hashmap approach can be easily extended to handle more than 4 arrays.

Above, we divided four arrays into two equal groups and processed each group independently. Same way, we will divide $k$ arrays into two groups. For the first group, we will have $\lfloor k/2 \rfloor$ nested loops to count sums. Another $\lceil k/2 \lceil$ nested loops will enumerate arrays in the second group to count sums as before. Finally, we count the pairs from the two groups with sums as 0.

#### Algorithm

1. Initialize the final result count `res` as 0.
2. Divide the $k$ given arrays into two groups:
    - `left`: the first $\lfloor k/2 \rfloor$ arrays
    - `right`: the rest $\lceil k/2 \lceil$ arrays
3. Enumerate within each group, count the sums of tuples that pick exactly one number from each array in the group. Now, we have the sums of all possible tuples within `left` and `right` respectively.
4. For each sum `s` in group `left`, multiple the count with the number of how many `-s` are counted in group `right`, and add the product to our final result. 

#### Implementation


```python
from collections import Counter


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        def sum_count(lsts: List[List[int]]) -> Counter:
            res = Counter({0: 1})
            for lst in lsts:
                temp = Counter()
                for a in lst:
                    for total in res:
                        temp[total + a] += res[total]
                res = temp
            return res

        lsts = [A, B, C, D]
        k = len(lsts)
        left, right = sum_count(lsts[:k//2]), sum_count(lsts[k//2:])
        return sum(left[s]*right[-s] for s in left)
```


#### Complexity Analysis

- Time Complexity: $\mathcal{O}(n^{\lceil k/2 \rceil})$, or $\mathcal{O}(n^2)$ for 4Sum II. We have to enumerate over at most $n^{\lfloor k/2 \rfloor}$ sums in the left group and $n^{\lceil k/2 \rceil}$ sums in the right group. Finally, we just need to check $\mathcal{O}{n^{\lfloor k/2 \rfloor}}$ sums in the left group and search if their negated number exists in the right group.

- Space Complexity: $\mathcal{O}(n^{\lceil k/2 \rceil})$, similarly, we create a HashMap for each group to store all sums, which contains at most $n^{\lceil k/2 \rceil}$ keys.

---

### Further Thoughts

For an interview, keep in mind the generalized implementation. Even if your interviewer is OK with a simpler code, you'll get some extra points by describing how your solution can handle more than 4 arrays.

It's also important to discuss trade-offs with your interviewer. If we are tight on memory, we can move some arrays from the first group to the second. This, of course, will increase the time complexity.

In other words, the time complexity can range from $\mathcal{O}(n^k)$ to $\mathcal{O}(n^{k/2})$, and the memory complexity ranges from $\mathcal{O}(1)$ to $\mathcal{O}(n^{k/2})$ accordingly.