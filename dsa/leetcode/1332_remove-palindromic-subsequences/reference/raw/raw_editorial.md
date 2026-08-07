[TOC]

## Solution

### Overview

If you're stuck on this question, don't worry, it has fooled many people! The algorithm that solves it is indeed very easy, and all the information you require is provided in the problem statement—you just need to read it very carefully and make sure you really understand the problem. This question is a great one for testing these important skills. So before reading the solution, make sure you look at the hints. Additionally, look very, very carefully at the examples, in particular example 3. It might make you realize you've made an incorrect assumption about the problem!

*Clarifying what is meant by a subsequence*

Let's start by making sure you're clear on the terminology around **subsequences**, as these terms come up a lot but can be confusing if you're not very familiar with them. If you're ever in doubt in an interview about what is being asked for, then ask the interviewer to clarify.

A **subsequence** is obtained by deleting some characters of the string. The **subsequence** is what's left, and doesn't have to be letters that were consecutive in the original string. For example, some of the subsequences of the word `computer` are:

- **co**~~m~~**p**~~uter~~ → **cop**
- ~~com~~**put**~~er~~ → **put**
- **co**~~m~~**p**~~ut~~**e**~~r~~ → **cope**
- **c**~~omp~~**ut**~~er~~ → **cut**
- ~~comput~~**e**~~r~~ → **e**
- computer → **computer**

Some of these are *also* what we call a **substring**. A **substring** is where the characters *are* consecutive in the original string. The subsequences above that are also substrings of `computer` are `put`, `e` and `computer`.

A **substring** is a type of **subsequence**, but a **subsequence** is *not* a type of **substring**. This also means that if the word **substring** is used, then you know for sure what it means, but if the word **subsequence** is used then you might need to ask for clarification, because it could be either. So in an interview, if you're asked to find **subsequences**, then clarify with the interviewer whether or not those subsequences have to also be substrings.

Here on Leetcode, either the problem statement will clarify what is intended, or at least one of the examples will.

For this question, the subsequence does *not* need to be consecutive. We can determine this by looking closely at example 3.

*Coming up with an algorithm*

A palindrome is a word that reads the same from front to back. For example, `lol`, `radar`, `a`, and `oooo`. We need to remove palindromic subsequences from the given string until it's empty, and we need to minimize how many of these removals we do.

The key observation to make is that any sequence of the same letter is a palindrome. For example `a`, `aa`, `aaa`, `aaaaaaaa`, etc. Because there are only 2 unique letters that can appear in the string, we know we can *always* solve the problem with at most 2 steps. i.e.

1. Remove all the `a`'s as a single palindromic subsequence.
2. Remove all the `b`'s as a single palindromic subsequence.

This leaves us with only 3 possible answers for any given string: `0`, `1`, or `2`. We will need to classify each string we're given into one of these 3 categories. If you haven't yet solved the problem, have another think about how you could do this before you read on.

An answer of `0` would mean we didn't need to remove any subsequences. The only case we don't need to remove any subsequences is when the string is empty to begin with. Therefore, the first part of algorithm should be:

```
if s is an empty string:
    return 0
```

Now, what about `1`? This would mean we only need to remove a single palindromic subsequence to get to an empty string. The only way this is possible is if the entire string is a palindrome.

```
if s is a palindrome:
    return 1
```

That leaves `2`. If the input string is non-empty, and it is not a palindrome, then we would have to firstly remove the `a`'s and then secondly remove the `b`'s. So if neither of the first 2 cases apply, we can simply return 2.

```
return 2
```

The first and third cases are straightforward, but the second case will require us to write some more code to check if `s` is a palindrome. The only difference between the approaches discussed below is how this palindrome check is done.

<br />

---

### Approach 1: Palindrome Check by Reversing String

**Intuition**

A palindrome is simply a string that reads the same backwards as it does forwards. i.e. if you reverse the letters in the string, you'll still have the same word. Therefore, the simplest way to check if a string is a palindrome is to reverse it. We can do the reversing using library functions.

**Algorithm**

*For Python programmers*: `s[::-1]` is the simplest way of reversing a string.

*For Java programmers*: there is no really simple way of reversing a `String`. Instead, you'll need to convert the `String` into a `StringBuilder` (a mutable string), reverse it, and then convert it back into a `String`.


```python
def removePalindromeSub(self, s: str) -> int:
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    return 2
```


For the Java code, you can also do the string reversing as a one-liner. This is a common pattern.


```java
class Solution {
    public int removePalindromeSub(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        String reversedString = new StringBuilder(s).reverse().toString();
        if (reversedString.equals(s)) {
            return 1;
        }
        return 2;
    }
}
```


**Complexity Analysis**

Let $$n$$ be the length of the input string.

- Time Complexity : $$O(n)$$.

    Reversing a string using the library methods above has a cost of $$O(n)$$. Checking if 2 strings are equal is also $$O(n)$$. Therefore, the overall function is $$O(n)$$.

    Be careful about doing the reversing yourself. Many naïve string reversing algorithms people write actually have a cost of $$O(n^2)$$.

- Space Complexity : $$O(n)$$.

    Reversing a string creates a second string the same length as the first. Therefore, this algorithm requires $$O(n)$$ space.

To learn about writing good algorithms to reverse a string, check out the [Solution Article for Reverse String](https://leetcode.com/problems/reverse-string/solution/).

<br />

---

### Approach 2: Palindrome Check with Two-Pointer Technique

**Intuition**

The approach above solved the problem, but it required $$O(n)$$ space. Another way of checking whether or not a string is a palindrome is to use the two-pointer technique.

**Algorithm**

For code readability, it's best to put the logic for checking whether or not a string is a palindrome into a separate function.


```python
def removePalindromeSub(self, s: str) -> int:
    def is_palindrome(s):
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    if not s:
        return 0
    if is_palindrome(s):
        return 1
    return 2
```



**Complexity Analysis**

Let $$n$$ be the length of the input string.

- Time Complexity : $$O(n)$$.

    The loop in the `isPalindrome(...)` function loops up to $$\frac{n}{2}$$ times, each time checking whether or not the characters at indexes `hi` and `lo` are equal. The division by `2` is treated as a constant so removed, and we're left with $$O(n)$$.

- Space Complexity : $$O(1)$$.

    We aren't creating any new data structures or string copies, so the total memory usage is $$O(1)$$.

This approach might not be considered as better than the first approach in practice though. While the space complexity is lower, (and the actual time taken will probably be lower by a constant amount too), the code is more complex and takes longer to write. If you knew $$n$$ was always going to be small, the first approach would be best.

<br />