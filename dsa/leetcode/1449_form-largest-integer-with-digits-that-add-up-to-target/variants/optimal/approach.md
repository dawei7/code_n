## General

**Separate “largest number” into two priorities.** The result contains only digits one through nine, so it has no leading zero. Any positive integer with more digits is larger than every positive integer with fewer digits. Therefore the first objective is to maximize the number of painted digits while using total cost exactly `target`.

If two feasible answers have the same number of digits, their numeric order is their lexicographic order after arranging digits from largest to smallest. The second objective is thus to prefer more copies of digit nine, then more copies of digit eight, and so on. The dynamic program maximizes length, while its tie rule and reconstruction enforce this larger-digit priority.

**Define the unbounded-knapsack state.** The table `f` has ten rows and `target + 1` columns. `f[i][j]` is the maximum number of digits that can be painted with exact total cost `j` using only digit values from one through `i`. Digits may be used repeatedly, so this is an unbounded rather than zero-one knapsack.

All entries begin at negative infinity, marking exact costs that are unreachable. `f[0][0] = 0` is the single initial feasible state: with no digit types, cost zero can form an empty selection containing zero digits. A positive cost cannot be formed with no digits.

The digit-cost array is enumerated starting at one. On an iteration with digit `i`, `c` is `cost[i - 1]`, exactly matching the problem's zero-indexed description.

**Choose between excluding and including the current digit.** For each exact cost `j`, there are two possibilities.

Excluding digit `i` leaves the best solution from the previous row, `f[i - 1][j]`. Including one copy requires `j >= c` and extends a solution of cost `j - c` by one digit. Because repeated copies are allowed, that predecessor is `f[i][j - c]` from the current row, not `f[i - 1][j - c]`. Its candidate length is `f[i][j - c] + 1`.

If `j < c`, inclusion is impossible. If inclusion produces strictly fewer digits than exclusion, the code copies `f[i - 1][j]`. In both cases it sets `g[i][j] = j`, recording that reconstruction should move to the previous digit row without changing the remaining cost.

Otherwise, inclusion is at least as good in length. The code stores `f[i][j - c] + 1` and sets `g[i][j] = j - c`. The changed cost records that one copy of digit `i` was selected. Reconstruction will stay on row `i`, making it possible to select the same digit again.

Negative infinity behaves correctly in the recurrence. Adding one to an unreachable state remains negative infinity. Some unreachable table cells may record an inclusion-style predecessor on a tie between two impossible values, but reconstruction is attempted only if `f[9][target]` is nonnegative, so those irrelevant predecessor choices are never used for an impossible final target.

**Why ties choose inclusion.** The comparison uses strict `<`. When inclusion and exclusion yield the same maximum digit count, the `else` branch includes the current digit. Rows are processed from digit one upward, so the current digit is larger than every digit available in the previous row. For equal-length answers, choosing a larger digit is preferable.

Repeated tie choices favor as many copies as feasible of the current larger digit before relying on smaller values. This supplies the lexicographic part of the objective without storing enormous candidate strings in every DP cell.

**The predecessor table reconstructs the digits.** `g[i][j]` stores the previous cost chosen for state `f[i][j]`. Reconstruction starts at `i = 9` and `j = target`.

If `j == g[i][j]`, the cost did not change when row `i` was computed, so digit `i` was excluded. Reconstruction decrements `i` and examines the next smaller digit.

If the stored predecessor is smaller than `j`, one copy of digit `i` was included. The code appends `str(i)` and changes `j` to that predecessor cost. It deliberately does not decrement `i`, because unbounded knapsack may include the same digit again.

The process starts at nine and moves downward only when a digit is excluded. Therefore appended digits are automatically in nonincreasing order. That arrangement is the greatest numeric ordering of the chosen multiset, and no later sort is needed.

Every inclusion decreases `j` by a positive cost, and every exclusion decreases `i`. The loop must terminate. For a reachable target, it eventually accounts for the full cost and reaches the zero-cost base through the predecessor decisions.

**Detect impossibility before reconstruction.** If `f[9][target] < 0`, no combination of digits has exact total cost `target`. The function returns the string `"0"` required by the problem. This is a sentinel answer; the digit zero itself is never paintable and never appears in a feasible constructed integer.

**Why maximizing length first is valid.** Consider one feasible number with `p` digits and another with `q` digits, where `p > q`. Since every leading digit is at least one, the first number is at least `10**(p - 1)`, while the second is below `10**q`. Hence the longer number is larger regardless of its individual digits. Among equal lengths, comparing the first differing digit decides numeric order, which is why descending reconstruction and larger-digit tie preference complete the objective.

**Why the DP is correct.** Any optimal selection for state `i, j` either contains no digit `i`, in which case it belongs to state `i - 1, j`, or contains at least one, in which case removing one copy leaves a selection for `i, j - c`. The recurrence considers both exhaustive cases and selects the greater length. On equal length it chooses the case with the larger available digit. Induction over rows and costs establishes the best length and tie preference for every reachable state. Following `g` reproduces those exact decisions, so the final string is the largest feasible integer.

## Complexity detail

Let `T` be `target`. The table has ten rows because there are nine digits plus the zero-type base row. Filling it performs nine passes over `T + 1` costs, with constant work per cell. Time is `O(9T)`, simplified to `O(T)` because nine is fixed.

Both `f` and `g` contain `10(T + 1)` entries, so their storage is `O(T)`. The reconstructed answer can contain at most `T` digits because every cost is at least one, adding another `O(T)` output space. Total space remains `O(T)`, matching the manifest.

Reconstruction performs at most nine row-decrement steps plus one step per output digit. Its time is `O(T)` in the worst case. Joining `ans` also copies `O(T)` characters, so it does not change the bound.

The numerical answer itself may have thousands of digits, which is why the algorithm stores a list of digit strings and returns a string instead of constructing a machine integer.

## Alternatives and edge cases

- **One-dimensional maximum-length DP:** Compute the best digit count for every cost, then greedily reconstruct from digit nine down whenever taking a digit preserves the optimal count. This reduces table constants but requires careful reconstruction logic.
- **Store best strings in DP:** Keeping the actual largest string for every cost is conceptually direct, but repeated string comparison and concatenation are much more expensive than storing lengths and predecessors.
- **Greedy by cheapest digit:** The cheapest digit maximizes possible length, but exact-cost constraints can require other costs, and among equal lengths larger digits matter. Pure greedy selection can get stuck or return a smaller number.
- **Zero-one knapsack transition:** Using `f[i - 1][j - c]` for inclusion would allow each digit at most once, violating the unlimited-use rule. The current-row predecessor is essential.
- **Impossible target:** A negative final DP value produces `"0"` and reconstruction is skipped.
- **Exact cost only:** A combination costing less than target is not acceptable even if it forms a large number. Unreachable entries remain negative infinity so leftover budget cannot be ignored.
- **Several digits share a cost:** For equal length and cost, the higher digit is better. Processing upward and taking inclusion on ties causes reconstruction to prefer it.
- **Cost one exists:** The answer can contain as many as `T` digits. The tables and reconstruction remain linear in `T`.
- **One digit exactly costs target:** It is feasible, but a multi-digit combination is preferred whenever one exists because length has higher priority.
- **Longer answer with smaller digits:** It correctly beats a shorter answer beginning with nine. Digit count determines magnitude before lexicographic order.
- **Equal-length answers:** Descending reconstruction and inclusion on ties choose the lexicographically largest digit sequence.
- **No zero digits:** The returned `"0"` means impossibility only. Successful reconstruction appends values one through nine.
- **Positive costs:** Every inclusion lowers the remaining cost, which guarantees reconstruction termination. A zero-cost digit would break the unbounded recurrence, but constraints exclude it.
- **Variable shadowing:** The inner DP uses `i` for digit value, while `target` remains the cost limit. No local name changes the input `cost` mapping.
- **Large output:** Building a list and joining once avoids repeated immutable-string concatenation, which could otherwise introduce quadratic copying.
