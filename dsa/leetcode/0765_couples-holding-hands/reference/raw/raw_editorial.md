[TOC]

### Approach Framework

**Observations**

First, instead of couples `(0, 1), (2, 3), (4, 5), ...`, we could just consider couples `(0, 0), (1, 1), (2, 2), ...` without changing the answer.  Also, we could imagine that we have `N` two-seat couches `0, 1, 2, ..., N-1`.  This is because the person sitting on the left-most seat of the row must be paired with the person sitting on the second-left-most seat, the third-left-most paired with the fourth-left-most, and so on.
Call a person happy if they are with their partner on the same couch.  Intuitively, a swap that keeps both persons swapped unhappy is not part of some optimal solution.  We'll call this the *happy swap assumption* (HSA), and we'll prove it in Approach #2.

---

### Approach #1: Backtracking [Time Limit Exceeded]

**Intuition**

We could guess without proof that a solution where we make the people on each couch happy in order is optimal.  This assumption is stronger than HSA, but it seems reasonable because at each move we are making at least 1 couple happy.  (See Approach #2 for a proof.)
Under such an assumption, for some couch with unhappy people X and Y, we either replace Y with X's partner, or replace X with Y's partner.
For each of the two possibilities, we can try both using a backtracking approach.

**Algorithm**

For each couch with two possibilities (ie. both people on the couch are unhappy), we will try the first possibility, find the answer as `ans1`, then undo our move and try the second possibility, find the associated answer as `ans2`, undo our move and then return the smallest answer.


```python
class Solution(object):
    def minSwapsCouples(self, row):
        N = len(row) / 2
        pairs = [[row[i]/2, row[i+1]/2]
                 for i in xrange(0, 2*N, 2)
                 if row[i]/2 != row[i+1]/2]

        def swap(a, b, c, d):
            pairs[a][b], pairs[c][d] = pairs[c][d], pairs[a][b]

        def solve(i = 0):
            if i == len(pairs): return 0
            x, y = pairs[i]
            if x == y: return solve(i+1)

            for j in xrange(i+1, len(pairs)):
                for k in xrange(2):
                    if pairs[j][k] == x: jx = j, k
                    if pairs[j][k] == y: jy = j, k

            swap(i, 1, *jx)
            ans1 = 1 + solve(i+1)
            swap(i, 1, *jx)

            swap(i, 0, *jy)
            ans2 = 1 + solve(i+1)
            swap(i, 0, *jy)

            return min(ans1, ans2)

        return solve()
```


**Complexity Analysis**

* Time Complexity: $$O(N * 2^N)$$, where $$N$$ is the number of couples, as for each couch we check up to two complete possibilities.  The $$N$$ factor is from searching for `jx` and `jy`; this factor can be removed with a more efficient algorithm that keeps track of where `pairs[j][k]` is `x` as we swap elements through pairs.

* Space Complexity: $$O(N)$$.

---
### Approach #2: Cycle Finding [Accepted]

**Intuition**

If we take the HSA as true, it means that if a couple is on two separate couches, there are two possible moves to make this couple happy, depending on which partner visits their partner and which stays in place.
This leads to the following idea: for each couple sitting at couches X and Y (possibly the same), draw an undirected edge from X to Y.  Call such a graph the couples graph.  This graph is 2-regular (every node has degree 2), and it is easy to see that every connected component of this graph must be a cycle.

<br />
<center>
    <img src="images/couples_cycle_finding.png" alt="Diagram of cyclic list" width="350"/>
</center>
<br />

Then, making a swap for $$X_1$$ to meet their partner $$X_2$$ has a corresponding move on the couples graph equivalent to contracting the corresponding edge to $$X_1X_2$$ plus having a node with a single self edge.
Our goal is to have `N` connected components in the graph, one for each couch.  Every swap (allowed by the scheme above) always increases that number by exactly 1, so under HSA, the answer is just `N` minus the number of connected components in the couples graph.

Now to prove HSA, observe that it is impossible with *any* swap to create more than 1 additional connected component in the couples graph.  So any optimal solution must have at least the number of moves in the answer we've constructed.  (This also proves the ordering assumption made in Approach #1, as we can make edge contractions of a cycle in any order without changing the answer.)

**Algorithm**

We'll construct the graph: `adj[node]` will be the index of the two nodes that this `node` is adjacent to.
After, we'll find all connected components (which are also cycles.)  If at some couch (node) a person is unvisited, we will visit it and repeatedly visit some neighbor until we complete the cycle.


```python
class Solution(object):
    def minSwapsCouples(self, row):
        N = len(row) / 2

        #couples[x] = [i, j]:
        #x-th couple is at couches i and j
        couples = [[] for _ in xrange(N)]
        for i, x in enumerate(row):
            couples[x/2].append(i/2)
        #adj[x] = [i, j]
        #x-th couch connected to couches i, j by couples
        adj = [[] for _ in xrange(N)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)
        #Answer is N minus the number of cycles in "adj"
        ans = N
        for start in xrange(N):
            if not adj[start]: continue
            ans -= 1
            x, y = start, adj[start].pop()
            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        return ans
```


**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of couples.

* Space Complexity: $$O(N)$$, the size of `adj` and associated data structures.

---
### Approach #3: Greedy [Accepted]

**Intuition**

From guessing, or by the proof in *Approach #2*, our strategy is to resolve each couch in order.

To resolve a couch, fix the first person and have their partner swap into the second seat if they are not already there.

**Algorithm**

If a person is number `x`, their partner is `x ^ 1`, where `^` is the bitwise XOR operator.

For each first person `x = row[i]` on a couch who is unpartnered, let's find their partner at `row[j]` and have them swap seats with `row[i+1]`.


```python
class Solution(object):
    def minSwapsCouples(self, row):
        ans = 0
        for i in xrange(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1: continue
            ans += 1
            for j in xrange(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1], row[j] = row[j], row[i+1]
                    break
        return ans
```


**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the number of couples.

* Space Complexity: $$O(1)$$ additional complexity: the swaps are in place.