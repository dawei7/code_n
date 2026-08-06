## Description

An array `prices` gives the prices of available chocolates. Each query has the form `[k, m]` and defines a separate purchase in which Bob must select exactly `m` chocolates under a payment threshold `k`.

For a chocolate priced at most `k`, Bob pays its entire price and Alice pays nothing. For a price greater than `k`, Bob pays exactly `k` and Alice pays the remaining amount. If their total payments are $b$ and $a$, respectively, Bob's relative loss is $b-a$.

For every query, choose exactly the requested number of chocolates so that Bob's relative loss is minimized. Return the minimum loss for each query in the original query order; a loss may be negative when Alice's total payment exceeds Bob's.
