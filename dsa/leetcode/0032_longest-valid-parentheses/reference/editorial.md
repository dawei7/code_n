[TOC]
## Summary

We need to determine the length of the largest valid substring of parentheses from a given string.

## Solution
---
### Approach 1: Brute Force

**Algorithm**

In this approach, we consider every possible non-empty even length substring from the given string and check whether it's
a valid string of parentheses or not. In order to check the validity, we use the Stack's Method.

Every time we
encounter a $\text{‘(’}$, we push it onto the stack. For every $\text{‘)’}$ encountered, we pop a $\text{‘(’}$ from the stack. If $\text{‘(’}$ isn't
 available on the stack for popping at anytime or if stack contains some elements after processing complete substring, the substring of parentheses is invalid. In this way, we repeat the
 process for every possible substring and we keep on
  storing the length of the longest valid string found so far.
```
Example:
"((())"

(( --> invalid
(( --> invalid
() --> valid, length=2
)) --> invalid
((()--> invalid
(())--> valid, length=4
maxlength=4
```

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append("(")
            elif stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if self.isValid(s[i:j]):
                    maxlen = max(maxlen, j - i)
        return maxlen
```

**Complexity Analysis**

* Time complexity: $O(n^3)$. Generating every possible substring from a string of length $n$ requires $O(n^2)$. Checking validity of a string of length $n$ requires $O(n)$.

* Space complexity: $O(n)$. A stack of depth $n$ will be required for the longest substring.
<br />
<br />
---

### Approach 2: Using Dynamic Programming

**Algorithm**

This problem can be solved by using Dynamic Programming. We make use of a $\text{dp}$ array where $i$th element of $\text{dp}$ represents the length of the longest valid substring ending at $i$th index. We initialize the complete $\text{dp}$ array with 0's. Now, it's obvious that the valid substrings must end with $\text{‘)’}$. This further leads to the conclusion that the substrings ending with $\text{‘(’}$ will always contain '0' at their corresponding $\text{dp}$ indices. Thus, we update the $\text{dp}$ array only when $\text{‘)’}$ is encountered.

To fill $\text{dp}$ array we will check every two consecutive characters of the string and if

1. $\text{s}[i] = \text{‘)’}$ and $\text{s}[i - 1] = \text{‘(’}$, i.e. string looks like $`.......()" \Rightarrow$

    $\text{dp}[i]=\text{dp}[i-2]+2$

    We do so because the ending "()" portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.

2. $\text{s}[i] = \text{‘)’}$ and $\text{s}[i - 1] = \text{‘)’}$, i.e. string looks like $`.......))" \Rightarrow$

    if $\text{s}[i - \text{dp}[i - 1] - 1] = \text{‘(’}$ then

    $\text{dp}[i]=\text{dp}[i-1]+\text{dp}[i-\text{dp}[i-1]-2]+2$

   The reason behind this is that if the 2nd last $\text{‘)’}$ was a part of a valid substring (say $sub_s$), for the last $\text{‘)’}$ to be a part of a larger substring, there must be a corresponding starting $\text{‘(’}$ which lies before the valid substring of which the 2nd last $\text{‘)’}$ is a part (i.e. before $sub_s$). Thus, if the character before $sub_s$ happens to be $\text{‘(’}$, we update the $\text{dp}[i]$ as an addition of $2$ in the length of $sub_s$ which is $\text{dp}[i-1]$. To this, we also add the length of the valid substring just before the term "(,sub_s,)" , i.e. $\text{dp}[i-\text{dp}[i-1]-2]$.

For better understanding of this method, see this example:

<!--![Longest_Valid_Parenthesis](images/32_LongestValidParenthesisDP.gif)-->

![Slide 1](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide1.JPG)

![Slide 2](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide2.JPG)

![Slide 3](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide3.JPG)

![Slide 4](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide4.JPG)

![Slide 5](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide5.JPG)

![Slide 6](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide6.JPG)

![Slide 7](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide7.JPG)

![Slide 8](images/slideshow_32_Longest_Valid2_32_Longest_Valid2Slide8.JPG)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = (
                        dp[i - 1]
                        + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
                        + 2
                    )
                maxans = max(maxans, dp[i])
        return maxans
```

**Complexity Analysis**

* Time complexity: $O(n)$. Single traversal of string to fill dp array is done.

* Space complexity: $O(n)$. dp array of size $n$ is used.
<br />
<br />

---

### Approach 3: Using Stack

**Algorithm**

Instead of finding every possible string and checking its validity, we can make use of a stack while scanning the given string to:

1. Check if the string scanned so far is valid.
2. Find the length of the longest valid string.

In order to do so, we start by pushing $-1$ onto the stack. For every $\text{‘(’}$ encountered, we push its index onto the stack.

For every $\text{‘)’}$ encountered, we pop the topmost element. Then, the length of the currently encountered valid string of parentheses will be the difference between the current element's index and the top element of the stack.

If, while popping the element, the stack becomes empty, we will push the current element's index onto the stack. In this way, we can continue to calculate the length of the valid substrings and return the length of the longest valid string at the end.

See this example for a better understanding.

<!--![Longest_Valid_Parenthesis](images/32_LongestValidParenthesisSTACK.gif)-->

![Slide 1](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide1.JPG)

![Slide 2](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide2.JPG)

![Slide 3](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide3.JPG)

![Slide 4](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide4.JPG)

![Slide 5](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide5.JPG)

![Slide 6](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide6.JPG)

![Slide 7](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide7.JPG)

![Slide 8](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide8.JPG)

![Slide 9](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide9.JPG)

![Slide 10](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide10.JPG)

![Slide 11](images/slideshow_32_Longest_Valid_stack_new_32_Longest_Valid1Slide11.JPG)

```python
# Python Solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans
```

**Complexity Analysis**

* Time complexity: $O(n)$. $n$ is the length of the given string.

* Space complexity: $O(n)$. The size of stack can go up to $n$.
<br />
<br />

---

### Approach 4: Without extra space

**Algorithm**

In this approach, we make use of two counters $left$ and $right$. First, we start traversing the string from the left towards the right and for every $\text{‘(’}$ encountered, we increment the $left$ counter and for every $\text{‘)’}$ encountered, we increment the $right$ counter. Whenever $left$ becomes equal to $right$, we calculate the length of the current valid string and keep track of maximum length substring found so far. If $right$ becomes greater than $left$ we reset $left$ and $right$ to $0$.

Next, we start traversing the string from right to left and similar procedure is applied.

Example of this approach:

<!--![Longest_Valid_Parenthesis](images/32_LongestValidParenthesisLR.gif)-->

![Slide 1](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide1.PNG)

![Slide 2](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide2.PNG)

![Slide 3](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide3.PNG)

![Slide 4](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide4.PNG)

![Slide 5](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide5.PNG)

![Slide 6](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide6.PNG)

![Slide 7](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide7.PNG)

![Slide 8](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide8.PNG)

![Slide 9](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide9.PNG)

![Slide 10](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide10.PNG)

![Slide 11](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide11.PNG)

![Slide 12](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide12.PNG)

![Slide 13](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide13.PNG)

![Slide 14](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide14.PNG)

![Slide 15](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide15.PNG)

![Slide 16](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide16.PNG)

![Slide 17](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide17.PNG)

![Slide 18](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide18.PNG)

![Slide 19](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide19.PNG)

![Slide 20](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide20.PNG)

![Slide 21](images/slideshow_32_Longest_Validlr_32_Longest_Valid3Slide21.PNG)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlength = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif left > right:
                left = right = 0
        return maxlength
```

**Complexity Analysis**

* Time complexity: $O(n)$. Two traversals of the string.

* Space complexity: $O(1)$. Only two extra variables $left$ and $right$ are needed.