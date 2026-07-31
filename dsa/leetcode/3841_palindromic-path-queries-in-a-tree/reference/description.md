## Description

An undirected tree has `n` nodes labeled from `0` through `n - 1`. Its `n - 1` edges are listed in `edges`; each pair `edges[i] = [u_i, v_i]` joins nodes `u_i` and `v_i`.

A lowercase string `s` of length `n` assigns one character to every node, with `s[i]` belonging to node `i`.

The array `queries` describes operations that must be processed in order. Each operation has one of two forms:

- `"update u_i c"` changes the character at node `u_i` to `c`, so subsequent operations use `s[u_i] = c`.
- `"query u_i v_i"` considers the characters on the unique path from `u_i` to `v_i`, including both endpoints, and asks whether those characters can be rearranged into a palindrome.

Return a boolean array containing one result for each `query` operation: its entry is `true` exactly when that path can be rearranged into a palindrome, and `false` otherwise.
