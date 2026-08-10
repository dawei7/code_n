
## Solution
---
### Approach 1: Greedy

**Intuition**

We have to push the items in order, so when do we pop them?

If the stack has say, `2` at the top, then if we have to pop that value next, we must do it now.  That's because any subsequent push will make the top of the stack different from `2`, and we will never be able to pop again.

**Algorithm**

For each value, push it to the stack.

Then, greedily pop values from the stack if they are the next values to pop.

At the end, we check if we have popped all the values successfully.

```python
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `pushed` and `popped`.

* Space Complexity:  $O(N)$.
<br />
<br />