## General
**Keep only relevant people to the right**

Scan the queue from right to left. Maintain a stack of heights that are still
potentially visible from positions farther left. From bottom to top, these
heights are strictly decreasing, so the top is the nearest surviving height.

For the current height $h$, repeatedly pop every smaller height. Each popped
person is visible: all nearer stack candidates that could block that person
have already been removed, and the remaining popped sequence rises toward
$h$. Once popped, that shorter person can never matter to someone farther left
because $h$ is both closer and taller.

**Count the first taller blocker**

After all shorter heights are popped, a remaining stack top is taller than
$h$. The current person can see that nearest taller person, so add one more,
but nobody beyond it can be visible because this taller person blocks the
view. Finally push $h$ as a candidate for positions farther left.

The current count therefore includes every shorter candidate exposed before
the first taller height and includes that taller blocker itself when it
exists. Every later person is blocked by one of those nearer people. This is
exactly the visibility condition, so the count written at each index is
correct.

## Complexity detail
Each height is pushed onto the stack once and popped at most once. Although one
iteration may perform several pops, the total number of stack operations over
the entire scan is $O(N)$, giving $O(N)$ time. The answer and monotonic stack
each use $O(N)$ space.

## Alternatives and edge cases
- **Pairwise visibility scan:** For every person, inspect all people to the
  right while tracking the tallest intervening height. This directly applies
  the definition but requires $O(N^2)$ time in the worst case.
- **Nearest-greater preprocessing:** Finding only the next taller person is
  insufficient because a person can also see multiple shorter record heights
  before that blocker.
- The rightmost person sees nobody, so its answer is always zero.
- In a strictly increasing queue, each person sees only the adjacent taller
  person.
- In a strictly decreasing queue, each person sees only the adjacent shorter
  person because that neighbor blocks every shorter person beyond it.
- Distinct heights avoid equality cases; after the smaller heights are popped,
  any remaining blocker is strictly taller.
- A one-person queue returns `[0]`.
