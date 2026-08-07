[TOC]

## Solution

--- 

### Overview

Different interviewers would probably expect different approaches to this problem. The holy war question is whether to use or not use built-in methods. As you may notice, most of the design problems on Leetcode are voted down because of two main reasons:

1. There was no approach with built-in methods/data structures in the article.

2. One of the approaches in the article did contain built-in methods/data structures.

Seems like the community has no common opinion yet, and in practice that means an unpredictable interview experience for some sort of problem. 
 
Here we consider three different solutions for linear time and space complexity:

1. Use built-in split and reverse. Benefits: in-place in Python (in-place, but linear space complexity!) and the simplest one to write.  

2. The most straightforward one. Trim the whitespaces, reverse the whole string, and then reverse each word. Benefits: This could be done in place for the languages with mutable strings.

3. Two passes approach with a deque. Move along the string, word by word, and push each new word in front of the deque. Convert the deque back into a string. Benefits: two passes.

### Approach 1: Built-in Split + Reverse

![fig](images/fun2.png)

**Implementation**


```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$, where N is the number of characters in the input string.

* Space complexity: $$\mathcal{O}(N)$$, to store the result of split by spaces.

<br /> 
<br />


---
### Approach 2: Reverse the Whole String and Then Reverse Each Word

The implementation of this approach will be different for Java/Python (= immutable strings) and C++ (= mutable strings). 

In the case of immutable strings, one has first to convert the string into a mutable data structure, and hence it makes sense to trim all spaces during that conversion. 

![fig](images/reverse_whole2.png)

In the case of _mutable_ strings, there is no need to allocate an additional data structure, one could get all jobs done in-place. In such a case it makes sense to reverse words and trim spaces at the same time.

![fig](images/mutable2.png)

**Implementation**


```python
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != " ":
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return "".join(l)
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$.

* Space complexity: $$\mathcal{O}(N)$$.
<br /> 
<br />


---
### Approach 3: Deque of Words

![fig](images/deque2.png)

**Implementation**


```python
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$.

* Space complexity: $$\mathcal{O}(N)$$.