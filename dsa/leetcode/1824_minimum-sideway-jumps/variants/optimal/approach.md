## General
**Keep the best cost for each lane at the current point**

Maintain three costs. At point 0 they are `[1, 0, 1]`: the frog is already in lane 2, while either other lane is reachable with one side jump. These states summarize every relevant path prefix; future decisions depend only on the point, lane, and side-jump count.

**Block forward-invalid states before relaxing side jumps**

At each following point, set the obstructed lane's cost to infinity because it cannot be occupied. Let `best` be the smallest remaining cost. Every unblocked lane can retain its current cost by moving forward, or be reached by one side jump from whichever unblocked lane achieved `best`. Replace its cost with the smaller of those choices.

**Why one relaxation finds every optimal state**

At most one lane is blocked, so at least two lanes are available. Any useful side jump at a point goes directly from one available lane to another; a second consecutive side jump can only add cost without reaching a lane unavailable after the first jump. Thus each new lane cost is either its forward-carried value or `best + 1`. Induction over points proves the three values remain the optimal costs, and their final minimum is the answer.

## Complexity detail
Each of the $n$ road transitions updates exactly three lane states, so time is $O(n)$. The fixed three-element cost array and scalar minimum use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Shortest-path search over `(point, lane)` states:** It is correct, but a priority queue adds unnecessary logarithmic overhead to this fixed-width acyclic progression.
- **Recompute every prefix:** Solving independently for each endpoint repeats earlier transitions and takes $O(n^2)$ time.
- **Recursive search without memoization:** Branching on side jumps revisits the same states and can become exponential.
- **No obstacles:** Stay in lane 2 and return zero.
- **Obstacle immediately in lane 2:** Side-jump at point 0 before advancing.
- **Repeated obstacles in one outer lane:** They do not matter when lane 2 remains clear.
- **Nonadjacent jump:** Moving directly between lanes 1 and 3 costs one side jump.
- **Final point:** It is guaranteed unblocked, so the minimum of all three final states is valid.
