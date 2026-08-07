[TOC]

## Solution
---
### Approach 1: Work Backwards

**Intuition**

Imagine we stamped the sequence with moves $m_1, m_2, \cdots$.  Now, from the final position `target`, we will make those moves in reverse order.

Let's call the `i`th *window*, a subarray of `target` of length `stamp.length` that starts at `i`.  Each move at position `i` is possible if the `i`th window matches the stamp.  After, every character in the window becomes a wildcard that can match any character in the stamp.

For example, say we have $stamp = "abca"$ and $target = "aabcaca"$.  Working backwards, we will reverse stamp at window `1` to get `"a????ca"`, then reverse stamp at window `3` to get `"a??????"`, and finally reverse stamp at position `0` to get `"???????"`.

**Algorithm**

Let's keep track of every window.  We want to know how many cells initially match the stamp (our "`made`" list), and which ones don't (our `"todo"` list).  Any windows that are ready (ie. have no todo list), get enqueued.

Specifically, we enqueue the positions of each character.  (To save time, we enqueue by character, not by window.)  This represents that the character is ready to turn into a `"?"` in our working `target` string.

Now, how to process characters in our queue?  For each character, let's look at all the windows that intersect it, and update their todo lists.  If any todo lists become empty in this manner `(window.todo is empty)`, then we enqueue the characters in `window.made` that we haven't processed yet.

```python
class Solution(object):
    def movesToStamp(self, stamp, target):
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in xrange(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in xrange(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in xrange(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # This window is affected
                    A[j][1].discard(i) # Remove it from todo list of this window
                    if not A[j][1]:  # Todo list of this window is empty
                        ans.append(j)
                        for m in A[j][0]: # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []
```

**Complexity Analysis**

* Time Complexity:  $O(N(N-M))$, where $M, N$ are the lengths of `stamp`, `target`.

* Space Complexity:  $O(N(N-M))$.
<br />
<br />