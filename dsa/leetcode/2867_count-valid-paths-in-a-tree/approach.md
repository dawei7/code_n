## General

**Every valid path has one distinguished prime.** A path is valid when exactly one node label on it is prime. Name that unique prime `p`. Remove all prime nodes conceptually. The remaining non-prime nodes split into connected components. Any valid path centered at `p` can have an endpoint at `p` itself or extend from `p` into one adjacent non-prime component on each side. It may never pass through a second prime.

This suggests two stages: identify the connected components made only of non-prime nodes, then count endpoint combinations around each prime.

**Precomputing primality.** The module creates boolean array `prime` up to a fixed bound above the maximum legal label. It marks zero and one non-prime. For each still-prime `i`, it marks multiples beginning at `i*i` composite. Smaller multiples already have a smaller prime factor and were marked earlier. This is the sieve of Eratosthenes.

**Contract non-prime regions with union-find.** While building the undirected adjacency list, the solution examines each edge `u-v`. If both endpoint labels are non-prime, expressed compactly as `prime[u] + prime[v] == 0`, it unions them. The union-find structure stores a representative and size for each component. Path compression in `find` and union by size make later representative queries very cheap.

No edge touching a prime is unioned. Therefore, after all edges are processed, `uf.size[uf.find(j)]` is exactly the number of non-prime nodes reachable from non-prime node `j` without crossing any prime.

**Count paths around one prime without double counting.** For each prime label `i`, the code scans its tree neighbors. Prime neighbors are ignored because any path using both prime endpoints would already contain at least two primes. For a non-prime neighbor `j`, `cnt` is the size of that adjacent non-prime component.

There are `cnt` valid paths with one endpoint at prime `i` and the other at a node of this component, so the source first adds `cnt`.

There are also paths whose endpoints lie in two different non-prime components adjacent to `i`. Every such path travels from the first component through `i` into the second and contains exactly that one prime. Variable `t` is the total size of components processed before the current one. Thus `t * cnt` counts all pairs choosing one endpoint from an earlier component and one from the current component. The code adds that product, then updates `t += cnt`.

This incremental product is equivalent to summing `size_a * size_b` over every unordered pair of adjacent components, but it uses constant state per prime.

**Why adjacent component identities cannot repeat.** In a tree, two different neighbors of the same prime cannot belong to the same non-prime component. If a non-prime path connected those neighbors without using the prime, adding their two edges to the prime would form a cycle. The tree guarantee forbids that. Consequently, scanning neighbors counts each component once without needing a local set.

**Why every valid path is counted once.** Take any valid path and its unique prime `p`. Removing `p` separates the two path sides. If one endpoint is `p`, the path is included in the `cnt` term for the other endpoint's component. Otherwise, its endpoints lie in two distinct non-prime components adjacent to `p` and are included once when the later of those components is processed in `t * cnt`. The path cannot be counted around another prime because it contains no other prime.

Conversely, every endpoint choice counted by either term has a unique tree path that passes through current prime and otherwise stays within non-prime components. It therefore contains exactly one prime and is valid.

## Complexity detail

Let $M$ be the fixed sieve bound and $n$ the tree size. The sieve costs $O(M\log\log M)$ time and $O(M)$ space as module-level preprocessing. Building the graph and processing edges uses $O(n)$ adjacency storage. Union-find operations total $O(n\alpha(n))$, effectively linear, and the final neighbor scans examine $2(n-1)$ adjacency entries.

Thus per call after preprocessing, time is $O(n\alpha(n))$ and space is $O(n)$; including sieve initialization, time is $O(M\log\log M+n\alpha(n))$ and space is $O(M+n)$. With $M$ fixed near $10^5$ and labels bounded by $n$, this is commonly summarized as $O(n\log\log n)$ time and $O(n)$ space.

## Alternatives and edge cases

- **DFS each non-prime component:** A graph traversal can label component sizes instead of union-find. It has the same linear asymptotic behavior but needs explicit visited state.
- **Path enumeration:** Checking every node pair and inspecting its path is at least quadratic and cannot handle $10^5$ nodes.
- **Prime-prime edge:** It contributes no path because even the two-node path contains two primes.
- **Prime with one non-prime component:** Only paths from the prime to nodes in that component are counted; there is no cross-component product.
- **Prime leaf:** If its sole neighbor is non-prime, every node in that neighbor's component forms one valid endpoint pair with the leaf.
- **Label one:** One is non-prime and is correctly available inside union-find components.
- **Single-node tree:** There are no endpoint pairs or edges. Whether label one is non-prime, the returned path count is zero.
- **Wide answer:** The number of paths can be quadratic in $n$, so fixed-width implementations need 64-bit accumulation.
