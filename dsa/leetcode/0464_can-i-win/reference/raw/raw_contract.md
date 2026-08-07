## Function Contract

**Inputs**

- `maxChoosableInteger`: The largest integer in the shared pool `1` through this value.
- `desiredTotal`: The running-total threshold that wins the game as soon as it is reached or exceeded.

**Return value**

- Return `True` if the first player has a strategy that wins against every optimal response; otherwise, return `False`.

Each integer may be chosen at most once, and the first player moves first.
