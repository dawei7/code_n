[TOC]

## Video Solution
---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/844727300" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>&nbsp;
</div>

## Solution Article

---

### Approach 1: Reverse the Whole String and Then Reverse Each Word

To have this problem in Amazon interview is a good situation since the input is a mutable structure and hence one could aim $$\mathcal{O}(1)$$ space solution without any technical difficulties.

> The idea is simple: reverse the whole string and then reverse each word. 

![fig](images/reverse.png)

**Algorithm**

Let's first implement two functions:

- `reverse(l: list, left: int, right: int)`, which reverses array characters between left and right pointers. C++ users could directly use built-in `std::reverse`. 

- `reverse_each_word(l: list)`, which uses two pointers to mark the boundaries of each word and the previous function to reverse it. 

Now `reverseWords(s: List[str])` implementation is straightforward:

- Reverse the whole string: `reverse(s, 0, len(s) - 1)`.

- Reverse each word: `reverse_each_word(s)`.

**Implementation**



![Slide 1](images/slideshow_186_LIS_186_slide_1.png)

![Slide 2](images/slideshow_186_LIS_186_slide_2.png)




```python
class Solution:
    def reverse(self, l: List[str], left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: List[str]) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)
        
        # reverse each word
        self.reverse_each_word(s)
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$, it's two passes along the string.

* Space complexity: $$\mathcal{O}(1)$$, it's a constant space solution.
<br /> 
<br />