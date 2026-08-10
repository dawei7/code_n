## General

**Sweep across x and maintain the union of active y-intervals**

Imagine moving a vertical line from left to right. Between two consecutive rectangle x-boundaries, the set of rectangles intersected by the sweep line is constant. If their combined covered height is `H` and the horizontal distance to the next boundary is `\Delta x`, that vertical strip contributes:

$$
H\Delta x
$$

to the union area.

The challenge is maintaining `H` while rectangles begin and end, without double-counting overlapping y-ranges. A coordinate-compressed segment tree maintains the total length covered by at least one active rectangle.

**Create two x-events per rectangle**

For rectangle `[x1,y1,x2,y2]`:

- event `(x1,y1,y2,+1)` adds its y-interval when the sweep enters the rectangle;
- event `(x2,y1,y2,-1)` removes it when the sweep leaves.

All events are stored in `segs` and sorted by x. The set `alls` collects every y-boundary `y1` and `y2` for coordinate compression.

Only boundaries matter because coverage changes nowhere between consecutive boundary values.

**Compress coordinates into elementary intervals**

After sorting distinct y-values:

`alls = [Y0,Y1,\ldots,Yp]`.

The segment tree does not represent the coordinate points themselves. Leaf index `r` represents the elementary half-open interval:

$$
[Y_r,Y_{r+1}).
$$

There are `len(alls)-1` such intervals.

Dictionary `m` maps each original y-coordinate to its compressed boundary index. Rectangle interval `[y1,y2)` covers elementary interval indices:

`m[y1]` through `m[y2]-1` inclusive.

That is why `modify` receives those endpoints.

Coordinate compression preserves exact physical lengths because tree nodes calculate length from original values in `nums`, not from compressed index differences.

**What each segment-tree node stores**

Node `u` represents a contiguous range of elementary interval indices from `l` through `r`.

It stores:

- `cnt`: how many active updates fully cover this entire node range;
- `length`: the physical y-length within this range covered by at least one active rectangle.

The tree is built over all leaf intervals. Internal nodes split their index range in half.

**Range updates**

`modify(u,l,r,k)` adds `k` to the coverage counts over compressed interval range `[l,r]`:

- `k=+1` for a rectangle entering;
- `k=-1` for a rectangle leaving.

If the update fully contains the current node, its `cnt` changes directly. Otherwise, recursion visits intersecting children.

Afterward, `pushup(u)` recomputes this node's covered length.

**The central coverage rule**

If `tr[u].cnt` is nonzero, at least one active rectangle fully covers the node's complete interval range. Its union length is therefore the full physical span:

`nums[r+1] - nums[l]`.

It does not matter how many additional rectangles overlap it; union area counts covered length once.

If `cnt==0` and the node is a leaf, nothing covers its elementary interval, so length is zero.

If `cnt==0` and the node is internal, coverage may still come from partial updates stored below. Its length is the sum of its two child lengths.

This rule makes the root's `length` exactly the union height of all active rectangle y-intervals.

**Accumulate area before applying the current event**

At event `i` with x-coordinate `x`, the code first adds:

`tree.length * (x - previous_x)`.

The tree currently represents rectangles active immediately after the previous event and throughout the open strip up to `x`. Thus, this multiplication measures exactly that strip.

Only after adding the strip does the code apply the current event to prepare coverage for the next x interval.

For the first event there is no preceding strip, so `if i` skips area accumulation.

**Multiple events at the same x**

Sorted events with equal x are processed sequentially. Between them, `x-previous_x=0`, so they add zero area. After all events at that x are applied, the tree contains the correct combined active set for the next positive-width strip.

The temporary order of additions and removals at one x cannot affect area because no width lies between same-x events.

**Why overlaps are counted once**

Coverage counts allow several rectangles to cover the same tree interval. As long as `cnt>0`, `pushup` reports its physical length once, not once per rectangle.

When one rectangle leaves, count decreases but the interval remains fully covered if another full-cover update is active. When the count reaches zero, child coverage determines whether partial active rectangles still cover portions.

This is precisely union-length behavior.

**Example intuition**

If active rectangles cover y-ranges `[0,2)` and `[1,3)`, their individual heights total four, but their union is `[0,3)` of height three. Compressed leaves split at 0, 1, 2, and 3. Each elementary interval is marked covered at least once, and the root length sums them to three.

Multiplying by the current horizontal strip width counts the overlapping middle band only once.

**Why the entire sweep is correct**

Every rectangle contributes active coverage exactly for x in `[x1,x2)`. Events establish that state. Between adjacent event x-values, coverage is constant, and the segment-tree root gives its exact y-union length. Multiplying height by width gives the union area of that strip.

These strips are disjoint in x and cover every region where rectangles exist. Summing them produces the total union area without omission or duplication.

The final modulo is applied after the exact integer area is accumulated. Modular reduction at the end is safe because only the remainder is requested and Python integers do not overflow.

## Complexity detail

Let `n` be the number of rectangles. There are `2n` events and at most `2n` distinct y-coordinates.

Sorting events and y-values takes `O(n\log n)` time. The segment tree has `O(n)` nodes. Each event performs one compressed range update in `O(\log n)` time, so all updates cost `O(n\log n)`. Total time is `O(n\log n)`.

The events, compressed y-values, coordinate map, and segment tree each use `O(n)` space. Recursive build and update depth is `O(\log n)`. Total auxiliary space is `O(n)`.

All coordinate and area calculations are exact integers.

## Alternatives and edge cases

- **Coordinate-compressed 2D cells:** Mark every rectangle over compressed x-y cells and sum covered cells. With up to `O(n^2)` cells, it is simpler but uses and processes quadratic space.

- **Sweep with a sorted list of active intervals:** Recompute merged y-length at each x event in `O(n)`, giving `O(n^2)` worst-case time.

- **Inclusion-exclusion over rectangle subsets:** Exponential and impractical.

- **One rectangle:** Its enter event activates its height, its exit event closes the strip, and area is width times height.

- **Disjoint rectangles:** Their y-union or separate x-strips add normally.

- **Fully overlapping rectangles:** Coverage counts exceed one, but covered length is reported once.

- **Shared boundary only:** Half-open intervals and zero-width event gaps contribute no duplicate area.

- **Same x for many events:** Intermediate area increments are zero, and final active coverage is correct for the next strip.

- **Large coordinate gaps:** Original coordinate differences in `nums` preserve their true physical length.

- **Nonuniform compression:** Compressed index width is irrelevant; length uses `nums[r+1]-nums[l]`.

- **Removal while another rectangle remains:** Positive coverage count or child coverage keeps the interval active.

- **Modulo:** It is applied to the final total using `10^9+7`.

- **Input immutability:** Events and coordinate structures are new; rectangle records are not changed.
