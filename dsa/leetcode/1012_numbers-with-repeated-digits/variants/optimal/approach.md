## General

**Count the easier complement set**

Directly describing “at least one repeated digit” inside a digit-by-digit construction requires remembering whether repetition has already occurred. An equally useful and cleaner route is to count positive integers whose digits are all distinct.

There are exactly `n` positive integers in `[1, n]`. Every one belongs to exactly one of two groups:

- all decimal digits are distinct;
- at least one digit repeats.

Therefore:

`repeated_count = n - distinct_digit_count`.

The digit DP computes the second term.

**Build numbers within the digit length of `n`**

String `s = str(n)` supplies the decimal upper-bound digit at each position. Helper

`dfs(i, mask, lead, limit)`

returns how many valid positive distinct-digit numbers can be formed from position `i` onward under the current state.

The state components mean:

- `i`: the position currently being chosen;
- `mask`: which actual digits have already appeared in the number;
- `lead`: whether every chosen position so far is still a leading zero placeholder;
- `limit`: whether the chosen prefix still exactly matches `n`'s prefix.

Memoization with `@cache` reuses all repeated states.

**Use a bitmask to forbid repeated digits**

Bit `j` of `mask` is one when digit `j` has already been used after the number started.

The expression conceptually equivalent to

`((mask >> j) & 1) ^ 1`

is true only when bit `j` is zero. Such a digit may be chosen, and the next mask becomes:

`mask | (1 << j)`.

Once set, that bit remains set, so the same actual digit cannot appear again.

Leading zero placeholders are deliberately not added to the mask. Otherwise, shorter numbers would appear to contain repeated zeros before their first real digit.

**Distinguish a leading placeholder from an actual zero digit**

When `lead` is true and chosen `j == 0`, the recursion remains in leading mode:

`dfs(i + 1, mask, True, False)`.

This does not mean the represented number begins with a written zero. It means no real digit has been selected yet, allowing a shorter number to align with the fixed length of `s`.

Once a nonzero digit starts the number, `lead` becomes false. A later zero is an actual decimal digit, is recorded in bit zero, and cannot be repeated.

For example, the two-digit DP representation of number seven uses placeholder zero then actual seven. Number 101 uses both zero and one as actual digits and is rejected because one repeats.

**Respect the upper bound with the tight flag**

If `limit` is true, the current digit cannot exceed `int(s[i])`. Otherwise, it may range through nine:

`up = int(s[i]) if limit else 9`.

Choosing exactly the bound digit preserves tightness. Choosing a smaller digit makes every continuation safely below `n`.

The transition uses `limit and j == up`. When already loose, this stays false. When tight, `up` is the current bound digit, so equality correctly preserves the limit.

Choosing a leading zero at the first position necessarily makes the represented number shorter than positive `n`, so the leading branch sets limit false. Subsequent leading positions are already loose.

**Exclude the all-placeholder number zero**

When `i` reaches the end, the recursion returns:

`lead ^ 1`.

If `lead` is still true, no real digit was ever chosen; this path represents zero and contributes zero because the requested range begins at one.

If `lead` is false, a positive number with no repeated digits has been completed and contributes one.

**Trace the counting idea for `n = 20`**

The DP includes all one-digit numbers one through nine. Among two-digit numbers at most twenty:

- ten, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, and twenty have distinct digits;
- eleven repeats digit one and is excluded from the DP.

There are nineteen distinct-digit positive integers at most twenty. The method returns `20 - 19 = 1`, identifying eleven as the only repeated-digit number.

For one hundred, the distinct-digit DP excludes every repeated case, including one hundred because zero appears twice. Subtracting from one hundred leaves the ten repeated-digit values described by the example.

**Why memoization is valid**

Once `i`, `mask`, `lead`, and `limit` are known, the exact earlier digit sequence no longer matters:

- `mask` captures every digit-availability restriction;
- `limit` captures whether the upper-bound prefix still constrains choices;
- `lead` captures whether zero is a placeholder or a real digit.

All prefixes reaching the same state have identical continuation counts, so caching loses no information.

**Why the subtraction gives exactly the answer**

Every positive integer at most `n` has one unique padded digit path in the DP. The mask transitions accept it precisely when no actual digit repeats. The limit transitions accept it precisely when it is no greater than `n`, and the base case excludes zero.

Thus `dfs(0, 0, True, True)` counts all and only distinct-digit positive integers in the range. Subtracting that disjoint group from all `n` positive integers leaves all and only numbers with at least one repeated digit.

## Complexity detail

Let `D` be the number of decimal digits in `n`. There are at most `D \cdot 2^{10} \cdot 2 \cdot 2` memo states. Each state tries at most ten next digits. Time complexity is `O(D \cdot 2^{10} \cdot 10)` and cache space is `O(D \cdot 2^{10})`.

Because the decimal alphabet size ten is fixed, these are often summarized as linear in `D` with a moderate constant. The exact state-space description is more informative for this implementation.

The recursion depth is `O(D)`.

## Alternatives and edge cases

- **Combinatorial prefix counting:** Count distinct-digit numbers of shorter lengths with permutations, then walk `n`'s digits and count smaller unused choices. This achieves roughly `O(D^2)` time and `O(D)` space but requires more delicate formulas.
- **Digit DP that tracks a repeated flag:** Count repeated-digit numbers directly. It is valid but adds a state dimension and makes the complement approach less simple.
- **Enumerate every number:** Check digit uniqueness for each integer through `n`, which is far too slow near one billion.
- **Leading zeros:** They are placeholders and must not reserve digit zero in the mask.
- **Actual zero after the number starts:** It is a normal digit and may appear at most once.
- **All digits distinct in `n`:** The tight path itself reaches the accepting base case.
- **A repeated digit in `n`:** The tight path stops when it tries to reuse that bit, but smaller loose alternatives remain counted.
- **Number zero:** The all-leading path is explicitly excluded because the range starts at one.
- **Ten-digit boundary:** Even though `10^9` has ten digits, the fixed 1024 masks keep the DP small.
- **Input preservation:** Only the string representation and cached states are created; `n` is not modified.
