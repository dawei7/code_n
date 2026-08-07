[TOC]

## Solution

### Overview

We introduce two different approaches here. The first one will use a built-in set to solve the problem, while in the second one we will write our hash function to get faster performance.

---

### Approach 1: Set

Recall (part of) the problem:
> Return True if every binary code of length k is a substring of s. Otherwise, return False.

We just need to check every substring with length `k` until we get all the possible binary codes. Since there are two possible char for each place: `0` or `1`, there will be $$2^k$$ possible binary code.

We can continue until we count up to $$2^k$$. We will return `false` if did not get $$2^k$$ counts after iteration. To prevent repeated counting, a set can be used to store the result we previously counted.

Note that `1 << k` is the same as $$2^k$$, and we use the previous one here.


```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
```


If you like short code, a shorter version in Python presented below. Also, when you shorten codes, it is important that the shortened version still keeps readability.


```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k
```



**Complexity Analysis**

Let $$N$$ be the length of `s`.

- Time complexity: $$\mathcal{O}(NK)$$. We need to iterate the string, and use $$\mathcal{O}(K)$$ to calculate the hash of each substring.

- Space complexity: $$\mathcal{O}(NK)$$. There are at most $$N$$ strings with length $$K$$ in the set.

<br/>

---

### Approach 2: Hash

Maybe you think the approach above is not fast enough. Let's write the hash function ourselves to improve the speed.

Note that we will have at most $$2^k$$ string, can we map each string to a number in [$$0$$, $$2^k-1$$]?

We can. Recall the binary number, we can treat the string as a binary number, and take its decimal form as the hash value. In this case, each binary number has a unique hash value. Moreover, the minimum is all `0`, which is zero, while the maximum is all `1`, which is exactly $$2^k-1$$.

Because we can directly apply bitwise operations to decimal numbers, it is not even necessary to convert the binary number to a decimal number explicitly.

What's more, we can get the current hash from the last one. This method is called [Rolling Hash](https://en.wikipedia.org/wiki/Rolling_hash). All we need to do is to remove the most significant digit and to add a new least significant digit with bitwise operations.

> For example, say `s="11010110"`, and `k=3`, and we just finish calculating the hash of the first substring: `"110"` (`hash` is 4+2=6, or `110`). Now we want to know the next hash, which is the hash of `"101"`. 
>
> We can start from the binary form of our hash, which is `110`. First, we shift left, resulting `1100`. We do not need the first digit, so it is a good idea to do `1100 & 111 = 100`. The all-one `111` helps us to align the digits. Now we need to apply the lowest digit of `"101"`, which is `1`, to our hash, and by using `|`, we get `100 | last_digit = 100 | 1 = 101`.

Write them together, we have: `new_hash = ((old_hash << 1) & all_one) | last_digit_of_new_hash`.

With rolling hash method, we only need $$\mathcal{O}(1)$$ to calculate the next hash, because bitwise operations (`&`, `<<`, `|`, etc.) are only cost $$\mathcal{O}(1)$$.

This time, we can use a simple list to store our hashs, and we will not have hash collision. Those advantages make this approach faster.


```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False]*need
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False
```


Let $$N$$ be the length of `s`.

- Time complexity: $$\mathcal{O}(N)$$. We need to iterate the string, and use $$\mathcal{O}(1)$$ to calculate the hash of each substring. 

- Space complexity: $$\mathcal{O}(2^k)$$. There are $$2^k$$ elements in the list.