[TOC]

---
### Approach #1: Insert Each Character [Accepted]

**Intuition**

We can write out each character in the string `S` one by one.

As we write characters, we can update `(lines, width)` that keeps track of how many lines we have used, and what is the length of the used space in the last line.

**Algorithm**

If the space `w` of the next character in `S` fits our current line, we will add it.  Otherwise, we will start a new line, and use `w` space to put that character on the next line.


```python
class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width
```


**Complexity Analysis**

* Time Complexity:  $$O(S\text{.length})$$, as we iterate through `S`.

* Space Complexity: $$O(1)$$ additional space, as we only use `lines` and `width`.  (In Java, our `toCharArray` method makes this $$O(S\text{.length})$$, but we could use `.charAt` instead).