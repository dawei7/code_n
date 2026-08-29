## General

**Build only prefixes that already satisfy the rule**

A number is valid when the absolute difference between each neighboring digit equals `k`.

Rather than test every `n`-digit integer, depth-first search grows valid prefixes. Once a prefix satisfies all relationships so far, only its last digit matters for the next choice.

**Avoid leading zeros at the start**

The outer loop starts DFS from digits one through nine.

An `n`-digit integer cannot begin with zero. Starting only from nonzero digits enforces this permanently, while later appended digits may be zero.

The constraints give `n >= 2`, so there is no special one-digit zero case.

**Recognize when a prefix has length `n`**

Variable `boundary = 10 ** (n - 1)` is the smallest `n`-digit integer.

DFS starts with a one-digit positive number and appends exactly one decimal digit per edge. Therefore, `x >= boundary` means the prefix has reached length `n`.

The helper appends it and returns before adding another digit. It cannot jump from fewer than `n` digits to more than `n` digits in one append.

**Derive possible next digits**

Let `last = x % 10`.

Next digit `d` must satisfy `abs(d - last) = k`. The only possibilities are:

- `d = last + k`;
- `d = last - k`.

The first branch is used when `last + k <= 9`. The second is used when `last - k >= 0`.

No other digit satisfies the difference, so DFS explores all and only valid extensions.

**Why `k == 0` needs duplicate prevention**

When `k = 0`, both formulas produce the same digit `last`.

Without condition `k != 0` on the subtraction branch, every prefix would recurse twice to the same child, creating duplicate answers and repeated work.

The addition branch alone generates repeated-digit numbers such as `11` and `222`.

**Trace**

For `n = 3` and `k = 7`:

- Start one, extend to eight, then back to one: 181.
- Start two, extend to nine, then back to two: 292.
- Start seven, extend to zero, then seven: 707.
- Starts eight and nine yield 818 and 929.

No number begins with zero.

For `k = 1`, prefix two can extend to three and one. Each child continues using its own final digit.

**Why the search is complete**

Take any valid `n`-digit number. Its first digit is one through nine, so the correct outer DFS begins its prefix.

At every later position, the next digit is previous plus `k` or previous minus `k` and passes the corresponding range check. DFS follows that exact path and emits the number.

**Why results are valid and unique**

Every recursive edge appends a digit whose difference from the previous last digit is `k`. Every emitted number has length `n` and a nonzero first digit.

Different digit sequences produce different integers. When `k > 0`, plus and minus children differ; when `k = 0`, the duplicate branch is suppressed. Each valid number appears exactly once.

**Why answer order does not matter**

DFS explores starting digits in ascending order and plus branches before minus branches. The resulting order is deterministic but not necessarily globally sorted. The problem accepts any order, so no final sort is needed.

**Why the boundary test is safe**

All prefixes are positive and contain no leading zero. Decimal magnitude therefore exactly identifies digit length. A one-digit append multiplies by ten and adds at most nine, increasing length by at most one.

**The DFS state needs only the prefix integer**

The current digit count is not passed separately. Magnitude relative to `boundary` tells whether construction is complete, while `x % 10` gives the only digit needed for future transitions.

Earlier digits need not be inspected again because their adjacent differences were validated when they were appended. This compact state makes every recursive step constant work.

**Maximum branching remains controlled**

At most two children exist per incomplete prefix, and boundary checks often leave only one. With `n <= 9`, recursion is shallow. More importantly, branches correspond to genuine valid prefixes rather than speculative invalid numbers, so work remains tied to the solution frontier.

## Complexity detail

Let `T` be the number of valid prefix states visited and `F` the number of returned integers.

Each state performs constant work and has at most two children, so time is `O(T)`. The search is output-sensitive and never explores invalid digit choices.

The answer list uses `O(F)` space. Recursion depth is `O(n)`, at most nine. Total space is `O(F + n)`, summarized as `O(F)` under the fixed small depth.

## Alternatives and edge cases

- **Breadth-first search:** Grow all prefixes one digit at a time. Work is similar, but a full frontier is stored.
- **Test every `n`-digit integer:** It performs enormous unnecessary work.
- **String construction:** It works, but integer arithmetic makes last-digit access and output direct.
- **`k = 0`:** Only repeated-digit numbers are valid, and the second identical branch must be skipped.
- **`k = 9`:** Only transitions between zero and nine are possible after a nonzero start.
- **Next digit zero:** Valid after the first position when the difference permits it.
- **No leading zero:** Guaranteed by starting from one through nine.
- **Both branches valid:** They are distinct when `k > 0`.
- **One branch out of range:** Its bounds check prunes it.
- **Output order:** Sorting is unnecessary.
