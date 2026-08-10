## General

**Reduce two current values into one**

Any legal expression using binary operators can be evaluated by repeatedly choosing two available subexpression values, combining them with one operator, and replacing them with the result.

Starting with four card values:

- the first operation leaves three values;
- the second leaves two;
- the third leaves one.

The recursive search enumerates every such reduction order and operation choice.

**Recursive state**

`dfs(nums)` receives the current multiset of floating-point values produced by card values or earlier subexpressions.

When only one value remains, no more binary operation can be applied. The branch succeeds when:

`abs(nums[0] - 24) < 1e-6`.

The tolerance is necessary because real division can produce repeating binary floating-point approximations. A mathematically exact result such as 24 may be represented as `23.999999999...`.

**Choose two distinct current entries**

The nested loops select ordered indices `i` and `j` with `i != j`.

`nxt` contains every current number except those two. Each list position represents a distinct available card or derived subexpression, so equal numeric values at different positions can still be selected separately.

The selected pair is combined, and its result is appended to `nxt` for the recursive call.

**Why ordered pairs matter**

Addition and multiplication are commutative, so trying both `a + b` and `b + a` duplicates work. Subtraction and division are not:

- `a - b` may differ from `b - a`;
- `a / b` may differ from `b / a`.

By iterating ordered pairs, the same four operation cases include both operand orders automatically. This is simpler than choosing unordered pairs and manually generating reverse subtraction and division.

**Try every allowed operation**

The tuple `ops` contains plus, minus, multiplication, and real division.

For each operation, the recursive state becomes the remaining values plus:

- `nums[i] + nums[j]`;
- `nums[i] - nums[j]`;
- `nums[i] * nums[j]`;
- `nums[i] / nums[j]`.

Division is skipped when the denominator `nums[j]` is zero. Zero may appear as an intermediate subtraction result even though original cards are positive.

No unary negation is introduced. A negative value can arise only from a valid binary subtraction, which respects the rules.

**Backtracking through new lists**

Each recursive call receives a newly built list. The caller's `nums` and `nxt` structure for other operation choices are not mutated by deeper calls.

This is a functional form of backtracking: after a recursive call returns, the loop simply tries another result without needing explicit undo operations.

**Early success**

`ok` accumulates recursive results. Once some operation for a selected pair makes `ok` true, the code finishes that small operation loop and returns true after the pair.

The statement `ok |= dfs(...)` evaluates the recursive call even if `ok` is already true, so it is not as aggressively short-circuiting as `ok = ok or dfs(...)`. Nevertheless, the immediate check after the four operations prevents exploration of later index pairs once success is known.

**A successful expression**

For cards `[4, 1, 8, 7]`, one search branch can:

- combine eight and four with subtraction to produce four;
- combine seven and one with subtraction to produce six;
- combine four and six to produce 24.

The final state contains one value within the tolerance and returns true. These reductions correspond to expression `(8 - 4) * (7 - 1)`.

**Why every parenthesization is covered**

A fully parenthesized binary expression is a binary tree. Every internal node combines results of two child subexpressions.

The search can evaluate any pair of child subexpressions when their component cards have already been reduced to current values. Repeated pair choices therefore realize every binary-tree shape, card ordering, and operator assignment.

Conversely, every recursive branch combines two disjoint current subexpressions with one allowed binary operator. Since the two selected values are removed and their result inserted, each original card is used exactly once. Every successful branch corresponds to a legal expression.

Thus exhaustive search returns true exactly when some allowed expression evaluates to 24.

**Why direct permutations are unnecessary**

Selecting ordered pairs dynamically already determines card order and parentheses. Explicitly generating all card permutations and all parenthesis templates would enumerate the same possibilities less naturally.

## Complexity detail

The contract fixes the input at exactly four cards. Therefore, the recursion tree has a fixed finite maximum size, independent of any growing input parameter. Under the problem's formal constraints, time and auxiliary space are both `O(1)`.

If generalized to `C` cards, the search is exponential or factorial in `C`: at a state of size `r` it considers `r(r - 1)` ordered pairs and four operations before recursing to size `r - 1`. Temporary list construction also costs `O(r)`. The constant claim is valid only because `C = 4`.

Recursion depth is three combination steps beyond the initial call. Temporary lists and floating-point values are likewise bounded by a constant for four cards.

## Alternatives and edge cases

- **Exact rational arithmetic:** Use fractions represented by numerator and denominator. This avoids floating-point tolerance and division-rounding concerns, at the cost of larger integer arithmetic.

- **Subset dynamic programming:** For every subset of cards, store every reachable value by splitting the subset into two parts. It systematically removes duplicate recomputation but is more machinery for four cards.

- **Enumerate permutations, operators, and parenthesis shapes:** This is finite and workable for four cards but easier to omit a shape or mishandle noncommutative operations.

- **Memoize normalized states:** Sort or canonicalize current values and cache failures. Floating-point keys need care, while exact fractions make memoization safer.

- **Division by zero:** The branch is skipped. Other operations with the same pair are still legal.

- **Intermediate fraction:** Real division is required; integer division would miss solutions such as those involving one third.

- **Floating-point rounding:** The epsilon comparison accepts tiny representation errors without treating visibly different values as 24.

- **Duplicate card values:** Indices, not values, identify available cards. Equal cards can both be used.

- **Negative intermediate value:** Binary subtraction may legally produce it and later operations may use it.

- **Zero intermediate value:** It may be added, subtracted, or multiplied, but cannot serve as a divisor.

- **Commutative duplicate branches:** Addition and multiplication are explored twice for reversed indices. This affects only a fixed constant here.

- **Exactly four cards:** The `O(1)` analysis relies on this fixed-size contract; it should not be generalized without stating exponential growth.

- **No concatenation:** Every starting number remains a separate card value; the algorithm never joins digit strings.

- **No unary operator:** Signs arise only from binary subtraction, consistent with the rules.
