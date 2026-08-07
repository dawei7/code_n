[TOC]

## Video Solution
---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/784616895" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>
</div>

## Solution Article

---

### Approach 1: Linear time solution

The best possible solution here could be of a linear time because to ensure that the character is unique you have to check the whole string anyway.

The idea is to go through the string and save in a hash map the number of times each character appears in the string. That would take $\mathcal{O}(N)$ time, where `N` is the number of characters in the string.

Then we go through the string the second time, this time we use the hash map as a reference to check if a character is unique or not. If the character is unique, one could just return its index. The complexity of the second iteration is $\mathcal{O}(N)$ as well.

![Slide 1](images/slideshow_387_LIS_387_slide_1.png)

![Slide 2](images/slideshow_387_LIS_387_slide_2.png)

![Slide 3](images/slideshow_387_LIS_387_slide_3.png)

![Slide 4](images/slideshow_387_LIS_387_slide_4.png)

![Slide 5](images/slideshow_387_LIS_387_slide_5.png)

![Slide 6](images/slideshow_387_LIS_387_slide_6.png)

![Slide 7](images/slideshow_387_LIS_387_slide_7.png)

![Slide 8](images/slideshow_387_LIS_387_slide_8.png)

![Slide 9](images/slideshow_387_LIS_387_slide_9.png)

![Slide 10](images/slideshow_387_LIS_387_slide_10.png)

![Slide 11](images/slideshow_387_LIS_387_slide_11.png)

![Slide 12](images/slideshow_387_LIS_387_slide_12.png)

![Slide 13](images/slideshow_387_LIS_387_slide_13.png)

![Slide 14](images/slideshow_387_LIS_387_slide_14.png)

![Slide 15](images/slideshow_387_LIS_387_slide_15.png)

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map: character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
```

**Complexity Analysis**

* Time complexity: $\mathcal{O}(N)$ since we go through the string of length `N` two times.
* Space complexity: $\mathcal{O}(1)$ because English alphabet contains 26 letters.