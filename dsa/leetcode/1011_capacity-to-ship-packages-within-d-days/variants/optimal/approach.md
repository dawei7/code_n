## General

**Binary-search the answer, not the package positions**

For any proposed ship capacity, the packages can be simulated in their fixed order to determine how many days are required.

Feasibility is monotone:

- if capacity `C` is too small, every smaller capacity is also too small;
- if capacity `C` works, every larger capacity also works.

Therefore, capacities form a sequence of false feasibility results followed by true results. The minimum feasible capacity is the first true position, exactly the boundary binary search is designed to find.

**Choose tight guaranteed bounds**

The ship must hold every individual package, so no capacity below

`left = max(weights)`

can work.

A capacity equal to `sum(weights)` can ship every package on the first day, so it is always feasible. The code sets

`right = sum(weights) + 1`

because Python `range(left, right)` excludes `right` and therefore includes the guaranteed feasible total weight as its final candidate.

This range contains every possible minimum answer and never calls the checker with a capacity too small for one package.

**Greedily determine the days needed for one capacity**

Helper `check(mx)` scans packages in order. Variable `ws` is the load on the current day, and `cnt` begins at one for that first day.

For each weight `w`:

1. add it to `ws`;
2. if `ws > mx`, the package does not fit on the current day;
3. start a new day by incrementing `cnt` and setting `ws = w`.

The package that caused overflow is not skipped. It becomes the first package of the next day.

Since `mx >= max(weights)` for every searched candidate, that single package always fits on the new day.

**Why filling each day as much as possible minimizes days**

The package order cannot change. For a fixed capacity, ending a day before the next package would exceed capacity cannot help: it moves one or more packages to later days without allowing any earlier package to move forward.

Thus the greedy simulation places the longest possible consecutive prefix on day one, then the longest possible next prefix on day two, and so on. Any valid schedule with the same capacity needs at least as many days.

Consequently, `cnt <= days` is an exact feasibility test, not merely one possible packing attempt.

**Use `bisect_left` on a virtual monotone Boolean sequence**

The return expression is:

`left + bisect_left(range(left, right), True, key=check)`.

This compact line deserves careful unpacking.

`range(left, right)` is a memory-efficient sequence of candidate capacities. For each capacity examined during binary search, the `key` function transforms it into `check(capacity)`, either `False` or `True`.

Python orders `False < True`. Because feasibility is monotone, the keyed sequence looks conceptually like:

`False, False, ..., False, True, True, ...`.

`bisect_left(..., True, key=check)` returns the zero-based position of the first true value. A range position is an offset rather than the capacity itself, so adding `left` converts that position back to the actual minimum capacity.

The range is not materialized; it uses constant storage.

**Trace capacities fourteen and fifteen**

For weights `[1,2,3,4,5,6,7,8,9,10]` and five allowed days:

With capacity fourteen, greedy loading needs:

- day one: `1,2,3,4`;
- day two: `5,6`;
- day three: `7`;
- day four: `8`;
- day five: `9`;
- day six: `10`.

Six days are too many, so fourteen is false.

With capacity fifteen:

- day one: `1,2,3,4,5`;
- day two: `6,7`;
- days three through five: `8`, `9`, `10`.

Five days suffice, so fifteen is true. Binary search finds fifteen as the first feasible boundary.

**Why order is preserved**

The checker scans `weights` once from left to right and only decides where one day ends and the next begins. It never rearranges or skips a package.

Each day's shipment is therefore a contiguous block of the conveyor sequence, exactly matching the contract.

**Why the returned boundary is minimal**

The greedy check correctly labels every capacity as feasible or infeasible. The lower and upper bounds include at least one true candidate, and monotonicity ensures a single false-to-true boundary.

`bisect_left` returns the first true position. Every smaller capacity is false, while that capacity is true, so it is exactly the least capacity able to ship within the allowed days.

**Special schedules arise naturally**

If `days = 1`, only the total-weight capacity is feasible and binary search returns the sum. If `days` equals the number of packages, capacity equal to the largest package is feasible because each package may occupy its own day.

No special branch is needed for either extreme.

## Complexity detail

Let `N` be the number of packages and let

`S = sum(weights) - max(weights) + 1`

be the number of candidate capacities in the inclusive search interval.

Binary search performs `O(\log S)` calls to `check`. Each call scans all `N` weights, so total time is `O(N \log S)`, plus `O(N)` to compute the maximum and sum.

The checker uses a constant number of integers, and Python's `range` is stored compactly rather than as a list. Auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Manual binary-search loop:** Maintain inclusive or half-open bounds and update them from `check(mid)`. It is more portable and expresses the same monotone search.
- **Test capacities one by one:** Starting at the largest package is correct but may scan a large capacity range, multiplying it by `O(N)` checking work.
- **Reorder packages for bin packing:** Forbidden; each day's packages must be the next consecutive items on the conveyor.
- **Stop checker early:** If `cnt` exceeds `days`, the helper could return false immediately. This improves some cases but does not change the bound.
- **One package:** Lower and guaranteed upper candidate coincide at its weight, which is returned.
- **One allowed day:** Capacity must equal the sum of all weights.
- **One day per package available:** The largest package weight is sufficient and minimal.
- **Package exactly fills remaining capacity:** Overflow uses strict `>`, so equality stays on the current day.
- **Package causes overflow:** It becomes the first load of the next day through `ws = w`.
- **Guaranteed true endpoint:** `sum(weights)` is included because the range's exclusive end is one larger.
- **Modern Python API:** The implementation relies on `bisect_left` supporting the `key` parameter.
- **Input preservation:** The weights are scanned but never reordered or modified.
