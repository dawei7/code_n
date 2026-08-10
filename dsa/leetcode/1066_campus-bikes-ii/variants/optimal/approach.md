## General

**Why a local nearest-bike choice is not enough**

Each worker must receive a distinct bike, and the objective is the total Manhattan distance. Giving the current worker its nearest bike can prevent a later worker from using the only bike close to that worker. A locally smallest distance can therefore create a worse global sum.

The constraints are small, with at most ten bikes. This makes it practical to represent the chosen-bike subset as a bitmask and use dynamic programming over assignments.

Workers are processed in their fixed index order. This does not restrict the set of matchings: any complete assignment can be described by the bike chosen for worker zero, then worker one, and so on. The DP considers every distinct-bike choice sequence and keeps only the smallest cost reaching each state.

**Represent a bike subset with bits**

With `m` bikes, a mask from zero through `2^m - 1` contains one bit per bike:

- Bit `k` equal to one means bike `k` is included in the current partial assignment.
- Bit `k` equal to zero means that bike is not included.

Because a mask records a set, it automatically prevents one bike from being assigned twice. A transition adds exactly one set bit for the current worker.

The exact solution builds a two-dimensional table:

```python
f = [[inf] * (1 << m) for _ in range(n + 1)]
f[0][0] = 0
```

Define `f[i][mask]` as the minimum total distance for assigning bikes to the first `i` workers using exactly the bikes whose bits are set in `mask`.

Every state begins at positive infinity, meaning it has not been reached by any valid assignment. The base state `f[0][0] = 0` says assigning no workers with no bikes costs zero.

No state `f[0][mask]` with a nonzero mask is valid because no worker exists to receive those bikes, so those cells correctly remain infinity.

**Process workers one layer at a time**

The outer loop is:

```python
for i, (x1, y1) in enumerate(workers, 1):
```

`enumerate` starts `i` at one, while `(x1, y1)` is the location of worker `i - 1`. Thus table row `i` adds an assignment for that worker on top of row `i - 1`, which already represents the first `i - 1` workers.

This layer order guarantees that a transition never assigns two bikes to one worker or skips a worker. Each row increases the assigned-worker count by exactly one.

**Try every mask and every possible last bike**

For one worker layer, the code visits every mask and bike:

```python
for j in range(1 << m):
    for k, (x2, y2) in enumerate(bikes):
```

Here `j` is the candidate set of bikes used after assigning the first `i` workers. Bike `k` is considered as the bike assigned specifically to worker `i - 1`.

The condition:

```python
if j >> k & 1:
```

checks whether bit `k` is set in `j`. Shifting `j` right by `k` moves that bit to the units position, and bitwise AND with one extracts it.

Only a set bit can be the final bike in a state whose mask claims that bike is used.

**Remove the last bike to identify the predecessor**

When bit `k` is set, the predecessor mask is:

```python
j ^ (1 << k)
```

`1 << k` contains only bit `k`. XOR toggles that bit. Because the condition proved it is one, XOR changes it to zero and leaves every other bit unchanged.

The predecessor therefore uses all bikes in `j` except `k`. It belongs to row `i - 1` because worker `i - 1` has not yet received a bike there.

**Add the Manhattan distance**

The cost of pairing the current worker at `(x1, y1)` with bike `k` at `(x2, y2)` is:

```python
abs(x1 - x2) + abs(y1 - y2)
```

The transition is:

```python
f[i][j] = min(
    f[i][j],
    f[i - 1][j ^ (1 << k)]
    + abs(x1 - x2)
    + abs(y1 - y2),
)
```

It takes a best assignment of the previous workers using the predecessor bike set, adds the current pairing, and compares this candidate with every other possible choice of the current worker's bike.

If the predecessor is unreachable, its value is infinity. Adding a finite distance leaves an infinite candidate, so it cannot incorrectly improve the state.

The code does not explicitly check that `j` contains exactly `i` set bits. That is unnecessary for correctness. Row zero reaches only the zero-bit mask. Every transition adds one set bit relative to a reachable predecessor. By induction, the only finite states in row `i` have exactly `i` bits set. Other masks are iterated but remain infinity.

**Why the recurrence considers every valid partial assignment**

Take any valid assignment of the first `i` workers that uses mask `j`. Worker `i - 1` receives one particular bike `k` whose bit is set in `j`. Removing that pairing leaves a valid assignment of the first `i - 1` workers using `j` with bit `k` cleared.

The transition examines exactly this predecessor and adds exactly this last Manhattan distance. Therefore every valid partial assignment appears among the candidates for its state.

Conversely, every finite transition starts from a valid predecessor and adds a bike absent from that predecessor. It assigns one new distinct bike to the next worker, so it creates a valid partial assignment.

Taking the minimum over all possible last bikes makes `f[i][j]` exactly the least cost for its definition.

**Select the best complete bike subset**

The return statement is:

```python
return min(f[n])
```

When there are more bikes than workers, a complete assignment uses some subset of `n` bikes rather than all `m` bikes. Every finite cell in row `n` represents one such subset and its best matching cost.

Taking the minimum over the whole row chooses the best subset as well as the best assignment within that subset. Cells with the wrong number of bits remain infinity and cannot win.

When `n == m`, only the all-ones mask can be finite in the final row, so the same expression still works.

**A small state example**

With two workers and three bikes, mask `101` means bikes zero and two are used.

For `f[2][101]`, the final worker might use bike zero. The predecessor is mask `100`, meaning the first worker used bike two. Or the final worker might use bike two, with predecessor mask `001`. The DP compares those two complete assignments and stores the cheaper one.

Bike one cannot be the final bike for mask `101` because its bit is zero.

## Complexity detail

Let `N` be the number of workers and `B` the number of bikes.

The exact source has three loops: `N` worker layers, `2^B` masks per layer, and `B` bikes per mask. Each transition is constant time. Its exact time complexity is:

```text
O(N * B * 2^B)
```

Since `N <= B`, this is at most `O(B^2 2^B)`. The exact code still iterates over unreachable masks, so the worker-layer factor cannot be omitted from its literal loop analysis.

The table has `N + 1` rows and `2^B` columns, requiring `O(N2^B)` auxiliary space. Other variables use constant space.

The manifest records `O(B2^B)` time and `O(2^B)` space. Those bounds describe the standard one-dimensional mask DP or memoized recursion.

In that optimized form, the number of already assigned workers is the mask's set-bit count, so it need not be a separate table dimension. Each reachable mask tries up to `B` unused bikes. There are at most `2^B` masks, producing `O(B2^B)` time and `O(2^B)` stored costs. It solves the same recurrence more compactly.

The small bound `B <= 10` makes both versions practical, but the exact protected source has the larger two-dimensional bounds stated above.

## Alternatives and edge cases

- **One-dimensional mask DP for the manifest target:** Let the next worker index be `popcount(mask)` and store one best cost per used-bike mask. Try every unused bike. This achieves `O(B2^B)` time and `O(2^B)` space.
- **Top-down memoization:** Recursively assign the next worker and memoize by mask. Worker index is implied by the number of set bits, giving the same optimized bounds and often skipping unreachable states naturally.
- **Brute-force backtracking:** Enumerate all ordered selections of `N` bikes from `B`. Its worst-case count is `B! / (B - N)!`, much larger than merging equal mask subproblems.
- **Hungarian algorithm:** General minimum-cost bipartite matching solves larger assignment instances in polynomial time. It is more complex than necessary for at most ten bikes.
- **Greedy nearest bike:** It can reserve a strategically important bike for the wrong worker and is not guaranteed to minimize total distance.
- **One worker:** Row one considers every single-bike mask, and the final minimum selects the nearest bike.
- **More bikes than workers:** Unused bikes correspond to zero bits in the chosen final mask. `min(f[n])` selects the best subset automatically.
- **Equal workers and bikes:** Every bike must be used, so only the all-ones final mask is reachable.
- **Several equally optimal assignments:** The table stores only their shared minimum numeric cost, which is all the problem requests.
- **Zero Manhattan distance:** A worker and bike at the same coordinates across the two entity sets contribute zero and require no special handling.
- **Unreachable table cells:** They retain infinity. Arithmetic with infinity cannot create a falsely finite minimum.
- **XOR safety:** The code clears bit `k` with XOR only after proving the bit is set. XOR without that condition would incorrectly add a missing bit.
- **Mask width:** `1 << m` creates exactly the number of subsets needed for bike indices zero through `m - 1`.
- **Input preservation:** Worker and bike coordinate lists are read only. All mutation is confined to the DP table.
