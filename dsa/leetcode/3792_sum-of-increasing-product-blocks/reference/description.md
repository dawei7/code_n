## Description

You are given an integer `n`.

Build a sequence of blocks from the positive integers in increasing order. The first block consists only of `1`, and the second block is the product `2 * 3`. More generally, block $i$ is formed by multiplying the next $i$ consecutive integers, continuing immediately after the final integer used by block $i-1$.

Let `F(n)` denote the sum of the products in the first `n` blocks. Return `F(n)` modulo $10^9 + 7$.
