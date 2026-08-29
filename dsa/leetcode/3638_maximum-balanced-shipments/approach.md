## General

A shipment ending at current parcel is balanced exactly when some earlier parcel in that shipment is strictly heavier than the last parcel.

The source scans left to right, maintains the maximum weight since the previous shipment closed, and closes a shipment at the earliest position where the current weight is below that maximum.

**State of the unfinished segment**

`mx` is the maximum weight among parcels seen since the last greedy closure. Because all weights are positive, resetting `mx=0` represents an empty unfinished segment safely.

For each new weight `x`:

`mx=max(mx,x)`.

If `x==mx`, the last parcel is equal to the segment maximum, so the current segment is not balanced.

If `x<mx`, some earlier parcel in the segment is heavier. The segment ending at x is balanced.

**Close immediately**

When a balanced endpoint appears, the source increments `ans` and resets `mx`. All parcels in that segment are assigned to one shipment, and the next parcel starts a fresh candidate segment.

Closing at the earliest possible endpoint leaves the longest possible suffix for additional non-overlapping shipments.

**Why no earlier balanced shipment was missed**

Suppose the current endpoint e is the first position after the last closure where `weight[e]<mx`.

If any balanced shipment ended earlier at j, it would contain an earlier parcel heavier than `weight[j]`. That heavier parcel is also inside the current unfinished scan region, so the running maximum at j would exceed `weight[j]` and the greedy method would have closed at j. This contradicts e being first.

Thus no valid shipment—regardless of where it starts inside the unfinished region—can finish before the greedy endpoint.

**Exchange argument for optimality**

Consider an optimal collection of shipments on the remaining suffix. If it contains no shipment, greedy is already no worse when it finds one.

Otherwise, let its first shipment end at f. By the previous argument, the greedy earliest endpoint e satisfies `e<=f`.

Replace that optimal first shipment with the greedy segment ending at e. It is balanced, and every later optimal shipment begins after f, hence also after e. The replacement creates no overlap and leaves at least as much suffix available.

Therefore, an optimal solution exists whose first shipment is the greedy one. Repeating this argument after every reset proves the total greedy count is maximum.

**Why including unused prefix parcels is harmless**

The problem permits parcels to remain unshipped, so an optimal shipment might start after the last greedy boundary. The greedy shipment instead includes the whole pending prefix.

Adding earlier parcels cannot lower a shipment's maximum. Since its last parcel is already below some earlier maximum, the enlarged segment remains balanced. Consuming this prefix does not block any shipment that could have ended earlier, because none exists by the earliest-end proof.

**Following the first example**

For `[2,5,1,4,3]`:

- 2 makes mx=2, no closure;
- 5 makes mx=5, no closure;
- 1 is below 5, so close `[2,5,1]` and reset;
- 4 makes mx=4;
- 3 is below 4, so close `[4,3]`.

The answer is 2.

**Equal weights**

For `[4,4]`, each 4 equals the running maximum. Strict inequality never holds, so answer remains zero.

A later equal maximum also cannot close a shipment. For example, `[2,5,5]` ends with 5 equal to maximum 5 and is not balanced.

**Single-parcel impossibility**

A one-element shipment's last weight equals its maximum, so it can never be balanced. The algorithm naturally waits for a later lower value.

**Why every greedy boundary is safe**

After processing a prefix:

- `ans` is the maximum number achieved by greedily closed shipments;
- `mx` is the exact maximum of the unassigned suffix since the last closure;
- no balanced shipment can end earlier within that suffix.

Updating mx preserves its meaning. A nonclosing element preserves the third statement. A closing element uses the exchange argument and begins an independent suffix. The final ans is optimal.

## Complexity detail

Each parcel is examined once, with constant-time comparison and assignment. Time complexity is `O(n)`.

Only `ans`, `mx`, and the loop variable are stored. Auxiliary space is `O(1)`.

The source does not construct shipment boundaries because only their maximum count is required.

## Alternatives and edge cases

- **Dynamic programming by endpoint:** It can model the same choices but is unnecessary because earliest closing has the exchange property.
- **Monotonic stack:** It can find earlier heavier elements, but one running maximum is enough after each reset.
- **Try every subarray:** It costs quadratic or worse time.
- **Strictly increasing weights:** No last parcel is below the segment maximum, so answer is zero.
- **Strictly decreasing weights:** Every pair can close a shipment, giving floor of n/2.
- **All weights equal:** Strict inequality never holds.
- **One large then many small values:** The first small value closes immediately; later small values need a new heavier predecessor.
- **Unshipped tail:** A suffix that never becomes balanced is simply left unused.
- **Unused prefix:** Greedy may include it in the first shipment without harming balance.
- **Positive weights:** They make zero a safe empty-state sentinel for mx.
- **Non-overlap:** Resetting after closure ensures future shipments start later.
- **Input preservation:** The source scans `weight` without modifying it.
- **Missing `List` import:** Standalone execution must provide the annotation name.
