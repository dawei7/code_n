## General

Represent the numbers of ways to hold blue and red as a row vector in that order. Moving upward once from node `u` applies the transition matrix

$$
T_u =
\begin{bmatrix}
\texttt{blue}_u & \texttt{white}_u \\
\texttt{white}_u & \texttt{red}_u
\end{bmatrix}.
$$

The first row says that a blue card either uses a blue gate and stays blue or uses a white gate and becomes red. The second row gives the corresponding choices from red. Matrix multiplication counts every sequence of specific gate instances, because each product term chooses one instance at each traversed node and each sum combines routes that finish in the same color.

Precompute binary-lifting tables. For every node `u` and bit `j`, store its ancestor after $2^j$ upward edges and the matrix product for exactly those edges, beginning with `u`. A one-edge product is `T_u`. Joining two adjacent $2^{j-1}$ segments gives the $2^j$ product in movement order. Matrix multiplication is associative, so any upward path can later be assembled from the set bits of its length.

Compute depths from the root with an explicit stack; this does not assume that a parent's numeric index precedes every child. To find an LCA, first lift the deeper node to the other depth, then inspect jump levels from largest to smallest until both nodes are immediate children of their LCA.

For one person's route from `node` to that LCA, begin with the identity matrix and append the stored products for the set bits of the depth difference. Select the blue row for card `0` or the red row for card `1`, then sum that row: either ending color is valid at the LCA. The identity matrix makes a zero-edge route contribute one automatically.

Alice's and Bob's choices are independent, so multiply their two route counts modulo $10^9 + 7$. XOR that reduced value into the answer for each query. This applies the modulus at the source-prescribed per-query boundary without incorrectly reducing the final XOR.

## Complexity detail

Let $n$ be the number of nodes and $q = \lvert\texttt{queries}\rvert$. There are $\lceil\log_2 n\rceil$ jump levels. Building ancestors and constant-size matrices takes $O(n\log n)$ time. Each LCA and the two path products take $O(\log n)$ time, for $O((n+q)\log n)$ total time. The two lifting tables use $O(n\log n)$ auxiliary space; depths, children, and the traversal stack use $O(n)$ more.

## Alternatives and edge cases

- **Walk to the LCA for every query:** Direct color dynamic programming along parent edges is simple and correct, but a chain with many deep queries requires $O(nq)$ time.
- **Euler tour plus a range structure:** An Euler-tour method can answer LCAs efficiently, but noncommuting transition matrices still need a directed path-product data structure; it does not remove the core composition problem.
- **Gate counts are multiplicities:** Three white gates create three distinct choices, not one transition merely labelled white.
- **Matrix order:** The product must follow movement from the starting node upward. Reversing adjacent jump products generally changes the result.
- **Root gates:** No route moves from node `0` to a parent, so the gate counts stored at the root are never consumed.
- **Starting at the LCA:** The empty sequence has one way for either card color, even if the LCA has no gates.
- **Blocked state:** A zero row in a node's matrix correctly eliminates every route arriving there with that card color.
- **Modulo and XOR:** Reduce matrix arithmetic and the two-person product modulo $10^9 + 7$, but never reduce or add the accumulated XOR.
