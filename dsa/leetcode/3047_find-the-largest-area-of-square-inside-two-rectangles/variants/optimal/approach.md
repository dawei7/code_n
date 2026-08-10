## General

**A square must fit inside a rectangle intersection.** For rectangles $R_1$ and $R_2$, their overlap—if it has positive area—is another axis-aligned rectangle. Its horizontal interval begins at the larger left boundary and ends at the smaller right boundary. Therefore its width is

$$
w=\min(x_2,x_4)-\max(x_1,x_3).
$$

Similarly, overlap height is

$$
h=\min(y_2,y_4)-\max(y_1,y_3).
$$

The largest axis-aligned square that fits in a $w$ by $h$ rectangle has side

$$
e=\min(w,h).
$$

Its area is $e^2$.

**Enumerate every rectangle pair.** `zip(bottomLeft, topRight)` associates each rectangle's two corners. `combinations(..., 2)` produces every unordered pair exactly once. The tuple unpacking gives coordinates of both rectangles directly.

For each pair, the source computes `w`, `h`, and `e`. Only when `e > 0` is there a square with positive side length. It updates `ans` with `e * e`.

**Why touching is not enough.** If rectangles meet only along an edge, one overlap dimension is zero. If they are disjoint in a dimension, that dimension is negative. In either case `e <= 0` and no positive-area square fits. The source correctly rejects both.

**Why checking pairs covers intersections of more than two rectangles.** The statement allows a square inside the intersection of at least two rectangles. If a square lies in three or more rectangles, it also lies in the intersection of every pair among them. Therefore some enumerated pair already witnesses that square. Maximizing pairwise intersections cannot miss a solution supported by a larger group.

Conversely, a square found inside one pair's overlap satisfies “at least two,” so every candidate counted is legal.

**A trace.** Suppose rectangles overlap horizontally from $x=2$ to $x=5$, giving width 3, and vertically from $y=4$ to $y=6$, giving height 2. The largest square side is 2 and area is 4. The extra horizontal unit cannot increase side length because the vertical dimension is the bottleneck.
For a fixed pair, any contained square's side cannot exceed overlap width or height, so it is at most $\min(w,h)$. When that minimum is positive, a square of exactly that side can be placed within the overlap, so the bound is attainable. Thus `e * e` is exactly the best area for the pair. Taking the maximum over every pair yields the global answer.

**No coordinate sweep is needed.** With at most 1000 rectangles, there are about half a million pairs. Constant arithmetic per pair is within bounds and avoids complicated plane-sweep structures.

## Complexity detail

For $N$ rectangles, `combinations` emits $N(N-1)/2=O(N^2)$ pairs. Each uses constant arithmetic, so time is $O(N^2)$.

The manifest describes $O(1)$ auxiliary space at the high-level algorithmic level. In CPython, however, `itertools.combinations` first converts its input iterable to a tuple pool. Because the input here is `zip(bottomLeft, topRight)`, that pool contains $N$ paired references and uses $O(N)$ auxiliary space. The iterator then stores constant index state.

Thus the exact Python source has $O(N)$ peak auxiliary space. The input coordinate arrays are not mutated.

## Alternatives and edge cases

- **Nested index loops:** They compute the same pairs and can avoid `combinations`' tuple pool, reaching genuine $O(1)$ extra space.
- **Plane sweep:** It is useful for more complex overlap queries but unnecessary for $N\le1000$ and pairwise square maximization.
- **Check only intersection area:** A large narrow rectangle may have large area but support only a small square; the relevant value is the smaller dimension.
- **Disjoint rectangles:** A negative width or height makes `e <= 0`, so the pair contributes nothing.
- **Edge or point contact:** Zero overlap dimension cannot contain a positive-area square and is rejected.
- **One rectangle contained in another:** Their overlap is the smaller rectangle; the formula handles it directly.
- **More than two overlapping rectangles:** Any feasible square is witnessed by a pair, so pair enumeration is sufficient.
- **Equal best areas:** Only the numeric maximum is requested, so no pair identity must be retained.
- **Large coordinates:** Differences and squaring fit comfortably in Python integers.
- **Input preservation:** Neither corner array is sorted or changed.
- **Manifest mismatch:** CPython's combinations pool makes exact peak space linear, despite constant per-pair state.
- **Axis alignment:** Rectangle edges are axis-aligned, and the source assumes the fitted square uses those same axes. The smaller overlap dimension is therefore the limiting side without any rotation calculation.
- **Why area is computed after side maximization:** Maximizing positive side length also maximizes its square because $e^2$ is increasing for $e>0$. Comparing areas or sides would select the same pair.
- **No need to construct square coordinates:** Once positive overlap width and height are known, placing a side-$e$ square at the overlap's bottom-left corner witnesses feasibility. Only its area is requested.
- **Unordered pair generation:** Intersecting rectangle $i$ with $j$ is identical to intersecting $j$ with $i$, so `combinations` avoids duplicate geometric work without losing candidates.
