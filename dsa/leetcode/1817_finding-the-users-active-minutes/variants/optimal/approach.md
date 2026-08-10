## General

**Deduplicate minutes separately for every user**

The same user may perform several actions during one minute, but that minute contributes only once to the user's active-minute count. Different users acting at the same minute must remain separate.

The appropriate representation is therefore a mapping:

`user ID -> set of action minutes`.

The protected solution creates `d = defaultdict(set)`. For every log `[i, t]`, it executes `d[i].add(t)`.

If the user has not appeared before, the default factory creates an empty set. If the exact minute is already present, adding it again changes nothing. This enforces uniqueness locally per user.

**Convert each user's set size into one histogram bucket**

After processing all logs, `len(ts)` is that user's UAM.

The requested answer is described with one-based UAM values but returned as a normal zero-based Python list. Therefore:

- UAM 1 belongs at index 0;
- UAM 2 belongs at index 1;
- in general, UAM $j$ belongs at index $j-1$.

The solution creates `ans = [0] * k` and, for each user's set `ts`, increments

`ans[len(ts) - 1]`.

The constraint guarantees `k` is at least the maximum UAM, so this index is always within the list.

**Following the first example**

Logs for user 0 contain minutes 5, 2, and 5. Their set becomes `{2,5}`, so UAM is two.

User 1 has minutes 2 and 3, also giving UAM two.

Both users increment index one. The result `[0,2,0,0,0]` means zero users have UAM one, two users have UAM two, and none have larger UAM values.

**Following the second example**

User 1's set is `{1}` and increments answer index zero. User 2's set is `{2,3}` and increments index one. The result is `[1,1,0,0]`.

**Why users with zero active minutes do not appear**

The input defines users through action logs. Every key placed in `d` came from at least one log, so every stored set has size at least one.

The answer begins with UAM one and has no bucket for zero, which is consistent with this data model.

**Why a global set would be wrong**

A global set of minutes would merge activity belonging to different users. The same minute may count once for each user who acted then. Nesting a separate set under each ID preserves this distinction.

Similarly, a set of raw `(user, minute)` pairs could deduplicate correctly, but the mapping of sets makes the later per-user cardinality direct.

**Why the result is correct**

For each user, set semantics retain exactly the distinct minutes present in that user's logs. Its size is therefore the UAM by definition.

The histogram loop visits each represented user once and increments exactly the bucket corresponding to that UAM. Hence every user contributes once to the right answer entry, and no duplicate action changes the result.

Notice that dictionary iteration order is irrelevant. Users can be visited in any order because every update is an addition to an independent histogram bucket. The returned array is ordered by UAM value through its indices, not by user ID or by the order in which logs appeared.

## Complexity detail

Let $n$ be the number of logs and $U$ the number of users. Each expected hash-map lookup and set insertion is $O(1)$, so building `d` takes expected $O(n)$ time.

Creating the answer takes $O(k)$ time, and visiting all $U\leq n$ user sets takes $O(U)$. Total expected time is $O(n+k)$, matching the manifest.

Across all sets, at most $n$ distinct user-minute pairs are stored. The mapping uses $O(U)$ metadata and the answer uses $O(k)$ entries, for $O(n+k)$ auxiliary/output space.

Hashing assumptions make these expected rather than adversarial worst-case bounds.

## Alternatives and edge cases

- **Sort logs by user and minute:** Deduplicate adjacent pairs and count runs in $O(n\log n)$ time without nested sets.
- **Global set of pairs:** `(user, minute)` pairs deduplicate correctly, but another grouping pass is still needed.
- **Count every log:** It overcounts users who perform several actions in one minute.
- **Global minute set:** It incorrectly merges different users' activity.
- **Duplicate identical log:** Set insertion leaves UAM unchanged.
- **Same user, different minutes:** Every distinct minute increases that user's set size.
- **Different users, same minute:** Each user's separate set counts the minute independently.
- **One log:** One user has UAM one and increments the first entry.
- **All logs for one user and minute:** The first answer bucket is one regardless of duplicate count.
- **Maximum UAM equals `k`:** Index `k - 1` is valid and receives the user.
- **Large sparse user IDs:** A dictionary avoids allocating an array up to the largest ID.
- **No zero-UAM bucket:** Only users present in logs are considered.
- **Output indexing:** Human UAM value $j$ maps to Python index $j-1$.
- **Input preservation:** Sets summarize logs without modifying the input rows.
