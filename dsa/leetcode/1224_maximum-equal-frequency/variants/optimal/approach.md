## General

**Evaluate every prefix without recounting it**

For each prefix, the question is whether deleting exactly one occurrence can make all values that remain have the same positive frequency. Rebuilding a frequency table for every prefix would repeat almost all earlier work and could take quadratic time.

The solution processes `nums` once and maintains two related summaries:

- `cnt[v]` is the number of times value `v` appears in the current prefix.
- `ccnt[f]` is the number of distinct values whose current frequency is exactly `f`.

For example, if the prefix has counts `{2: 3, 5: 3, 8: 2}`, then `ccnt[3] == 2` and `ccnt[2] == 1`. This “frequency of frequencies” table makes it possible to recognize the few shapes that one deletion can repair.

The variable `mx` is the greatest value frequency in the current prefix. It never decreases as the prefix grows. The variable `ans` remembers the longest valid prefix length found so far. Because enumeration starts at one, `i` is the current prefix length rather than a zero-based index.

**Update both tables consistently**

When a new `v` arrives, it moves from its old frequency bucket to the next bucket. If `v in cnt`, the old frequency is positive, so `ccnt[cnt[v]] -= 1` removes one distinct value from that bucket. Then `cnt[v] += 1` raises its occurrence count, `mx` is updated, and `ccnt[cnt[v]] += 1` places it in the new bucket.

Zero-valued entries may remain in the `Counter`, but they do not hurt the arithmetic. A missing key also reads as zero.

**There are only three repairable frequency shapes**

Deleting one occurrence changes the frequency of exactly one value by one. If that frequency was one, the value disappears entirely and is no longer among the values that “have appeared” after deletion. All other values keep their frequencies. Therefore, before deletion, a valid prefix must have one of three shapes.

**Shape one: every frequency is one**

If `mx == 1`, every distinct value occurs once. Delete any one element. Its value disappears, while every remaining value still occurs once. A one-element prefix also qualifies because deleting its only element leaves no values, which the statement considers valid.

The code records `ans = i` immediately for this case.

**Shape two: one value is ahead by one**

Suppose the desired frequency after deletion is \(mx-1\). Exactly one value may currently occur \(mx\) times; deleting one of its copies lowers it to \(mx-1\). Every other value must already occur \(mx-1\) times.

The code verifies this with two conditions. First, `ccnt[mx] == 1` requires a unique maximum-frequency value. Second,

\[
\texttt{ccnt[mx]}\cdot mx+
\texttt{ccnt[mx-1]}\cdot(mx-1)=i
\]

requires every occurrence in the prefix to belong to either the \(mx\) bucket or the \(mx-1\) bucket. If some value had another positive frequency, the two counted buckets would cover fewer than the \(i\) total elements and equality would fail.

For counts `{a: 3, b: 2, c: 2}`, \(mx=3\), the unique maximum is `a`, and the weighted total is \(1\cdot3+2\cdot2=7\). Deleting one `a` leaves all three values with frequency two.

**Shape three: one singleton can disappear**

The other possibility is that one value occurs exactly once and all remaining values occur \(mx\) times. Delete the singleton; that value disappears, and every still-present value has frequency \(mx\).

The code requires `ccnt[1] == 1` and

\[
\texttt{ccnt[mx]}\cdot mx+1=i.
\]

Again, equality ensures there is no unaccounted third frequency. For counts `{a: 4, b: 4, c: 1}`, deleting `c` leaves equal frequency four.

**Why these cases are complete**

If the deleted occurrence belongs to a value with old frequency greater than one, that value remains and its new frequency is one smaller. Since every untouched value must equal it afterward, all untouched values had that smaller frequency before deletion. This is shape two.

If the deleted value had old frequency one, it disappears. All untouched values must already share one frequency, which is shape three. Shape one is the special situation in which all values are singletons and deleting any one works, including the prefix of length one.

There is no fourth possibility because one deletion cannot change two different value counts, cannot reduce a frequency by more than one, and cannot repair three distinct positive frequency levels.

**Why the longest answer is returned**

After updating the summaries, the code tests the current prefix. Whenever it matches one of the valid shapes, `ans = i` replaces the previous length. Prefixes are visited in increasing order, so the last recorded valid length is the maximum. An invalid later prefix does not erase `ans`.

For `[2,2,1,1,5,3,3]`, the counts are two each for 2, 1, and 3, plus one for 5. Shape three applies: \(3\cdot2+1=7\) and there is exactly one singleton. Deleting 5 leaves three values occurring twice.

## Complexity detail

Let \(n=\lvert\texttt{nums}\rvert\). Each element causes a constant expected number of hash-table operations and three constant-time shape checks, so expected time is \(O(n)\). As usual for Python hash tables, this is an expected bound; pathological collisions can degrade individual operations.

`cnt` stores at most one entry per distinct input value. `ccnt` stores frequency keys from one through at most \(n\), though only encountered frequencies matter. Both therefore use \(O(n)\) auxiliary space in the worst case. All scalar state is \(O(1)\).

## Alternatives and edge cases

- **Recount every prefix:** Building a new frequency map and testing it after each extension can take \(O(n^2)\). Maintaining `cnt` and `ccnt` shares the work.
- **Track a set of frequencies only:** A set reveals which frequencies exist but not how many values occupy each one. The conditions require knowing whether the maximum or singleton bucket contains exactly one value.
- **All values distinct:** `mx == 1` makes every prefix valid, because one singleton can be removed and all remaining counts stay one.
- **All values equal:** Every prefix is valid. Deleting one occurrence leaves the single remaining value with any positive frequency, or leaves no values for a length-one prefix.
- **Exactly one singleton:** It is removable only when every other value has the same frequency. The weighted-total equation rules out hidden frequency levels.
- **Unique value one above the rest:** This is repairable by deleting one copy of that unique maximum. Two maximum values would require two deletions, so `ccnt[mx] == 1` is necessary.
- **Stale zero buckets:** Decrementing `ccnt` can leave keys with value zero. Weighted arithmetic and equality checks remain correct because those buckets contribute nothing.
- **Exactly one deletion:** The cases do not merely test whether frequencies are already equal. For equal frequencies greater than one across multiple values, deleting one creates inequality and the prefix is not automatically valid.
- **Positive input values:** Hash-map logic would also work for zero or negative values, but the given domain is positive.
- **Returning a prefix length:** The algorithm need not remember which occurrence to delete. The matching shape identifies that a deletion exists, which is sufficient for the requested length.
