## General

**Identify exactly which values can appear**

Removing zero digits from a positive integer leaves a positive integer whose decimal representation contains no zero.

Also, the result cannot exceed its source. Removing a digit shortens the decimal representation or leaves it unchanged; for positive decimal numbers this never increases the value. Therefore every written result is a zero-free positive integer at most `n`.

The converse is immediate: every zero-free positive integer `y<=n` appears by choosing source `x=y`. Removing zeros changes nothing because `y` has none.

Hence there is a bijection between distinct written results and positive integers at most `n` whose decimal representation contains no zero. The problem becomes a digit-counting task; it does not require processing all `n` source integers.

**Pad shorter numbers with leading zeros**

Let `s=str(n)` and let `D=len(s)`. Digit DP constructs a length-`D` digit sequence bounded by `s`. Numbers with fewer digits are represented by leading zeros, which are padding rather than decimal digits of the number.

This distinction explains the `lead` state. While `lead` is true, choosing digit zero continues the leading padding and must not disqualify the number.

Once a nonzero digit starts the number, any later zero is a real decimal zero and makes the candidate invalid. The `zero` state records whether such a forbidden non-leading zero has appeared.

**Meaning of the four-state recursion**

`dfs(i, zero, lead, lim)` counts valid completions starting at digit position `i`:

- `zero` says a real zero has already appeared.
- `lead` says no nonzero digit has started the number yet.
- `lim` says the chosen prefix still equals `n`'s prefix, so the current digit cannot exceed `s[i]`.

If `lim` is true, `up=int(s[i])`; otherwise digits through nine are allowed.

For chosen digit `j`:

`nxt_zero = zero or (j == 0 and not lead)`

flags zero only if the number had already started before this position.

`nxt_lead = lead and j == 0`

keeps leading status only while all chosen digits are padding zeros.

`nxt_lim = lim and j == up`

keeps tightness when the chosen digit equals `n`'s current bound digit. When `lim` is false, the conjunction remains false regardless of `up=9`.

**Accept only positive zero-free completed numbers**

At `i==D`, the recursion returns one exactly when `zero` is false and `lead` is false.

`not zero` means no decimal zero appeared after the number began. `not lead` excludes the all-padding-zero sequence, which represents integer zero and is outside the positive range.

Every accepted padded digit sequence represents one distinct zero-free integer from one through `n`. Every such integer has one unique padded representation, so no value is counted twice.

For `n=10`, the accepted numbers are one through nine. Ten is rejected because its final zero is non-leading, producing answer nine.

For `n=105`, shorter zero-free numbers are handled through leading padding, while three-digit candidates are constrained lexicographically by `lim`. A candidate such as 99 is represented as `099`: the first zero is leading and harmless.

**Why memoization makes the recursion small**

Without caching, many digit prefixes lead to the same combination of position and flags. `@cache` evaluates each state once. There are only `D` positions and eight Boolean combinations, with at most ten outgoing digit choices.

The function closes over `s`, which is assigned before the initial call. Python resolves that nonlocal value when the function executes.

## Complexity detail

Let `D` be the number of decimal digits in `n`. There are $O(D)$ flag states because the Boolean dimensions are constant. Each considers at most ten digits, also constant. Time complexity is $O(D)$.

The memoization table and recursion stack store $O(D)$ states/depth. The decimal string also has length `D`, so auxiliary space is $O(D)$.

For `n<=10^{15}`, `D` is at most sixteen, but the symbolic bound explains the digit-DP scaling.

## Alternatives and edge cases

- **Iterate from one through `n`:** The bound reaches $10^{15}$, making direct generation impossible.
- **Insert stripped results into a set:** This still requires visiting every source and potentially enormous storage. The zero-free bijection counts results directly.
- **Count all numbers with digits one through nine by length only:** That handles shorter lengths but not the partial final length bounded by `n`. Tight-state digit DP covers both uniformly.
- **Treat leading zeros as forbidden zeros:** Then every shorter number would be rejected. `lead` separates padding from real digits.
- **Count integer zero:** The all-leading-zero path is excluded by `not lead`.
- **`n<10`:** Every positive number through `n` is zero-free, so the answer is `n`.
- **`n=10`:** Ten maps to one, which already exists; the count remains nine.
- **Zeros inside `n`:** Tightness can move below the bound before that position, allowing nonzero digits in candidates even when `n` has zero there.
- **Trailing zero in a candidate:** It sets `zero` and is rejected at completion.
- **Repeated stripped outputs:** The bijection proves duplicates correspond to the same zero-free representative, counted once.
- **Cache flags:** Including `lim` is necessary because equal-prefix states have different digit bounds from already-smaller states.
- **Positive-input guarantee:** There is always at least one possible result, but the base logic still explicitly excludes zero.
