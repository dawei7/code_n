## General

**Make the unique prime the owner of a valid path**

Every valid path contains exactly one prime-labeled node, so that prime can count the path without ambiguity. Remove all prime nodes temporarily. The remaining forest consists entirely of non-prime labels. Any path within one of its connected components contains no prime, and the size of that component tells how many endpoint choices it contributes when a neighboring prime is restored.

Compute primality for every label from $1$ through $n$ with the sieve of Eratosthenes. Then traverse only edges whose endpoints are both non-prime. Record the size of each resulting component on all of its nodes. Because the input is a tree, the total work across these traversals is linear after the sieve.

**Count paths around one prime**

Fix a prime node `p`. Ignore its prime neighbors: crossing such an edge would immediately put at least two prime labels on the path. Each non-prime neighbor belongs to one adjacent component. Let their sizes be $s_1,s_2,\ldots,s_k$.

A valid path owned by `p` has one of two forms:

- one endpoint is `p` and the other is any node in one adjacent component, contributing $\sum_i s_i$ paths;
- the endpoints lie in two different adjacent components, contributing $\sum_{i<j}s_i s_j$ paths.

Endpoints from the same component do not qualify through `p`: their unique tree path stays inside that component and never reaches `p`.

Accumulate the pair products without a nested loop. Before processing a component of size `size`, let `previous` be the total size of earlier components. Add `previous * size`, then include `size` in `previous`. After all components, add `previous` for paths whose endpoint is `p` itself.

Every counted path contains `p` and no other prime. Conversely, any valid path reaches its unique prime from either one adjacent non-prime component or two distinct ones, so it appears in exactly one of these terms and is counted once.

## Complexity detail

Let $n$ be the number of nodes. The sieve takes $O(n \log \log n)$ time. Constructing the adjacency list, finding all non-prime components, and scanning the neighbors of every prime together take $O(n)$ time because a tree has $n-1$ edges. The total time is therefore $O(n \log \log n)$.

The primality table, adjacency list, component sizes, traversal stacks, and temporary component nodes use $O(n)$ space.

The benchmark uses $n$ as `size` and supplies legal chains from 16 through 256 nodes. Component contraction scales with the tree size. A correct implementation that traverses the tree independently from every possible first endpoint completes all tiers but exhibits $O(n^2)$ scaling.

## Alternatives and edge cases

- **All-pairs tree traversal:** Starting a traversal at every node can count the same valid pairs correctly, but it takes $O(n^2)$ time and cannot handle $10^5$ nodes.
- **Disjoint-set union:** Non-prime components can also be built by unioning every edge with two non-prime endpoints. This has near-linear time but requires a separate parent-and-size structure.
- **Prime-to-prime edge:** No valid path can cross an edge whose two endpoint labels are both prime because it already contains two primes.
- **Prime endpoint:** Paths from a prime to nodes in one adjacent non-prime component are valid and form the $\sum_i s_i$ term.
- **Same non-prime component:** Two nodes in the same component have a prime-free path and must not be counted for a neighboring prime.
- **Unordered endpoints:** Pair products select two different components without assigning an orientation, so each path is counted once.
- **Singleton tree:** There is no pair of distinct endpoints, so the answer is zero regardless of label primality.
- **Large answer:** The number of paths can be quadratic in $n$, requiring a 64-bit integer type in fixed-width languages.
