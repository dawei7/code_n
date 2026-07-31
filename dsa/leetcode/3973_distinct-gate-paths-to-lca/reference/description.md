## Description

An undirected tree is rooted at node `0`. Its `n` nodes are numbered from `0` through `n - 1`, and `parent[i]` identifies the parent of node `i`.

Every node `i` owns three collections of gates, recorded as `gates[i] = [red_i, blue_i, white_i]`:

- A **red** gate accepts a red card and leaves it red.
- A **blue** gate accepts a blue card and leaves it blue.
- A **white** gate accepts either card color and flips it.

Alice and Bob each begin at a query-specified node with a red card (`1`) or blue card (`0`). They travel independently upward until they reach the lowest common ancestor (LCA) of their two starting nodes.

One move from a node `u` to `parent[u]` must select exactly one gate instance located at `u`. A red card can use a red gate or a white gate; a blue card can use a blue gate or a white gate. White gates can therefore flip a card repeatedly across different moves. If the current node has no gate usable with the current card color, that route cannot continue. Instances of the same gate color remain distinct choices and are counted separately.

Each query has the form `queries[i] = [aNode_i, aCard_i, bNode_i, bCard_i]`, giving Alice's node and card followed by Bob's node and card. Count the distinct pairs of valid gate-choice sequences that bring both people to their LCA. Two pairs are different whenever Alice or Bob selects a different gate instance. Reduce each query's count modulo $10^9 + 7$, then return the bitwise XOR of all reduced query values.

Someone who starts at the LCA makes no move and contributes exactly one way. As usual, a node is considered its own descendant when defining the LCA.
