## Hint

**Hint 1:** Define a prefix function that counts the requested digit occurrences from `1` through a bound `x`. The required interval count is then the prefix through `high` minus the prefix through `low - 1`.

**Hint 2:** Compute that prefix function with a dynamic program over the decimal digits of `x`.
