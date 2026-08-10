## General

**Simulate consumption one liter at a time**

The transfer rule triggers after every fifth liter consumed from the main tank, including liters that were previously transferred into it. The exact implementation models this directly.

`mainTank` is the amount currently available to burn. `additionalTank` is the reserve. `cur` counts total liters burned so far, and `ans` stores distance traveled.

The loop continues while `mainTank` is positive, because every available main-tank liter can propel the truck another ten kilometers.

**Process one liter**

On each iteration:

- increment `cur` by one;
- add ten to `ans`;
- subtract one from `mainTank`.

This represents consuming exactly one liter and traveling the fixed mileage. The order places the transfer check after consumption, matching “whenever five liters get used up.”

**Transfer only at consumption multiples of five**

After burning a liter, `cur % 5 == 0` precisely means total consumption has reached 5, 10, 15, and so on.

If the reserve is nonempty at such a moment, the code subtracts one from `additionalTank` and adds one to `mainTank`. That liter can be consumed by a future iteration.

If the reserve is empty, no transfer occurs. A later multiple of five cannot restore reserve fuel, so all remaining driving comes only from whatever is already in the main tank.

**Transferred liters can enable later transfers**

This is the subtle part. Suppose the initial main tank has nine liters and reserve fuel exists. After five liters, one reserve liter enters. The main tank now contains five usable liters in total: four original plus the transferred one. Burning all five reaches total consumption ten and can trigger another transfer.

Counting transfers simply as `mainTank // 5` from the initial amount would miss this feedback. The simulation automatically includes it because `cur` counts every consumed liter, regardless of origin.

**Trace mainTank five**

With five main liters and a nonempty reserve, the loop burns five liters, reaches `cur=5`, and travels 50 kilometers. The main tank is momentarily zero, but the trigger immediately transfers one reserve liter into it.

The loop therefore runs once more, burns that liter, and adds ten kilometers. `cur=6` is not a multiple of five, no transfer follows, and the main tank becomes zero. The result is 60.

**Why every loop iteration is useful**

The truck always gains ten kilometers from the liter consumed in an iteration. There is no decision that could make saving a liter preferable: mileage is fixed, transfers depend only on total consumption, and reserve fuel can enter only after consuming.

Thus burning until the main tank is empty maximizes distance.

**How many transfers are possible**

The first transfer requires five initial liters. Each later transfer effectively needs four more initial-or-already-available liters because the preceding transferred liter also contributes to the next group of five consumed liters.

The maximum number of transfers is:

$$
\min\left(\texttt{additionalTank},
\left\lfloor\frac{\texttt{initialMainTank}-1}{4}\right\rfloor\right).
$$

The exact code does not calculate this formula. It discovers the same count through the loop. Mentioning the formula helps explain termination and exposes the mismatch with the manifest summary, which describes a closed-form solution.

**Exact source versus manifest**

The manifest says the implementation counts transfers with a closed-form threshold formula in $O(1)$ time. The protected source instead consumes one liter per loop iteration.

Under the stated bounds of at most 100 liters in each tank, the number of iterations is absolutely bounded and may be treated as constant relative to an unbounded external input model. Algorithmically, however, the source's work grows with usable fuel.


Each iteration corresponds to one legally usable main-tank liter and adds exactly its ten-kilometer contribution. After every fifth total consumed liter, the code performs exactly one reserve transfer if available, matching the sudden transfer rule. It stops exactly when no main-tank fuel remains and no trigger has just replenished it. Therefore it consumes every and only usable liter, so `ans` is the maximum possible distance.

## Complexity detail

Let $M$ be the initial main-tank fuel, $A$ the reserve, and $T$ the number of successful transfers. The loop runs once for each consumed liter, exactly $M+T$ times. Its time is $O(M+T)$, with:

$$
T\le\min\left(A,\left\lfloor\frac{M-1}{4}\right\rfloor\right).
$$

It stores four integers and uses $O(1)$ auxiliary space.

Because legal `M` and `A` are at most 100, $M+T$ is bounded by a small constant for this problem. That permits a constraint-relative $O(1)$ label, but the precise generalized behavior is linear in usable fuel and is not the closed form claimed by the manifest.

## Alternatives and edge cases

- **Closed-form transfer count:** Compute the threshold formula and return ten times initial fuel plus transfers; this truly uses $O(1)$ operations.
- **Simulate five-liter chunks:** Can reduce iterations while preserving trigger semantics, but must handle the last partial chunk carefully.
- **Initial main tank below five:** No transfer trigger is reached, so distance is ten times `mainTank`.
- **Reserve empty:** The source constraints make it positive, but with zero reserve no transfer would occur.
- **Exactly five main liters:** One reserve liter is transferred if available, yielding six consumed liters total.
- **Transferred fuel reaches another multiple:** It is counted by `cur` and can trigger another transfer.
- **Large unused reserve:** Reserve fuel that never receives a trigger remains unusable.
- **Immediate trigger timing:** Transfer occurs after the fifth liter is consumed, even if the main tank just became empty.
- **No strategic choices:** Consuming every available liter is always optimal.
- **Manifest mismatch:** The exact code is a per-liter simulation, not a closed-form computation.
