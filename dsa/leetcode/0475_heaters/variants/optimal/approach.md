## General
**Reduce the global radius to nearest-heater distances**

For each house, the smallest radius that covers it is its distance to the nearest heater. A common radius covers every house exactly when it is at least all of those local distances, so the answer is their maximum.

**Find neighboring heaters by binary search**

Sort heater positions. For a house, binary-search the first heater not left of it. Only that heater and its immediate predecessor can be nearest; every other heater lies still farther in the same direction. Take the smaller available distance and update the maximum.

**Why the maximum is both necessary and sufficient**

Any radius below the largest nearest-heater distance leaves that particular house uncovered. Choosing the largest distance covers each house by the heater that established its local minimum, so no larger radius is necessary.

## Complexity detail
Sorting `t` heaters costs $O(t \log t)$, and `h` binary searches cost $O(h \log t)$, within $O((h + t) \log(h + t))$. The sorted copy uses $O(t)$ space.

## Alternatives and edge cases
- **Sort houses and use two pointers:** advances a heater pointer toward the nearest position in $O(h \log h + t \log t)$ total time.
- **Binary-search the radius:** checks coverage for each candidate but adds a coordinate-range logarithm.
- **Scan every heater per house:** is correct but costs $O(h \cdot t)$ time.
- **House on a heater:** contributes distance zero.
- **House outside heater range:** only the nearest endpoint heater is available.
- **Duplicate coordinates:** do not affect nearest distances.
- **One heater:** the answer is the farther distance to the extreme houses.
