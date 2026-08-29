## General

**Store both directions of the question**

The data structure must support two different kinds of information:

- `add(number)` and `deleteOne(number)` need the current occurrence count of one particular number.
- `hasFrequency(frequency)` needs to know whether any number has one particular occurrence count.

A map from numbers to counts answers the first question directly, but it does not answer the second one quickly. If only that map existed, every `hasFrequency` call would have to scan all numbers and compare their counts with the requested frequency.

The solution therefore keeps two maps:

- `cnt[number]` is how many copies of `number` are currently present.
- `freq[f]` is how many distinct numbers currently occur exactly `f` times, for positive `f`.

The second map is a set of frequency buckets. It turns the existential question “does at least one number occur this many times?” into the constant-time test `freq[frequency] > 0`.

**Think of every update as moving one number between buckets**

Suppose `number` currently occurs `old` times. Adding one copy changes its count to `old + 1`. The number must leave its old frequency bucket and enter its new one:

1. decrement `freq[old]`;
2. increment `cnt[number]`;
3. increment `freq[old + 1]`.

The code expresses the new bucket as `freq[cnt[number]]` after incrementing `cnt[number]`. Only this one number changes frequency, so no other bucket needs adjustment.

Deleting one copy is the reverse movement. If the old count is positive:

1. decrement the bucket for the old count;
2. decrement the number's count;
3. increment the bucket for the new count.

This transition bookkeeping is the central idea. Updating both views at the same moment prevents them from disagreeing.

**Why deletion first checks the count**

`deleteOne(number)` must do nothing when the structure contains no copy of `number`. The condition `if self.cnt[number]` tests whether its count is nonzero.

Without this guard, a missing number would move from frequency zero to frequency negative one. Negative occurrence counts have no meaning and would corrupt all later operations on that number.

Because `cnt` is a `defaultdict(int)`, reading a previously unseen key yields zero. The read can create an entry with value zero, but that bookkeeping detail has no observable effect: the number still has no positive count, no positive frequency bucket changes, and every permitted query remains correct.

**The useful invariant concerns positive frequencies**

After every completed operation, for every positive integer $f$:

$$
\texttt{freq[f]}
=
\#\{x : \texttt{cnt[x]}=f\}.
$$

The qualification “positive” matters for the exact implementation. It adjusts `freq[0]` while adding a previously absent value and while deleting the last copy of a value. There are infinitely many integers absent from the structure, so a genuine count of all zero-frequency values would not be useful or even finite. In addition, adding a never-seen number can make the stored `freq[0]` value negative because that absent number was never registered in a zero bucket.

That does not harm the algorithm. The contract queries only positive frequencies, and every positive bucket is maintained exactly. `freq[0]` is merely an unused side effect of applying the same transition formula at the boundary.

**Trace several additions**

Begin with both maps effectively returning zero.

After `add(5)`:

- `cnt[5]` moves from zero to one;
- `freq[1]` becomes one;
- exactly one tracked number, namely 5, has frequency one.

After another `add(5)`:

- 5 leaves bucket one, so `freq[1]` becomes zero;
- `cnt[5]` becomes two;
- 5 enters bucket two, so `freq[2]` becomes one.

After `add(8)`:

- `cnt[8]` becomes one;
- `freq[1]` becomes one;
- `freq[2]` remains one.

Now `hasFrequency(1)` and `hasFrequency(2)` are both true. The first is witnessed by 8 and the second by 5.

**Trace deletion and the last-copy boundary**

Continue from counts `5 -> 2` and `8 -> 1`. Calling `deleteOne(5)` moves 5 from bucket two to bucket one:

- `freq[2]` falls from one to zero;
- `cnt[5]` falls to one;
- `freq[1]` rises from one to two.

Both tracked values now occur once. Deleting 8 moves it from bucket one to the unused zero bucket. The meaningful result is that `freq[1]` falls from two to one and `cnt[8]` becomes zero.

Deleting 8 again changes nothing because the guard sees zero. The remaining copy of 5 still makes `hasFrequency(1)` true.

**Why the query is sufficient**

For a positive requested frequency $f$, the invariant says `freq[f]` equals the number of values that occur exactly $f$ times.

If `freq[f] > 0`, that count proves at least one such value exists. If it equals zero, no such value exists. Thus the comparison returns true exactly when the contract's existential condition holds.

Negative bucket values are possible only for the unused zero bucket, not for positive buckets maintained by valid transitions.

**Why this is the optimal organization**

Every operation changes or asks about only a constant amount of abstract state. With hash maps, each relevant count or bucket is reached directly by key.

The extra reverse summary in `freq` avoids scanning all distinct values during a query. This is a general technique: when updates are local and queries ask about an aggregate category, maintain the category counts incrementally rather than recomputing them.

## Complexity detail

Let $d$ be the number of distinct values that have been referenced and let $m$ be the number of operations.

Each `add` performs a constant number of expected $O(1)$ hash-map reads and writes. Each successful `deleteOne` does the same, while an unsuccessful deletion performs only the count lookup. `hasFrequency` performs one bucket lookup and one comparison. Therefore every operation takes expected $O(1)$ time.

The `cnt` map can contain at most $O(m)$ referenced numbers, including zero-count entries created by missing deletions. The `freq` map can contain at most $O(m)$ different frequency keys. Total auxiliary space is $O(m)$, commonly stated as $O(n)$ for the number of operations stored by the tracker.

## Alternatives and edge cases

- **Scan the number-count map for every query:** This uses only `cnt` but makes `hasFrequency` take $O(d)$ time.
- **Maintain sets of numbers per frequency:** Moving values between sets also supports expected $O(1)$ operations, but stores more information than the query needs.
- **Use a fixed count array:** This works only when the numeric value domain is small and known; hash maps handle the full allowed range naturally.
- **Add a new number:** It enters positive frequency bucket one even though the unused zero bucket is not a meaningful census.
- **Delete the last copy:** The value leaves bucket one and becomes absent; positive bucket accounting remains correct.
- **Delete a missing number:** The guard makes the operation a no-op.
- **Several numbers in one bucket:** `freq[f]` counts all of them, so removing one does not make the query false while another remains.
- **Move the only number out of a bucket:** The bucket count becomes zero and `hasFrequency` correctly becomes false.
- **Query frequency zero:** The problem restricts queries to positive frequencies; the exact implementation does not maintain a semantic zero-frequency bucket.
- **Repeated add and delete cycles:** Each transition reverses the corresponding prior transition, keeping both maps synchronized.
- **Hash-map complexity:** Constant time is expected rather than deterministic worst-case because it relies on ordinary hash-table behavior.
