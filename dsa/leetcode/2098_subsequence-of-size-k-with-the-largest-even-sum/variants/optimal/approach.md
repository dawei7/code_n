## General
**Starting from the unconstrained maximum**

Sort the values in descending order and select the first `k`. No other size-$k$ choice has a larger unrestricted sum. If this total is even, it is immediately optimal because adding the parity requirement cannot produce a sum greater than the unrestricted maximum.

**Repairing an odd total with one exchange**

An odd total must change parity. Exchanging two values of the same parity leaves the parity unchanged, so a valid repair must replace one selected value with an unselected value of the opposite parity.

There are only two useful exchange types: remove the smallest selected even and add the largest unselected odd, or remove the smallest selected odd and add the largest unselected even. The sorted order exposes these four boundary candidates. For each feasible type, calculate the repaired sum and keep the larger result.

**Why one boundary exchange is sufficient**

Any even size-$k$ choice differing from the unrestricted top `k` must make enough exchanges to change the total parity. Consider one such choice. Among its exchanges, at least one removed and added pair has opposite parity. Using the smallest selected value of that removed parity and the largest unselected value of the added parity loses no more sum than that pair. This single exchange already produces an even total and is at least as large as a repair involving additional exchanges.

Consequently, the better of the two boundary exchanges is globally optimal. If neither exchange type is available, no size-$k$ selection can change the odd total to even, so return `-1`.

## Complexity detail
Sorting $n$ values takes $O(n \log n)$ time. The selected and unselected scans take $O(n)$ additional time. The sorted copy or language sorting storage uses $O(n)$ space under the app contract, while the parity candidate records use constant extra space.

## Alternatives and edge cases
- **Separate parity lists:** Sort even and odd values independently, build prefix sums, and try every feasible even count of selected odd values. This is also $O(n \log n)$ but uses more bookkeeping.
- **Dynamic programming by count and parity:** Tracking the best sum for every selected count and parity takes $O(nk)$ time, which is unnecessary at the maximum constraints.
- **Heap selection:** Maintain the `k` largest values and the needed parity-boundary candidates in $O(n \log k)$ time; this can improve work when `k` is small but is more intricate.
- When `k = n`, there are no unselected replacements; the sum itself must be even.
- Zero is even and may be the best or only parity-changing replacement.
- Duplicate values are separate selectable elements and require no special handling.
- A one-element answer exists exactly when at least one selected candidate can be even.
