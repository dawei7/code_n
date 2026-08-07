### Approach #1: Insert Into Sorted Structure [Accepted]

**Intuition**

Let's add flowers in the order they bloom. When each flower blooms, we check it's neighbors to see if they can satisfy the condition with the current flower.

**Algorithm**

We'll maintain `active`, a sorted data structure containing every flower that has currently bloomed. When we add a flower to `active`, we should check it's lower and higher neighbors. If some neighbor satisfies the condition, we know the condition occurred first on this day.

```python
class Solution(object):
    def kEmptySlots(self, flowers, k):
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1
```

**Complexity Analysis**

* Time Complexity (Java): $O(N \log N)$, where $N$ is the length of `flowers`. Every insertion and search is $O(\log N)$.

* Time Complexity (Python): $O(N^2)$.  As above, except `list.insert` is $O(N)$.

* Space Complexity: $O(N)$, the size of `active`.

---
### Approach #2: Min Queue [Accepted]

**Intuition**

For each contiguous block ("window") of `k` positions in the flower bed, we know it satisfies the condition in the problem statement if the minimum blooming date of this window is larger than the blooming date of the left and right neighbors.

Because these windows overlap, we can calculate these minimum queries more efficiently using a sliding window structure.

**Algorithm**

Let $\text{days}[x] = i$ be the time that the flower at position `x` blooms. For each window of `k` days, let's query the minimum of this window in (amortized) constant time using a `MinQueue`, a data structure built just for this task. If this minimum is larger than its two neighbors, then we know this is a place where "`k` empty slots" occur, and we record this candidate's answer.

To operate a `MinQueue`, the key invariant is that `mins` will be an increasing list of candidate answers to the query `MinQueue.min`.

For example, if our queue is `[1, 3, 6, 2, 4, 8]`, then `mins` will be `[1, 2, 4, 8]`. As we `MinQueue.popleft`, `mins` will become `[2, 4, 8]`, then after 3 more `popleft`'s will become `[4, 8]`, then after 1 more `popleft` will become `[8]`.

As we `MinQueue.append`, we should maintain this invariant. We do it by popping any elements larger than the one we are inserting. For example, if we appended `5` to `[1, 3, 6, 2, 4, 8]`, then `mins` which was `[1, 2, 4, 8]` becomes `[1, 2, 4, 5]`.

Note that we used a simpler variant of `MinQueue` that requires every inserted element to be unique to ensure correctness. Also, the operations are amortized constant time because every element will be inserted and removed exactly once from each queue.

```python
from collections import deque
class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]

class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))

        return ans if ans < len(days) else -1
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `flowers`. In enumerating through the $O(N)$ outer loop, we do constant work as `MinQueue.popleft` and `MinQueue.min` operations are (amortized) constant time.

* Space Complexity: $O(N)$, the size of our `window`.

---
### Approach #3: Sliding Window [Accepted]

**Intuition**

As in *Approach #2*, we have $\text{days}[x] = i$ for the time that the flower at position `x` blooms. We wanted to find *candidate* intervals `[left, right]` where $\text{days}[left], \text{days}[right]$ are the two smallest values in `[days[left], days[left+1], ..., days[right]]`, and $right - left = k + 1$.

Notice that these candidate intervals cannot intersect: for example, if the candidate intervals are `[left1, right1]` and `[left2, right2]` with `left1 < left2 < right1 < right2`, then for the first interval to be a candidate, $\text{days}[left2] > \text{days}[right1]$; and for the second interval to be a candidate, $\text{days}[right1] > \text{days}[left2]$, a contradiction.

That means whenever some interval can be a candidate and it fails first at `i`, indices `j < i` can't be the start of a candidate interval. This motivates a sliding window approach.

**Algorithm**

As in *Approach #2*, we construct `days`.

Then, for each interval `[left, right]` (starting with the first available one), we'll check whether it is a candidate: whether $\text{days}[i] > \text{days}[left]$ and $\text{days}[i] > \text{days}[right]$ for `left < i < right`.

If we fail, then we've found some new minimum $\text{days}[i]$ and we should check the new interval `[i, i+k+1]`.  If we succeed, then it's a candidate answer, and we'll check the new interval `[right, right+k+1]`.

```python
class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k+1
        while right < len(days):
            for i in xrange(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+k+1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1
```

**Complexity Analysis**

* Time and Space Complexity: $O(N)$. The analysis is the same as in Approach #2.