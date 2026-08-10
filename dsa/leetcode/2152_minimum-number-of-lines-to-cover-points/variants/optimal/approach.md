## General

There are at most ten points, so an exponential subset dynamic program is practical. A bitmask records which points are already covered, and each transition adds one line that covers at least one previously uncovered point.

**Test collinearity without division**

For three points $P_i=(x_1,y_1)$, $P_j=(x_2,y_2)$, and $P_k=(x_3,y_3)$, the helper returns true when

$$
(x_2-x_1)(y_3-y_1)=(x_3-x_1)(y_2-y_1).
$$

These are equal cross products. Equality means the direction vectors from $P_i$ to the other two points have zero cross product and lie on the same straight line.

This formulation handles vertical lines naturally and avoids floating-point slopes or division by zero. All coordinates and products remain exact integers.

**Define the covered-state recurrence**

In `state`, bit `i` equals one when point `i` has already been covered by some selected line. The full state is `(1 << n) - 1`, with every bit set. It needs no more lines, so `dfs(full_state)` returns zero.

For a non-full state, the helper searches transitions and initializes `ans = inf`. Whenever it finds an uncovered point `i`, it considers drawing a line through `i` and every later point `j`.

The mask begins as

`nxt = state | 1 << i | 1 << j`.

This marks both defining points covered. Point `j` may already have been covered; it is still a real geometric point and may define a useful new line through the uncovered `i`.

The inner `k` loop checks later points. If point `k` is not already covered and is collinear with `i` and `j`, its bit is added to `nxt`. One recursive transition then costs `dfs(nxt) + 1` because one new line has just been drawn.

**Why considering pairs is sufficient**

Any useful line covering at least two input points can be defined by two of those points. Once its pair is chosen, all other collinear points may be covered by the same line.

The exact code checks only `k > j`. If a desired line contains several uncovered points after `i`, the transition that chooses the smallest-index one as `j` includes every later collinear point. Transitions choosing a later `j` may omit an earlier collinear point, but the minimum considers the complete transition as well, so the optimum is not lost.

**Cover a single remaining point**

A straight line may cover one point even when no useful second uncovered point remains: infinitely many lines pass through one point. For `i < n-1`, the code can pair `i` with any later point, even one already covered, and thereby add a line covering `i`. For the last index there is no later `j`, so the special condition `if i == n - 1` adds `dfs(state | 1 << i) + 1`.

This guarantees that every non-full state has a way to make progress.

**Memoize repeated covered subsets**

Different sequences of chosen lines can produce the same covered mask. The `@cache` decorator stores the best answer for each `state`, so that subset is solved only once.

The recurrence has optimal substructure: after choosing the next line, only the newly covered set matters. Earlier line identities do not affect which future points remain or how they can be covered.

**Why the result is minimal**

Every transition corresponds to a real line through two points, or the special one-point line, and marks only points lying on that line. Therefore a recursion path using $q$ transitions constructs a valid $q$-line cover.

Conversely, consider an optimal cover for the points not yet covered in a state. Choose one of its lines containing an uncovered point `i`. If it covers another suitable indexed point, one pair transition can represent the same line; choosing the earliest later defining point ensures its later collinear points are included. If it covers only the final remaining point, the singleton transition represents it. The recursion considers a transition compatible with an optimal first line and then optimally solves the remaining mask. Taking the minimum returns the global optimum.

## Complexity detail

There are at most $2^n$ covered masks. In the exact source, one state may run three nested point loops over `i`, `j`, and `k`, and `check` is recomputed inside those loops. A direct worst-case bound is therefore $O(2^n n^3)$ time.

The manifest’s $O(n^3+n2^n)$ bound corresponds to precomputing a coverage mask for every point pair and then using a more tightly structured subset DP. The exact stored solution does not perform that precomputation, so its written bound is higher, although $n\le10$ keeps it practical.

The cache can store $O(2^n)$ integer results. Recursive depth is at most $n$ because every transition covers at least one new point. Aside from the cache and call stack, only scalar masks and coordinates are used, so peak auxiliary space is $O(2^n+n)$, conventionally $O(2^n)$.

## Alternatives and edge cases

- **Precompute pair line masks:** For every pair, scan all points once to build its collinear mask, then transition using stored masks. This produces the manifest’s $O(n^3+n2^n)$ style and avoids repeated geometry checks.
- **Always choose the first uncovered point:** Restricting each state to one canonical uncovered `i` reduces redundant transitions while preserving optimality.
- **Slope as floating point:** Comparing divided slopes risks precision errors and vertical-line exceptions. Cross multiplication is exact.
- **Greedy line with most uncovered points:** Covering the most points now need not minimize the total number of later lines; subset DP explores the interactions.
- **One point:** The full pair loop is unavailable, and the last-index singleton branch returns one.
- **Two points:** One line through them covers both, so the answer is one.
- **All points collinear:** Choosing the earliest pair adds every later point and reaches the full mask with one line.
- **No three collinear:** Each line can cover at most two points, giving $\lceil n/2\rceil$ lines.
- **Vertical line:** The cross-product equation works when all relevant $x$ differences are zero.
- **Negative coordinates:** Integer subtraction and multiplication handle them without special cases.
- **Already-covered defining point:** A later covered `j` may still define a line that covers an uncovered `i` and additional points.
- **Unique points:** Distinct coordinates ensure a pair really determines a line.
- **Cached state meaning:** It depends only on covered points, not on the line used to arrive there.
- **Input preservation:** Point coordinates are read but never modified.
