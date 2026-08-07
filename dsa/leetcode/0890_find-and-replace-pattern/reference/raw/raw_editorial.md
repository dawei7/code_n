[TOC]

## Solution
---
### Approach 1: Two Maps

**Intuition and Algorithm**

If say, the first letter of the pattern is `"a"`, and the first letter of the word is `"x"`, then in the permutation, `"a"` must map to `"x"`.

We can write this bijection using two maps: a forward map $$\text{m1}$$ and a backwards map $$\text{m2}$$.

$$
\text{m1} : \text{"a"} \rightarrow \text{"x"}
$$
$$
\text{m2} : \text{"x"} \rightarrow \text{"a"}
$$

Then, if there is a contradiction later, we can catch it via one of the two maps.  For example, if the `(word, pattern)` is `("aa", "xy")`, we will catch the mistake in $$\text{m1}$$ (namely, $$\text{m1}(\text{"a"}) = \text{"x"} = \text{"y"}$$).  Similarly, with `(word, pattern) = ("ab", "xx")`, we will catch the mistake in $$\text{m2}$$.


```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
```


**Complexity Analysis**

* Time Complexity:  $$O(N * K)$$, where $$N$$ is the number of words, and $$K$$ is the length of each word.

* Space Complexity:  $$O(N * K)$$, the space used by the answer.
<br />
<br />


---
### Approach 2: One Map

**Intuition and Algorithm**

As in *Approach 1*, we can have some forward map $$\text{m1} : \mathbb{L} \rightarrow \mathbb{L}$$, where $$\mathbb{L}$$ is the set of letters.  

However, instead of keeping track of the reverse map $$\text{m2}$$, we could simply make sure that every value $$\text{m1}(x)$$ in the codomain is reached at most once.  This would guarantee the desired permutation exists.

So our algorithm is this: after defining $$\text{m1}(x)$$ in the same way as *Approach 1* (the forward map of the permutation), afterwards we make sure it reaches distinct values.


```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
```


**Complexity Analysis**

* Time Complexity:  $$O(N * K)$$, where $$N$$ is the number of words, and $$K$$ is the length of each word.

* Space Complexity:  $$O(N * K)$$, the space used by the answer.
<br />
<br />