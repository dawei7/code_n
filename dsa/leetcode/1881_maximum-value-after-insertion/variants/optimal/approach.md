## General

**Maximizing depends on the sign.** Inserting one digit makes every candidate have the same final number of digits, so the first position at which two candidates differ determines which numerical value is larger. For a positive number, the goal is the lexicographically largest digit sequence: place `x` before the first existing digit smaller than `x`. For a negative number, a numerically larger result has a smaller absolute magnitude, so the goal reverses: place `x` before the first magnitude digit larger than `x`.

**Handle the minus sign before scanning digits.** Variable `i` begins at zero. If `n[0] == "-"`, the code increments `i` to one so insertion can never occur to the left of the sign. The remaining characters are all digits. For a positive number, scanning naturally begins at zero. This single boundary difference lets the returned slices preserve the sign without treating it as a numeric digit.

**Positive-number rule.** The loop continues while `int(n[i]) >= x`. Every digit greater than `x` should remain before `x` because moving `x` ahead of it would make the first differing digit smaller and therefore reduce the result. Equal digits can also be passed: inserting before or after an equal digit produces the same complete digit sequence. The first digit below `x` is the first position where inserting `x` improves the most significant available place. The loop stops there, and insertion occurs before that smaller digit.

For `n = "73"` and `x = 6`, digit `7` is at least six, so the scan passes it. Digit `3` is below six, so insertion gives `"763"`. Inserting at the front would give `"673"`, whose first digit is worse, while appending would give `"736"`, which loses at the second digit. The first-smaller rule selects the maximum without constructing all candidates.

**Negative-number rule.** After skipping the sign, the loop continues while `int(n[i]) <= x`. For a negative value, smaller magnitude digits should appear as early as possible, so every existing digit below `x` remains before it. Equal digits again make no difference. The first digit greater than `x` is where inserting the smaller `x` reduces the magnitude at the earliest possible position and therefore makes the signed number less negative.

For `n = "-13"` and `x = 2`, the scan passes digit `1` because it is at most two, then stops before digit `3`. The result `"-123"` is greater than `"-132"` and `"-213"`. Although `123 < 132 < 213` in magnitude, placing the minus sign reverses their numerical order, which explains the inverted comparison.

**Append when no decisive digit exists.** If a positive number contains only digits at least `x`, putting `x` at the end is optimal: inserting earlier would move `x` ahead of a larger digit. If a negative number contains only digits at most `x`, appending is likewise optimal because moving the larger magnitude digit earlier would make the number more negative. The loop reaching `len(n)` naturally implements both cases.

**Construct exactly one result.** The expression `n[:i] + str(x) + n[i:]` keeps the prefix before the selected position, inserts the one-character decimal form of `x`, and then keeps the suffix. Because `x` is guaranteed to lie from one through nine, `str(x)` is exactly one digit. Slicing also preserves the minus sign in the negative prefix because `i` never falls below one in that branch.

**Why the first qualifying position is globally optimal.** Consider the positive case. Every earlier digit is at least `x`, so placing `x` before any strictly larger earlier digit makes that earlier position worse; passing equal digits does not change the resulting sequence. At the first smaller digit, inserting `x` creates the greatest possible digit at the earliest position where improvement is available. Later digits cannot compensate for losing that earlier comparison. The negative case applies the same first-difference argument to absolute values with the order reversed. Thus no later insertion can beat the chosen one, and no earlier insertion is better.

**Input and output stay textual.** The number may contain up to $10^5$ digits, far beyond ordinary integer ranges. The algorithm never parses the entire number. It converts only one character at a time for comparison and returns a new string, so its behavior is independent of machine integer size.

## Complexity detail

Let $N$ be the length of the input string, including a possible minus sign. The scan advances `i` monotonically and inspects at most every digit once, costing $O(N)$ time. Constructing the prefix slice, digit string, suffix slice, and concatenated result also copies $O(N)$ characters. Total time is $O(N)$.

The returned string has $N+1$ characters. Python slicing and concatenation create new string objects whose total storage is $O(N)$, matching the manifest. Excluding the required output, transient slices are still linear in this exact expression. The index and individual converted digit use constant space.

Converting `n[i]` with `int` is constant time because it is a one-character string known to be a digit. The code never performs arithmetic on the full large number. This distinction is why the method remains linear even for the maximum $10^5$-character input.

## Alternatives and edge cases

- **Generate every insertion candidate:** Constructing $O(N)$ strings of length $O(N)$ and comparing them costs $O(N^2)$ time and space traffic. The first-difference rule identifies the winner in one scan.
- **Parse into an integer:** The input can be vastly larger than fixed-width numeric types, and converting plus multiplying by powers of ten is unnecessary. String order contains all information needed.
- **Use character comparisons:** Because digits `'1'` through `'9'` have the same lexicographic and numeric order, comparing characters with `str(x)` could avoid repeated `int` calls. The exact source uses integer comparison explicitly.
- **All digits equal to `x`:** The scan passes every equal digit and appends `x`. Inserting anywhere produces the same final string, so this tie choice is valid.
- **Positive number with every digit smaller than `x`:** The scan stops immediately and inserts `x` at the front, the most significant possible position.
- **Negative number with every digit larger than `x`:** The scan stops just after the minus sign, placing the smaller digit at the front of the magnitude and maximizing the negative value.
- **Insertion beside the sign:** For a negative input, starting at index one permits insertion immediately after `'-'` but never before it, exactly matching the rule.
- **No zero digits:** The contract restricts all digits and `x` to one through nine. If zeros were allowed, the same comparison proof would still work, but representation rules around leading zeros might need separate clarification.
- **Input preservation:** Python strings are immutable. The source returns a newly assembled string and cannot modify `n` in place.
