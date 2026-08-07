[TOC]

## Solution

--- 

### Overview

One could solve the problem using built-in functions. 


```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
```


Since these functions are well-known, most probably the interviewees will ask to implement them. In this article we will consider two solutions:

- Usage of hashmap `A --> a, B --> b, ..., Z --> z`.

- Implementation of Python function `lower`, which uses the fact that the ASCII code of a small letter is equal to the ASCII code of the corresponding capital letter + $$2^5$$.

<br /> 
<br />


---
### Approach 1: HashMap

**Algorithm**

- Build hashmap uppercase letter --> lowercase letter.

- Parse the string. If the current character is an uppercase letter, _i.e._ it's in the hashmap, then replace it with the hashmap value. Otherwise, keep it unchanged.

![fig](images/hashmap.png)

**Implementation**


```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))
        
        return ''.join([h[x] if x in h else x for x in s])
```


**Complexity Analysis**

* Time complexity: $$O(N)$$ to parse the input string. 

* Space complexity: $$O(N)$$ to keep the output.
<br /> 
<br />


---
### Approach 2: Implementation of Python Function lower

Let's reproduce the [implementation of Python function `lower`](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Objects/unicodectype.c#L223).

For that, we need two functions.

The first one, `is_upper`, simply checks if the character is between `A` and `Z` characters.

The second one, `to_lower`, should convert the uppercase letter into the corresponding lowercase one. 

> It's based on the fact that the ASCII code of a small letter is equal to the ASCII code of the corresponding capital letter + $$2^5$$: `ord('a') = ord('A') + 32`, or `ord('a') = ord('A') | 32`.

![fig](images/shift.png)

**Implementation**



![Slide 1](images/slideshow_709_LIS_709_slide_2.png)

![Slide 2](images/slideshow_709_LIS_709_slide_3.png)

![Slide 3](images/slideshow_709_LIS_709_slide_4.png)

![Slide 4](images/slideshow_709_LIS_709_slide_5.png)

![Slide 5](images/slideshow_709_LIS_709_slide_6.png)

![Slide 6](images/slideshow_709_LIS_709_slide_7.png)

![Slide 7](images/slideshow_709_LIS_709_slide_8.png)

![Slide 8](images/slideshow_709_LIS_709_slide_9.png)

![Slide 9](images/slideshow_709_LIS_709_slide_10.png)

![Slide 10](images/slideshow_709_LIS_709_slide_11.png)




```python
class Solution:
    def toLowerCase(self, s: str) -> str: 
        is_upper = lambda x : 'A' <= x <= 'Z'
        to_lower = lambda x : chr(ord(x) | 32)
        
        return ''.join([to_lower(x) if is_upper(x) else x for x in s])
```


**Complexity Analysis**

* Time complexity: $$O(N)$$ to parse the input string. 

* Space complexity: $$O(N)$$ to keep the output.
<br /> 
<br />