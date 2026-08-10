## General

**What makes one person unhappy**

Let person `x` be paired with `y`. Person `x` is unhappy if there is some person `u` whom `x` prefers over `y`, and `u` in turn prefers `x` over `u`’s assigned partner `v`.

The important quantifier is “there exists.” One witnessing person `u` is enough to mark `x` unhappy. The answer counts unhappy people, not unhappy relationships or witnessing pairs, so the implementation must stop searching once it finds the first witness for a particular `x`.

Two fast lookup structures make the condition efficient:

- `d[x][z]` gives the rank of person `z` in `x`’s preference list;
- `p[x]` gives `x`’s assigned partner.

With these structures, each preference comparison and partner lookup takes expected constant time.

**Converting preference order into rank**

Each `preferences[x]` list is already ordered from most preferred to least preferred. Comparing two people by repeatedly searching that list would cost linear time per comparison. The solution instead builds

`d = [{x: j for j, x in enumerate(p)} for p in preferences]`.

For every person’s preference list `p`, the dictionary comprehension maps each friend identifier `x` to position `j`. A smaller position means stronger preference. Thus:

`d[a][b] < d[a][c]`

means person `a` prefers `b` over `c`.

The comprehension’s reused local name `x` is only the key variable inside construction; it does not conflict with the later loop’s person `x`. Each preference list contains every other person exactly once, so every needed rank lookup exists and no key is overwritten by a duplicate.

**Building a partner lookup in both directions**

The input gives unordered pairs such as `[x, y]`. For each pair, the code assigns both `p[x] = y` and `p[y] = x`. After processing all pairs, `p` is a symmetric mapping: asking for either member returns the other.

The constraints guarantee every person appears in exactly one pair. Therefore, every person has exactly one partner entry, and later lookups such as `p[x]` and `p[u]` are defined.

**Search only people preferred over the assigned partner**

For each person `x`, the code first retrieves `y = p[x]`. The rank `d[x][y]` is the index of `x`’s assigned partner in `x`’s ordered list.

Everyone appearing before that index is preferred over `y`; everyone at or after it cannot satisfy the first unhappy condition. The loop

`for i in range(d[x][y])`

therefore visits exactly the useful prefix and no irrelevant suffix. For each position, `u = preferences[x][i]` selects a person that `x` definitely prefers over `y`.

The code then obtains `v = p[u]`, the assigned partner of candidate `u`. The second condition is checked as

`d[u][x] < d[u][v]`.

Because lower ranks mean stronger preferences, this inequality says `u` prefers `x` over `v`. Both conditions from the definition now hold: `x` prefers `u` over `y`, and `u` prefers `x` over `v`.

When this happens, `ans` is incremented and `break` ends the inner loop. Continuing might find more witnesses, but it must not increment `ans` again for the same unhappy person.

**A concrete trace**

Suppose person 1 is paired with person 0, and person 1’s preference list places person 3 before person 0. The loop for `x = 1` examines person 3 because person 3 lies in the prefix before assigned partner 0.

If person 3 is paired with person 2, the code compares `d[3][1]` with `d[3][2]`. When person 1 has the smaller rank, person 3 prefers person 1 over partner 2. Person 3 is a witness that person 1 is unhappy, so the answer increases once and the search for person 1 stops.

Notice that this does not automatically count person 3. The outer loop evaluates every person separately. Person 3 is counted only if, from person 3’s own perspective, there is a suitable witness—perhaps person 1—satisfying both preference conditions.

**Why every counted person is unhappy**

A person `x` is counted only inside the conditional. The candidate `u` came from an index below `d[x][y]`, so `x` ranks `u` ahead of partner `y`. The inequality in the conditional proves `u` ranks `x` ahead of partner `v`. Those are exactly the two requirements in the definition. Therefore, every increment corresponds to a genuinely unhappy friend.

**Why every unhappy person is counted**

Suppose `x` is unhappy. By definition, some witness `u` is preferred over partner `y`. Since the preference list is sorted, `u` must appear at an index smaller than `d[x][y]`. The inner loop examines every index in precisely that prefix, so it eventually reaches `u` unless an earlier valid witness has already caused a count.

For the defining witness, `u` prefers `x` over partner `v`, which the rank dictionaries express as `d[u][x] < d[u][v]`. The conditional succeeds, and `x` is counted. If an earlier witness succeeds, `x` has already been counted correctly. Thus no unhappy person is missed.

The `break` also proves uniqueness of counting. There is one outer iteration per person, and at most one increment during that iteration. The final answer is the number of unhappy friends rather than the number of witness pairs.

**Why the quadratic preprocessing is worthwhile**

There are $N$ preference lists, each containing $N-1$ people, so the input itself contains $\Theta(N^2)$ preference entries. Building inverse-rank dictionaries takes linear time in that input size.

Without them, each test “does `u` prefer `x` over `v`?” might scan `u`’s list or call a linear-time index search. Since up to $\Theta(N^2)$ candidates can be tested, that would raise the worst-case running time to $O(N^3)$. Rank maps reduce each test to two dictionary lookups and one integer comparison.

## Complexity detail

Let $N$ be the number of friends.

Constructing `d` processes all $N(N-1)$ preference entries, taking $O(N^2)$ expected time. Building the symmetric partner map processes $N/2$ pairs, taking $O(N)$ expected time.

For each person `x`, the inner loop examines only the people ranked before `x`’s partner. In the worst case, that prefix has $N-2$ people, and this can occur across $N$ outer iterations. Each candidate uses expected $O(1)$ dictionary lookups, so the search costs $O(N^2)$ expected time. The complete time complexity is $O(N^2)$.

The rank dictionaries collectively store $N(N-1)$ entries, giving $O(N^2)$ space. The partner map stores $N$ entries, and the remaining variables use $O(1)$ state. The total auxiliary space complexity is therefore $O(N^2)$.

The expected qualifier comes from Python dictionary operations. The number of stored ranks and candidate checks remains quadratic independent of hash-table implementation details.

## Alternatives and edge cases

- **Scan preference lists for every comparison:** This avoids the rank dictionaries but can cost $O(N^3)$ time because each candidate condition may require linear searches. The inverse ranks are the standard time-space tradeoff.
- **Check every possible `u`:** Testing all $N-1$ other people is correct if both conditions are evaluated, but people ranked below partner `y` can never satisfy the first condition. Stopping the candidate range at `d[x][y]` avoids needless work.
- **Count all witnessing pairs:** A person can have several witnesses, but the requested answer counts that person once. The checked-in `break` is essential.
- **Mark unhappy people in a set:** A set can deduplicate counts when examining relationships from another iteration order. The person-centered loop already counts at most once, so no set is needed.
- **Two friends:** Each person is paired with the only other person, so the prefix before the partner is empty for both. The answer is zero.
- **Partner ranked first:** `d[x][y] == 0` makes `range(0)` empty. Person `x` cannot prefer anyone over the partner and is necessarily happy.
- **Partner ranked last:** Every other eligible person is examined until a witness is found or the prefix is exhausted.
- **Several valid witnesses:** The first one increments `ans` and terminates the inner loop, preventing double counting.
- **Mutual unhappiness:** If `x` and `u` prefer each other over their partners, each is evaluated and counted in its own outer iteration. That correctly contributes two unhappy friends.
- **One-sided preference:** If `x` prefers `u` but `u` prefers partner `v` over `x`, the rank inequality fails. Attraction from only one side is insufficient.
- **Symmetric partner mapping:** Both directions must be inserted. Storing only `p[x] = y` from each input pair would leave lookups undefined when the later search starts from the other member.
- **Unique preference entries:** The dictionary rank representation relies on each friend appearing once in a preference list. The problem guarantees uniqueness and excludes the person themself.
- **Even `n` and complete pairing:** These guarantees ensure every person has one partner. Without them, `p[x]` could be missing and the unhappy definition would need additional handling.
- **Dictionary variable names:** The inner comprehension’s `x` is local to that comprehension in Python 3. The later `for x in range(n)` independently represents the person being evaluated.
