
---
### Approach #1: Build String [Accepted]

**Intuition**

Let's individually build the result of each string (`build(S)` and `build(T)`), then compare if they are equal.

**Algorithm**

To build the result of a string `build(S)`, we'll use a stack based approach, simulating the result of each keystroke.

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
```

**Complexity Analysis**

* Time Complexity:  $O(M + N)$, where $M, N$ are the lengths of `S` and `T` respectively.

* Space Complexity:  $O(M + N)$.

---
### Approach #2: Two Pointer [Accepted]

**Intuition**

When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.

**Algorithm**

Iterate through the string in reverse.  If we see a backspace character, the next non-backspace character is skipped.  If a character isn't skipped, it is part of the final answer.

See the comments in the code for more details.

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
```

**Complexity Analysis**

* Time Complexity:  $O(M + N)$, where $M, N$ are the lengths of `S` and `T` respectively.

* Space Complexity:  $O(1)$.