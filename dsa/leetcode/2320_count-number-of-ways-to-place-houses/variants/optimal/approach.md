## General

**Solve one side of the street before combining both sides**

The adjacency restriction applies only to consecutive plots on the same side. A house on plot `i` on one side does not prevent a house on plot `i`, `i - 1`, or `i + 1` on the other side. Therefore the choices for the two sides are independent.

If one side has `v` valid arrangements, then the left side may choose any of those `v` arrangements and the right side may independently choose any of the same `v` arrangements. The multiplication rule gives `v \cdot v = v^2` complete-street arrangements.

The main task is consequently to count binary strings of length `n` with no adjacent ones, where one means “house” and zero means “empty,” for a single side.

**Keep separate counts based on the current plot**

The arrays `f` and `g` describe one-side arrangements through each plot index:

- `f[i]` is the number of valid arrangements for plots `0` through `i` in which plot `i` contains a house.
- `g[i]` is the number of valid arrangements for plots `0` through `i` in which plot `i` is empty.

At the first plot, there is exactly one arrangement ending with a house and one ending with an empty plot. The code creates both arrays filled with ones, so `f[0] = 1` and `g[0] = 1` provide these base cases. Later entries are overwritten by the recurrence.

**A house may follow only an empty plot**

To place a house at index `i`, plot `i - 1` must be empty. Every valid arrangement counted by `g[i - 1]` can be extended in exactly one way by adding a house, so

`f[i] = g[i - 1]`.

An arrangement ending with a house cannot be used because that would create two adjacent houses. This transition enforces the entire restriction at the moment a new plot is processed.

**An empty plot may follow either state**

If plot `i` is empty, the previous plot may contain a house or may also be empty. Appending an empty plot to any valid shorter arrangement never creates adjacent houses. Therefore

`g[i] = f[i - 1] + g[i - 1]`.

The code reduces this sum modulo `10^9 + 7`. `f[i]` merely copies the already reduced `g[i - 1]`, so every stored entry remains below the modulus.

For `n = 2`, the one-side sequences are `00`, `01`, and `10`. Starting from `f[0] = 1` and `g[0] = 1`, the recurrence produces `f[1] = 1` and `g[1] = 2`, for a total of three. Squaring gives nine arrangements for the two independent sides.

**Combine the final one-side states**

Every one-side arrangement ends in exactly one of the two states: its last plot is occupied or empty. Thus

`v = f[-1] + g[-1]`

is the complete one-side count. The two categories do not overlap, so addition neither misses nor duplicates an arrangement.

The method returns `v * v % mod` to select one valid arrangement for each side and reduce the potentially large product. Although `v` itself is not immediately reduced after the final addition, each addend is below the modulus, so `v < 2 \cdot mod` and the subsequent modular multiplication is safe in Python.

**Why the recurrence is correct**

For the base plot, the occupied and empty states list all two valid possibilities exactly once. Assume `f[i - 1]` and `g[i - 1]` correctly count all valid prefixes through the previous plot, separated by their final state.

Every valid prefix ending with a house at `i` must have been empty at `i - 1`, and every prefix in that previous-empty state can receive the house. This is a one-to-one correspondence proving the `f` transition.

Every valid prefix ending empty at `i` comes from exactly one valid shorter prefix, regardless of its previous final state. Appending empty is always legal, which proves the `g` transition.

Induction gives the exact one-side count at index `n - 1`. Since there is no cross-street constraint, every ordered pair of one-side arrangements is valid and every full arrangement has one unique left/right pair. Squaring therefore gives exactly the requested total.

**The sequence is closely related to Fibonacci numbers**

The total number of one-side arrangements satisfies the familiar recurrence “current total equals the previous total plus the total two positions back.” The two-state version is often easier to derive because it makes the adjacency restriction explicit and avoids special handling during transitions.

The exact source stores every state in arrays, even though iteration `i` reads only entries at `i - 1`. A truly rolling version could keep just two current numbers.

## Complexity detail

The loop processes indices one through `n - 1` once, performing constant-time arithmetic per index under modular values. Its running time is `O(n)`.

The exact implementation allocates two lists of length `n`, so its auxiliary space is `O(n)`. This differs from the manifest's `O(1)` description, which corresponds to the same recurrence implemented with two rolling scalar states. Since no transition uses entries older than `i - 1`, reducing the storage is straightforward, but it is not what the provided source literally does.

All stored state values are reduced modulo `10^9 + 7` either directly in `g` or by copying a reduced `g` entry into `f`. The final multiplication is performed with Python integers and then reduced. The input `n` is a number and cannot be mutated.

## Alternatives and edge cases

- **Two rolling states:** Replace the arrays with the previous occupied and empty counts and update them each iteration. This preserves `O(n)` time while achieving genuine `O(1)` auxiliary space.
- **Single Fibonacci recurrence:** Compute the total number of valid strings directly from the prior two totals. This is compact but requires carefully chosen base cases; occupied/empty states explain the rule more transparently.
- **Matrix exponentiation:** Exponentiate the two-state transition matrix in `O(\log n)` time. It is useful for enormous `n` but unnecessarily complex for `n <= 10000`.
- **Enumerate all plot subsets:** There are `2^n` choices per side before filtering, which is exponential. The DP combines all prefixes sharing the same relevant final state.
- **Treat corresponding plots across the street as adjacent:** The statement explicitly allows houses at the same index on both sides. Adding a cross-street restriction would undercount.
- **Multiply by two instead of square:** Each side has `v` independent possibilities, so the product is `v^2`, not `2v`.
- **Count the two sides together with four states:** This can work, but because the sides have no interaction it repeats a separable calculation and makes the proof harder.
- **`n = 1`:** The one-side count is two, and the loops are skipped. Squaring gives four: neither house, either single-side house, or both houses.
- **All plots empty:** This arrangement appears once per side and is included by the empty-ending transitions.
- **Alternating houses:** Patterns such as `1010...` are valid and naturally produced because every occupied state comes from an empty state.
- **Two consecutive houses:** No transition enters `f[i]` from `f[i - 1]`, so such a pattern is never counted.
- **Modulo placement:** Reducing `g[i]` at each step keeps counts bounded. Because modular addition and multiplication preserve the final remainder, this does not change the requested result.
- **Exact-source storage:** Although old array entries are never read again after advancing, they remain allocated. Complexity documentation should not call that literal code constant-space.
