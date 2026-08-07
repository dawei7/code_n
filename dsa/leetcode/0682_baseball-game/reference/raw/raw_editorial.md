### Approach #1: Stack [Accepted]

**Intuition and Algorithm**

Let's maintain the value of each valid round on a stack as we process the data. A stack is ideal since we only deal with operations involving the last or second-last valid round.


```python
class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
```


**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `ops`. We parse through every element in the given array once, and do $$O(1)$$ work for each element.

* Space Complexity: $$O(N)$$, the space used to store our `stack`.