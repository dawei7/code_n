## General

Any pair other than the two globally cheapest chocolates has a sum at least as large. Therefore, if the cheapest pair is unaffordable, no pair can be purchased; if it is affordable, it also maximizes the leftover balance.

Maintain `cheapest` and `second_cheapest` while scanning `prices`. When a price is smaller than `cheapest`, move the old minimum into the second slot and install the new minimum. Otherwise, update only the second slot when the price is smaller than it. The `elif` structure is important: each array occurrence can occupy only one slot, while two equal prices from different positions can still become both minima.

After every processed prefix, the two variables are its two smallest occurrences. The update preserves this property for the next price, so after the final element their sum is the minimum cost of any legal two-chocolate purchase. Subtract that sum when it does not exceed `money`; otherwise return the untouched budget.

## Complexity detail

Let $n$ be the number of prices. The algorithm performs one constant-work update per price, taking $O(n)$ time and $O(1)$ auxiliary space. The benchmark uses `size` as $n$ and compares the single pass with a correct enumeration of all $\binom{n}{2}$ pairs.

## Alternatives and edge cases

- **Sort all prices:** Sorting and reading the first two values is simple but takes $O(n\log n)$ time and may mutate the input.
- **Enumerate every pair:** Checking all distinct pairs is correct but performs $O(n^2)$ comparisons.
- **Use one minimum twice:** This is invalid unless the minimum price occurs at two distinct indices; tracking two occurrences handles duplicates correctly.
- A pair whose cost equals `money` is affordable and leaves `0`.
- If no pair is affordable, return the original `money`, not a negative balance.
- An array of exactly two prices has only one possible pair.
- Duplicate cheapest prices must both be considered when they occur at different positions.
