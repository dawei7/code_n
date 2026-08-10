## General

**Parity fixes which digits may occupy each position**

An odd digit may swap only with another odd digit, and an even digit only with another even digit. Therefore, a position that originally contains an odd digit can ultimately contain any of the number's odd digits, but never an even digit. The same holds for even positions of the parity pattern.

Because arbitrary pairs of equal-parity digits may be swapped any number of times, every permutation within the odd group and every permutation within the even group is reachable. The task is to assign those digits to their allowed positions to make the decimal number largest.

**Maximize from the most significant position**

Two positive integers with the same number of digits are compared at their first differing digit. The larger digit at the earliest position always wins, regardless of later digits.

Thus, at each original position, the optimal choice is the largest unused digit having the required parity. Choosing a smaller available digit there cannot be compensated by placing a larger same-parity digit later. Swapping those two assignments would increase the earlier digit and produce a larger number.

Applying this argument from left to right proves the greedy placement.

**Count available digits instead of sorting**

The solution converts `num` to its decimal digits:

`nums = [int(c) for c in str(num)]`.

`Counter(nums)` stores how many copies of each digit remain. Since digits belong to the fixed range zero through nine, counts are a compact alternative to sorting separate odd and even lists.

The array `idx = [8, 9]` stores the current largest candidate for each parity. Index zero begins at largest even digit eight; index one begins at largest odd digit nine.

For an original digit `x`, `x & 1` is zero when `x` is even and one when it is odd. The solution uses that parity as an index into `idx`.

**Find the largest remaining digit of the required parity**

The loop

`while cnt[idx[x & 1]] == 0: idx[x & 1] -= 2`

skips unavailable digits while preserving parity. Subtracting two moves from eight to six, four, two, zero for evens, or from nine to seven, five, three, one for odds.

A valid digit is always found. At each output position, the original digit itself belongs to the required parity. Across all remaining positions of that parity, the number of remaining counted digits equals the number of positions still needing them. Previous placements consumed only one same-parity digit each.

Once found, the digit is appended numerically with

`ans = ans * 10 + idx[x & 1]`,

and its counter is decremented. Multiplying by ten shifts the already built prefix left by one decimal place.

The pointer for a parity never moves upward. After all copies of a large digit are used, it descends permanently to the next available value. This is safe because counts only decrease; an exhausted larger digit can never reappear.

**Why the constructed number is reachable**

Every chosen output digit has the same parity as the digit originally occupying that position. The output uses each digit no more often than its original counter, and after all positions it uses every original digit exactly once.

It is therefore a parity-preserving permutation of the original multiset. Since arbitrary swaps can realize any permutation within each parity group, the constructed arrangement is reachable by allowed operations.

**Why no reachable number is larger**

Consider the first position where another reachable arrangement differs from the greedy result. All earlier positions match and have consumed the same multisets. At this position, both arrangements must use a digit of the original position's parity. The greedy algorithm chose the largest remaining such digit, so the alternative cannot place a larger one.

If it places a smaller digit, its complete number is smaller immediately. If it places the same digit, this was not actually the first differing position. Therefore, no reachable arrangement exceeds the greedy construction.

**Trace the parity pools**

For `1234`, odd digits are one and three, while evens are two and four. The first position requires odd, so it receives three. The second requires even, so it receives four. Remaining odd one and even two fill the last positions, producing `3412`.

For `65875`, the even positions can draw from six and eight, and odd positions from five, seven, five. Greedy placement yields eight, seven, six, five, five, or `87655`.

**Leading zero cannot be introduced**

The input is positive, so its first digit is nonzero. If the first digit is odd, every candidate is nonzero because odd digits are at least one. If it is even, the even pool contains that original nonzero digit, and the greedy algorithm chooses the largest even digit, which cannot be zero while a nonzero candidate remains. The result retains the same digit length.

## Complexity detail

Let `d` be the number of decimal digits. Converting to digits, building the counter, and constructing the answer each take `O(d)` time. The parity pointers descend across only five possible digits per parity in total, so all while-loop decrements together are `O(1)` for decimal digits.

Generalized complexity is `O(d)` time. Under `num <= 10^9`, `d` is at most ten, so the manifest describes this as `O(1)` time.

The digit list uses `O(d)` space, while the counter has at most ten keys. Under the fixed input bound this is `O(1)` space. In a generalized digit-length model, the explicit list is `O(d)`.

## Alternatives and edge cases

- **Sort odd and even lists descending:** Then consume the next digit from the appropriate list at each position. This is simpler conceptually but costs `O(d \log d)` sorting time; with at most ten digits the practical difference is tiny.
- **Try all same-parity swaps:** Exploring reachable permutations is factorial in the number of digits and repeats equivalent arrangements when digits duplicate.
- **Globally sort every digit:** This may place an odd digit into an originally even position or vice versa, violating the swap invariant.
- **One digit:** Its parity pool contains only itself, so the number is unchanged.
- **All digits one parity:** The method arranges all digits in descending order because every position draws from the same pool.
- **Already maximal arrangement:** Each position receives the same value and the result is unchanged.
- **Repeated digits:** `Counter` preserves multiplicity, and each placement decrements exactly one copy.
- **Zeros:** Zero participates in the even pool and is used only after larger remaining evens.
- **First digit parity:** The parity pattern of positions is fixed by the original digits; only values within each parity group move.
- **Duplicate maximum digit:** The pointer remains at that value until its count reaches zero.
- **Pointer exhaustion:** It cannot fall below zero or one while a position of that parity remains, because the remaining counts and remaining parity positions are equal.
- **Input preservation:** `num` is immutable; the method builds a new numeric result.
