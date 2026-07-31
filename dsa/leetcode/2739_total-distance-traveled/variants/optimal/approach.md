## General

Each reserve transfer adds one usable liter, but that transfer occurs only after five main-tank liters have been consumed. After a transfer, reaching the next trigger needs only four more liters that were present initially: the transferred liter supplies the fifth liter of that next block.

**Count the possible trigger events.** The first event requires $5$ initial liters, the second requires $9$, the third $13$, and in general the $k$th event requires $4k+1$ initial liters. Therefore at most `floor((mainTank - 1) / 4)` transfers can be triggered by the available main fuel. The reserve independently limits the number to `additionalTank`, so take the smaller value.

Every initial main-tank liter and every feasible transferred liter is eventually consumed. Add those quantities and multiply by the fixed mileage of $10$ kilometers per liter. The event formula counts every possible transfer and no impossible one, so this total is the maximum reachable distance.

## Complexity detail

The method performs a fixed number of arithmetic operations, so it takes $O(1)$ time and $O(1)$ auxiliary space. Both inputs are at most $100$, which also makes the legal workload a fixed bounded domain; the package records a bounded-domain complexity certificate rather than an artificial scaling benchmark.

## Alternatives and edge cases

- **Liter-by-liter simulation:** Repeatedly consuming fuel and transferring at milestones is straightforward and correct, but it performs work proportional to the liters consumed instead of using the closed form.
- **Five-liter block simulation:** Consuming whole blocks reduces iterations but still requires careful handling because each transferred liter contributes toward the next trigger.
- A main tank below $5$ liters never triggers a transfer, regardless of reserve size.
- Exactly $5$ initial liters trigger exactly one transfer when reserve fuel exists.
- Reserve fuel may run out before all potential main-fuel milestones are reached.
- A large reserve does not guarantee that all of it is usable; the main tank must supply enough fuel to reach each next event.
- Integer arithmetic avoids any precision issue when converting usable liters into distance.
