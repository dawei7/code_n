## General

**Enumerate the shorter quantity range**

Swap the two costs when necessary so `cost1` is the larger cost. The number of
affordable quantities of this item is then no greater than the quantity range
for the cheaper item.

For every feasible amount spent on the first item, the remaining money is
`total - spent`. The second-item quantity may be any integer from zero through
`(total - spent) // cost2`, giving one more choice than that quotient. Add this
count for every first-item quantity.

Every valid purchase pair appears in exactly one iteration determined by its
first-item quantity, and that iteration counts its second-item quantity because
the pair is affordable. Conversely, every counted second-item quantity fits
within the remaining budget. The sum therefore counts all valid pairs exactly
once.

## Complexity detail

With $T$, $c_1$, and $c_2$ as defined in the contract, iterating quantities of
the more expensive item takes $O(T/\max(c_1,c_2))$ time. The arithmetic count
uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate both quantities:** Testing every affordable pen and pencil pair is correct but can take $O((T/c_1)(T/c_2))$ time.
- **Enumerate the cheaper item:** It produces the same answer but may perform many more iterations when the costs differ greatly.
- **Both items unaffordable:** The pair `(0, 0)` is still one valid way.
- **Equal costs:** Either item may be chosen for the outer loop.
- **Exact budget use:** Choices spending exactly `total` are included.
- **Unused money:** Spending less than `total` remains valid.
- **Zero quantities:** Neither item kind is required to appear in a purchase.
