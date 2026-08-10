## General

For each query, the physical route is fixed. Alice must repeatedly follow parent links from her starting node to the lowest common ancestor, and Bob must do the same from his starting node. The only choices are which gate instance each person uses and, as a result, which card color they hold after each move.

The two people act independently once the LCA is known. Therefore the number of joint ways is

$$
\text{AliceWays}\cdot\text{BobWays}\pmod{10^9+7}.
$$

The difficulty is answering many queries without walking one parent edge at a time. The source uses binary lifting for both parts:

- ancestor tables find each LCA in `O(\log n)`;
- matrix tables count all card transitions along a long upward path in `O(\log n)`.

**One node is a two-state transition matrix**

Card value zero means blue and card value one means red. Suppose node `u` has gate counts

$$
[\texttt{red}_u,\texttt{blue}_u,\texttt{white}_u].
$$

When leaving `u`:

- blue to blue has `blue_u` choices;
- blue to red has `white_u` choices;
- red to blue has `white_u` choices;
- red to red has `red_u` choices.

These four counts form the matrix

$$
M_u=
\begin{bmatrix}
\texttt{blue}_u & \texttt{white}_u\\
\texttt{white}_u & \texttt{red}_u
\end{bmatrix}.
$$

Rows represent the card color before the move, and columns represent the color after the move. The source stores the matrix as a row-major tuple:

```python
(blue, white, white, red)
```

Each gate instance is counted separately, so a matrix entry contains a count rather than a boolean. A zero entry means that particular color transition is impossible at that node.

**Why matrix multiplication counts consecutive gate choices**

Suppose a person first leaves node `u` and then leaves its parent `v`. For starting color `a` and ending color `c`, the intermediate color `b` can be blue or red. The number of two-move gate sequences is

$$
\sum_{b\in\{0,1\}}M_u[a,b]M_v[b,c].
$$

This is exactly entry `[a,c]` of matrix product `M_uM_v`.

The multiplication order follows movement order: the lower node's matrix comes first, followed on the right by the next node's matrix. Every product term chooses one specific gate at each node, so distinct gate sequences remain distinct.

The helper `multiply(left,right)` implements ordinary `2\times2` multiplication and reduces every entry modulo `10^9+7`. Modular reduction is safe because only additions and multiplications of counts remain.

**The gate at the destination LCA is not used**

A gate is selected when moving from a node to its parent. Once a person reaches the LCA, movement stops. Therefore a path from node `u` upward by distance `d` uses the matrices of exactly `d` nodes:

$$
u,\ \texttt{parent}[u],\ldots
$$

ending with the node immediately below the ancestor. It does not multiply the ancestor's gate matrix.

If the start already equals the LCA, the distance is zero, no gate is used, and there is exactly one empty sequence.

**Preparing depths without recursion**

The source builds child lists from the parent array, then uses an explicit stack beginning at root zero. When it visits a child, it records

```python
depth[child] = depth[node] + 1
```

and pushes that child for later processing.

Since the input is a valid rooted tree, every non-root node appears in exactly one child list and receives its depth exactly once. The iterative stack avoids recursion-depth problems on a long chain.

**Binary-lifting ancestor table**

Let `ancestors[b][u]` be the ancestor reached by moving `2^b` edges upward from `u`.

At level zero, one upward move reaches `parent[u]`. For the root, the source stores zero itself so that table lookups remain valid:

```python
ancestors[0][u] = parent[u]  # non-root
ancestors[0][0] = 0
```

For a larger jump, first move `2^{b-1}` steps to `middle`, then make another jump of the same length:

$$
\texttt{ancestors}[b][u]
=
\texttt{ancestors}[b-1]
[\texttt{ancestors}[b-1][u]].
$$

There are `\lceil\log_2 n\rceil` relevant jump sizes, supplied by `n.bit_length()`.

**Binary-lifting matrix table**

In parallel, `matrices[b][u]` is the product of gate matrices for the `2^b` consecutive departure nodes beginning at `u`.

The base table is

$$
\texttt{matrices}[0][u]=M_u.
$$

For a double-length segment, `middle` is the node reached after the first half. The route uses the first half's gates and then the second half's gates, so:

$$
\texttt{matrices}[b][u]
=
\texttt{matrices}[b-1][u]
\cdot
\texttt{matrices}[b-1][middle].
$$

The ancestor and matrix tables are built together because both use the same midpoint.

The root's base matrix exists in the table, and jumps above the root are clamped to zero. Valid query distances never overshoot their requested ancestor, so repeated-root padding is never included in a counted route.

**Finding the LCA**

The `lift(node,distance)` helper decomposes `distance` into powers of two. For every set bit `b`, it replaces `node` with `ancestors[b][node]`. This moves upward exactly the requested number of edges in `O(\log n)` time.

To find the LCA of `first` and `second`:

1. swap them if needed so `first` is at least as deep;
2. lift `first` until both depths match;
3. if they are now equal, that node is the LCA;
4. otherwise inspect jump sizes from largest to smallest and lift both whenever their `2^b` ancestors differ;
5. after this process, the two nodes are distinct children of their LCA, so return either immediate parent.

The large-to-small step keeps both nodes below the LCA while moving them upward as far as possible.

**Counting gate sequences along one upward path**

`count_paths(node,ancestor,card)` begins with the identity matrix

$$
I=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}.
$$

It computes the distance from `node` to `ancestor` and decomposes that distance into powers of two. Whenever bit `b` is set, it appends the corresponding path segment:

```python
product = multiply(product, matrices[bit][node])
node = ancestors[bit][node]
```

Although bits are inspected from low to high, `node` advances after every selected chunk. The chunks therefore remain in their actual bottom-to-top route order. Matrix multiplication appends each later chunk on the right.

When all chunks are processed, `product[a][c]` counts sequences starting with card `a` and arriving at the ancestor with card `c`. Either final card is acceptable, so the source sums both entries of the starting row.

In flattened storage, row zero begins at index zero and row one begins at index two. That explains:

```python
row = 2 * card
return (product[row] + product[row + 1]) % MODULO
```

For a zero-length route, `product` remains the identity. Either row sums to one, correctly counting the single no-move sequence.

**Combining and XORing queries**

For each query, the source finds one LCA, evaluates Alice's path and Bob's path separately, multiplies their counts modulo `MODULO`, and XORs that residue into `answer`.

Multiplication is appropriate because any valid Alice gate sequence can be paired with any valid Bob gate sequence. If either count is zero, no joint route exists and the product is zero.

The XOR is applied after the per-query modular product. It is not a modular sum, and no final modulo is taken over the XOR accumulator.

## Complexity detail

Let `q` be the number of queries and `L=\lceil\log_2 n\rceil`.

Building child lists and depths costs `O(n)`. The ancestor and matrix tables each have `L` levels and `n` entries per level. Every entry requires constant work because a `2\times2` matrix multiplication has eight scalar multiplications and four additions. Preprocessing time is `O(n\log n)`.

Each LCA query takes `O(\log n)`. Each of the two path-count calls also processes at most `O(\log n)` bits. Therefore all queries take `O(q\log n)`, and total time is

$$
O((n+q)\log n).
$$

The child lists, depths, and traversal stack use `O(n)` space. The two lifting tables dominate with `O(n\log n)` entries. Each matrix entry is a fixed four-integer tuple, so total auxiliary space is `O(n\log n)`.

The query helpers use only constant scalar state beyond the precomputed tables. Inputs are not modified.

## Alternatives and edge cases

- **Walk to the LCA one edge at a time:** This is simple but can cost `O(n)` per person per query on a chain, producing `O(nq)` total time.

- **Enumerate gate choices:** A path can have exponentially many gate sequences. Matrix entries count all sequences without generating them.

- **Track only a total number of ways:** The next node's usable gates depend on current card color. Blue-ending and red-ending counts must remain separate until the route stops.

- **Use matrix addition between nodes:** Consecutive choices combine multiplicatively through possible intermediate colors. Matrix multiplication performs exactly that sum-of-products composition.

- **Reverse matrix order:** `M_uM_{\texttt{parent}[u]}` follows upward movement. Reversing the product would describe gates used in the opposite order and can change the result.

- **Include the LCA's gates:** Reaching the LCA ends the route, so no departure occurs there. Its matrix must be excluded.

- **Start already at the LCA:** The identity product yields one route, regardless of starting card, matching the zero-length-route rule.

- **No usable gate at a path node:** The relevant row of that node matrix may be all zero. Subsequent multiplication preserves zero ways for that starting state.

- **Only white gates:** Every move flips color, and each white gate instance contributes a separate choice. Off-diagonal matrix entries model both facts.

- **Multiple identical gates:** Counts, not mere availability flags, belong in the matrix because different instances define distinct ways.

- **Equal query nodes:** Their LCA is that same node, both routes have length zero, the joint count is one, and that query contributes one to the XOR.

- **One query participant is an ancestor of the other:** The ancestor participant contributes one no-move way; only the descendant path needs gate multiplication.

- **Modular arithmetic:** Matrix entries and the joint product are reduced modulo `10^9+7`. XOR is then applied to each reduced query result exactly as required.

- **Recursive depth traversal:** A recursive DFS could compute depths but may fail on a long legal chain. The source uses an explicit stack.

- **Root self-ancestor entries:** They keep lifting table indices valid. Exact lifts to a real ancestor never consume extra root gate matrices.

- **Table level count:** `n.bit_length()` supplies enough powers of two to cover every possible depth below `n`.
