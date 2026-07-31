## General

Computer $0$ is the only initially available root. Consider any later computer $i$. Every permitted predecessor has a smaller label, so repeatedly following predecessors must eventually reach label $0$. Complexity strictly decreases along that chain. Consequently, if `complexity[i] <= complexity[0]`, no such chain can exist and no permutation can unlock every computer.

This gives the complete feasibility test: `complexity[0]` must be strictly smaller than every other value. When that condition holds, computer $0$ itself is a valid predecessor for every $i>0$, regardless of which other computers have already appeared. The dependency rules then impose no ordering restriction among labels $1$ through $n-1$.

Fix computer $0$ first and permute the remaining $n-1$ distinct labels arbitrarily. There are $(n-1)!$ such orders. Scan the array once to reject any value at most the root, then multiply the integers from $2$ through $n-1$ modulo $10^9+7$.

## Complexity detail

The feasibility scan and factorial loop each take linear time, for total time $O(n)$. Only the root value, modular product, and loop variables are retained, so auxiliary space is $O(1)$.

The benchmark defines $S=n$ and uses arrays whose root is the unique minimum, forcing both complete linear passes. The calibrated slower implementation recomputes the minimum and its multiplicity for every prefix, taking $O(S^2)$ while returning the same count.

## Alternatives and edge cases

- **Dependency graph or topological sorting:** Explicitly building every usable edge can require $O(n^2)$ work, but the root-minimum observation determines feasibility without constructing a graph.
- **Sorting the complexities:** Sorting can detect the minimum in $O(n\log n)$ time, but it discards useful index structure and is slower than a direct scan.
- **Prefix minimum recomputation:** Checking every prefix independently is correct but repeats work and grows quadratically.
- **Strict inequality:** A later value equal to `complexity[0]` is just as impossible as a smaller value; the root must be the unique minimum.
- **Repeated values above the root:** They are allowed because each corresponding computer can still use computer `0` as its predecessor.
- **Permutation anchor:** Computer `0` is fixed first; counting $n!$ would incorrectly move the sole initial root among the other positions.
- **Modulo arithmetic:** Reduce each factorial multiplication modulo $10^9+7$ so the product remains bounded.
