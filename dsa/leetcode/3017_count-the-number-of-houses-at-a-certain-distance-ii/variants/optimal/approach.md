## General

**See the graph hidden inside the street.** Houses $1$ through $n$ normally form a path: each house is connected to the next one. The extra street between $x$ and $y$ either changes nothing or turns part of that path into a cycle. The answer array is a distance histogram. Entry `answer[d - 1]` must contain the number of ordered pairs of distinct houses whose shortest-path distance is $d$. “Ordered” matters: if houses $a$ and $b$ are distance $d$ apart, both $(a,b)$ and $(b,a)$ contribute.

The exact solution constructs this histogram through closed-form pieces instead of inspecting every pair. Its arrays use zero-based indices, so index $q$ represents distance $q+1$.

**Handle a useless extra street immediately.** When $|x-y|\le 1$, the added street is either a self-loop or duplicates an existing path edge. It cannot shorten any route. In an ordinary path of $n$ houses, there are $n-d$ unordered pairs at distance $d$, hence $2(n-d)$ ordered pairs. The return value

`[2 * x for x in reversed(range(n))]`

is `[2(n-1), 2(n-2), ..., 2, 0]`. The final zero corresponds to distance $n$, which no pair of distinct houses can have.

**Decompose the useful case into a cycle and tails.** Assume $x<y$ after the code's normalization. The original path from $x$ to $y$ has $y-x$ edges; adding the shortcut edge $(x,y)$ creates a cycle of length

$$
L = y-x+1 = |x-y|+1.
$$

There are $x-1$ houses in the left tail and $n-y$ houses in the right tail. Every shortest route can now be understood using this cycle-with-two-tails shape. For two cycle locations, the shorter direction around the cycle wins. For a tail-to-cycle pair, the tail distance is added to the nearer of the two cycle directions. For a left-tail-to-right-tail pair, the shortcut acts as a contracted connection between the attachment points.

**Establish the backbone histogram.** The code defines `n2 = n - cycle_len + 2` and initializes

`res = [2 * x for x in reversed(range(n2))]`.

This is the ordered-pair histogram of a path obtained by collapsing the interior of the cycle while retaining its two attachment positions. It supplies the baseline contributions that behave like distances along the two tails and across the shortcut backbone. The list is then padded with zeros until it has exactly $n$ entries, because the required output always has length $n$.

This baseline is not yet the complete answer. Collapsing the cycle discarded the choices of internal cycle houses, so the solution adds their distance distributions in two carefully designed layers.

**Add distances entirely inside the cycle.** For a cycle of length $L$, each vertex has two vertices at distance $d$ for every $1\le d<L/2$. Therefore there are $2L$ ordered pairs at each such distance. If $L$ is even, every vertex has exactly one antipodal vertex at distance $L/2$, producing $L$ ordered pairs rather than $2L$.

The array `res2` encodes exactly these counts:

`res2 = [cycle_len * 2] * (cycle_len >> 1)`

creates one entry for each possible positive cycle distance. For even $L$, `res2[-1] = cycle_len` applies the antipodal correction. Then `res2[0] -= 2` removes the two orientations of the shortcut endpoints, because that distance-one relationship is already present in the collapsed backbone. Adding `res2` into `res` restores all other within-cycle ordered pairs without double counting.

**Add interactions between each tail and the cycle interior.** The loop runs once for `tail1 = x - 1` and once for `tail2 = n - y`. A zero-length tail contributes nothing. For a nonempty tail, `res3` is a closed-form histogram for pairs having one endpoint in that tail and the other in the non-collapsed part of the cycle.

The shortest distance from a tail house to a cycle house equals its distance to the attachment point plus the smaller direction around the cycle. As the cycle endpoint moves away from the attachment, the number of endpoint choices rises symmetrically from both directions around the cycle, may form a plateau, and then falls. Ordered orientations and the two cycle directions make the interior contribution change in multiples of four. That is why the code builds a block initially filled with `val_mx`, writes the ascending and mirrored values `4, 8, ...` near its ends, and then makes parity corrections.

The statements `res3[0] = res3[1] = 0` remove relationships already owned by the backbone representation. When $L$ is even, the unique antipodal location has only one shortest cycle direction rather than two, so `res3[-1] = 0` and the later even-cycle loop correct that central layer. The loop `for i in range(1, tail + 1): res3[i] += 2` accounts for the two ordered orientations as the chosen tail endpoint gets farther from its attachment. Finally, `res3` is added element by element to the global histogram.

Although these index manipulations are compact, their purpose is consistent: partition all ordered pairs among a contracted backbone, pairs internal to the cycle, and the omitted tail-to-cycle interactions. Those classes cover every pair, and the explicit subtraction/corrections prevent overlap. Therefore the resulting histogram counts every ordered pair once at its true shortest distance.

**Why the output still has $n$ positions.** The largest possible finite distance in this graph is below $n$, especially after adding a shortcut. The problem nevertheless requests $n$ buckets for distances $1$ through $n$. Padding with zeros preserves that interface, and buckets beyond the graph's diameter correctly remain zero.

## Complexity detail

Let $N=n$ and $L=|x-y|+1$. Creating the baseline list and padding it costs $O(N)$. The cycle histogram has $O(L)$ entries. Each of the two tail passes creates and edits a list whose length is $O(N)$ in the worst case, and its loops are linear in the tail length or the corresponding histogram length. Adding each temporary histogram to `res` is also linear in its size. There are only two tails, so all work sums to $O(N)$ time.

The returned list itself has $N$ entries and necessarily uses $O(N)$ output space. The temporary lists `res2` and `res3` can also contain $O(N)$ integers, so the exact implementation uses $O(N)$ auxiliary space in addition to the output. Its peak remains linear because only a constant number of linear-sized lists are live.

The manifest's high-level description may suggest range additions, but the protected source does not use a difference array or deferred range updates. It explicitly constructs and adds the closed-form histograms. The asymptotic bound is still $O(N)$; documenting the actual mechanism matters for understanding both the proof and memory behavior.

## Alternatives and edge cases

- **Enumerate every ordered pair:** Running a shortest-distance formula for all $N(N-1)$ pairs is conceptually direct but costs $O(N^2)$ time, which does not meet the large input bound.
- **Breadth-first search from every house:** The graph has only $O(N)$ edges, but $N$ BFS traversals still cost $O(N^2)$ time and add considerable overhead.
- **Difference-array pair counting:** One can derive another linear solution by classifying endpoint ranges and applying range increments. That can be elegant, but it is not what this exact source implements; this source builds explicit cycle-and-tail histograms.
- **Self-loop, $x=y$:** The edge returns to the same house and cannot shorten a path. The `abs(x - y) <= 1` branch correctly returns the ordinary path counts.
- **Adjacent endpoints:** An extra edge between already adjacent houses duplicates the existing connection. This is handled by the same early branch.
- **Reversed input endpoints:** The cycle length uses an absolute difference, then the code swaps `x` and `y` when necessary before calculating tail lengths. The answer is therefore symmetric in the supplied endpoint order.
- **No left or right tail:** If the shortcut touches house 1 or house $n$, one tail length is zero. The corresponding contribution is skipped, avoiding invalid indexing and correctly leaving only the other tail.
- **Even cycle:** The opposite vertex is unique at distance $L/2$, so counts at that distance are $L$, not $2L$. The source has explicit even-parity corrections in both the cycle-only and tail interaction histograms.
- **Odd cycle:** There is no single antipodal vertex. Two directions remain distinct up to distance $\lfloor L/2\rfloor$, so the general $2L$ cycle count applies.
- **Ordered rather than unordered pairs:** Every geometric relationship contributes in both directions. The factors of two and four in the formulas encode those orientations; dividing the result by two would answer a different question.
- **Last bucket:** Distance $N$ is impossible between distinct houses in an $N$-vertex connected graph, so the last result entry is always zero.
