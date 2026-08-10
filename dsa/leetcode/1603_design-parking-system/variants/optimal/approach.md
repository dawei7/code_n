## General

**Store remaining capacity directly**

The system has exactly three independent car types. To decide whether a new car can park, the only needed information is how many spaces of that type remain.

The constructor stores:

`self.cnt = [0, big, medium, small]`.

Index zero is an unused dummy. Big, medium, and small capacities occupy indices one, two, and three, matching the platform’s `carType` codes exactly.

This one-based layout avoids subtracting one in every operation. The constant extra slot has no asymptotic impact.

**Why remaining slots are sufficient state**

An alternative representation could store both the original capacity and the number of cars already admitted, then test whether admitted count is below capacity. Their difference is the remaining capacity.

Keeping that difference directly compresses the state. Every successful admission subtracts one. No method removes cars, changes capacities, or asks how many have parked, so no other information is required.

The three types are independent. A free medium slot cannot accept a big car, and a failed small-car attempt must not affect big or medium counts. Direct indexing isolates each category.

**Processing `addCar`**

For a requested `carType`, the method first checks:

`if self.cnt[carType] == 0`.

Zero means every slot of that exact type is occupied. The method returns `False` immediately and leaves the count unchanged.

If the count is positive, one slot is available. The source decrements it:

`self.cnt[carType] -= 1`

and returns `True`.

The order is important. A failed request does not decrement capacity below zero. This keeps `cnt` a truthful remaining-slot count after any sequence of calls.

**The class invariant**

After construction and after every method call, `self.cnt[t]` equals:

$$
\text{initial capacity for type }t
-\text{number of successful admissions of type }t.
$$

It is always non-negative.

The constructor establishes the invariant because no cars have been admitted. On a failed call, the count is zero and remains unchanged, so the invariant holds. On a successful call, exactly one car of that type is admitted and the count decreases by one, preserving the equality. Other indices never change.

Therefore, the zero test is true exactly when no appropriate slot remains, and every return value is correct.

**Tracing repeated calls**

Suppose the system starts with capacities one big, one medium, and zero small. The list is `[0,1,1,0]`.

- `addCar(1)` sees one big slot, decrements it to zero, and returns true.
- `addCar(2)` sees one medium slot, decrements it, and returns true.
- `addCar(3)` sees zero small slots and returns false without mutation.
- another `addCar(1)` sees the big count remains zero and returns false.

This matches the sequence represented by the example’s output. The caller receives one Boolean per method invocation; the class does not assemble the output array itself.

**Why the constructor returns nothing**

This is a design problem. The online judge creates one `ParkingSystem` object, then invokes `addCar` repeatedly on that persistent instance. The constructor’s role is to initialize state, not produce a problem answer. Its represented output is null, while each method call produces a Boolean.

**Why no map or object per space is needed**

Car types are a fixed dense set of three codes. An array gives constant-time access with less machinery than a dictionary. Individual parking spaces have no identities and are never queried, so representing each slot separately would store irrelevant detail.

## Complexity detail

The constructor creates a list of four integers, a fixed size independent of input capacities, so its time and space are $O(1)$.

Each `addCar` call performs one indexed read, one comparison, and at most one decrement. Its time is $O(1)$. Across $Q$ calls, total operation time is $O(Q)$, matching the package manifest.

Persistent auxiliary space remains $O(1)$ because `self.cnt` always has four entries regardless of the number of calls or the numeric capacities. Failed and successful calls allocate no growing history.

## Alternatives and edge cases

- **Zero-based capacity array:** Store `[big, medium, small]` and access `carType - 1`. It is equally correct; the checked-in source uses a dummy zero slot for direct indexing.
- **Separate fields per type:** Three named counters work for this fixed problem but repeat branching logic. An indexed array makes the method uniform.
- **Dictionary keyed by type:** It provides constant expected access and could support sparse or dynamic types, but is unnecessary for three dense integer codes.
- **Store occupied and capacity counts:** The availability decision uses only their difference. Remaining capacity is sufficient and simpler.
- **Decrement before checking:** This risks negative counts or requires undoing failure. The source checks zero first and mutates only on success.
- **Initial capacity zero:** Every request of that type returns false, and the counter stays zero.
- **Capacity one:** The first matching request succeeds and every later one fails.
- **Interleaved car types:** Each call changes only its own index, so activity for one type cannot consume another type’s slots.
- **Repeated failed calls:** They return false without pushing the count negative.
- **Maximum initial capacities:** Numeric magnitude does not affect operation count or storage size.
- **Valid car codes:** Direct indexing assumes `carType` is one, two, or three, exactly as guaranteed. An invalid code would need validation but is outside the contract.
- **Dummy index zero:** It is never read by a valid call and costs only one constant list entry.
- **Persistent object state:** Capacities must live on `self` so successive judge calls observe earlier successful admissions.
- **No removal operation:** Because cars never leave through the interface, remaining capacity only decreases and no additional event handling is needed.
