## General

**Turn bit strings into vertices of a hypercube**

Every legal number has exactly $m$ relevant binary positions after adding leading zeroes. Think of each $m$-bit number as a vertex of an $m$-dimensional hypercube. Two vertices share an edge when they differ in exactly one bit.

Moving along one edge flips one bit, so the shortest-path distance between two vertices is exactly their Hamming distance. This lets a breadth-first search compute minimum Hamming distances without comparing every pair in `nums`.

The array `dist` has one entry for every bit pattern from 0 through $2^m-1$. Every value appearing in `nums` is marked with distance zero. These are simultaneous BFS sources.

**Multi-source BFS**

The initial frontier `q = nums` contains all source values. At BFS layer `k`, the code considers every bit position $i$ and forms

`y = x ^ (1 << i)`.

XOR toggles exactly bit $i$, so `y` is one hypercube neighbor of `x`. If `dist[y] == -1`, this is the first time any source reaches `y`. BFS's layer order guarantees that `k` is the minimum Hamming distance from `y` to any input value. The code records it and places `y` in the next frontier.

After the BFS completes,

$$
\texttt{dist[v]}=\min_{a\in\texttt{nums}}\operatorname{Ham}(v,a)
$$

for every $m$-bit pattern $v$.

Duplicate values in `nums` appear more than once in the initial frontier, but `dist` still marks them as the same source vertex. They may cause repeated checks during the first layer, yet `dist[y] == -1` ensures each nonsource vertex is enqueued only once.

**Convert a maximum distance into a minimum distance**

The desired value for input $x$ is

$$
\max_{a\in\texttt{nums}}\operatorname{Ham}(x,a).
$$

Multi-source BFS naturally gives minimum distances, not maxima. The fixed-width complement supplies the bridge.

Let

`mask = (1 << m) - 1`

and `c = x ^ mask`, the bitwise complement of $x$ within exactly $m$ positions. At every bit position, $x$ and $a$ differ exactly when $c$ and $a$ agree. Therefore,

$$
\operatorname{Ham}(x,a)+\operatorname{Ham}(c,a)=m.
$$

Rearranging and maximizing over $a$ gives

$$
\max_a \operatorname{Ham}(x,a)
=m-\min_a\operatorname{Ham}(c,a).
$$

The minimum on the right is precisely `dist[c]`. This yields the returned expression

`m - dist[x ^ ((1 << m) - 1)]`.


The BFS invariant says that before layer $k$ begins, every vertex at distance less than $k$ from the source set has its final distance, and no undiscovered vertex is closer than $k$. Flipping each of the $m$ bits enumerates every edge, so all vertices at distance $k$ are discovered from layer $k-1$. By induction, `dist` contains exact nearest-source Hamming distances.

For each query value $x$, the complement identity holds independently for every possible partner $a$. The partner minimizing distance from the complement is exactly a partner maximizing distance from $x$. Substituting the BFS result therefore produces the requested maximum.

**Example**

Let $m=4$ and $x=12$, binary `1100`. Its four-bit complement is `0011`, value 3. If the nearest input value to `0011` is `1011` at Hamming distance 1, then the farthest Hamming distance from `1100` is $4-1=3$. Indeed, `1100` and `1011` differ in three positions.

The complement must be restricted to $m$ bits. Python's unlimited-width bitwise negation would create negative integers with infinitely many leading ones, so XOR with the finite mask is the correct operation.

## Complexity detail

There are $V=2^m$ hypercube vertices and $mV$ directed neighbor examinations. Every nonsource vertex is enqueued once, while duplicate initial sources can add at most $n$ extra frontier entries. Since $n\le2^m$, total time is $O(m2^m+n)$, usually written $O(m2^m)$.

Initializing `dist` costs $O(2^m)$, and creating the final answer costs $O(n)$. These terms are contained in the stated bound.

The distance array uses $O(2^m)$ space. The current and next frontiers can together hold $O(2^m)$ vertices. The returned answer has $O(n)$ entries; excluding required output, auxiliary space remains $O(2^m)$ because $n\le2^m$.

The assignment `q = nums` aliases the input list only for the initial frontier; the code does not mutate it and later rebinds `q` to a new list.

With $m\le17$, the state space has at most 131,072 vertices, making full hypercube exploration feasible. A pairwise method would cost $O(n^2)$ and can be much larger.

## Alternatives and edge cases

- **Compare every pair:** Compute `(a ^ b).bit_count()` for all pairs. It is simple but costs $O(n^2)$ time.
- **Run BFS from each input separately:** This repeats the same hypercube work $n$ times. Multi-source BFS combines all nearest-source computations in one traversal.
- **Bitwise trie search:** A trie can greedily prefer opposite bits to seek large Hamming distance, but maximizing total differing positions is not always captured by a single greedy path without richer state.
- **Subset transforms:** Min-plus or Boolean transforms over masks can propagate distance information, but BFS is the direct shortest-path interpretation.
- **Duplicate input values:** They receive identical answers. Duplicate initial frontier entries do not change distances, only some first-layer checks.
- **Complement also present:** If $x$'s exact complement is in `nums`, `dist[complement] = 0` and the answer is the maximum possible $m$.
- **All inputs identical:** The only available partner value is the same bit pattern, so every answer is zero, even if indices differ.
- **Leading zeroes:** The finite $m$-bit representation makes them real Hamming positions and is enforced by the mask.
- **m equal to one:** The hypercube has two vertices; answers are either zero or one depending on whether the opposite bit occurs.
- **Source list is nonempty:** The constraint has at least two entries, so BFS has sources and every hypercube vertex is eventually reached.
- **Frontier level value:** `k` starts at 1 because neighbors of source vertices are exactly one bit flip away.
- **Input preservation:** `q` initially references `nums`, but neither `pop` nor other mutation is used, so the caller's list remains unchanged.
