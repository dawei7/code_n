## General

**The graph can only be a path or a cycle**

The graph is connected and every node has degree at most two.

If some node has degree one, connectivity and the degree bound force the whole graph to be one simple path. It has `n-1` edges.

If every node has degree two, the connected graph is one simple cycle. It has `n` edges.

Thus the source needs only:

`len(edges) == n`

to distinguish a cycle from a path. The identities of the edges affect which graph nodes receive which labels, but not the optimal score: along a path or cycle, labels can be arranged in any desired sequence.

**Rewrite adjacent products using squared differences**

For labels `a` and `b`:

`2ab = a^2 + b^2 - (a-b)^2`.

This identity transforms maximizing products into minimizing squared differences between adjacent labels.

The sum of label squares:

`1^2 + 2^2 + ... + n^2`

is fixed regardless of assignment. The only optimizable part is how far adjacent labels differ, plus endpoint effects for a path.

**Cycle score identity**

In a cycle, every label appears in exactly two edges. Summing the identity over all edges gives:

`score = sum(i^2) - (1/2) * sum_over_edges((a-b)^2)`.

Therefore, maximize score by minimizing the sum of squared absolute adjacent differences around the cycle.

**Lower-bound the cycle's total variation**

Let each edge difference magnitude be positive integer `d_e`. The cycle contains label one and label `n`. The two distinct arcs between those vertices must each change by total magnitude at least `n-1`. Hence:

`sum d_e >= 2(n-1)`.

There are `n` positive integer differences. For a fixed total at least `2n-2`, convexity of squares makes the smallest square sum occur when differences are as equal as possible. The ideal integer distribution is:

- two differences of one;
- `n-2` differences of two.

Their sum is `2 + 2(n-2) = 2n-2`, and square sum is:

`2*1^2 + (n-2)*2^2 = 4n-6`.

Thus every cycle assignment has squared-difference sum at least `4n-6`.

**Construct a cycle that reaches the bound**

Arrange labels as:

`1,3,5,...` in increasing odd order, followed by the even labels in decreasing order:

`...,6,4,2`.

Consecutive differences are two except:

- the transition between the largest odd-side and even-side labels is one;
- the closing edge from two back to one is one.

This exactly realizes the lower-bound pattern. Therefore the maximum cycle score is:

`sum(i^2) - (4n-6)/2`

`= sum(i^2) - 2n + 3`.

**Path score identity**

In a path, internal labels appear in two edges but endpoint labels `p` and `q` appear once. Summing the same identity gives:

`score = sum(i^2) - (p^2 + q^2 + sum d_e^2)/2`.

Now the objective is to minimize endpoint squares plus squared adjacent differences.

**Lower-bound the path variation**

Assume `p < q`. Any path ordering starts at `p`, ends at `q`, and must visit both extreme labels one and `n`. The minimum possible total absolute variation while visiting both extremes is:

`2(n-1) - (q-p)`.

One way to see this is the route from `p` down to one, across to `n`, then back to `q`. Any order visiting both extremes cannot use less movement on the number line.

For every positive integer `d`:

`d^2 >= 3d - 2`,

because `d^2-3d+2=(d-1)(d-2) >= 0` for integer `d>=1`.

Across the `n-1` path edges:

`sum d_e^2 >= 3 sum d_e - 2(n-1)`

`>= 4(n-1) - 3(q-p)`.

Also:

`p^2 + q^2 - 3(q-p) >= 2`.

Writing `q=p+D` with `p>=1,D>=1`, the left side is minimized at `p=1` and becomes:

`D^2-D+2 >= 2`.

Combining these bounds:

`p^2 + q^2 + sum d_e^2 >= 4n-2`.

**Construct a path that reaches its bound**

Use the same odd-increasing, even-decreasing sequence but do not close the final edge:

`1,3,5,...,6,4,2`.

The endpoints are one and two, whose squares sum to five. Among the `n-1` adjacent differences, one is one and `n-2` are two, giving squared sum:

`1 + 4(n-2) = 4n-7`.

Endpoint squares plus difference squares equal:

`5 + 4n-7 = 4n-2`,

meeting the lower bound. The maximum path score is therefore:

`sum(i^2) - (4n-2)/2`

`= sum(i^2) - 2n + 1`.

**Match the closed-form source**

The sum of squares formula is:

`n(n+1)(2n+1)/6`.

The source computes:

`path_score = sum_squares - 2n + 1`.

If edge count equals `n`, the graph is a cycle and the cycle optimum is exactly two larger:

`sum_squares - 2n + 3`.

It therefore returns `path_score + 2` for a cycle and `path_score` otherwise.

**Why no actual assignment is required**

The method returns only the maximum score. The constructive sequences prove the closed forms are attainable, and any path/cycle graph can receive those labels by walking through its vertices in order. There is no need to output or store the assignment.

## Complexity detail

The protected source performs a constant number of arithmetic operations and one `len(edges)` check. Under the standard word-RAM model, time and auxiliary space are `O(1)`.

It does not inspect individual edge endpoints. This is safe only because connectedness, simplicity, and maximum degree two guarantee that edge count fully identifies path versus cycle.

Python integer arithmetic technically depends on the bit length of `n`, but with `n<=50,000` values fit ordinary machine words. The returned score requires 64-bit range in fixed-width languages because the sum of squares grows as `Theta(n^3)`.

## Alternatives and edge cases

- **Dynamic programming over label permutations:** Completely unnecessary; the path/cycle structure and squared-difference identity yield a closed form.
- **Greedily put largest labels on high-degree nodes:** All cycle degrees are equal, and path internal degrees are equal, so degree alone cannot determine the optimal adjacent arrangement.
- **Sort labels monotonically along the path:** It creates one large endpoint effect and does not minimize the combined squared-difference objective as well as the odd/even arrangement.
- **Brute-force assignments:** There are `n!` possibilities and the closed-form proof dominates them.
- **Path graph:** Edge count `n-1` selects `sum squares -2n+1`.
- **Cycle graph:** Edge count `n` adds exactly two.
- **Two-node path:** Formula gives `1*2=2`, the only edge product.
- **Three-node cycle:** Formula gives `1*2+2*3+3*1=11`, independent of cyclic ordering.
- **Graph identities:** Node numbers do not matter; labels can be mapped along the discovered path or cycle.
- **Connectedness guarantee:** Without it, several path/cycle components would require distributing labels jointly and edge count alone would be insufficient.
- **Degree-at-most-two guarantee:** Without it, the graph need not be a path or cycle and the formula fails.
- **No repeated edges:** Supports the simple path/cycle classification.
- **Score overflow:** Use 64-bit arithmetic outside Python.
- **Manifest O(1):** The exact source genuinely uses constant problem-level work because it relies entirely on structural guarantees and edge count.
