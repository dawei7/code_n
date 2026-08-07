[TOC]

---
### Approach #1: Next Array [Accepted]

**Intuition**

Let $\text{left}[i]$ be the distance from seat `i` to the closest person sitting to the left of `i`.  Similarly, let $\text{right}[i]$ be the distance to the closest person sitting to the right of `i`.  This is motivated by the idea that the closest person in seat `i` sits a distance $min(\text{left}[i], \text{right}[i])$ away.

**Algorithm**

To construct $\text{left}[i]$, notice it is either $left[i-1] + 1$ if the seat is empty, or `0` if it is full.  $\text{right}[i]$ is constructed in a similar way.

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in xrange(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i-1] + 1

        for i in xrange(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N-1: right[i] = right[i+1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `seats`.

* Space Complexity:  $O(N)$, the space used by `left` and `right`.

---
### Approach #2: Two Pointer [Accepted]

**Intuition**

As we iterate through seats, we'll update the closest person sitting to our left, and closest person sitting to our right.

**Algorithm**

Keep track of `prev`, the filled seat at or to the left of `i`, and `future`, the filled seat at or to the right of `i`.

Then at seat `i`, the closest person is $min(i - prev, future - i)$, with one exception.  $i - prev$ should be considered infinite if there is no person to the left of seat `i`, and similarly $future - i$ is infinite if there is no one to the right of seat `i`.

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `seats`.

* Space Complexity:  $O(1)$.

---
### Approach #3: Group by Zero [Accepted]

**Intuition**

In a group of `K` adjacent empty seats between two people, the answer is $(K+1) / 2$.

**Algorithm**

For each group of `K` empty seats between two people, we can take into account the candidate answer $(K+1) / 2$.

For groups of empty seats between the edge of the row and one other person, the answer is `K`, and we should take into account those answers too.

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans,seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return ans
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `seats`.

* Space Complexity:  $O(1)$.