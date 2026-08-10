## General

**Why this is a search over remaining needs**

At any moment, the only information that matters for future purchases is how many units of each item are still needed. It does not matter which sequence of earlier offers produced those remaining amounts: from the same remaining-needs state, the same individual purchases and the same applicable special offers are available.

That observation gives the dynamic-programming state. If the current remaining quantities are `[r0, r1, ..., r(M-1)]`, define the answer for that state as the minimum additional cost required to reduce every quantity to zero without ever buying too many items. The original problem asks for the answer at the initial `needs` state.

A direct recursive search would try all legal offer sequences. Many different sequences can reach the same remaining state, so that search repeats substantial work. Memoization removes the repetition: the first call computes the optimum for a state, and every later call with the same state immediately reuses it.

**Packing all quantities into one integer**

The exact solution uses one integer `cur` as the memoization key instead of a tuple. Each need is at most ten, which fits in four binary bits because four bits can represent values from zero through fifteen. Item `i` occupies the four-bit field beginning at bit position `4 * i`.

To build the initial state, the solution shifts each quantity left by its field position and combines it into `mask`. To read item `i` later, it shifts the state right by `4 * i` and keeps the lowest four bits with `& 0xF`. To subtract `q` units of item `i`, it subtracts `q << (4 * i)` from the packed integer.

The fields do not interfere with one another because the algorithm subtracts an offer only after verifying that every requested field has at least the offered quantity. Thus no field becomes negative and borrows across its four-bit boundary. Four bits are safe specifically because every reachable remaining quantity is between zero and its initial need, and every initial need is at most ten.

For example, with two remaining quantities `[3, 5]`, the packed state stores three in the low four bits and five in the next four bits. An applicable offer `[1, 2]` subtracts one from the first field and two from the second, producing the representation of `[2, 3]`. Packing changes only representation; it does not change what a state means.

**Why buying every remaining item separately is the baseline**

Inside `dfs(cur)`, the first candidate cost is the price of purchasing all remaining units individually. For each item, the solution extracts its remaining quantity, multiplies that quantity by the item's unit price, and adds the products.

This baseline is crucial for two reasons. First, individual buying is always legal, so every state immediately has a complete feasible answer. Second, using no special offer at all may be optimal, especially when an offer contains an unwanted combination or costs more than its units bought separately. The recursion therefore never needs a special “no applicable offer” failure case.

**Trying one special offer as the next decision**

For every special offer, the solution checks each item quantity. If the offer asks for more units of any item than `cur` still needs, using it would overbuy, so the inner loop stops and that offer is ignored. This directly enforces the contract's rule that extra items cannot be purchased.

If every item passes the check, `nxt` is the state after subtracting the offer's quantities. Python's `for ... else` construction expresses this distinction precisely: the `else` block runs only if the item loop did not execute `break`. Therefore, recursive evaluation happens only for a fully applicable offer.

For such an offer, the complete candidate cost is:

- the offer's listed price, plus
- the minimum cost `dfs(nxt)` for satisfying what remains afterward.

The current answer becomes the smaller of its previous value and this candidate. Trying every offer covers every possible special offer that could be chosen first from this state.

**Why no separate “used offer” dimension is needed**

An offer may be used any number of times, but that does not require recording a use count. After one use, the recursive call sees smaller remaining quantities. If the same offer is still applicable, that recursive state can choose it again. If it is no longer applicable, the overbuy check rejects it. The remaining quantities already contain all information needed to determine how many additional uses are possible.

The source guarantee that every offer contains at least one positive item quantity is important. Every applicable offer strictly reduces at least one remaining need. Consequently, recursive calls always move toward the all-zero state and can never call themselves with exactly the same state. The recursion therefore terminates.

**Why the recurrence finds the minimum**

Consider an arbitrary remaining state. Any legal completion has one of two forms. It either uses no more special offers, in which case buying everything individually gives exactly the baseline cost, or it chooses some legal special offer next and then legally satisfies the smaller remaining state.

The algorithm includes the first form through the baseline. For the second form, it examines every special offer, rejects exactly those that would overbuy, and for every legal one combines its price with the recursively optimal cost of the resulting state.

Assume recursively that smaller states return their true minimum costs. Then the candidate for each possible first offer is the cheapest completion beginning with that offer. Taking the minimum across the individual-only option and every legal first offer therefore gives the cheapest completion of the current state. Because every recursive transition strictly reduces the total remaining quantity, this reasoning reaches the zero state and applies upward to the initial state. Memoization changes only how often a state is evaluated, not which candidates are considered, so it preserves correctness.

At the all-zero state, the individual-purchase baseline is zero. No positive-quantity offer is applicable, so the function returns zero naturally without a separately coded base case.

## Complexity detail

Let `M` be the number of item types, `S` the number of special offers, and
`P = product(needs[i] + 1)` over all item indices. Each quantity can independently range from zero through its initial need, so `P` is an upper bound on the number of distinct reachable memoized states.

For one new state, computing the individual-purchase baseline examines all `M` items. Checking one offer also examines at most `M` item quantities, and there are `S` offers. The work per state is therefore `O(SM)`, with the smaller baseline term absorbed. Across at most `P` states, the time bound is `O(SM * P)`.

The cache stores one numeric answer for each visited packed state, so the cache itself uses `O(P)` entries. The recursion depth is at most the sum of the initial needs because every selected offer removes at least one unit. Each active call holds loop and candidate data; in the exact Python implementation, this contributes stack space proportional to the recursion depth. A conservative state-representation analysis may describe storage as `O(M * P)` when accounting for an unpacked logical vector per state, matching the manifest's stated bound. The packed implementation is tighter in practice because each cache key is one integer, giving `O(P)` cache storage plus the recursion stack.

The four-bit encoding gives constant-time field extraction under the usual fixed-size model because `M` is at most six and the packed integer is small. The algorithm's exponential-looking factor is the finite state-space product, not the number of offer orderings; memoization is what collapses all orderings that reach the same state.

## Alternatives and edge cases

- **Memoization with a tuple key:** Using `tuple(remaining)` is often easier to read and avoids bit manipulation. It has the same dynamic-programming recurrence and asymptotic state count, but constructing and hashing an `M`-element tuple costs and stores more than the compact scalar key. It is still an excellent clarity-first alternative.

- **Bottom-up multidimensional dynamic programming:** States can be filled from smaller needs toward the target. This avoids recursion, but iterating a variable-dimensional grid and applying every offer is more cumbersome. It may also visit every theoretical state even when many are unreachable.

- **Enumerating offer sequences without memoization:** This repeats the same remaining state through different orderings and can grow explosively. Remembering the optimum for each state is the essential optimization.

- **Greedily choosing the offer with the largest apparent discount:** A locally attractive bundle can consume quantities that prevent a better combination of later offers. Because offers overlap across item types, no simple per-offer discount ordering guarantees the global minimum.

- **Filtering dominated or non-saving offers:** An offer costing at least the individual price of its contents can be removed as a preprocessing optimization, and some dominated offers can also be removed. The exact solution does not need this for correctness; its individual baseline ensures such an offer can never improve the answer.

- **Offer quantity greater than a remaining need:** The item check breaks immediately, the `for ... else` body does not run, and no subtraction occurs. This prevents both overbuying and invalid cross-field borrowing in the packed representation.

- **Offer entries as large as fifty:** Although fifty does not fit in four bits, only remaining needs are stored in four-bit fields. An offer quantity above a remaining field is rejected before it is subtracted, so it never needs to be encoded inside that field.

- **Repeated use of one offer:** Each legal use produces a smaller state. The recursive call can select the same offer again, so unlimited reuse is supported without an explicit loop over use counts.

- **Offer containing zero of some items:** Zero simply leaves those fields unchanged. The source guarantee that at least one item quantity is positive ensures the complete offer still makes progress.

- **No useful special offer:** The function retains the individual-purchase baseline and returns the same cost as buying all needed units separately.

- **Zero needs for some item:** Its field begins at zero. Any offer containing a positive amount of that item is rejected, which correctly enforces the no-overbuy rule.

- **All needs are zero:** The packed mask is zero, the baseline is zero, no positive offer can apply, and the result is zero.

- **Negative or overflowing packed fields:** These cannot occur after the applicability test. Keeping that test before subtraction is a correctness requirement, not merely an optimization.
