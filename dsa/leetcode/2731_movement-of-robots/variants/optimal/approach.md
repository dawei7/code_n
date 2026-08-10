## General

**Collisions can be ignored when robot identities do not matter**

Every robot moves at the same unit speed. When two robots moving in opposite directions collide, both reverse. From the viewpoint of labeled robots, their individual paths bounce. From the viewpoint of occupied positions, the event is indistinguishable from the two robots passing straight through each other and exchanging labels.

Imagine a right-moving robot arriving at a collision from the left and a left-moving robot arriving from the right. After bouncing, one trajectory leaves left and one leaves right. If they instead pass through, one trajectory also leaves left and one leaves right; only which robot name follows which trajectory changes.

The requested answer sums distances over all unordered pairs of positions. Renaming robots does not change that multiset of positions or its pairwise-distance sum. Therefore the algorithm can pretend every robot continues in its original direction without reacting to collisions.

This equivalence also covers a meeting between integer timestamps or the example where adjacent robots cross without sharing an integer position at the next whole second. Their labels swap conceptually, while the final collection of coordinates remains the same.

**Compute collision-free final coordinates**

A robot beginning at `nums[i]` and moving right travels distance `d` to:

$$
\texttt{nums}[i]+d.
$$

A left-moving robot ends at:

$$
\texttt{nums}[i]-d.
$$

The first loop applies this directly, adding `d` for `'R'` and subtracting it for `'L'`.

The exact implementation mutates `nums` in place. After this loop, the array no longer contains initial coordinates; it contains the collision-free final coordinates whose multiset is also the true final multiset.

**Sort so absolute values become ordinary differences**

For arbitrary coordinates, summing every `abs(a-b)` pair directly takes $O(n^2)$ time. Sorting the final positions as:

$$
x_0\le x_1\le\cdots\le x_{n-1}
$$

removes the absolute-value ambiguity. For every earlier index $j<i$, the distance to $x_i$ is $x_i-x_j$.

Equal final coordinates are allowed after movement. Their pairwise distance is zero, and nondecreasing sorting handles them naturally.

**Use a prefix sum for all distances ending at x_i**

Let `s` store the sum of coordinates before the current one:

$$
s=x_0+x_1+\cdots+x_{i-1}.
$$

There are $i$ earlier coordinates. Their total distance to $x_i$ is:

$$
\sum_{j=0}^{i-1}(x_i-x_j)
=i\cdot x_i-s.
$$

The code adds `i * x - s` to `ans`, then adds `x` to the prefix sum. This groups all pairs by their larger sorted endpoint. Every unordered pair $(j,i)$ with $j<i$ appears exactly once, during iteration `i`.

**Variable reuse in the exact code**

The input direction string is named `s`. After all directions have been consumed in the first loop, the assignment `ans = s = 0` reuses that local name as the numerical prefix sum.

This is safe because the direction string is never needed again. It is compact but can be surprising: within the second loop, `s` no longer means directions.

**Trace the first example**

Start with coordinates `[-2,0,2]`, directions `"RLL"`, and `d=3`. Ignoring collisions gives final coordinates:

- negative two plus three equals one;
- zero minus three equals negative three;
- two minus three equals negative one.

After sorting, the positions are `[-3,-1,1]`.

At index zero, there are no earlier positions, so the contribution is zero and the prefix becomes negative three.

At index one, the contribution is $1(-1)-(-3)=2$.

At index two, the prior prefix is negative four, so the contribution is $2(1)-(-4)=6$.

The total is eight, matching distances two, four, and two in the collision simulation.

**Why taking modulo only at the end works**

The code accumulates the exact integer sum and returns `ans % mod`. Addition and multiplication respect modular arithmetic, so reducing once at the end produces the same residue as reducing after every update.

Python integers do not overflow, even though coordinates and the pair sum can be large. Each sorted contribution is nonnegative despite coordinates themselves possibly being negative.


Replacing every bounce by a pass-through preserves the multiset of positions at every time, changing only labels. Thus the adjusted coordinates are the true final position multiset. Sorting them allows each pair distance to be written as larger minus smaller. At position `i`, `i * x - s` equals the sum of distances from that coordinate to all earlier ones, so every unordered pair is added exactly once. The final modulo therefore equals the requested pair-distance sum modulo $10^9+7$.

## Complexity detail

Let $n$ be the number of robots. Computing final coordinates takes $O(n)$ time. Sorting dominates at $O(n\log n)$, and the prefix-sum pass is $O(n)$. Total time is $O(n\log n)$.

The code modifies the input `nums` rather than allocating a separate coordinate array. Python's list sort may use $O(n)$ temporary memory in the worst case, so the conservative auxiliary-space bound is $O(n)$, matching the manifest. The explicit scalar state outside the sort is $O(1)$.

The collision simulation itself is avoided entirely; runtime is independent of the number of collisions and of the magnitude of `d`.

## Alternatives and edge cases

- **Simulate collisions over time:** Can require enormous work for large `d` and adds identity bookkeeping that the aggregate answer does not need.
- **Enumerate all pairs after movement:** Correct but costs $O(n^2)$ time instead of using sorted prefix sums.
- **Reduce modulo at every iteration:** Also correct and can be useful in fixed-width languages; Python safely delays it.
- **d equal to zero:** Coordinates remain unchanged, and the same sorted pair-sum computation applies.
- **Two robots:** The prefix formula produces their one absolute distance.
- **Equal final coordinates:** Their mutual contribution is zero.
- **Negative coordinates:** Sorting and subtraction remain valid; no special case is required.
- **Many collisions:** Pass-through equivalence removes them all from the computation.
- **Input mutation:** Callers observe `nums` changed into sorted final coordinates.
- **Robot labels:** The method is valid because the result depends only on positions, not on which original label occupies each position.
