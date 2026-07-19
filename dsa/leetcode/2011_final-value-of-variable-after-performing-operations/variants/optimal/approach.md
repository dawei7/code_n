## General
**Reduce each statement to its signed effect.** The prefix or postfix position
does not change this problem's result. Every valid string containing `+`
contributes $1$, while every valid string containing `-` contributes $-1$.
Accumulate those contributions from an initial total of zero.

**Why the accumulated sum is the final value.** After any processed prefix,
the running total equals the number of increments in that prefix minus its
number of decrements. Applying the next operation changes both the simulated
variable and this total by the same signed unit. The equality therefore holds
for every prefix, including the complete list, so the final sum is exactly the
requested value.

## Complexity detail
Here $N$ is the number of operations. Inspecting each fixed-length string once
takes $O(N)$ time. The running total uses $O(1)$ additional space.

## Alternatives and edge cases
- **Four explicit string branches:** Comparing against each allowed literal is
  correct but repeats logic that the shared sign already identifies.
- **Count then subtract:** Compute the number of increment strings and use
  `increments - (N - increments)`; this has the same asymptotic costs.
- Prefix and postfix forms have identical effects for this task because no
  surrounding expression observes an intermediate value.
- A single decrement returns $-1$; the result is not restricted to
  nonnegative values.
- Equal numbers of increment and decrement operations return zero regardless
  of their order.
