## Function Contract

**Inputs**

- `stations`: a strictly increasing list of integer gas-station positions on the x-axis.
- `k`: the exact number of new gas stations to add.

New stations may be placed at arbitrary real-valued positions. Once the existing and new stations are ordered by position, only distances between adjacent stations contribute to `penalty()`.

**Return value**

- The smallest possible maximum adjacent-station distance after all `k` additions, returned as a floating-point value accurate within $10^{-6}$.
