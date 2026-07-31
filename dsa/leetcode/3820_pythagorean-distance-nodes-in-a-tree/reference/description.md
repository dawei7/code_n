## Description

You are given an integer `n` and an undirected tree containing `n` nodes labeled from `0` through `n - 1`. The tree is supplied as an array `edges` of length `n - 1`; each pair `[u_i, v_i]` represents one undirected edge.

Three pairwise-distinct target nodes `x`, `y`, and `z` are also provided.

For every tree node `u`:

- Let `dx` be the distance from `u` to `x`.
- Let `dy` be the distance from `u` to `y`.
- Let `dz` be the distance from `u` to `z`.

Node `u` is **special** when these three distances form a Pythagorean triplet. Return the total number of special nodes.

To test a Pythagorean triplet, sort its three integer values in ascending order as $a$, $b$, and $c$. The condition is

$$
a^2+b^2=c^2.
$$

The distance between two tree nodes is the number of edges on their unique connecting path.
