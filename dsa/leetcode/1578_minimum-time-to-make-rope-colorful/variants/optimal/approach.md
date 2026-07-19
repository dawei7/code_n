## General
**Treat each maximal color run independently**

Consider one maximal consecutive run of the same color. At most one balloon from that run may remain; keeping two would leave equal adjacent colors. Removing the entire run is never cheaper than keeping one balloon because all removal times are positive.

Therefore, every valid optimum removes all but one balloon from each repeated-color run. To minimize the removal cost, retain the balloon with the largest removal time and pay for all other balloons in that run.

**Accumulate the cheaper balloon on every collision**

Scan from left to right while storing the color and removal time of the balloon currently chosen to survive its run. When the next color differs, begin a new run. When it matches, add the smaller of the two removal times to the answer and keep the larger time as the run's surviving candidate.

After processing a whole run, this has paid its total removal time minus its maximum value. Since different maximal runs have different boundary colors, choices inside one run cannot create a new same-color conflict with another run. Summing their independent optima is therefore globally optimal.

## Complexity detail
The scan examines each balloon once and performs constant work per position, giving $O(N)$ time.

Only the accumulated cost, previous color, and largest retained time for the active run are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sum each run then subtract its maximum:** explicitly track a run sum and maximum. This is also $O(N)$ time and $O(1)$ extra space.
- **Dynamic programming:** track the minimum cost for which color survives at each prefix. It can express the same choice but uses unnecessary state for this local greedy structure.
- **Repeated deletion simulation:** repeatedly find an equal adjacent pair and delete the cheaper balloon. It is correct, but array deletions and rescans can require $O(N^2)$ time.
- **All colors distinct:** no balloon is removed, so the answer is zero.
- **One balloon:** the rope is already colorful.
- **One long equal-color run:** remove every balloon except the most expensive one.
- **Equal removal times:** either tied balloon may survive; the minimum total is unchanged.
- **Multiple separated runs:** optimize every maximal run independently and add their costs.
- **Largest time in the middle:** the scan must continue carrying that maximum across the rest of the run.
- **Removing a boundary balloon:** maximal runs already have different neighboring colors, so resolving a run never merges it with another run of the same color.
