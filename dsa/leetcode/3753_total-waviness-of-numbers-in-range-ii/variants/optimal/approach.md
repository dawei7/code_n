## General

**Turn an inclusive range into two numeric prefixes**

Define `prefix(x)` as the total waviness of every integer from zero through `x`. Then the requested inclusive range is

$$
\operatorname{prefix}(\texttt{num2})-\operatorname{prefix}(\texttt{num1}-1).
$$

The helper returns zero for a nonpositive bound, which handles the lower subtraction safely.

The range can contain far too many integers to enumerate, so `prefix` uses digit DP to count all bounded decimal strings together.

**Remember the previous two significant digits**

A digit's peak or valley status becomes known only after its right neighbor is chosen. When placing a new `digit`, the state remembers:

- `previous_previous`: the digit two significant positions back.
- `previous`: the most recently placed significant digit.

If both exist, `previous` is newly confirmed as a peak when it exceeds both values, or a valley when it is below both.

The sentinel `-1` means that insufficient significant digits exist. Leading padding zeros keep both sentinels at `-1`, so shorter numbers do not gain artificial zero neighbors.

**Respect the upper bound with `tight`**

Digits are processed left to right using the decimal tuple of `bound`. When `tight` is true, the current digit cannot exceed the corresponding bound digit. Choosing exactly that digit preserves tightness; choosing less makes all later digits unrestricted through nine.

The expression `next_tight = tight and digit == limit` is correct because when tight is true, `limit` is the bound digit. When tight is false, the conjunction remains false.

**Return both number count and total waviness**

`count(state)` returns `(ways,waviness)`:

- `ways` is the number of completed padded numbers below this state.
- `waviness` is their combined future contribution.

For each candidate digit, recursion returns `suffix_ways` and `suffix_waviness`. If the newly formed triple makes `previous` a peak or valley, every one of those suffix completions receives one extra point. Therefore the transition adds

`added * suffix_ways`

rather than merely one.

It also adds `suffix_waviness`, which already includes peaks and valleys determined farther right.

At the end of all digit positions, one completed padded number has been formed and no new middle digit remains to evaluate, so the base returns `(1,0)`.

**Handle leading zeros without changing the number**

When `previous==-1` and the chosen digit is zero, the code treats it as continued leading padding and recurses with both previous states still `-1`. Once a nonzero digit starts the number, later zeros are ordinary significant digits and are passed into the history.

The all-leading-zero path represents integer zero and contributes zero waviness. Including it in both numeric prefixes is harmless; it cancels in range subtraction and has no score.

For a number like `201`, the significant history sees two, zero, one. When one is placed, zero is recognized as below both neighbors and adds one to every completion of that branch.

For a shorter number such as `98` under a three-digit bound, the padded path is `0,9,8`. The first zero remains leading and is not stored as a neighbor, so only two significant digits exist and waviness stays zero. This demonstrates why the sentinel logic matches ordinary decimal representation rather than fixed-width padding.

**Why the aggregate is exact**

Every integer from zero through the bound has one unique fixed-length representation with leading padding. Tightness includes it exactly once. Each interior significant digit is evaluated exactly when its right neighbor is appended, never before and never twice. Multiplying a new contribution by subtree ways assigns that point to all and only numbers sharing the triple.

Memoization merges states with the same position, tightness, and last two significant digits; their future possibilities and waviness behavior are identical.

The `ways` component also includes branches that later remain all-leading-zero. Their score is zero, but retaining them keeps subtree multiplication uniform and does not alter the prefix sum.

## Complexity detail

Let `D` be the decimal digit count. There are $O(D)$ positions, two tight values, and a constant $11*11$ set of previous-digit/sentinel combinations. Each state tries at most ten digits. With base ten fixed, time complexity is $O(D)$ and cached space is $O(D)$.

The recursion stack and digit tuple also use $O(D)$ space. `prefix` is invoked twice sequentially, so their caches do not coexist beyond each call's lifetime.

## Alternatives and edge cases

- **Enumerate the range:** The endpoint reaches $10^{15}$, making $O(RD)$ work impossible.
- **Track only one previous digit:** A peak or valley needs both neighbors; two significant digits of history are necessary.
- **Count a new peak once per branch:** A branch may contain many suffix completions, so the contribution must be multiplied by `suffix_ways`.
- **Treat leading zeros as digits:** This would create false peaks and valleys in shorter numbers.
- **Numbers below 100:** They never form a valid triple and naturally contribute zero.
- **Equal neighbors:** Strict comparisons make `added=0`.
- **Zero inside a number:** After the number starts, zero is significant and can be a valley.
- **Single-number range:** Prefix subtraction isolates that number's waviness.
- **Bound below one:** The helper's early zero result handles `num1-1` safely.
- **All-leading-zero number:** It is counted as one way but adds no waviness, so it cannot affect the returned sum.
