[TOC]

## Video Solution
---

<div>
  <div class="video-container">
    <iframe src="https://player.vimeo.com/video/482204478" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
  </div>
</div>

<div>
</div>

## Solution Article

---

### Approach 1: Sliding Window

**Intuition**

To solve the problem in one pass let's use here _sliding window_ approach with two set pointers `left` and `right` serving as the window boundaries.

The idea is to set both pointers in the position `0` and then move `right` pointer to the right while the window contains not more than two distinct characters. If at some point we've got `3` distinct characters, let's move `left` pointer to keep not more than `2` distinct characters in the window.

![compute](images/sliding.png)

Basically, that's the algorithm: to move the sliding window along the string, to keep not more than `2` distinct characters in the window, and to update the max substring length at each step.

> There is just one more question to reply - how to move the left pointer to keep only `2` distinct characters in the string?

Let's use for this purpose a hashmap containing all characters in the sliding window as keys and their rightmost positions as values. At each moment, this hashmap could contain not more than `3` elements.

![compute](images/move_left.png)

For example, using this hashmap one knows that the rightmost position of character `e` in `"eeeeeeeet"` window is `8` and so one has to move `left` pointer in the position $8 + 1 = 9$ to exclude the character `e` from the sliding window.

Do we have here the best possible time complexity? Yes, we do - it's the only one who passes along the string with `N` characters and the time complexity is $\mathcal{O}(N)$.

**Algorithm**

Now one could write down the algortihm.

- Return `N` if the string length `N` is smaller than `3`.
- Set both set pointers at the beginning of the string $left = 0$ and $right = 0$ and init max substring length $\text{max}_{len} = 2$.
- While `right` pointer is less than `N`:
* If the hashmap contains less than `3` distinct characters, add the current character $s[right]$ in the hashmap and move `right` pointer to the right.
* If the hashmap contains `3` distinct characters, remove the leftmost character from the hashmap and move the `left` pointer so that the sliding window contains `2` distinct characters only.
* Update $\text{max}_{len}$.

**Implementation**

![Slide 1](images/slideshow_159_LIS_159_slide_1.png)

![Slide 2](images/slideshow_159_LIS_159_slide_2.png)

![Slide 3](images/slideshow_159_LIS_159_slide_3.png)

![Slide 4](images/slideshow_159_LIS_159_slide_4.png)

![Slide 5](images/slideshow_159_LIS_159_slide_5.png)

![Slide 6](images/slideshow_159_LIS_159_slide_6.png)

![Slide 7](images/slideshow_159_LIS_159_slide_7.png)

![Slide 8](images/slideshow_159_LIS_159_slide_8.png)

![Slide 9](images/slideshow_159_LIS_159_slide_9.png)

![Slide 10](images/slideshow_159_LIS_159_slide_10.png)

![Slide 11](images/slideshow_159_LIS_159_slide_11.png)

![Slide 12](images/slideshow_159_LIS_159_slide_12.png)

![Slide 13](images/slideshow_159_LIS_159_slide_13.png)

![Slide 14](images/slideshow_159_LIS_159_slide_14.png)

![Slide 15](images/slideshow_159_LIS_159_slide_15.png)

![Slide 16](images/slideshow_159_LIS_159_slide_16.png)

![Slide 17](images/slideshow_159_LIS_159_slide_17.png)

![Slide 18](images/slideshow_159_LIS_159_slide_18.png)

![Slide 19](images/slideshow_159_LIS_159_slide_19.png)

![Slide 20](images/slideshow_159_LIS_159_slide_20.png)

![Slide 21](images/slideshow_159_LIS_159_slide_21.png)

![Slide 22](images/slideshow_159_LIS_159_slide_22.png)

![Slide 23](images/slideshow_159_LIS_159_slide_23.png)

![Slide 24](images/slideshow_159_LIS_159_slide_24.png)

![Slide 25](images/slideshow_159_LIS_159_slide_25.png)

![Slide 26](images/slideshow_159_LIS_159_slide_26.png)

![Slide 27](images/slideshow_159_LIS_159_slide_27.png)

![Slide 28](images/slideshow_159_LIS_159_slide_28.png)

![Slide 29](images/slideshow_159_LIS_159_slide_29.png)

```python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # when the slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ where `N` is the number of characters in the input string.

* Space complexity: $\mathcal{O}(1)$ since additional space is used only for a hashmap with at most `3` elements.

**Problem generalization**

The same sliding window approach could be used to solve the generalized problem :

[Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)