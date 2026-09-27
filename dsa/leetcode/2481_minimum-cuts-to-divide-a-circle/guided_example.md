# Guided Example: Minimum Cuts to Divide a Circle

## 1. The Cut Vocabulary: Chords Through the Centre

The whole problem lives in the geometry of the disk, so the lesson starts by
fixing exactly what a legal cut is. Only two shapes are permitted:

- a **diameter cut** — a straight segment whose two endpoints lie on the
  circumference and which passes through the centre; and
- a **radius cut** — a straight segment running from one point of the
  circumference to the centre.

A free-floating chord that misses the centre is *not* a cut. Neither is an arc,
nor a segment that stops short of the centre, nor a line that passes through the
centre but halts before reaching the circumference. Every legal cut therefore
intersects the centre, and the difference between the two shapes is purely how
many circumference points it consumes: a diameter cut claims **two**, a radius
cut claims **one**.

The request is to divide the disk into $n$ equal slices — congruent sectors
meeting at the centre — using the fewest cuts. For the official instance
$n = 4$ the answer is $2$, and for $n = 3$ it is $3$. Those two numbers look
unrelated until the parity of $n$ is put at the centre of the analysis.

## 2. A Diameter Cut Always Delivers Slices in Pairs

Here is the observation that decides the problem. A diameter cut is a straight
line through the centre, and a straight line through the centre of a disk is an
axis of reflective symmetry of the disk. Consequently the two half-disks it
produces are mirror images, and every subsequent cut is reflected into a partner
cut across that axis.

Label the circumference by an angle $\theta \in [0, 2\pi)$. If the diameter cut
sits on the axis at angle $\phi$, it consumes the two circumference points

$$
\theta = \phi \quad \text{and} \quad \theta = \phi + \pi .
$$

The second point is the antipode of the first. Read modulo $2\pi$, this is a
rotation by half a turn, so any boundary point created by this diameter is
matched by another boundary point exactly $\pi$ radians away.

Now suppose the finished arrangement has $n$ equal slices. Its slice boundaries
are radial lines meeting the centre at the equally spaced angles

$$
0, \frac{2\pi}{n}, \frac{4\pi}{n}, \dots, \frac{2(n-1)\pi}{n},
$$

and each boundary line ends at a circumference point. Every one of those $n$
points must be claimed by some cut, because a boundary that is not backed by a
cut does not exist.

The parity conclusion is now immediate. For the point at index $k$ to be paired
with another point under a half-turn, the angle $\frac{2\pi k}{n} + \pi$ must
itself be a multiple of $\frac{2\pi}{n}$, which requires $k + \frac{n}{2}$ to be
an integer. When $n$ is **even**, $n/2$ is an integer and the pairing works: the
$n$ points split into $n/2$ antipodal pairs, so $n/2$ diameter cuts suffice.
When $n$ is **odd**, $n/2$ is not an integer, so no boundary point and no
diameter cut can be part of the finished figure. Every boundary must then be
produced by a radius cut, one per boundary, giving $n$ cuts.

## 3. The Counting Invariant

The parity argument can be compressed into a single counting identity that holds
for *every* legal arrangement, whether or not it is optimal:

$$
n \;=\; 2d + r,
$$

where $d$ is the number of diameter cuts, $r$ the number of radius cuts, and $n$
the number of slices. The identity is just the statement that every slice
boundary terminates at a distinct circumference point, each diameter supplies
two such points, and each radius supplies one.

Two immediate consequences follow. First, the total number of cuts is
$d + r$, and since $r = n - 2d$ we have $d + r = n - d$. So **using more
diameters is always at least as good as using more radii**, and the objective is
equivalent to maximising $d$ subject to $2d \le n$. Second, $d \le \lfloor n/2
\rfloor$, which gives the universal lower bound

$$
\text{cuts} \;=\; n - d \;\ge\; n - \left\lfloor \frac{n}{2} \right\rfloor
\;=\; \left\lceil \frac{n}{2} \right\rceil .
$$

For even $n$ this bound is attained by taking $d = n/2$ and $r = 0$, so the
answer is $n/2$ and the work is done. For odd $n$ the bound $\lceil n/2
\rceil$ is *not* attainable, because a single radius is forced (section 2) and a
single radius breaks the equal-spacing requirement: the $n$ boundaries must sit
at the $n$ distinct angles $\frac{2\pi k}{n}$, and a lone radius can supply only
one of them while leaving its antipode unclaimed. Hence the odd case saturates
at $n$ cuts, matching the official example $n = 3 \to 3$.

## 4. The Full Slice-Count Ladder

The next table evaluates the rule on every small instance, including both
official examples and the extremes of the constraint $1 \le n \le 100$. The
"cuts" column is read from the package's authored expectations.

| $n$ | Parity | Max diameters $\lfloor n/2 \rfloor$ | Minimum cuts | Achievable arrangement | Check |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | odd | 0 | `0` | the uncut disk is already one slice | matches authored `0` |
| 2 | even | 1 | `1` | one diameter cut | matches authored `1` |
| 3 | odd | 1 | `3` | three radius cuts at $120^\circ$ apart | matches authored `3` |
| 4 | even | 2 | `2` | two perpendicular diameter cuts | matches official example `2` |
| 5 | odd | 2 | `5` | five radius cuts at $72^\circ$ apart | matches authored `5` |
| 6 | even | 3 | `3` | three diameter cuts at $60^\circ$ | matches authored `6` |
| 99 | odd | 49 | `99` | ninety-nine radius cuts | matches authored `99` |
| 100 | even | 50 | `50` | fifty diameter cuts | matches authored `50` |

$n = 1$ deserves its own sentence. It is odd, yet the formula for odd $n$ would
suggest $1$. The correct answer is $0$, and the reason is that no boundary needs
to exist at all: a single slice is the whole disk, and the disk is already
divided into one equal slice before any cut is made. This is why the closed form
must be written with an explicit exceptional case rather than as a bare parity
rule.

## 5. Worked Instance: $n = 3$, Where the First Cut Does Nothing

Take the odd instance $n = 3$, the official example that the statement singles
out with the remark *the first cut will not divide the circle into distinct
parts*. Place the three boundary targets at $0^\circ$, $120^\circ$, and
$240^\circ$, and perform radius cuts in that order.

| Cut | Segment performed | Circumference points claimed | Boundary angles now present | Regions on the disk | Equal slices so far |
|:---:|:---|:---:|:---|:---:|:---:|
| — | start: no cut | none | none | 1 | 0 |
| 1 | centre to $0^\circ$ | $0^\circ$ | $0^\circ$ | 1 | 0 |
| 2 | centre to $120^\circ$ | $120^\circ$ | $0^\circ$, $120^\circ$ | 2 | 1 sector of $120^\circ$ |
| 3 | centre to $240^\circ$ | $240^\circ$ | $0^\circ$, $120^\circ$, $240^\circ$ | 3 | 3 sectors of $120^\circ$ |

Cut 1 is the surprising row. A radius cut from the centre to the rim is a
straight segment that is entirely interior to the disk; both of its ends lie on
already-present boundary, so it slices the disk into a piece and its complement
only if it meets the existing boundary at more than the centre. With no earlier
cut present there is nothing to meet, so the region count stays at $1$. The
general principle is that the $j$-th legal cut adds one region plus one for each
interior intersection it makes with a previous cut, and because all legal cuts
pass through the centre, that count is at most one added region per cut after the
first.

Cut 2 produces two sectors, but they are unequal: $120^\circ$ and $240^\circ$.
Only after cut 3 does the partition become three congruent $120^\circ$ sectors.
So the run shows both the wasted first cut and the fact that intermediate
partitions are allowed to be uneven — the requirement of equality applies to the
finished configuration, not to every prefix of the process.

## 6. Why a Half-Turn Symmetry Cannot Survive an Odd Slice Count

The geometric obstruction is worth restating in its cleanest form. Suppose $n$
is odd and the finished figure has $n$ equal slices. Fix any diameter cut $D$ in
the figure, lying on the axis at angle $\phi$. The reflection in $D$ maps the
disk to itself and preserves the cut configuration, so it maps the set of slice
boundaries to itself. That set is $\{ \frac{2\pi k}{n} : 0 \le k < n \}$.

The reflection sends the boundary at angle $\frac{2\pi k}{n}$ to the boundary at
angle $2\phi - \frac{2\pi k}{n}$. Applying this twice returns the original
boundary, so the reflection is an involution and the $n$ boundaries group into
fixed points and pairs. But a reflection of a circle has exactly two fixed
directions — the two rays of its axis — and the axis already holds the diameter
$D$. Checking the pairing combinatorially instead: a half-turn around the centre
sends index $k$ to index $k + \frac{n}{2}$, which is not an integer when $n$ is
odd, so no boundary is invariant and no two boundaries are paired. A set of odd
cardinality cannot be partitioned into pairs, so either some boundary is fixed
by the half-turn (it is not, as just shown) or the count is even (it is not).
Contradiction. Therefore no diameter cut exists in an optimal odd configuration,
and the counting identity $n = 2d + r$ degenerates to $r = n$, forcing $n$
radius cuts. The construction with radius cuts at the $n$ equally spaced angles
realises exactly this, so the bound is tight.

## 7. The Two Official Instances Side by Side

The pair of official examples is the clearest possible contrast between the even
and odd regimes, because the request differs by a single slice while the answer
nearly doubles.

| Feature | $n = 4$ | $n = 3$ |
|:---|:---|:---|
| Parity | even | odd |
| Diameter cuts available | $4/2 = 2$ antipodal pairs | none usable |
| Chosen cuts | `2` diameter cuts at $90^\circ$ | `3` radius cuts at $120^\circ$ |
| Boundary points supplied | $2 \times 2 = 4$ | $3 \times 1 = 3$ |
| Slice angle | $90^\circ$ | $120^\circ$ |
| Answer | `2` | `3` |
| Counting identity | $4 = 2\cdot 2 + 0$ | $3 = 2\cdot 0 + 3$ |

The even case spends two circumference points for the price of one cut; the odd
case can never do so and must pay one cut per boundary. That single sentence is
the entire algorithm.

## 8. Boundary Traps and Alternative Readings

| Trap or alternative | Description | Why it fails or when it is right |
|:---|:---|:---|
| Applying the parity rule to $n = 1$ | treating $1$ as a generic odd count and answering `1` | The uncut disk is already one equal slice; the answer is `0`. |
| Assuming the first cut always splits the disk | expecting the region count to equal the cut count | A radius cut with nothing to intersect adds no region, as the $n = 3$ trace shows. |
| Using $\lceil n/2 \rceil$ for odd $n$ | the universal counting lower bound | It is not attainable: one radius is forced, which breaks equal spacing, so $n$ is required. |
| Claiming a diameter cut alone gives $n$ slices | one diameter gives exactly $2$ equal slices | True only for $n = 2$; for larger $n$ the diameters must be spread at $180^\circ/n$ apart. |
| Requiring every intermediate step to be equal | insisting that each prefix of cuts yields equal slices | Equality is a property of the final configuration; prefixes may be uneven. |
| Arbitrary chords through the interior | using a chord that misses the centre to save a cut | Not a legal cut under the statement's definition. |

## 9. Complexity

The decided rule depends only on the parity of $n$ and one halving operation: an
even $n$ answers $n/2$ and an odd $n > 1$ answers $n$ itself, with $n = 1$ as
the explicit exception. Let $n$ be bounded by $100$ as the constraints state.

- **Time:** $O(1)$. One parity test and at most one shift-or-halve operation
  are performed; no loop depends on $n$.
- **Auxiliary space:** $O(1)$. Nothing is stored beyond the input and the
  single result value — no list of boundary angles, no slice table, and no
  simulation of the cutting process.

The lesson's tables are expository scaffolding for a constant-time decision, not
a description of the algorithm's cost: the geometry proves *why* the parity
split is correct, and that proof is what the constant-time rule encodes.