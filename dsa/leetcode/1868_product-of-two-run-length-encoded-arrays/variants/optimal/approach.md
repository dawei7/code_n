## General
**View the current runs as two remaining intervals**

Keep one pointer in each encoding and track the unconsumed frequency of both current runs. Their decoded positions overlap for the smaller remaining frequency. Every position in that overlap has the same product, so append exactly one product run for that many positions.

**Advance every exhausted boundary**

Subtract the overlap length from both remaining frequencies. Advance a pointer whenever its current frequency reaches zero; when both reach zero together, advance both. Each iteration therefore consumes at least one complete input run, so the number of iterations is at most $M+N-1$.

**Preserve canonical compression**

The same product can arise on both sides of an input boundary. Before appending, compare the product with the last output value. Equal values extend the last frequency; different values start a new output pair. Every decoded position is covered once, in order, and receives the product of its two source values, while this merge rule guarantees that the returned encoding has no adjacent equal values.

## Complexity detail
Each input pointer advances monotonically and visits every run once, giving $O(M+N)$ time. The output contains at most $M+N-1$ runs, so including the returned data the space use is $O(M+N)$. Apart from that output, the pointer and remaining-frequency state is $O(1)$. These bounds are independent of the decoded array length.

## Alternatives and edge cases
- **Decode, multiply, and re-encode:** This is straightforward but costs time and memory proportional to the decoded length, which may be far larger than $M+N$.
- **Queue of expanded values:** Streaming expanded values avoids two full arrays but still performs one operation per decoded element.
- **Coincident boundaries:** When both remaining frequencies reach zero, both pointers must advance.
- **Unequal run boundaries:** Consume only the smaller remaining frequency; the other run continues into the next overlap.
- **Equal neighboring products:** Merge them even when the underlying input values changed.
- **One run against many:** The longer run remains active while the opposite pointer advances several times.
- **Large frequencies:** Never loop once per represented element.
