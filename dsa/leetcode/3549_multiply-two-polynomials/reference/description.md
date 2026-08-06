## Description

Two integer arrays `poly1` and `poly2` encode polynomials in ascending exponent order. An entry at index $i$ is the coefficient multiplying $x^i$, so index `0` stores the constant term and trailing entries represent the highest supplied powers. Zero coefficients are meaningful positions and must not be discarded.

Multiply the two represented polynomials. Return every coefficient of the product in the same ascending-exponent order. If the input lengths are $n$ and $m$, the returned array must have exactly $n+m-1$ entries, including a zero coefficient at the highest position when cancellation or a supplied trailing zero produces one.
