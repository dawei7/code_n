## Function Contract

### Inputs

- `edges`: The $n-1$ undirected edges of one tree, with each edge written as `[a_i, b_i]`.

The nodes are the consecutive integers from $0$ through $n-1$, where

$$
n = \lvert \texttt{edges} \rvert + 1.
$$

The input is guaranteed to be connected and acyclic. Edge orientation and row order carry no meaning.

### Return value

Return the greatest number of edges on a simple path between any two nodes. When $n=1$, `edges` is empty and the diameter is `0`.
