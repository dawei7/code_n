## General

**Scan from right to left so future prices are already known.** For item `i`, the discount is the first later price no greater than its original price. Processing from the end lets a stack summarize useful candidates to the right.

The source saves `x = prices[i]` before modifying the array. This original value must be pushed later; a discounted final price must never serve as another item's discount.

**Remove candidates that current x dominates.** While the stack top is strictly greater than `x`, it is popped. Such a value cannot discount `x`. It also cannot be the first useful discount for an earlier item in preference to `x` when `x` is closer and smaller, so it is permanently dominated.

The comparison is strict. If the top equals `x`, it is a valid no-greater discount for the current item and must remain long enough to be used.

After all larger tops are removed, an existing top is no greater than `x`. The stack construction guarantees it corresponds to the nearest qualifying later item among undominated candidates, so the code subtracts it.

Then the original `x` is pushed. It becomes the closest right-side candidate for the next item processed to the left.

**Understand the stack's order.** From bottom to top, retained prices are nondecreasing. When a smaller `x` arrives, every larger top is removed until that order can be restored; equal values may remain. More importantly, the top represents the closest surviving position to the current index because items are pushed as the scan moves left. Value monotonicity enables efficient rejection, while stack order preserves the required nearest-position rule.

**Trace the sample.** Starting from `[8,4,6,2,3]`, three is pushed. Processing two pops three because it is larger, leaving no discount for two, then pushes two. Processing six sees two and subtracts it. Processing four also sees two. Processing eight eventually sees four as the nearest qualifying price and subtracts four.

**Why the nearest rule survives popping.** A popped price `p` is greater than the current closer value `x`. For any future item to the left that could use `p`, `x` is also no greater than that item and occurs earlier than `p`, so `p` can never be selected. Removing it loses no answer.

Values that remain preserve the necessary nearest candidates. The top is always the first usable one for the current original price after dominated entries are removed.

Suppose a farther value is smaller than the top. It does not replace the top merely for being cheaper because the rule requests the minimum index, not the greatest discount. The stack leaves the nearer qualifying top accessible. This distinction is why a global suffix minimum would answer a different problem.

**Mutation is intentional.** Discounts are written directly into `prices[i]`, and the same list is returned. Storing original `x` before subtraction isolates stack logic from those mutations.
Before processing index `i`, the stack contains exactly the undominated candidates from positions to its right, ordered so its top is the nearest candidate that survives the monotonic filter. Popping removes only candidates proven unusable for `i` and dominated for every earlier index. If a top remains, it is the first later price no greater than `x`; otherwise none exists. Pushing original `x` establishes the invariant for index `i - 1`.

## Complexity detail

Each of `N` original prices is pushed once and popped at most once. Although a while loop is nested inside the scan, total stack operations are `O(N)`, so time is `O(N)`.

The stack may contain all prices, such as for a nondecreasing pattern viewed from the appropriate scan direction, giving `O(N)` auxiliary space. The result reuses the input list rather than allocating another output array.

Membership, comparisons, subtraction, and list-end operations are amortized constant time.

The manifest's `O(N)` time and space accurately describe this source.

## Alternatives and edge cases

- **Left-to-right index stack:** Keep unresolved item indices and apply the current price when it is the first smaller-or-equal value. It is the common equivalent formulation.
- **Nested scan:** Search rightward from every item and stop at the first qualifying price. It is simpler but `O(N^2)` in the worst case.
- **Equal next price:** Equality qualifies; the strict pop condition preserves it for subtraction.
- **No qualifying later price:** The stack empties after larger values are removed, so the original price remains unchanged.
- **Last item:** It has no later item and is pushed without a discount.
- **Strictly increasing prices:** No item finds a no-greater later price, so values remain unchanged.
- **Repeated prices:** The nearest equal price supplies the discount.
- **Original versus final price:** The stack receives `x` captured before mutation, never the discounted value.
- **Zero final price:** Equal price can be subtracted completely, which is valid.
- **Nearest rather than cheapest:** A farther smaller price must not replace an earlier qualifying price; stack position preserves this rule.
- **Stack value order:** Strictly larger tops are removed, while equal values remain long enough to serve as valid discounts.
- **Single item:** The stack is initially empty, so its price remains unchanged.
- **Input mutation:** The caller's `prices` list is changed and returned.
- **Amortized proof:** Popped entries never return, bounding all while iterations by `N`.
- **Nearest-index requirement:** Dominance removal is safe specifically because the current value is closer to all future left-side items.
