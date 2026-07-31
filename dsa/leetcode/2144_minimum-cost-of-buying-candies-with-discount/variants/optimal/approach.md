## General

**Make each free candy as valuable as possible**

Sort all prices in descending order. Consider the largest remaining candy. It
cannot be free: making it free would require two unassigned candies costing at
least as much, which do not exist. The two largest remaining candies must
therefore be paid for.

After paying for those two, the largest remaining candy is eligible for the
discount because it costs no more than either purchased candy. Choosing any
cheaper candy for free would pay unnecessarily for this larger eligible one,
so the third price should be free.

**Repeat descending groups of three**

Apply the same exchange argument to each consecutive group of three sorted
prices: pay for the first two and omit the third from the total. Any final one
or two candies have no complete discount group and must be paid for. Summing
indices whose zero-based positions are not congruent to `2` modulo `3` yields
the minimum cost.

## Complexity detail

Let $n$ be the number of candies. Sorting takes $O(n\log n)$ time and the scan
takes $O(n)$ time. Creating a separate sorted list uses $O(n)$ space.

## Alternatives and edge cases

- **Repeated maximum extraction:** Selecting and removing the next three
  largest prices without sorting once is correct but takes $O(n^2)$ time with
  a list.
- **Counting frequencies:** Because prices are bounded by $100$, a frequency
  array can process prices descending in $O(n+100)$ time and $O(100)$ space.
- With fewer than three candies, every candy must be purchased.
- Equal prices still form valid groups because the free cost may equal the
  cheaper purchased cost.
- One or two prices remaining after complete groups are both paid.
