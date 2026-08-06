## Function Contract

**Inputs**

- `n`: The number of houses, labeled from `1` through `n`.
- `wells`: A length-$n$ array in which `wells[i - 1]` is the cost of building a well at house $i$.
- `pipes`: An array of offers. Each `pipes[j] = [house1_j, house2_j, cost_j]` gives the cost of a bidirectional pipe between two different houses.

Parallel offers between the same two houses are allowed. Water may travel through any number of selected pipes. Let $p$ be `pipes.length` and let $e=n+p$, the total number of well and pipe choices.

**Return value**

- The minimum integer sum of selected well-building and pipe-laying costs that supplies all $n$ houses.
