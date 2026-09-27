# Guided Example: Count Total Number of Colored Cells

## 1. The instance and the two words that decide everything

One cell is colored at minute 1; on every later minute, each still-uncolored cell that shares an edge with an already blue cell becomes blue. The question is how many cells are blue after $n$ minutes, and the instance traced here is $n = 4$, whose required answer is `25`.

Two phrases in the statement carry all of the difficulty. "**Every** uncolored cell that touches a blue cell" means the process colors a whole frontier per minute rather than a single cell, and "**any** arbitrary unit cell" means the first choice fixes only where the figure sits, not what it looks like. Together they make the growth deterministic: the size of the blue region depends on $n$ alone.

## 2. Why the blue region is always a diamond

Give the seed cell coordinates $(0,0)$ and measure distance on the grid with the Manhattan metric

$$
\lVert (dx, dy) \rVert_1 = \lvert dx \rvert + \lvert dy \rvert .
$$

The claim is an invariant that describes the entire blue region after every minute:

> after minute $k$, the blue cells are exactly the cells with $\lvert dx \rvert + \lvert dy \rvert \le k - 1$, that is, the closed diamond of radius $k-1$ around the seed.

The base case is minute 1, which colors $(0,0)$: precisely the ball of radius $0$. For the inductive step, note that edge adjacency moves a cell by one unit along one axis, so it changes the Manhattan distance by exactly $1$.

- A cell $c$ at distance $\lVert c \rVert_1 \le k-1$ that is not the seed has a neighbour closer to the seed, at distance $\lVert c \rVert_1 - 1 \le k-2$. That neighbour is blue by minute $k-1$, so $c$ turns blue at minute $k$.
- A cell $c$ at distance $\lVert c \rVert_1 \ge k$ has every neighbour at distance at least $\lVert c \rVert_1 - 1 \ge k-1$, and no cell at distance $k-1$ or more is blue by minute $k-1$. So $c$ cannot turn blue at minute $k$.

The two directions together prove the invariant. This also explains why the wording "any arbitrary unit cell" is harmless: the four-neighbourhood is symmetric under the rotations and reflections that map a diamond to itself, so translating the seed only translates the figure, and the count is unaffected.

## 3. Ring accounting: what one minute actually adds

Because the blue set is a ball, the cells colored during minute $k$ are exactly the sphere of radius $r = k - 1$: the cells at distance precisely $r$ from the seed. For $r = 0$ the sphere is the single seed. For $r \ge 1$, split the sphere into four sides by the signs of the coordinates. The north-east side $\{(dx, dy) : dx \ge 0,\ dy \ge 0,\ dx + dy = r\}$ contains the $r+1$ lattice points $(0, r), (1, r-1), \dots, (r, 0)$, and the other three sides contribute $r+1$ points each. Adding $4(r+1)$ counts each of the four axis points $(r,0)$, $(0,r)$, $(-r,0)$, $(0,-r)$ exactly twice, so the sphere contains

$$
4(r+1) - 4 = 4r
$$

cells. The frontier therefore grows linearly: each additional minute adds four more cells than the previous minute did.

| Radius $r$ | Sphere size $4r$ | Cells on that sphere | Colored during minute |
|---|---|---|---|
| 0 | 1 | $(0, 0)$ | minute 1 |
| 1 | 4 | $(1,0)$, $(0,1)$, $(-1,0)$, $(0,-1)$ | minute 2 |
| 2 | 8 | $(2,0)$, $(1,1)$, $(0,2)$, $(-1,1)$, $(-2,0)$, $(-1,-1)$, $(0,-2)$, $(1,-1)$ | minute 3 |
| 3 | 12 | the twelve cells with $\lvert dx \rvert + \lvert dy \rvert = 3$ | minute 4 |

## 4. Worked trace for `n = 4`

Running the minutes one at a time on this instance gives the accumulation below. The totals in the fourth column are the answers the package's authored cases expect for the same values of $n$, so the trace doubles as a correctness check of the growth rule.

| Minute $k$ | Radius colored $r = k-1$ | New cells $4r$ | Total colored | Authored case it matches |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | `n = 1` expects `1` |
| 2 | 1 | 4 | 5 | `n = 2` expects `5` |
| 3 | 2 | 8 | 13 | `n = 3` expects `13` |
| 4 | 3 | 12 | 25 | `n = 4` expects `25` |

The new-cell column is the part worth staring at: `1, 4, 8, 12` is an arithmetic progression after the first term, not a constant and not a geometric sequence. The jump from `1` to `4` is the seed being a single cell; from minute 2 onward the increment is exactly $4$.

```mermaid
flowchart LR
    accTitle: Nested diamond rings grown around the seed cell
    accDescr: Minute one colors the seed, and each later minute colors the ring of cells at Manhattan distance k minus one, a ring that always holds four times its radius in cells.
    A["minute 1 radius 0 adds 1 cell"] --> B["minute 2 radius 1 adds 4 cells"]
    B --> C["minute 3 radius 2 adds 8 cells"]
    C --> D["minute 4 radius 3 adds 12 cells"]
    D --> E["total 25 colored cells"]
```

## 5. The same figure counted row by row

An independent check of `25` comes from slicing the radius-3 diamond into horizontal rows. A cell lies at vertical offset $dy$ only if $\lvert dy \rvert \le 3$, and such a row contains every $dx$ with $\lvert dx \rvert \le 3 - \lvert dy \rvert$, so its length is $2(3 - \lvert dy \rvert) + 1$.

| Row offset $dy$ | Allowed $dx$ | Cells in the row | Running total |
|---|---|---|---|
| $-3$ | $0$ | 1 | 1 |
| $-2$ | $-1, 0, 1$ | 3 | 4 |
| $-1$ | $-2, \dots, 2$ | 5 | 9 |
| $0$ | $-3, \dots, 3$ | 7 | 16 |
| $1$ | $-2, \dots, 2$ | 5 | 21 |
| $2$ | $-1, 0, 1$ | 3 | 24 |
| $3$ | $0$ | 1 | 25 |

The row lengths $1, 3, 5, 7, 5, 3, 1$ split into the odd numbers $1 + 3 + 5 + 7 = 16 = 4^2$ and the odd numbers $5 + 3 + 1 = 9 = 3^2$. That is the second closed form for this problem: a diamond of radius $n-1$ contains $n^2$ cells in its lower half including the middle row, and $(n-1)^2$ cells above it.

## 6. The closed form, and why the seed choice is irrelevant

Summing the rings gives the answer directly:

$$
1 + \sum_{k=2}^{n} 4(k-1) = 1 + 4\sum_{r=1}^{n-1} r = 1 + 4 \cdot \frac{(n-1)n}{2} = 2n(n-1) + 1 .
$$

The row-slicing identity gives the equivalent $n^2 + (n-1)^2$, and the two agree for every $n$ because $n^2 + (n-1)^2 = 2n^2 - 2n + 1$.

| $n$ | $n^2$ | $(n-1)^2$ | $2n(n-1) + 1$ | Authored expected output |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | `1` |
| 2 | 4 | 1 | 5 | `5` |
| 3 | 9 | 4 | 13 | `13` |
| 4 | 16 | 9 | 25 | `25` |
| 999 | 998001 | 996004 | 1994005 | `1994005` |
| 100000 | 10000000000 | 9999800001 | 19999800001 | `19999800001` |

Nothing in the derivation referred to the location of the seed, and that is not an accident: the invariant of Section 2 is stated in terms of the Manhattan distance to the seed, and every step of the induction uses only that distance. Since the grid is infinite and the neighbourhood rule is invariant under translations, reflections and quarter turns, the count after $n$ minutes is the same for every possible first choice.

## 7. Traps this instance exposes

| Decision | Wrong handling and its result at $n = 4$ | Correct outcome | Why the wrong reading fails |
|---|---|---|---|
| What "touches" means | counting corner contact too, which grows a square of side $2n-1$: $(2n-1)^2 = 49$ | `25` | diagonal neighbours differ by $2$ in Manhattan distance, so they lie on a different ring |
| Which radius a minute colors | using radius $k$ instead of $k-1$, which shifts every ring outward | `25` | minute 1 already colors the radius-0 ball, so minute $k$ extends to radius $k-1$ |
| The first minute | treating the seed as a ring of size $0$ and starting the sum at $4$ | `1` | the seed is one cell, and it is the only ring that is not a multiple of four |
| Arithmetic width | a 32-bit accumulator at $n = 10^{5}$, where the answer is `19999800001` | `19999800001` | the value exceeds $2^{31}-1$ even though $n$ itself is small |
| Integer division | dividing the triangular number by 2 after an inexact product, or dividing $4 \cdot (n-1) \cdot n$ in the wrong order | `25` | $(n-1)n$ is always even, so halving it first is exact at every $n$ |
| Effort spent | simulating cell by cell up to radius $n-1$ on an infinite grid | `25` | the ring sizes are known in closed form, so no region has to be materialized |

## 8. Time and auxiliary space

| Resource | Bound | Derivation |
|---|---|---|
| Time | $O(1)$ | the closed form costs a constant number of multiplications and one addition |
| Auxiliary space | $O(1)$ | two intermediate products and the result; no grid, ring list, or visited set is stored |

The last row of the trap table is the practical difference. A minute-by-minute accumulation of the ring sizes is $O(n)$ time and $O(1)$ auxiliary space, and it would still fit $n \le 10^{5}$, but it would materialize nothing and prove less. The closed form is preferred because the ring-size derivation shows the accumulation is a simple arithmetic series, which collapses to $2n(n-1)+1$ with constant work and needs no wider representation of the grid than the seed's own coordinates.