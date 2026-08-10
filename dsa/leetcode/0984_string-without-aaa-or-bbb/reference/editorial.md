
## Solution
---
### Approach 1: Greedy

**Intuition**

Intuitively, we should write the most common letter first.  For example, if we have $A = 6, B = 2$, we want to write `'aabaabaa'`.  The only time we don't write the most common letter is if the last two letters we have written are also the most common letter

**Algorithm**

Let's maintain `A, B`: the number of `'a'` and `'b'`'s left to write.

If we have already written the most common letter twice, we'll write the other letter.  Otherwise, we'll write the most common letter.

```python
class Solution(object):
    def strWithout3a3b(self, A, B):
        ans = []

        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                ans.append('a')
            else:
                B -= 1
                ans.append('b')

        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity:  $O(A+B)$.

* Space Complexity:  $O(A+B)$.
<br />
<br />