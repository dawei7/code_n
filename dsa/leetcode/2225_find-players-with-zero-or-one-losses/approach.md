## General

**Store one loss count for every participant**

Each match supplies two facts: both IDs participated, and only the loser gains one loss. A map from player ID to total losses captures everything needed for the final classification.

The solution uses `Counter` as that map. A missing key behaves as though its count were zero, but a player who only wins still must be inserted explicitly so the method knows that player participated. For each pair `winner, loser`:

- if `winner` is not yet a key, `cnt[winner] = 0` records participation with zero losses;
- `cnt[loser] += 1` records the loss, automatically creating the loser with count one when previously unseen.

If a winner already has a map entry, the code leaves its value unchanged. Winning does not erase earlier losses. If the loser was already recorded through wins or losses, incrementing correctly advances the total.

**Why a single map covers all player histories**

A player can first appear as a winner, first appear as a loser, or have appeared earlier in either role.

If first seen as a winner, the explicit membership check creates count zero. If first seen as a loser, `Counter` supplies default zero and incrementing creates count one. Later wins preserve the current count because the membership test fails; later losses each add one.

After every processed match, `cnt[x]` therefore equals the number of processed matches lost by player `x` for every participant seen so far. This is an invariant of the scan. It is true after the first match, and each new match changes exactly its loser's count while ensuring its winner exists.

Players absent from all matches never become keys. That precisely enforces the instruction to consider only players who played at least one match.

**Produce both lists in increasing order**

After counting, the solution initializes `ans = [[], []]`. It iterates through `sorted(cnt.items())`. Sorting map items without a custom key orders tuples by their first component, the player ID, because all IDs are distinct keys. Thus, qualifying players are encountered in increasing numeric order.

For each player `x` with loss count `v`, only counts below two matter. The condition `if v < 2` admits exactly `v = 0` and `v = 1` because loss counts cannot be negative.

The elegant statement `ans[v].append(x)` uses the count itself as the destination:

- count zero appends to `ans[0]`;
- count one appends to `ans[1]`.

Players with two or more losses are ignored. Since the traversal is sorted, both inner lists are already increasing and need no separate sort.

**Why every returned player belongs**

Any ID appended to `ans[0]` has map value zero. The invariant says that value is its exact number of losses, and existence in the map says it participated. It therefore satisfies the first output rule.

Any ID appended to `ans[1]` has exact count one, so it satisfies the second rule. Counts of two or more fail `v < 2` and cannot enter either list.

**Why no qualifying player is omitted**

Every participant appears as a winner or loser in at least one pair. Winner handling inserts unseen winners, while loser incrementing inserts unseen losers. Therefore, every participant is present in `cnt`.

If such a player's final loss total is zero or one, the sorted traversal visits its entry and the `v < 2` branch appends it to exactly the matching list. Hence, all and only requested players appear.

**Trace role changes**

Suppose player `4` first wins. It is inserted with zero. If it later loses, incrementing changes the value to one. Another later win does nothing to that value, correctly leaving one recorded loss. If it loses again, the value becomes two and the final filter excludes it.

A player who loses in its very first appearance is inserted directly with one, without needing a separate “seen” set. This is one benefit of `Counter`'s zero default.

The guarantee that match outcomes are unique does not materially change the counting logic. Even if two players meet in different directions, each listed loser occurrence is still one distinct loss.

## Complexity detail

Let `m` be the number of matches and `p` the number of distinct participating players. The first loop performs expected constant-time hash operations for two IDs per match, taking expected `O(m)` time.

Sorting `p` map entries by player ID takes `O(p \log p)` time. The final traversal and appends take `O(p)`. Total time is `O(m + p \log p)`, matching the Optimal manifest.

The counter stores one entry per participant, requiring `O(p)` space. The sorted item list also contains `p` entries, and the output can contain up to `p` IDs. Peak additional storage remains `O(p)`.

Hash operations are expected constant time under the standard model. Python integers safely store loss counts and player IDs within the constraints.

## Alternatives and edge cases

- **Three status sets:** Maintain separate sets for zero, one, and multiple losses and move losers between them. This works but requires more transition cases than storing the numeric count directly.
- **A seen set plus a loser counter:** Record every participant in one set and only losses in a map. It is correct, but the exact solution folds participation and loss count into one structure.
- **Fixed counting array:** Player IDs are bounded by `100000`, so an array initialized with a sentinel can count losses and be scanned in numeric order in `O(m + U)` time, where `U` is the ID range. It avoids sorting but allocates space for IDs that never appear.
- **Sort only after filtering:** Collect the zero-loss and one-loss IDs from an unsorted map and sort both lists. This has the same asymptotic bound; sorting all items once makes the exact output ordering straightforward.
- **Player only wins:** It is explicitly inserted with count zero and appears in the first list.
- **Player loses on first appearance:** `Counter`'s default zero becomes one, so the player appears in the second list unless another loss occurs.
- **Wins after losses:** Winner handling must not reset an existing count to zero. The membership guard preserves prior losses.
- **Exactly two losses:** The count fails `v < 2` and is excluded from both lists.
- **No one-loss players:** `ans[1]` remains an empty list, which is a valid required result.
- **No zero-loss players:** The first inner list can likewise be empty.
- **Participant-only rule:** IDs never appearing in `matches` are absent from the counter and never returned, even though they could be described informally as having zero losses.
- **Increasing order:** Iterating an ordinary map is not a numeric-order guarantee. `sorted(cnt.items())` is the step that establishes the required ordering.
- **Output positions:** Count zero maps to index zero and count one to index one; swapping the lists would violate the contract even if their contents were correct.
