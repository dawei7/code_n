[TOC]

## Solution

---

#### Intuition

First we should make sure we understand what "lexicographical order" means. Comparing strings doesn't work the same way as comparing numbers. Strings are compared from the first character to the last one. Which string is greater depends on the comparison between _the first unequal corresponding character_ in the two strings. As a result any string beginning with `a` will always be less than any string beginning with `b`, regardless of the ends of both strings. 

Because of this, the optimal solution will have _the smallest characters as early as possible_. We draw two conclusions that provide different methods of solving this problem in $$O(N)$$:

1. The leftmost letter in our solution will be the smallest letter such that the suffix from that letter contains every other. This is because we know that the solution must have one copy of every letter, and we know that the solution will have the lexicographically smallest leftmost character possible.

    If there are multiple smallest letters, then we pick the leftmost one simply because it gives us more options. We can always eliminate more letters later on, so the optimal solution will always remain in our search space.

2. As we iterate over our string, if character `i` is greater than character `i+1` and another occurrence of character `i` exists later in the string, deleting character `i` will **always** lead to the optimal solution. Characters that come later in the string `i` don't matter in this calculation because `i` is in a more significant spot. Even if character `i+1` isn't the best yet, we can always replace it for a smaller character down the line if possible.

Since we try to remove characters as early as possible, and picking the best letter at each step leads to the best solution, "greedy" should be going off like an alarm.  

---

### Approach 1: Greedy - Solving Letter by Letter

**Algorithm**

We use idea number one from the intuition. In each iteration, we determine leftmost letter in our solution. This will be **the smallest character such that its suffix contains at least one copy of every character in the string**. We determine the rest of our answer by recursively calling the function on the suffix we generate from the original string (leftmost letter is removed).


**Implementation**

```python
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            c[s[i]] -=1
            if c[s[i]] == 0: break
        # our answer is the leftmost letter plus the recursive call on the remainder of the string
        # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

```


Note that the code in this section is a translated / commented version of the code [in this post](https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution) originally written by [lixx2100](https://leetcode.com/lixx2100/).

**Complexity Analysis**

* Time complexity : $$O(N)$$. Each recursive call will take $$O(N)$$. The number of recursive calls is bounded by a constant (26 letters in the alphabet), so we have $$O(N) * C = O(N)$$.

* Space complexity : $$O(N)$$. Each time we slice the string we're creating a new one (strings are immutable). The number of slices is bound by a constant, so we have $$O(N) * C = O(N)$$.


---
### Approach 2: Greedy - Solving with Stack

**Algorithm**

We use idea number two from the intuition. We will keep a stack to store the solution we have built as we iterate over the string, and we will delete characters off the stack whenever it is possible and it makes our string smaller.

Each iteration we add the current character to the solution if it hasn't already been used. We try to remove as many characters as possible off the top of the stack, and then add the current character

The conditions for deletion are:

1. The character is greater than the current characters
2. The character can be removed because it occurs later on

At each stage in our iteration through the string, we greedily keep what's on the stack as small as possible.

The following animation makes this more clear:



![Slide 1](images/slideshow_316_remove_duplicate_letters_1.png)

![Slide 2](images/slideshow_316_remove_duplicate_letters_2.png)

![Slide 3](images/slideshow_316_remove_duplicate_letters_3.png)

![Slide 4](images/slideshow_316_remove_duplicate_letters_4.png)

![Slide 5](images/slideshow_316_remove_duplicate_letters_5.png)

![Slide 6](images/slideshow_316_remove_duplicate_letters_6.png)

![Slide 7](images/slideshow_316_remove_duplicate_letters_7.png)

![Slide 8](images/slideshow_316_remove_duplicate_letters_8.png)

![Slide 9](images/slideshow_316_remove_duplicate_letters_9.png)

![Slide 10](images/slideshow_316_remove_duplicate_letters_10.png)

![Slide 11](images/slideshow_316_remove_duplicate_letters_11.png)

![Slide 12](images/slideshow_316_remove_duplicate_letters_12.png)



**Implementation**

```python
class Solution:
    def removeDuplicateLetters(self, s) -> str:

        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}


        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)

```


**Complexity Analysis**

* Time complexity : $$O(N)$$. Although there is a loop inside a loop, the time complexity is still $$O(N)$$. This is because the inner while loop is bounded by the total number of elements added to the stack (each time it fires an element goes). This means that the _total_ amount of time spent in the inner loop is bounded by $$O(N)$$, giving us a total time complexity of $$O(N)$$

* Space complexity : $$O(1)$$. At first glance it looks like this is $$O(N)$$, but that is not true! `seen` will only contain unique elements, so it's bounded by the number of characters in the alphabet (a constant). You can only add to `stack` if an element has not been seen, so `stack` also only consists of unique elements. This means that _both_ `stack` and `seen` are bounded by constant, giving us $$O(1)$$ space complexity.