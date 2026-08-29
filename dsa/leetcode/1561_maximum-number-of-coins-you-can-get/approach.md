## General

**Understand what one chosen triple gives you**

Within any selected three piles, Alice takes the largest, you take the second largest, and Bob takes the smallest.

The globally largest remaining pile can never belong to you. If it appears in a chosen triple, Alice takes it. If it is postponed, Alice will still take it whenever it is eventually chosen.

To obtain the best possible pile for yourself in a round, pair the largest remaining pile with the second largest. Alice consumes the unavoidable largest pile, leaving the second largest for you.

Bob should receive the smallest remaining pile because his choice only consumes a resource and contributes nothing to your score.

Repeating this rule gives Alice the current largest, you the current second largest, and Bob the current smallest.

**Sort to expose the ownership pattern**

Let the input length be $3q$, so there are exactly $q$ rounds. After sorting in ascending order, Bob can be assigned the $q$ smallest piles.

The remaining $2q$ piles alternate by ownership:

- At the high end, the largest goes to Alice.
- The next largest goes to you.
- Then the next goes to Alice.
- The next goes to you, continuing inward.

Viewed in ascending order from index `q`, the pattern is you, Alice, you, Alice, and so on.

Therefore your piles are exactly sorted indices:

$$
q,\ q+2,\ q+4,\ldots,3q-2.
$$

**Decode the two slices**

The source sorts `piles` in place, then evaluates:

`piles[len(piles) // 3:][::2]`.

The first slice removes the smallest third, the piles assigned to Bob. The second slice takes every other value from the remaining ascending sequence, beginning with its first element.

Those selected elements are precisely your piles according to the ownership pattern. `sum(...)` returns their total.

For six piles, `q = 2`. Bob receives sorted indices zero and one. Your slice selects indices two and four, while Alice receives three and five.

**Tracing the first example**

Sorting `[2,4,1,2,7,8]` gives `[1,2,2,4,7,8]`.

The smallest third `[1,2]` is reserved for Bob. The remaining list is `[2,4,7,8]`. Taking every other element from its beginning gives two and seven, totaling nine.

These values correspond to choosing triples that give Alice eight and four while Bob receives the two small discarded piles.

**Why Bob can always take the smallest third**

For each round, pair one of Bob's small piles with two piles from the upper $2q$ region. Since every upper-region pile is at least as large, Bob's pile is the smallest in that triple.

Among the two upper piles, give the larger to Alice and the smaller to yourself. Thus the sorted ownership pattern describes a realizable grouping, not merely an arithmetic selection.

Equal pile sizes cause no difficulty. Even when values tie, the roles can be assigned to distinct pile occurrences, and the score remains the same.

**Why the greedy pattern is optimal**

Sort the remaining piles at any round. You cannot take its largest value. The greatest score available to you now is the second largest, achieved by placing it with the largest.

Choosing any smaller pile for yourself cannot create a later opportunity to take the current largest; Alice must eventually consume that pile. So taking the second largest now loses no superior future option.

Bob's pile should be as small as possible because saving a smaller pile while discarding a larger one to Bob cannot improve any future second-largest choice. An exchange can swap the smaller saved pile with Bob's larger pile, preserving Alice's and your current roles while leaving a no-worse remaining multiset.

Inductively, every round of the greedy allocation is compatible with an optimal complete grouping. The slice sums exactly those greedy rewards.

**Another global upper-bound view**

After Bob consumes some $q$ piles, $2q$ piles remain for Alice and you. When arranged in ascending pairs, you can receive at most the smaller member of each pair because Alice takes the larger.

Making Bob consume the $q$ smallest values leaves the largest possible pool for those pairs. Pairing adjacent values within that upper pool yields smaller members at indices `q, q+2, ...`, exactly the source's selection.

This realizes the upper bound and proves optimality.

**Input mutation and allocation**

`piles.sort()` changes the supplied list into ascending order. The exact Python source then creates a list for the suffix slice and another list for the step-two slice before summing.

An index-based loop could avoid those slice allocations while selecting the same values, but that is not what this stored implementation does.

## Complexity detail

Let $N$ be total pile count. Python sorting costs $O(N\log N)$ time. The two slices and `sum` together process $O(N)$ elements, so total time remains $O(N\log N)$.

The slice copies use $O(N)$ auxiliary space. Python's Timsort may also require $O(N)$ temporary space. Thus exact auxiliary space is $O(N)$, matching the manifest.

The result sum contains exactly $N/3$ selected piles.

## Alternatives and edge cases

- **Deque simulation:** Pop the largest for Alice, next largest for yourself, and smallest for Bob. It is intuitive but allocates a deque.
- **Index loop after sorting:** Sum indices from `N/3` to `N-1` in steps of two, avoiding slice copies.
- **Counting sort:** With the bounded pile values, frequencies can reduce sorting cost, but adds value-domain machinery.
- **Single round:** Sorting three piles and taking the middle value is exactly the rule.
- **All equal piles:** Every allocation gives the same score, and the slice selects the correct number of occurrences.
- **Duplicate values:** Ownership concerns pile occurrences, so ties do not invalidate the greedy argument.
- **Smallest third:** Assigning them to Bob protects larger piles for the two scoring roles.
- **Largest pile:** It can never be yours because Alice always takes a selected triple's maximum.
- **Second largest:** It is the largest remaining value you can secure in a round.
- **Length divisible by three:** It guarantees the ownership pattern ends cleanly after exactly $N/3$ selections.
- **Input mutation:** In-place sorting does not preserve the caller's original ordering.
- **Slice allocation:** The exact concise expression uses linear extra memory despite requiring no explicit queue.
