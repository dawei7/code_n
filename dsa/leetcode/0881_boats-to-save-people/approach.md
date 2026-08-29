## General

Each boat carries at most two people, so the heaviest remaining person must take a boat on the current step. The only useful decision is whether that person can share with someone. Sorting makes the lightest and heaviest remaining weights available through two pointers.

After `people.sort()`:

- `i` points to the lightest person not yet assigned.
- `j` points to the heaviest person not yet assigned.

Each loop iteration assigns the person at `j` to one boat and increments `ans`. If the lightest and heaviest fit together, `people[i] + people[j] <= limit`, the lightest person shares that boat and `i` advances. Whether or not a partner fits, `j` decreases because the heaviest person has been rescued.

**Why try the lightest partner.** If the heaviest remaining person cannot share with the lightest remaining person, then they cannot share with anyone. Every other remaining person is at least as heavy as `people[i]`, so every other pair sum is even larger. The heaviest person must go alone.

If the heaviest can share with the lightest, pairing them is safe. The heaviest must consume a boat anyway. Placing the lightest in its otherwise available second seat rescues an additional person without increasing the boat count.

An exchange argument shows this does not damage an optimal arrangement. Suppose an optimal solution pairs the heaviest person with some other person `p` while the lightest person is assigned elsewhere. Since the lightest weighs no more than `p`, replacing `p` with the lightest keeps the heaviest pair within the limit. The displaced `p` can take the lightest person's former place if that place was alone, or the exchange can be viewed simply as preserving one two-person boat and leaving an equivalent remaining subproblem. Thus an optimum exists containing the greedy pair.

**Why the heaviest anchors every iteration.** Choosing boats around the heaviest person immediately resolves the most constrained passenger. A lighter person might have many possible partners, but the heaviest has the fewest. Once their boat is fixed, the same reasoning applies to the smaller sorted interval.

By induction on the number of remaining people, the algorithm uses the minimum number of boats. For one person, one boat is necessary. For a larger interval, if the heaviest cannot pair with the lightest, every solution needs a solo boat for the heaviest; the greedy choice is forced. If they can pair, an optimal solution can be transformed to use that pair, as argued above. Removing the assigned one or two people leaves a smaller instance solved optimally by the subsequent iterations.

**Loop boundary.** The loop uses `i <= j`. When `i < j`, at least two people remain. When `i == j`, exactly one person remains. The expression `people[i] + people[j]` then adds that person's weight twice, but this does not create an incorrect extra pairing: the code may increment `i` if twice the weight fits, yet it always decrements `j` and adds exactly one boat. The loop ends afterward. Conceptually, that final person rides alone.

A more explicit version could handle `i == j` separately, but the exact implementation's pointer movement still yields the correct count.

For `people = [3,2,2,1]` and `limit = 3`, sorting gives `[1,2,2,3]`. Person 3 cannot pair with 1, so they ride alone. The remaining heaviest 2 pairs with 1. The last 2 rides alone. The result is three boats.

Sorting mutates the input list, which is acceptable for this method's contract because only the boat count is returned. If caller-visible order must be preserved, sort a copy instead.

## Complexity detail

Let $n$ be the number of people. Sorting dominates the scan.

- **Time complexity:** $O(n\log n)$.
- **Space complexity:** The manifest states $O(n)$, accounting for sorting's implementation-level temporary storage. The two-pointer scan itself uses $O(1)$ extra state.

Python's in-place sort modifies `people` and may use up to linear temporary memory depending on detected runs. The loop runs at most $n$ iterations and performs constant work each time.

## Alternatives and edge cases

- **Try every pairing:** Searching all pair combinations or matchings is far more expensive and unnecessary because sorted extremes determine a safe greedy choice.
- **Pair the two heaviest:** This often exceeds the limit and can waste opportunities to place light passengers with heavy ones.
- **Fill boats starting from the lightest:** Pairing two light people may leave two heavy people needing separate boats, whereas each light person could potentially share with a heavy one.
- **Counting sort:** Weight and limit are bounded by $3\cdot10^4$, so frequency counts can avoid comparison sorting and approach $O(n+\texttt{limit})$ time, at the cost of an additional weight-frequency array.
- **One person:** Exactly one boat is counted, regardless of whether twice that weight would fit.
- **All people exceed half the limit:** No two can share, so the loop uses one boat per person.
- **Every extreme pair fits:** Each boat takes two people, except possibly one final unpaired person.
- **Pair sum exactly equals limit:** The `<=` comparison allows the pair, as required.
- **Every individual is feasible:** The constraint `people[i] <= limit` guarantees no person is impossible to rescue alone.
- **Duplicate weights:** Sorting and pointer movement treat each occurrence as a distinct person.
- **Input mutation:** `people.sort()` changes the caller's order. Use `sorted(people)` if preservation is required.
- **At most two people:** Even when three or more light people have a combined weight under the limit, a boat cannot carry more than two; the algorithm never assigns a third passenger.
