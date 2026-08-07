[TOC]

---
### Approach #1: Brute Force [Accepted]

**Intuition**

The first two elements of the array uniquely determine the rest of the sequence.

**Algorithm**

For each of the first two elements, assuming they have no leading zero, let's iterate through the rest of the string.  At each stage, we expect a number less than or equal to `2^31 - 1` that starts with the sum of the two previous numbers.


```python
class Solution(object):
    def splitIntoFibonacci(self, S):
        for i in xrange(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in xrange(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []
```


**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `S`, and with the requirement that the values of the answer are $$O(1)$$ in length.

* Space Complexity:  $$O(N)$$.