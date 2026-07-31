## Function Contract

`solve(n, parent, gates, queries) -> int`

**Inputs**

- `n`: The number of nodes in the rooted tree.
- `parent`: An array describing each node's parent; the root uses `parent[0] = -1`.
- `gates`: For each node, `[red, blue, white]` gives the number of separate gate instances of each color.
- `queries`: Query quadruples `[alice_node, alice_card, bob_node, bob_card]`, where card `0` is blue and card `1` is red.

Let $q = \lvert\texttt{queries}\rvert$. The arrays describe one valid tree, and every query node is a valid node index.

**Output**

Return one integer: the bitwise XOR of the $q$ per-query joint route counts after each count has been reduced modulo $10^9 + 7$.

For one query, Alice's and Bob's route counts are independent and are multiplied modulo $10^9 + 7$. A zero-length route from a starting node already equal to the LCA has count one.
