## General
Maintain the current second and the two remaining capacities. If the larger
capacity is smaller than the current second, then both sticks are too small and
the current state is exactly the required crash state.

Otherwise, compare the capacities. Subtract the current second from the first
stick when it is at least as large as the second stick; this `>=` comparison is
what implements the required first-stick tie rule. If the second stick is
larger, subtract from it instead. Then advance to the next second and repeat.
Each successful iteration reproduces one allocation from the definition, so
the first iteration that cannot run returns the correct crash time and
unchanged remaining capacities.

## Complexity detail
After $t$ successful seconds, the program has allocated
$1+2+\cdots+t=t(t+1)/2$ bits. This cannot exceed $M$, so
$t=O(\sqrt{M})$. Each simulated second takes constant time, giving
$O(\sqrt{M})$ total time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Closed-form phase calculations:** arithmetic can skip groups of
  allocations, but handling the changing larger stick and the first-stick tie
  rule makes that approach substantially more delicate.
- **Bit-by-bit allocation:** decrementing one bit at a time produces the same
  states but performs $O(M)$ work instead of one update per second.
- If both sticks start at zero, the crash occurs immediately at second one.
- Equal capacities must select the first stick, including equalities reached
  after earlier allocations.
- A stick may become exactly zero after a successful request; the crash is
  reported only at the next request that neither stick can satisfy.
