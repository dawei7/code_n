## General

Scan the available suffix while maintaining its maximum weight. The first position whose weight is strictly below that running maximum is the earliest possible endpoint of any balanced shipment in this suffix. Close a shipment there, increment the answer, and reset the running maximum for parcels after that endpoint.

Parcels before the maximum do not need special treatment: including them at the front of the same shipment preserves contiguity and cannot lower the shipment maximum. When the current value is not below the maximum, update the maximum and continue.

**Why the earliest closing shipment is safe.** No balanced shipment using the current suffix can end before the greedy endpoint, because every earlier final value equals the running maximum at its position. Any optimal solution's first shipment therefore ends at or after the greedy endpoint. Replacing that first shipment with the greedy one leaves a suffix at least as long for all later shipments and cannot reduce their possible count. Applying the same exchange argument after every reset proves the greedy total is optimal.

The closing parcel belongs to the shipment just completed, so it cannot seed the next running maximum. Since all weights are positive, zero safely represents an empty current shipment after a reset.

## Complexity detail

Let $n$ be the parcel count. The scan processes every parcel once for $O(n)$ time. It stores only the running maximum and shipment count, using $O(1)$ auxiliary space.

The benchmark uses $S=n$. The accepted greedy is $O(S)$, while a dynamic program that tries every possible contiguous shipment endpoint takes $O(S^2)$ time.

## Alternatives and edge cases

- **Interval dynamic programming:** Enumerating every balanced interval and combining it with the best suffix is correct but quadratic.
- **Monotonic stack:** A stack can locate a previous greater value, but the earliest-closing greedy needs only the current segment maximum.
- **Equal weights:** The last parcel must be strictly lighter; equality never closes a shipment.
- **Single-parcel interval:** Its last value equals its maximum, so it is never balanced.
- **Closing parcel reuse:** Non-overlap prohibits using it as the first parcel of the next shipment.
- **Unused parcels:** They may remain outside shipments, but including earlier unused parcels in the current segment cannot hurt balance.
- **Increasing suffix:** If no later value drops below its running maximum, it contributes no shipment.
- **Strictly decreasing array:** Consecutive pairs can form $\lfloor n/2\rfloor$ shipments.
