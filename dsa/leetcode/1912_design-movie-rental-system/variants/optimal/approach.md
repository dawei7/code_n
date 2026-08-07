## General
Algorithm uses single-pass sequential scanning. Maintains hash map lookup (`dict`) for $O(1)$ average speed. Applies bitwise operations (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(E \log E + Q \log(E + Q))$ — Operation count bound.
- **Space Complexity**: $O(E + Q)$ — Auxiliary memory allocation bound.
