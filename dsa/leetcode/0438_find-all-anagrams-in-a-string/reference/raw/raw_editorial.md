[TOC]

## Solution

--- 

### Solution Template

![traversal](images/snake3.png)

This is a problem of multiple pattern searches in a string. All such problems usually could be solved by a sliding window approach in a linear time. The challenge here is how to implement a constant-time slice to fit into this linear time. 

If the patterns are not known in advance, i.e. it's a "find duplicates" problem, one could use one of two ways to implement constant-time slice: Bitmasks or Rabin-Karp. Please check the article [Repeated DNA Sequences](https://leetcode.com/articles/repeated-dna-sequences/) for a detailed comparison of these two algorithms. 

Here the situation is more simple: patterns are known in advance, and the set of characters in the patterns is very limited as well: 26 lowercase English letters. Hence one could allocate an array or hashmap with 26 elements and use it as a letter counter in the sliding window. 

![traversal](images/anagrams2.png)
<br />
<br />


---
### Approach 1: Sliding Window with HashMap

Let's start from the simplest approach: sliding window + two counter hashmaps `letter -> its count`. The first hashmap is a reference counter `pCount` for string `p`, and the second one is a counter `sCount` for a string in the sliding window.

The idea is to move the sliding window along the string `s`, recompute the second hashmap `sCount` in a constant time, and compare it with the first hashmap `pCount`. If `sCount == pCount`, then the string in the sliding window is a permutation of string `p`, and one could add its start position in the output list. 

**Algorithm**

- Build reference counter `pCount` for string `p`. 

- Move the sliding window along the string `s`:

    - Recompute sliding window counter `sCount` at each step by adding one letter on the right and removing one letter on the left. 
    
    - If `sCount == pCount`, update the output list.
    
- Return output list.   

**Implementation**



![Slide 1](images/slideshow_438_LIS_438_slid_1.png)

![Slide 2](images/slideshow_438_LIS_438_slid_2.png)

![Slide 3](images/slideshow_438_LIS_438_slid_3.png)

![Slide 4](images/slideshow_438_LIS_438_slid_4.png)

![Slide 5](images/slideshow_438_LIS_438_slid_5.png)

![Slide 6](images/slideshow_438_LIS_438_slid_6.png)

![Slide 7](images/slideshow_438_LIS_438_slid_7.png)

![Slide 8](images/slideshow_438_LIS_438_slid_8.png)

![Slide 9](images/slideshow_438_LIS_438_slid_9.png)




```python
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()
        
        output = []

        # sliding window on the string s
        for i in range(ns):
            # Add one more letter 
            # on the right side of the window
            s_count[s[i]] += 1

            # Remove one letter 
            # from the left side of the window
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # Compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
```


**Complexity Analysis**

Let $$N_s$$ and $$N_p$$ be the length of `s` and `p` respectively. Let $$K$$ be the maximum possible number of distinct characters. In this problem, $$K$$ equals $$26$$ because `s` and `p` consist of lowercase English letters.

* Time complexity: $$O(N_s)$$

  We perform one pass along each string when $$N_s \geq N_p$$ which costs $$O(N_s + N_p)$$ time.  Since we only perform this step when $$N_s \geq N_p$$ the time complexity simplifies to $$O(N_s)$$. 

* Space complexity: $$O(K)$$

  `pCount` and `sCount` will contain at most $$K$$ elements each. Since $$K$$ is fixed at $$26$$ for this problem, this can be considered as $$O(1)$$ space.
  
<br /> 
<br />


---
### Approach 2: Sliding Window with Array

**Algorithm**

Hashmap is quite complex structure, 
[with known performance issues in Java](https://github.com/vavr-io/vavr/issues/571).
Let's implement approach 1 using 26-elements array instead of hashmap: 

- Element number 0 contains count of letter `a`.

- Element number 1 contains count of letter `b`.

- ...

- Element number 25 contains count of letter `z`.

**Algorithm**

- Build reference array `pCount` for string `p`. 

- Move sliding window along the string `s`:

    - Recompute sliding window array `sCount` at each step by adding 
    one letter on the right and removing one letter on the left. 
    
    - If `sCount == pCount`, update the output list.
    
- Return output list. 

**Implementation**


```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output
```


**Complexity Analysis**

Let $$N_s$$ and $$N_p$$ be the length of `s` and `p` respectively. Let $$K$$ be the maximum possible number of distinct characters. In this problem, $$K$$ equals $$26$$ because `s` and `p` consist of lowercase English letters.

* Time complexity: $$O(N_s)$$

  We perform one pass along each string when $$N_s \geq N_p$$ which costs $$O(N_s + N_p)$$ time.  Since we only perform this step when $$N_s \geq N_p$$ the time complexity simplifies to $$O(N_s)$$. 

* Space complexity: $$O(K)$$

  `pCount` and `sCount` contain $$K$$ elements each. Since $$K$$ is fixed at $$26$$ for this problem, this can be considered as $$O(1)$$ space.
  
<br /> 
<br />