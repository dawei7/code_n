[TOC]

## Solution

--- 

### Overview

Let's start with the naive straightforward solution.

> Compare each word with all the following words one by one. If two words have no common letters, update the maximum product `maxProd`.

Let's omit for the moment the implementation of `noCommonLetters` function.


```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2):
            # TODO
            
        n = len(words)
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letters(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod
```


The number of operations performed in the nested loops is
 
$$(N - 1) + (N - 2) + ... + 2 + 1 = \frac{N(N - 1)}{2}$$

that results in $$\mathcal{O}(N^2 \times f(L_1, L_2))$$ time complexity. Here $$f(L_1, L_2)$$ is a complexity of function `noCommonLetters(String s1, String s2)`, i.e. the price to compare two words of lengths $$L_1$$ and $$L_2$$.

> What could be done here?

![fig](images/methods2.png)

- Approach 1: minimize time complexity $$f(L_1, L_2)$$ of `noCommonLetters` function.

- Approach 2: minimize the number of word comparisons. There is no need to always perform $$\mathcal{O}(N^2)$$ comparisons. Among all the strings with the same set of letters ($$ab$$, $$aaaaabaabaaabb$$, $$bbabbabba$$) it's enough to keep the longest one ($$aaaaabaabaaabb$$). 
<br /> 
<br />


---
### Approach 1: Optimize noCommonLetters function: Bitmasks + Precomputation

The idea is to minimize first the time complexity $$f(L_1, L_2)$$ of word comparison.

![fig](images/methods.png)

**Naive Solution : $$\mathcal{O}(L_1 \times L_2)$$ time**

This naive solution is simple but not optimal. Check the characters in the first word one by one. For each character ensure that this character is _not_ in the second word.


```python
def no_common_letters(s1, s2):
    for ch in s1:
        if ch in s2:
            return False
    return True
```

 
**Bitmasks : $$\mathcal{O}(L_1 + L_2)$$ time**

A more elegant and fast solution would be to use bitmasks.

Words contain only lower case letters and hence an absence or presence of each letter in a word could be encoded with a bitmask of 26 elements. Let's set bit number 0 equal to 1 if character `a` is present in the word, and to 0 otherwise. Now bit number 1. Let's set it equal to 1 if character `b` is present in the word, and to 0 otherwise. And so on and so forth, till the bit number 26 which is equal to 1 if `z` is present in the word.

![fig](images/n_th.png)

> How to set the n-th bit? Use standard bitwise trick : `n_th_bit = 1 << n`.

> How to compute bitmask for a word? Iterate over the word, letter by letter, compute bit number corresponding to that letter `n = (int)ch - (int)'a'`, and add this n-th bit `n_th_bit = 1 << n` into bitmask `bitmask |= n_th_bit`.

![fig](images/bitmask.png)

This way one could compute two bitmasks, character by character, in $$\mathcal{O}(L_1 + L_2)$$ time. Then the word comparison itself could be done in one operation and in a constant time.


```python
def no_common_letters(s1, s2):
    bit_number = lambda ch : ord(ch) - ord('a')

    bitmask1 = bitmask2 = 0
    for ch in s1:
        bitmask1 |= 1 << bit_number(ch)
    for ch in s2:
        bitmask2 |= 1 << bit_number(ch)
    return bitmask1 & bitmask2 == 0
```


**Bitmasks + Precomputation : Comparison in $$\mathcal{O}(1)$$ time**

In the previous approach, one computes a bitmask of each word N times. In fact, each bitmask could be precomputed just once, memorized, and then used for the runtime comparison in a constant time.

Let's use two integer arrays to store bitmasks and string lengths. That's a Java-optimised way since in general Java works faster with arrays than with hashmaps. 

**Algorithm**

- Precompute bitmasks for all words and save them in the array `masks`. Use array `lens` to keep the lengths for all words.

- Compare each word with all the following words one by one. If two words have no common letters, update the maximum product `maxProd`. Perform "no common letters" check in a constant time with the help of precomputed `masks` array: `(masks[i] & masks[j]) == 0`.

- Return `maxProd`.

**Implementation**


```python
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            masks[i] = bitmask
            lens[i] = len(words[i])
            
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lens[i] * lens[j])
        return max_val
```


**Complexity Analysis**

* Time complexity : $$\mathcal{O}(N^2 + L)$$ where $$N$$ is a number of words and $$L$$ is a total length of all words together. The precomputation takes $$\mathcal{O}(L)$$ time because we iterate over all characters in all words. The runtime word comparison takes $$\mathcal{O}(N^2)$$ time. In total, that results in $$\mathcal{O}(N^2 + L)$$ time complexity.

* Space complexity : $$\mathcal{O}(N)$$ to keep two arrays of N elements.
<br /> 
<br />


---
### Approach 2: Optimise Number of Comparisons: Bitmasks + Precomputation + Hashmap

Now, when the comparison itself is optimized, one could optimize the number of comparisons. There is no need to always perform $$\mathcal{O}(N^2)$$
comparisons. Among all the strings with the same set of letters ($$ab$$, $$aaaaabaabaaabb$$, $$bbabbabba$$) it's enough to keep the longest one ($$aaaaabaabaaabb$$). 

For that, instead of two arrays of length $$N$$ as in Approach 1, one could use a hashmap: bitmask -> max word length with that bitmask.

![fig](images/same.png)

This way the total number of word comparisons could be reduced, which speeds up the solution in Python. Note that for Java, this way is not the optimal one because of known problems with [HashMap performance](https://github.com/vavr-io/vavr/issues/571).  

**Algorithm**

- Precompute bitmasks for all words and save them in the hashmap bitmask -> max word length with such a bitmask. (There could be several words with the same bitmask, for example, "a" and "aaaaaaa").

- Compare each word with all the following words one by one. If two words have no common letters, update the maximum product `maxProd`. Perform "no common letters" check in a constant time with the help of precomputed hashmap of bitmasks: `(x & y) == 0`.

- Return `maxProd`.

**Implementation**


```python
from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        hashmap = defaultdict(int)
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for word in words:
            bitmask = 0
            for ch in word:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            # there could be different words with the same bitmask
            # ex. ab and aabb
            hashmap[bitmask] = max(hashmap[bitmask], len(word))
        
        max_prod = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    max_prod = max(max_prod, hashmap[x] * hashmap[y])
        return max_prod
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N^2 + L)$$ where N is the number of words and L is the total length of all words together. If you want to have some fun, here is a [bloody discussion](https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76976/Bit-shorter-C++/80869) that all this is for "small" N only when $$N < 2^{26}$$. The idea is that the number of bitmasks is not more than $$2^{26}$$ and hence for $$N > 2^{26}$$ the complexity is $$\mathcal{O}(L)$$. 

* Space complexity : $$\mathcal{O}(N)$$ to keep a hashmap of N elements if $$N < 2^{26}$$. Otherwise, it's $$\mathcal{O}(2^{26})$$ = $$\mathcal{O}(1)$$.