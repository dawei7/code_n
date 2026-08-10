## General

**Represent a combination by positions in the source range**

The intended implementation sets `nums` to the sequence `1, 2, ..., n` and represents a combination by `k` increasing zero-based indices `idxs`. The initial indices `[0, 1, ..., k - 1]` select the first combination `[1, 2, ..., k]`.

Working with indices makes the maximum legal value at each position explicit. At position `i`, the greatest possible index is

`i + n - k`.

There must be `k - i - 1` larger indices after it, so it cannot move any farther right. For example, with `n = 5` and `k = 3`, the maxima for positions zero, one, and two are 2, 3, and 4, giving the final index combination `[2, 3, 4]` and value combination `[3, 4, 5]`.

**Find the rightmost position that can advance**

The reversed loop examines positions from `k - 1` down to zero. It stops at the first index whose value is not yet its position-specific maximum. Choosing the rightmost movable position preserves lexicographic order: more significant positions stay fixed as long as a later position can change.

Python's `for ... else` has a precise role. The `else` block runs only if the loop completes without `break`. In this algorithm, that means every index has reached its maximum, so the current combination is the final one and the outer `while True` terminates.

If a movable `i` is found, `idxs[i] += 1` selects its next value. Every later index is then reset through `idxs[j] = idxs[j - 1] + 1`. This produces the smallest strictly increasing suffix possible after the increment, so the new combination is the immediate lexicographic successor rather than skipping valid outputs.

**Why resetting the suffix is necessary**

Suppose indices are `[0, 3, 4]` for `n = 5`, `k = 3`. The final index cannot move, nor can index one because its maximum is 3. Index zero can move from 0 to 1. The old suffix `[3, 4]` is no longer the smallest suffix following 1; resetting gives `[1, 2, 3]`, the combination immediately after `[0, 3, 4]`.

Without the reset, the generator would jump to `[1, 3, 4]` and miss `[1, 2, 3]`, `[1, 2, 4]`, and `[1, 2, 5]` in value terms. Consecutive rebuilding is what guarantees completeness.

**Convert each index vector into an independent value list**

The comprehension `[nums[i] for i in idxs]` maps the current positions to their values and creates a new list. Appending that new list is safe because later index mutations cannot alter already stored output combinations.

The initial combination is appended before the loop. Each successful successor step appends exactly one additional combination. The final all-maximal vector was appended by the preceding iteration or was the initial vector when `n == k`; the `for ... else` then stops without duplicating it.

**Conditional correctness of the intended generator**

Assuming `idxs` is a mutable list, it is initially the lexicographically smallest increasing `k`-index vector. Each successor step finds the rightmost position that can increase and resets the suffix to its smallest legal values, which is exactly the next increasing vector. No vector is repeated or skipped. Termination occurs at the unique maximal vector.

There is a one-to-one mapping between increasing `k`-index vectors and size-`k` subsets of `nums`. Thus the intended process emits every requested combination exactly once and in lexicographic order, which is a valid order under the contract.

**The exact source assumes Python 2 `range` behavior**

The file assigns `idxs = range(k)`. In Python 2, `range` produced a mutable list, so `idxs[i] += 1` and later indexed assignments were legal. In Python 3, `range` produces an immutable range object. Whenever a second combination exists, the generator finds a movable position and its first assignment raises `TypeError: 'range' object does not support item assignment`.

The source happens to return correctly when `n == k`: only one combination exists, every index is already maximal, and the loop exits before attempting mutation. For ordinary cases such as `n = 4`, `k = 2`, it appends the first combination and then fails rather than returning the full result.

A Python 3 repair must make the indices mutable with `idxs = list(range(k))`. `nums` can remain a range because it is only indexed, not modified.

**The defensive impossible-input check**

The stated constraints guarantee `k <= n`, but `if k > n: return []` makes the intended generator robust outside that domain. Without it, constructing and indexing an initial `k`-vector against only `n` values could fail. The branch does not affect valid-input complexity.

## Complexity detail

For the intended mutable-index implementation, there are $\binom{n}{k}$ outputs. Finding a movable position, resetting a suffix, and copying the selected values each take at most $O(k)$ per output. Total intended time is $O(k\binom{n}{k})$, matching the manifest and also matching the unavoidable size of the returned data up to constants.

The mutable index vector uses $O(k)$ working space. Loop indices are scalar. Excluding the returned result, intended auxiliary space is $O(k)$, as declared. The result itself necessarily occupies $\Theta(k\binom{n}{k})$ space.

For the exact Python 3 source, successful asymptotic generation does not occur when more than one combination exists because mutation of `range` raises `TypeError`. The declared bounds describe the intended Python 2 algorithm, not the current runtime behavior.

## Alternatives and edge cases

- **Python 3 repair:** Wrap `range(k)` in `list` so index assignments are legal; no algorithmic change is otherwise needed.
- **Backtracking with pruning:** Build increasing combinations recursively and stop choices that leave too few values. It has the same output-sensitive order of growth and often reads more naturally.
- **Iterative backtracking:** Maintain a current combination and simulate recursion without call frames; the file's unselected `Solution2` demonstrates this style.
- **Standard library combinations:** It provides a tested lazy iterator but may be disallowed when the exercise expects construction logic.
- **`n == k`:** The initial vector is already maximal, so one complete combination is returned even under Python 3.
- **`k == 1`:** Intended successors advance the sole index from zero through `n - 1`; exact Python 3 fails on the first advancement when `n > 1`.
- **`k > n`:** The defensive branch returns an empty list.
- **`k == 0` outside the contract:** The structure would produce one empty combination, consistent with the usual combinatorial convention.
- **Rightmost movable position:** Choosing an earlier movable position first would skip combinations sharing the current prefix.
- **Suffix reset:** Later indices must become consecutive to produce the immediate next vector.
- **Independent outputs:** Each comprehension creates a fresh list, so later index changes cannot mutate earlier answers.
- **Python-version audit:** Old code using `range` as a mutable list must be converted explicitly when run under Python 3.
