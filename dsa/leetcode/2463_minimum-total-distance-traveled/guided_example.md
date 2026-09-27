# Guided Example: Minimum Total Distance Traveled

## 1. The representative instance and the cost of an assignment

Robots and factories live on the X-axis. Robot $i$ starts at `robot[i]`, and factory $j$
sits at `factory[j][0]` and can repair at most `factory[j][1]` robots. Every robot is
repaired by exactly one factory, and a robot's contribution to the total is the distance
it travels to reach the factory that repairs it.

Take the instance

$$\texttt{robot} = [0,\,4,\,6], \qquad \texttt{factory} = [(2,2),\ (6,2)],$$

so there are three robots at positions `0`, `4`, `6`, and two factories: one at position
`2` with a limit of two repairs, one at position `6` with a limit of two repairs. The
required answer is `4`, realised by the plan

| Robot position | Repaired at factory | Distance travelled |
|:---:|:---:|:---:|
| `0` | `2` | `2` |
| `4` | `2` | `2` |
| `6` | `6` | `0` |
| total | — | `4` |

Both factories are used, one of them twice, and the interesting question is not "which
factory is nearest" but "which factory should spend its capacity on which robot".

## 2. From movement to a capacity-constrained assignment

The physical rules look like they might matter — robots pick one direction, they stop at
whichever factory repairs them, they may cross each other, and they pass through
factories that are already full. Sorting out what they actually constrain is the first
step.

- Robots never interact: two robots moving in opposite directions cross without
  colliding, and two moving in the same direction never collide. So the movement of one
  robot never blocks another.
- Factory capacity is the only shared resource. A factory repairs at most `limit` robots
  and ignores everything that passes afterwards.
- Choosing the direction of a robot is the same as choosing which side its assigned
  factory lies on, and the travelled distance is then the absolute difference of the two
  positions.

Consequently, any plan can be described abstractly as an assignment of every robot to
exactly one factory such that each factory receives at most `limit` robots; its cost is
the sum of $\lvert \texttt{robot}[i] - \text{position}_j \rvert$ over assigned pairs. A
physical run realises such an assignment by pointing each robot at its factory; a robot
that meets a spare-capacity factory earlier simply stops sooner, which can only reduce its
travelled distance. Capacities are never violated because the process stops a robot as
soon as its repairing factory is full.

So the whole problem is: assign robots to factories, respect capacities, minimise the sum
of absolute distances.

## 3. Uncrossing: sorting reveals the structure

Two robots at positions $a < b$ and two factories at positions $p \le q$ may be paired in
two ways. The **crossing** pairing sends $a \to q$ and $b \to p$; the **nested** pairing
sends $a \to p$ and $b \to q$. For absolute distance the nested pairing is never worse:

$$\lvert a - p \rvert + \lvert b - q \rvert \;\le\; \lvert a - q \rvert + \lvert b - p \rvert .$$

The difference of the two sides is governed by $h(x) = \lvert a - x \rvert - \lvert b - x \rvert$,
which equals $a - b$ for $x \le a$, equals $2x - a - b$ on $[a, b]$, and equals $b - a$ for
$x \ge b$: a non-decreasing function of $x$. Since $p \le q$, $h(p) \le h(q)$, which is
exactly the displayed inequality.

| Robot positions $a, b$ | Factories $p, q$ | Crossing cost $\lvert a-q\rvert + \lvert b-p\rvert$ | Nested cost $\lvert a-p\rvert + \lvert b-q\rvert$ |
|:---|:---|:---:|:---:|
| `0`, `10` | `2`, `9` | `9 + 8 = 17` | `2 + 1 = 3` |
| `0`, `4` | `2`, `6` | `4 + 2 = 6` | `2 + 2 = 4` |
| `-5`, `2` | `-4`, `3` | `8 + 6 = 14` | `1 + 1 = 2` |

Because swapping a crossing pair for a nested pair preserves every factory's load and
never increases the total, any assignment can be turned into an uncrossed one by repeated
swaps. Sorting the robots ascending and the factories ascending therefore loses no
optimality.

## 4. The shape of an uncrossed assignment: consecutive blocks

After sorting, an uncrossed plan assigns robots to factories in a monotone way: if robot
rank $u$ goes to factory rank $j'$ and robot rank $w > u$ goes to factory rank $j$, then
$j' \le j$. Monotonicity forces two structural facts.

1. The robots repaired by one factory form a **contiguous block** of the sorted robot
   sequence: an interleaved pattern would create a crossing.
2. Empty factories are allowed, and a factory's block length is at most its `limit`.

The decision problem is therefore a left-to-right partition: walk the factories in
ascending position, and for each one decide how many of the not-yet-repaired robots — they
are always the next few in sorted order — it repairs.

## 5. Block costs for the instance

Write $C_j(i, t)$ for the cost of giving the next $t$ robots of the sorted sequence
(ranks $i, \dots, i+t-1$) to factory $j$. For `robot = [0,4,6]` the two factories give:

| Factory | $C(0,1)$ | $C(0,2)$ | $C(0,3)$ | $C(1,1)$ | $C(1,2)$ | $C(2,1)$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| position `2`, limit `2` | `2` | `4` | not allowed | `2` | `6` | `4` |
| position `6`, limit `2` | `6` | `8` | not allowed | `2` | `2` | `0` |

The limits matter as much as the distances: the factory at `2` may take at most two
robots, so $C(0,3) = 2 + 2 + 4 = 8$ is not a legal option, and neither is $C(1,3)$.

## 6. The recurrence and its filled table

Let $D(i, j)$ be the minimum total distance needed to repair the robots of ranks
$i, \dots, n-1$ using only factories $j, \dots, m-1$, with $D(i,j) = \infty$ when that
subproblem is infeasible. The block structure yields

$$D(i,j) \;=\; \min\Bigl(\; \underbrace{D(i,\,j+1)}_{\text{factory } j \text{ repairs nothing}},\; \min_{1 \le t \le \text{limit}_j}\bigl[\,C_j(i,t) + D(i+t,\,j+1)\,\bigr] \;\Bigr),$$

with the base cases $D(n, j) = 0$ for every $j$ (no robots left to repair) and
$D(i, m) = \infty$ for $i < n$ (robots left but no factories).

For the instance, evaluated from the right:

| $D(i,j)$ | $j = 0$ (factory at `2`, limit `2`) | $j = 1$ (factory at `6`, limit `2`) | $j = 2$ (no factories left) |
|:---|:---:|:---:|:---:|
| $i = 0$ (robots `0,4,6`) | `4` | infeasible | infeasible |
| $i = 1$ (robots `4,6`) | `2` | `2` | infeasible |
| $i = 2$ (robot `6`) | `0` | `0` | infeasible |
| $i = 3$ (no robots) | `0` | `0` | `0` |

The infeasible column is informative: the single factory at `6` has only two slots, so it
cannot repair all three robots, and the state that leaves it three robots must be
rejected rather than repaired with a large-looking number.

The root is $D(0,0) = 4$. Unfolding its three candidate decisions shows where that value
comes from:

| Decision at $D(0,0)$ | Block cost | Remaining subproblem | Candidate total |
|:---|:---:|:---:|:---:|
| factory `2` repairs nothing | `0` | $D(0,1)$ infeasible | infeasible |
| factory `2` repairs robot `0` | `2` | $D(1,1) = 2$ | `4` |
| factory `2` repairs robots `0, 4` | `4` | $D(2,1) = 0$ | `4` |

Two different plans tie at `4`: either the factory at `2` takes only robot `0` and the
factory at `6` takes robots `4` and `6` (costs `2 + 2 + 0`), or the factory at `2` takes
robots `0` and `4` and the factory at `6` takes robot `6` (costs `2 + 2 + 0`). Both are
optimal, and the recurrence takes the minimum over both without needing to prefer one.

The table also exposes the trap that a nearest-factory rule falls into. Robot `4` is
exactly equidistant from the two factories, so "go to the nearest factory" is ambiguous,
and robot `6` sits on the second factory while the first factory is two units away; only
the capacity bookkeeping decides which grouping is affordable.

## 7. Correctness: why the block recurrence is exhaustive and sound

The recurrence is *exhaustive* because every uncrossed assignment has exactly the shape it
enumerates. Fix an uncrossed assignment; read the factories in ascending position. Each
factory $j$ repairs a contiguous block of the sorted robots, and that block begins at the
rank left over by the previous factories; the block's length is between $0$ and
`limit[j]`. The recurrence explores precisely these choices for $j = 0, \dots, m-1$, so
the assignment's cost appears as one of the candidates along its own decision path.

The recurrence is *sound* because every candidate it builds is realisable. If a candidate
assigns robots $i, \dots, i+t-1$ to factory $j$, those robots are consecutive in sorted
order and no factory receives more robots than its `limit`; the invariant "the first $i$
robots are repaired, using only factories before $j$" holds before and after the step.
Pointing each robot at its assigned factory realises the plan, and a robot that stops at an
earlier factory with spare capacity travels no farther than its assigned distance, so the
achievable total never exceeds the computed value. Combined with the uncrossing argument of
Section 3 — which shows that some optimal assignment is uncrossed — the minimisation over
blocks equals the true optimum. For the instance, that common value is `4`.

## 8. Boundary cases and the traps they expose

Every row below was checked against the required output for its instance.

| Instance | Answer | What it exposes |
|:---|:---:|:---|
| `robot = [1,-1]`, `factory = [(-2,1),(2,1)]` | `2` | negative coordinates; each factory has exactly one slot, so the pairing is forced |
| `robot = [1,2,3]`, `factory = [(1,1),(2,1),(3,1)]` | `0` | every robot already stands on its factory; zero distance is optimal |
| `robot = [5]`, `factory = [(1,1)]` | `4` | the smallest legal instance, one robot and one factory |
| `robot = [10,-5,2]`, `factory = [(3,2),(-4,1)]` | `9` | unsorted input; sorting both axes precedes any DP work |
| `robot = [0,10]`, `factory = [(0,0),(5,2)]` | `10` | a zero-capacity factory is a factory that repairs nothing and is always skipped |
| `robot = [0,1,10]`, `factory = [(0,2),(9,1)]` | `2` | limited capacity at the left factory forces robot `10` to the right factory |
| `robot = [-1000000000,1000000000]`, `factory = [(0,2)]` | `2000000000` | the total can exceed the 32-bit signed range |

Four traps are worth naming.

- **Assuming each robot can choose its nearest factory independently.** Capacity couples
  the decisions. In the representative instance robot `4` is equidistant from the two
  factories, and whichever factory repairs it spends a slot that another robot may need;
  in the row `robot = [0,1,10]`, the factory at `0` can take only two robots, so the third
  robot's distance is decided by how the first two were grouped. The recurrence chooses
  block lengths jointly instead of deciding robot by robot.
- **Forgetting that a block is bounded by the limit.** A factory's block length may not
  exceed `limit[j]`; treating the limit as irrelevant produces plans that cannot be
  realised.
- **Treating infeasible subproblems as cheap.** A state with more robots left than the
  remaining factories can repair must be rejected. Adding a large finite number instead of
  rejecting it can make a doomed branch look attractive.
- **Ignoring what happens between robots.** Robots cross and pass each other freely and a
  full factory is transparent, so no path-planning or collision constraint ever enters the
  cost; adding one would over-constrain the search.

## 9. Time and auxiliary-space complexity

**Time: $\mathcal{O}(n^2 m)$**, where $n$ = `robot.length` and $m$ = `factory.length`.
There are $n + 1$ robot prefixes and $m + 1$ factory suffixes, so the memoised state space
has $\mathcal{O}(nm)$ entries. Evaluating one state tries every block length from $0$ up to
`limit[j]`, which is at most $n$; the running block cost is accumulated incrementally, so
each tried length costs $\mathcal{O}(1)$ beyond that accumulation. The triple loop is
therefore bounded by $n$ prefix choices multiplied by $m$ factories multiplied by at most
$n$ block lengths, giving $\mathcal{O}(n^2 m)$; with $n, m \le 100$ this is at most about
$10^6$ elementary operations. Sorting costs $\mathcal{O}(n \log n + m \log m)$, which the
triple loop dominates.

**Auxiliary space: $\mathcal{O}(nm)$.** The memo table for the $\mathcal{O}(nm)$ states is
the dominant term, and the recursion depth is at most $m$ nested factories (each factory
advances the factory index by one), so the call stack contributes $\mathcal{O}(m)$ and is
absorbed by the table. Sorting the two input lists needs only $\mathcal{O}(n + m)$ scratch
space. The cost arithmetic itself stores no path: only the returned total, which can reach
$2 \cdot 10^9$ on the extreme instance and therefore needs wide integers rather than 32-bit
values.