[TOC]

---
### Approach #1: Dynamic Programming [Memory Limit Exceeded]

**Intuition**

Let $\text{dp}[n][k]$ be the answer for adding `k` more gas stations to the first `n` intervals of stations.  We can develop a recurrence expressing $\text{dp}[n][k]$ in terms of $\text{dp}[x][y]$ with smaller `(x, y)`.

**Algorithm**

Say the `i`th interval is $\text{deltas}[i] = stations[i+1] - \text{stations}[i]$.  We want to find `dp[n+1][k]` as a recursion.  We can put `x` gas stations in the `n+1`th interval for a best distance of $deltas[n+1] / (x+1)$, then the rest of the intervals can be solved with an answer of $\text{dp}[n][k-x]$.  The answer is the minimum of these over all `x`.

From this recursion, we can develop a dynamic programming solution.

```python
class Solution(object):
    def minmaxGasDist(self, stations, K):
        N = len(stations)
        deltas = [stations[i+1] - stations[i] for i in xrange(N-1)]
        dp = [[0.0] * (K+1) for _ in xrange(N-1)]
        #dp[i][j] = answer for deltas[:i+1] when adding j gas stations
        for i in xrange(K+1):
            dp[0][i] = deltas[0] / float(i + 1)

        for p in xrange(1, N-1):
            for k in xrange(K+1):
                dp[p][k] = min(max(deltas[p] / float(x+1), dp[p-1][k-x])
                               for x in xrange(k+1))

        return dp[-1][K]
```

**Complexity Analysis**

* Time Complexity:  $O(N K^2)$, where $N$ is the length of `stations`.

* Space Complexity: $O(N K)$, the size of `dp`.

---
### Approach #2: Brute Force [Time Limit Exceeded]

**Intuition**

As in *Approach #1*, let's look at `deltas`, the distances between adjacent gas stations.

Let's repeatedly add a gas station to the current largest interval, so that we add `K` of them total.  This greedy approach is correct because if we left it alone, then our answer never goes down from that point on.

**Algorithm**

To find the largest current interval, we keep track of how many parts $\text{count}[i]$ the `i`th (original) interval has become.  (For example, if we added 2 gas stations to it total, there will be 3 parts.)  The new largest interval on this section of road will be $\text{deltas}[i] / \text{count}[i]$.

```python
class Solution(object):
    def minmaxGasDist(self, stations, K):
        N = len(stations)
        deltas = [float(stations[i+1] - stations[i]) for i in xrange(N-1)]
        count = [1] * (N - 1)

        for _ in xrange(K):
            #Find interval with largest part
            best = 0
            for i, x in enumerate(deltas):
                if x / count[i] > deltas[best] / count[best]:
                    best = i

            #Add gas station to best interval
            count[best] += 1

        return max(x / count[i] for i, x in enumerate(deltas))
```

**Complexity Analysis**

* Time Complexity:  $O(N K)$, where $N$ is the length of `stations`.

* Space Complexity: $O(N)$, the size of `deltas` and `count`.

---
### Approach #3: Heap [Time Limit Exceeded]

**Intuition**

Following the intuition of *Approach #2*, if we are taking a repeated maximum, we can replace this with a heap data structure, which performs repeated maximum more efficiently.

**Algorithm**

As in *Approach #2*, let's repeatedly add a gas station to the next larget interval `K` times.  We use a heap to know which interval is largest.  In Python, we use a negative priority to simulate a max heap with a min heap.

```python
class Solution(object):
    def minmaxGasDist(self, stations, K):
        pq = [] #(-part_length, original_length, num_parts)
        for i in xrange(len(stations) - 1):
            x, y = stations[i], stations[i+1]
            pq.append((x-y, y-x, 1))
        heapq.heapify(pq)

        for _ in xrange(K):
            negnext, orig, parts = heapq.heappop(pq)
            parts += 1
            heapq.heappush(pq, (-(orig / float(parts)), orig, parts))

        return -pq[0][0]
```

**Complexity Analysis**

Let $N$ be the length of stations, and $K$ be the number of gas stations to add.

* Time Complexity:  $O(N + K \log N)$

- First of all, we scan the stations to obtain a list of intervals between each adjacent stations.

- Then it takes another $O(N)$ to build a heap out of the list of intervals.

- Finally, we repeatedly pop out an element and push in a new element into the heap, which takes $O(\log N)$ respectively. In total, we repeat this step for $K$ times (_i.e._ to add $K$ gas stations).

- To sum up, the overall time complexity of the algorithm is $O(N) +$\mathcal{O}(N)$+$\mathcal{O}(K \cdot \\log N)$= O(N + K\cdot \log N)$.

* Space Complexity: $O(N)$, the size of `deltas` and `count`.

---

### Approach #4: Approach #3.5: Preprocessing + Heap + Greedy [Accepted]

#### Intuition

The heap-based approach from Approach #3 adds stations one by one, which can become inefficient when the number of new stations `K` is large. We can improve this by first making a conservative estimation of how many stations each interval should have based on an upper bound distance, and then refining the allocation greedily using a heap.

The idea is to first assume the maximum possible distance between any two stations, `D`, if there were no existing stations. This gives us an initial upper bound for the maximum allowed interval distance. Using this distance, we can estimate how many stations each current interval should get (using the floor division). This step distributes a large portion of stations efficiently in one pass.

Then, since this conservative distribution might not use all `K` stations, we use a max heap to distribute the remaining stations one by one to the intervals with the largest current distances. This ensures that the largest interval is always split next, minimizing the overall maximum distance.

---

#### Algorithm

1. Compute an initial upper bound for the maximum distance if there were no existing stations:
   $D = \frac{stations[-1] - \text{stations}[0]}{K + 1}$

2. For each interval `i` between consecutive stations:
   - Compute the interval length:
     $L_i = stations[i+1] - \text{stations}[i]$
   - Estimate the number of new stations conservatively:
     $k_i = \lfloor \frac{L_i}{D} \rfloor$
   - Compute the actual distance in this interval after adding $k_{i}$ stations:
     $d_i = \frac{L_i}{k_i + 1}$
   - Decrease `K` by $k_{i}$, since those stations are now allocated.
   - Push $(-d_{i}, L_{i}, k_{i})$ into a max heap (negative distance used for max behavior).

3. While there are still remaining stations (`K > 0`):
   - Pop the interval with the largest current distance $d_{i}$.
   - Add one more station to it ($k_{i} += 1$).
   - Recompute the new distance for that interval:
     $d_i = \frac{L_i}{k_i + 1}$
   - Push the updated interval back into the heap.

4. The final answer is the largest remaining distance in the heap, i.e., $-\text{heap}[0][0]$.

```python
from heapq import heappush, heappop
from math import floor

class Solution:
    def minmaxGasDist(self, stations, k):
        n = len(stations)

        # Step 1: Compute an upper bound for distance
        dist_upper = (stations[-1] - stations[0]) / (k + 1)

        # Step 2: Conservative allocation
        heap = []  # (-distance, interval_length, current_station_count)
        for i in range(n - 1):
            interval = stations[i + 1] - stations[i]
            ki = floor(interval / dist_upper)
            actual_dist = interval / (ki + 1)
            k -= ki
            heappush(heap, (-actual_dist, interval, ki))

        # Step 3: Allocate remaining stations greedily
        for _ in range(k):
            neg_dist, interval, ki = heappop(heap)
            ki += 1
            new_dist = interval / (ki + 1)
            heappush(heap, (-new_dist, interval, ki))

        # Step 4: The largest remaining interval
        return -heap[0][0]
```

#### Complexity Analysis

Let $N$ be the number of intervals.

- Time Complexity: $O(N \log N)$

    Preprocessing (initial conservative distribution): $O(N)$

    Building heap: $O(N)$

    Distributing remaining stations (each pop/push in $O(\log N)$): $O(N \log N)$ in total

- Space Complexity: $O(N)$

    We store up to $N$ intervals in the heap

---

### Approach #5: Binary Search [Accepted]

**Intuition**

Let's ask `possible(D)`: with `K` (or less) gas stations, can we make every adjacent distance between gas stations at most `D`?  This function is monotone, so we can apply a binary search to find $D^{\text{*}}$.

**Algorithm**

 More specifically, there exists some `D*` (the answer) for which $possible(d) = False$ when `d < D*` and $possible(d) = True$ when `d > D*`.  Binary searching a monotone function is a typical technique, so let's focus on the function `possible(D)`.

 When we have some interval like $X = stations[i+1] - \text{stations}[i]$, we'll need to use $\lfloor \frac{X}{D} \rfloor$ gas stations to ensure every subinterval has size less than `D`.  This is independent of other intervals, so in total we'll need to use $\sum_i \lfloor \frac{X_i}{D} \rfloor$ gas stations.  If this is at most `K`, then it is possible to make every adjacent distance between gas stations at most `D`.

```python
class Solution(object):
    def minmaxGasDist(self, stations, K):
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in xrange(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo
```

**Complexity Analysis**

* Time Complexity:  $O(N \log W)$, where $N$ is the length of `stations`, and $W = 10^{14}$ is the range of possible answers ($10^8$), divided by the acceptable level of precision ($10^{-6}$).

* Space Complexity: $O(1)$ in additional space complexity.