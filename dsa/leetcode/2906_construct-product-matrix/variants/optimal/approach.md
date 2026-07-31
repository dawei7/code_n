## General

Division is unsafe here because the modulus $12345$ is composite, so many values have no modular inverse. Instead, order the matrix cells in row-major order and split the product excluding each cell into the values before it and the values after it.

During a forward pass, maintain the product of all earlier cells modulo $12345$. Store that prefix directly in the corresponding output cell, then incorporate the current input value. At this point, each output cell contains exactly the contribution from positions before it.

Next traverse the cells in reverse row-major order while maintaining the product of all later cells. Multiply each stored prefix by this suffix before incorporating the current input. The two factors cover every position except the current one, so their product is precisely the required value.

The output matrix doubles as prefix storage, avoiding separate flattened, prefix, or suffix arrays. Reducing after every multiplication is valid because modular multiplication is associative and keeps intermediate integers bounded.

## Complexity detail

Let $N=nm$ be the number of matrix cells. The forward and reverse passes each visit every cell once, so the running time is $O(N)$. The returned matrix occupies $O(N)$ space; beyond that required output, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recompute every excluded product:** Multiplying all other cells separately for each output is correct but takes $O(N^2)$ time.
- **Divide a total product:** Ordinary division fails when a value does not divide cleanly after modular reduction, and modular division is invalid for non-invertible factors of composite $12345$.
- **Separate prefix and suffix matrices:** This remains linear but uses two unnecessary $O(N)$ auxiliary structures.
- **A value divisible by 12345:** Every output that includes it is zero, while the output excluding it can remain nonzero.
- **Separate composite factors:** Values such as $3$, $5$, and $823$ can jointly contribute a zero product modulo $12345$ even when no cell equals the modulus.
- **Rectangular matrices:** Row boundaries do not alter the row-major prefix and suffix order.
