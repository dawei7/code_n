## General

**Count ages instead of people**

The decision to send a request depends only on the sender's age and the recipient's age. Individual identities matter only for excluding a person from sending to themself.

Ages are bounded from 1 through 120, so the solution builds `cnt` of length 121, where `cnt[a]` is the number of people aged `a`. This compresses as many as 20,000 people into at most 121 age categories.

The two nested loops then examine every ordered pair of ages `(ax, ay)`. Variable `x` is the number of possible senders aged `ax`, and `y` is the number of possible recipients aged `ay`.

**Apply the rejection rules exactly**

A sender aged `ax` does not request a recipient aged `ay` when at least one condition holds:

$$
ay\le 0.5ax+7,
$$

$$
ay>ax,
$$

or

$$
ay>100\ \text{and}\ ax<100.
$$

The code places these three conditions inside `not (...)`. It enters the counting branch only when none is true, exactly matching the statement's “otherwise.”

Age zero entries exist in the count array only for convenient indexing and have count zero, so they add nothing.

**Count ordered requests**

If `ax != ay` and the age pair is permitted, any of the `x` senders may request any of the `y` recipients. That gives `x * y` directed requests.

Direction matters. A request from person A to person B is distinct from a request from B to A, and the reverse age pair is evaluated separately by the loops. The rules are not generally symmetric.

When `ax == ay`, the raw product `x * y = x^2` includes each person choosing themself. For every one of the `x` senders, exactly one of the `y` same-aged recipients is that sender. Therefore, each sender has only `y - 1` valid same-age recipients, giving `x(y-1)`.

The expression

`x * (y - int(ax == ay))`

handles both cases. The equality converts to 1 for the same age and 0 otherwise.

For two people aged 16, the pair 16 to 16 passes because `16 > 15` and is not older than the sender. The contribution is `2 * (2 - 1) = 2`, representing the two opposite directed requests.

**Why category multiplication is exact**

Every ordered pair of distinct people belongs to one unique ordered age pair. The rules give the same decision for all people in that category. If disallowed, the code contributes zero; if allowed, it counts every possible sender-recipient combination, subtracting precisely the self-pairs when ages match.

Thus, no valid request is missed and no invalid or self request is included. Summing across all age pairs produces the complete total.

**The third condition is preserved**

Under the other two inequalities, the condition involving 100 may appear redundant for the given formulation, but the exact solution still checks it verbatim. Keeping it makes the implementation directly faithful to the stated contract and avoids depending on an unstated simplification.

The bounded-domain approach is preferable to sorting individual ages because the number of possible age values is tiny and fixed.

## Complexity detail

Let `n` be the number of people and `A = 121` be the size of the age domain.

Building `cnt` takes `O(n)` time. The nested loops examine `A^2` age pairs. Since `A` is a fixed bound, this is constant in the problem's input growth; written parametrically, the time is `O(n + A^2)`. With the fixed age domain, this is reported as `O(n + A)` or simply `O(n)` in the manifest.

The count array uses `O(A)` space. All loop values and the accumulator use constant additional storage. No structure proportional to the number of possible person pairs is created.

The compression is the source of the efficiency: direct examination of every ordered pair of people would take `O(n^2)`.

## Alternatives and edge cases

- **Check every pair of people:** It follows the definition directly but takes quadratic time. Age frequencies aggregate people with identical behavior.

- **Sort and use two pointers:** Sorting can count eligible recipient ranges per sender age, but the fixed 1–120 domain makes a frequency table simpler.

- **Prefix sums by age:** They can sum allowed recipient counts for each sender age. This reduces a generalized `A^2` scan to `O(A)`, though `A = 121` already makes the direct pair scan tiny.

- **Same person:** The subtraction for `ax == ay` removes exactly one recipient choice per sender.

- **Same age, several people:** Requests are directed, so `x` people contribute `x(x-1)` when that age pair is allowed.

- **Only one person at an allowed age:** Same-age contribution is zero because there is nobody else to request.

- **Age pair disallowed by several rules:** It is still skipped once; the Boolean disjunction needs only one true condition.

- **Empty age bucket:** `x = 0` or `y = 0` makes the contribution zero without a special branch.

- **Requests are asymmetric:** Both ordered age pairs are tested independently; acceptance in one direction does not imply acceptance in reverse.

- **Boundary equality:** `ay <= 0.5 * ax + 7` is forbidden, so equality at the threshold must be rejected.

- **Maximum age:** Index 120 exists because the array length is 121.

- **No input mutation:** The algorithm builds a separate count array and leaves `ages` unchanged.
