## General

**Separate letter frequency from keypad placement**

Once a letter is assigned to a button position, every occurrence of that letter has the same cost. A first-position letter costs one press per occurrence, a second-position letter costs two, and a third-position letter costs three.

The physical button number does not affect cost. First position on button one costs the same as first position on button nine. Therefore, the available placement costs form a multiset:

- nine slots cost one press each;
- nine slots cost two presses each;
- nine slots cost three presses each.

There are 27 slots for 26 lowercase letters, so every letter can be assigned while leaving one slot unused. The optimization is solely about matching letter frequencies to these costs.

**Count how often each letter matters**

`Counter(s)` builds a mapping from every character that occurs in `s` to its frequency. If a letter occurs `x` times and is assigned to a position costing `k` presses, its contribution to the total is `kx`.

Letters absent from `s` do not appear in the counter. That is safe even though all 26 letters must be mapped: absent letters have frequency zero and can fill any remaining keypad slots without changing the cost of typing `s`. The algorithm only needs to optimize positions for positive-frequency letters.

**Give cheap positions to frequent letters**

The frequencies are sorted in descending order. The first nine receive multiplier one, the next nine receive multiplier two, and any remaining frequencies receive multiplier three.

This greedy order follows an exchange argument. Suppose two letters have frequencies `a \ge b`, but the more frequent letter is assigned a more expensive cost `q` while the less frequent letter has cheaper cost `p`, with `p < q`. Their current contribution is

$$
aq + bp.
$$

Swapping their placements gives

$$
ap + bq.
$$

The current cost minus the swapped cost is

$$
(a-b)(q-p) \ge 0.
$$

Therefore, placing the more frequent letter in the cheaper slot never makes the answer worse and makes it strictly better when both inequalities are strict. Repeatedly removing such inversions produces the descending-frequency, ascending-cost assignment used by the solution.

**Follow the one-based position counter**

The loop uses `enumerate(..., 1)`, so `i` starts at one. The multiplier `k` begins at one.

For frequencies one through nine, `k = 1`. After processing index nine, `i % 9 == 0` and `k` becomes two. Frequencies ten through eighteen therefore cost two presses each. After index eighteen, `k` becomes three for positions nineteen through twenty-six.

Incrementing `k` after adding the ninth item is important. If it happened before the contribution, the ninth cheap slot would incorrectly cost two presses.

**Accumulate the total contribution**

For each sorted frequency `x`, the statement `ans += k * x` adds the number of presses needed for all occurrences of that letter under its assigned cost tier. Since each character occurrence belongs to exactly one letter, summing these independent contributions yields the total presses needed for the full string.

The algorithm does not construct an explicit mapping from letters to buttons. The identity of letters with equal frequencies is irrelevant, and the result requests only the minimum number of presses. Frequencies and tier capacities contain all information needed for that number.

**Trace two common distributions**

For `s = "apple"`, frequencies are two for `'p'` and one each for `'a'`, `'l'`, and `'e'`. There are only four used letters, all of which fit in the nine one-press slots. The total is `2 + 1 + 1 + 1 = 5`.

If twelve distinct letters each appear once, the first nine occupy one-press slots and the remaining three occupy two-press slots. The total becomes

$$
9 \cdot 1 + 3 \cdot 2 = 15.
$$

This matches the example with `"abcdefghijkl"`.

**Why button capacity is respected**

Each group of nine equal-cost slots corresponds to one position across all nine buttons. Assigning the first nine letters to cost one uses at most one first position per button. The next nine use second positions, and the final group uses third positions.

An explicit keypad can always be reconstructed by distributing the entries of each tier across the nine buttons. Since there are at most 26 letters and 27 total positions, the frequency assignment is feasible. The computation is not relaxing any keypad constraint.

**Why the greedy total is globally minimum**

Every legal keypad assignment induces one placement of all letter frequencies into the fixed set of position costs. The exchange argument shows that any assignment with a higher frequency in a more expensive slot than a lower frequency can be swapped without increasing cost. Thus, some optimal assignment has frequencies in non-increasing order as costs rise.

The loop evaluates exactly that ordered pairing. It is feasible under the nine-slot tiers, so its total is both attainable and no greater than any legal assignment's total. Hence it is the global minimum.

## Complexity detail

Let `n` be the length of `s` and `A = 26` be the alphabet size. Building the counter takes `O(n)` time. Sorting at most `A` frequencies takes `O(A \log A)`, and the final loop takes `O(A)`. Because `A` is fixed, total time is `O(n)`.

The counter and sorted frequency list each contain at most 26 entries. Their sizes do not grow beyond the fixed lowercase alphabet, so auxiliary space is `O(1)` with respect to `n`. If alphabet size were treated as a variable, the more general bounds would be `O(n + A \log A)` time and `O(A)` space.

The input string is read only, and the total answer fits comfortably in ordinary wide integer arithmetic under the constraints.

## Alternatives and edge cases

- **Explicitly construct the keypad:** It can realize the same greedy assignment, but button identities are irrelevant when only total cost is requested.
- **Try all letter mappings:** There are far too many permutations; the exchange argument removes the need to search assignments.
- **Alphabet-sized frequency array:** A 26-entry list can replace `Counter` and gives the same bounds.
- **Ascending frequency sort:** It would place rare letters in cheap positions and frequent letters in expensive ones, maximizing the wrong tendency.
- **Priority queue:** Repeatedly taking the largest frequency works but is more machinery than sorting 26 values once.
- **At most nine distinct used letters:** Every used letter receives a one-press slot, so the answer equals `len(s)`.
- **Ten distinct used letters:** Nine use cost one and the least frequent one uses cost two.
- **All 26 letters used:** The tier sizes are nine, nine, and eight; the unused 27th slot has no effect.
- **Absent letters:** They can occupy leftover expensive or unused positions because their typing contribution is zero.
- **Equal frequencies:** Swapping their positions leaves the total unchanged, so any order among ties is optimal.
- **One overwhelmingly frequent letter:** Descending sorting guarantees it receives a one-press position.
- **Repeated string order:** Only frequency matters; rearranging `s` without changing counts does not change the optimum.
- **Tier boundary after nine:** `k` increases only after the ninth contribution, preserving all nine one-press slots.
- **Tier boundary after eighteen:** Entries nineteen onward correctly receive multiplier three.
- **Capacity guarantee:** Nine buttons times three characters gives 27 positions, enough for the 26-letter alphabet.
- **Input preservation:** Counting and sorting derived frequencies do not alter `s`.
