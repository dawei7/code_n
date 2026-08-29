## General

**Each second should reduce the two largest remaining needs**

At most two cups can be filled per second, and they must have different water types. The method repeatedly sorts the three remaining amounts. It always reduces the largest entry and, when positive, also reduces the second-largest entry.

Sorting makes `amount[2]` the largest and `amount[1]` the second largest. Filling one cup of the largest type is always necessary while work remains. Pairing it with the largest other positive type uses the second available dispenser slot without consuming the same type twice.

If only one type remains positive, `amount[1]` is zero. The assignment `max(0, amount[1] - 1)` leaves it at zero, so that second fills only one cup.

**Why pairing the two largest is safe**

Suppose a schedule fills the largest type together with a smaller positive type while a larger alternative type is also waiting. Exchanging the smaller partner for the larger partner cannot increase the number of remaining dominant cups and makes the remaining demands no more imbalanced.

The difficult case is always a type that could be left with many cups after the other two run out. Reducing the largest two prevents avoidable imbalance. Repeating the exchange argument transforms an optimal schedule so its first second matches the greedy choice, then applies the same reasoning to the remaining amounts.

**Two lower bounds explain the optimum**

Let `S` be the total number of cups and `M` the largest type count.

Since one second fills at most two cups, at least `ceil(S/2)` seconds are necessary.

Since a second can fill at most one cup of any particular type, the dominant type alone requires at least `M` seconds.

Thus every schedule needs at least

`max(M, ceil(S/2))`

seconds.

The greedy simulation attains this bound. If `M` exceeds the total of the other two types, pair the dominant type with another type until those are exhausted, then finish the remaining dominant cups alone; total time is `M`. Otherwise, no type dominates the combined remainder, so two positive different types can keep being paired until at most one cup remains; total time is `ceil(S/2)`.

Selecting the two largest types maintains exactly the conditions needed for this construction.

**Follow the exact loop state**

`ans` starts at zero. While `sum(amount)` is nonzero, at least one cup remains. Sorting identifies current priority, `ans` increases by one for the elapsed second, and the method fills one cup from `amount[2]` plus a possible cup from `amount[1]`.

Every iteration reduces total remaining demand by one or two and never makes an amount negative. Therefore the loop terminates with all three entries zero. `ans` is the number of simulated seconds.

For `[1,4,2]`, sorted choices repeatedly pair warm with another available type until the other types are gone, then use one final warm-only second. The loop returns four, matching both lower bounds because the dominant count is four.

For `[5,4,4]`, no type dominates the other two combined. Six seconds fill twelve cups in pairs and one second fills the remaining cup, returning `ceil(13/2) = 7`.

**The exact source simulates rather than using the formula**

The manifest summary describes directly taking the maximum of the two lower bounds. The provided source reaches that same value through greedy second-by-second sorting. With only three types and counts capped at 100, the simulation is bounded and simple, but its literal work depends on the number of cups.

The method sorts and decrements the caller-provided `amount` list. At return, it has been reordered repeatedly and all entries are zero, so input mutation is observable.

## Complexity detail

Let `S = sum(amount)` initially. Each iteration fills at least one cup, so there are at most `S` iterations. Sorting exactly three elements is constant time, as are the sum and updates. Parameterized running time is `O(S)`.

Under the source bound of at most 100 cups in each of three types, `S <= 300`, so the runtime is also bounded by a fixed constant and is reported as `O(1)` in the manifest. A direct formula would be unconditionally constant in the numeric amounts under unit-cost arithmetic.

Only `ans` and the fixed three-element input list are used. Sorting may use constant-size temporary storage because the list length is always three, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Closed-form bound:** Return `max(max(amount), (sum(amount) + 1) // 2)`. This is the simplest true `O(1)` implementation and follows directly from the two lower bounds.
- **Max heap:** Repeatedly pop the two largest positive counts, decrement, and reinsert. This generalizes to more types but adds unnecessary machinery for exactly three.
- **Pair arbitrary positive types:** It can waste pairing capacity and leave a dominant type to be filled alone longer. Choosing the two largest prevents that imbalance.
- **Fill one cup even when two types remain:** This can never improve the schedule because filling a second different cup in the same second is free.
- **All zeros:** The loop is skipped and the answer is zero.
- **Only one positive type:** Every iteration fills one cup of it, so time equals that amount.
- **Two positive types with equal counts:** Every second pairs them, and time equals either count.
- **One dominant type:** The answer equals its count because at most one cup of that type can be filled each second.
- **Balanced totals:** The answer is total cups rounded up by two.
- **Odd total:** At least one second fills only one cup, accounted for by the ceiling.
- **Second-largest zero:** The `max(0, ...)` guard prevents a negative count.
- **Repeated sorting:** It restores the meaning of indices one and two after decrements; fixed water-type identities are irrelevant to the count.
- **Input mutation:** The source consumes and reorders `amount` until it becomes three zeros.
- **Fixed constraints:** Calling the simulation `O(1)` relies on the numeric cap. In terms of total cups `S`, its literal complexity is linear.
