## General

**Turn the decoding rules into prefix counting**

A valid letter consumes either one encoded character or two encoded characters. That means the number of decodings of a prefix can be determined from only the two immediately shorter relevant prefixes:

- consume the last character alone and extend every decoding that ends just before it;
- consume the last two characters together and extend every decoding that ends just before that pair.

Let `dp[i]` mean the number of ways to decode the first `i` characters of `s`. The recurrence has the form
`dp[i] = one(i) * dp[i - 1] + two(i) * dp[i - 2]`,
where `one(i)` is the number of valid single-digit interpretations of the final character and `two(i)` is the number of valid two-digit interpretations of the final pair.

The multipliers matter because `*` is not one fixed digit. It independently represents any digit from one through nine, and several replacements may make the same one- or two-character segment valid.

**Why the empty prefix has one decoding**

Before reading any characters, `dp[0]` is one, not zero. It represents the one empty decoding. This is the neutral starting point that lets a valid first character create the proper number of length-one decodings. For example, a first character `*` has nine possible meanings, so it contributes `9 * dp[0] = 9`.

There is no valid prefix of length negative one, so the rolling variable corresponding to `dp[-1]` starts at zero. The exact implementation initializes `a = 0` and `b = 1`. Before the first iteration, these conceptually represent `dp[-1]` and `dp[0]`. Two-character logic is skipped when `i` is one, so only the meaningful `b` value is used at that point.

**Count the one-character interpretations**

For position `i`, the final character is `s[i - 1]`:

- If it is `*`, it may be any of one through nine, so there are nine valid single-character choices. Their contribution is `9 * dp[i - 1]`.
- If it is an ordinary nonzero digit, it maps to exactly one letter, so the contribution is `dp[i - 1]`.
- If it is zero, it cannot stand alone, so the single-character contribution is zero.

The solution stores this contribution in `c` first. It then adds all valid two-character contributions.

**Count every two-character pattern**

Once at least two characters have been read, inspect the previous character and the current character together. A two-digit code is valid only when its numeric value is between ten and twenty-six.

If both characters are `*`, the valid replacements are eleven through nineteen and twenty-one through twenty-six. That is nine choices beginning with one and six choices beginning with two, for fifteen choices total. The contribution is therefore `15 * dp[i - 2]`.

If only the previous character is `*` and the current character is fixed:

- A current digit from zero through six can be preceded by either one or two, producing two valid codes. This includes zero: ten and twenty are both valid.
- A current digit from seven through nine can only be preceded by one, producing one valid code.

The exact comparison `s[i - 1] > "6"` works because all compared values are single decimal characters whose character order matches their numeric order.

If the previous character is fixed and the current one is `*`:

- Previous `1` allows eleven through nineteen, giving nine choices.
- Previous `2` allows twenty-one through twenty-six, giving six choices.
- Any other previous digit allows no valid two-character interpretation with `*`.

Finally, if both characters are fixed digits, the pair contributes one copy of `dp[i - 2]` exactly when the previous digit is not zero and the numeric value is at most twenty-six. The nonzero test rules out strings such as `06`. Because the value has two characters and the first is nonzero, it is automatically at least ten.

These cases are mutually exclusive and collectively cover every possible kind of final pair, so no replacement is counted twice or omitted.

**Why two rolling values are enough**

At the beginning of a normal iteration, `a` represents `dp[i - 2]` and `b` represents `dp[i - 1]`. The code calculates the new count in `c` using only those two values. It then performs `a, b = b, c`, moving the window forward for the next character.

The value of `c` is assigned anew by the one-character branch on every iteration before any two-character contribution is added. Therefore, no count from a previous iteration leaks into the current one even though `c` is not reset in a separate statement.

This rolling form stores the same values that a full dynamic-programming array would store, but discards older entries once no future recurrence can use them.

**Why the recurrence is correct**

Take any valid decoding of the first `i` characters. Its final letter must have been formed from either the final one encoded character or the final two encoded characters; no letter uses any other length. These two categories cannot overlap because they consume different final segments.

In the first category, choosing one valid interpretation of the last character can be combined with every valid decoding of the first `i - 1` characters. This creates exactly `one(i) * dp[i - 1]` decodings. In the second category, choosing one valid interpretation of the final pair can be combined with every valid decoding of the first `i - 2` characters, creating exactly `two(i) * dp[i - 2]` decodings.

Every combination constructed this way is valid, and removing the last decoded letter maps it back to one unique shorter-prefix decoding. Thus the recurrence counts every valid decoding exactly once. Applying it from the empty prefix through the complete string makes the final `c` equal to the required answer.

**Why the modulo can be applied during the computation**

Counts can grow exponentially with string length, but only the answer modulo `1,000,000,007` is requested. Addition and multiplication are compatible with modular arithmetic, so reducing intermediate one- and two-character contributions produces the same final remainder as computing the enormous exact count first. The solution applies the modulo after the initial single-character multiplication where needed and after each added pair contribution, keeping values bounded.

## Complexity detail

Let `N` be the length of `s`. The loop visits each position exactly once. Every iteration performs a fixed number of character comparisons, arithmetic operations, and assignments, independent of `N`. The running time is therefore `O(N)`.

Only `a`, `b`, `c`, the index, and a few fixed constants are stored. No dynamic-programming array or recursion stack grows with the input, so auxiliary space is `O(1)`. The input string itself is read but not copied as part of the algorithm, and the integer values stay bounded by the modulus.

The modulo operations are treated as constant-time because their operands remain within a constant-size multiple of the fixed modulus. This is another reason to reduce throughout instead of allowing arbitrary-size exact counts to accumulate.

## Alternatives and edge cases

- **Full dynamic-programming array:** Storing `dp[0]` through `dp[N]` makes prefix meanings visually explicit and uses the same recurrence. It is correct in `O(N)` time but requires `O(N)` space even though only the previous two entries are ever needed.

- **Top-down recursion with memoization:** A recursive function can decode from a chosen index and memoize the number of suffix decodings. It has the same asymptotic time, but uses `O(N)` cache and call-stack space and risks recursion-depth limits for a string as long as one hundred thousand.

- **Expanding every wildcard first:** Each `*` has nine choices, so materializing replacements takes exponential time and space. The multipliers in the recurrence count those choices symbolically instead.

- **Treating `*` as zero through nine:** The wildcard represents only digits one through nine. It can participate in a code ending in zero only when the actual zero already appears as the other character, as in `*0` becoming ten or twenty.

- **A standalone zero:** It contributes no one-character decoding. It survives only when paired with a preceding one or two, including the corresponding choices supplied by a preceding wildcard.

- **The pair `**`:** It has fifteen two-character interpretations, not eighteen. Values twenty-seven, twenty-eight, and twenty-nine are outside the letter range.

- **The pair `*0`:** It has two interpretations, ten and twenty. The current zero contributes nothing by itself, so the pair contribution is the only way such a suffix can remain valid.

- **The pair `0*`:** It has no two-character interpretation because a code cannot begin with zero, and `*` must be decoded using some other grouping if possible.

- **A prefix with zero valid decodings:** Its rolling count becomes zero. Later characters cannot repair an invalid boundary unless a valid two-character grouping uses the immediately previous character; the recurrence handles this because that pair uses `dp[i - 2]` rather than `dp[i - 1]`.

- **One-character input:** The pair logic is skipped. A wildcard returns nine, a nonzero digit returns one, and zero returns zero.

- **Modulo placement:** Postponing all reductions is mathematically valid in Python but causes needlessly huge integers. In fixed-width languages it can overflow, so modular multiplication and addition should be applied as each contribution is formed.
