## General

The process asks the same membership question repeatedly: does the current value of `original` appear anywhere in `nums`? If yes, double it and ask again; if no, return it. A hash set makes each membership test direct.

**Build a reusable membership structure**

The exact solution creates `s = set(nums)`. A set stores each distinct input value once and supports expected $O(1)$ membership testing.

Duplicates do not affect the process. Finding one occurrence is enough to trigger a doubling, and the array is not consumed: even if a value appears once, it remains considered present for every lookup. Collapsing duplicates into a set therefore preserves exactly the needed information.

**Follow the forced doubling chain**

The loop condition is `while original in s`. When it is true, the next value is not a choice; the rules require doubling.

The source performs `original <<= 1`. A left bit shift by one multiplies a nonnegative integer by two:

$$
\textit{original}\ll1=2\cdot\textit{original}.
$$

All legal values are positive, so this bit operation has the same meaning as `original *= 2`.

The loop immediately tests the new value. For `nums = [5,3,6,1,12]` and `original = 3`, set membership drives the chain $3\to6\to12\to24$. Since 24 is absent, the loop ends and returns 24.

**Why the first missing value is the answer**

At every loop iteration, the current value occurs in the input, so the mandated operation is performed. The loop cannot legally stop at any earlier value.

When the condition becomes false, the current value does not occur. The problem says the process must stop in exactly that situation. Therefore the returned value is neither premature nor delayed; it is the unique final value of the deterministic process.

**Why the loop terminates**

`original` begins positive and doubles on every iteration, so it strictly increases. The set is finite and contains at most $n$ distinct values. A strictly increasing doubling chain cannot revisit a previous value, and it can encounter at most every distinct set element once. Eventually a doubled value is absent and the loop stops.

The final value may exceed the maximum original constraint of 1000. That is allowed: the bound applies to input values, not to the returned result.

**Why no array rescan is needed**

A literal implementation could test `original in nums` against the list each time. List membership is linear, so repeated doublings would rescan values already examined. The set pays one linear preprocessing pass and then answers each new question in expected constant time.

**Order has no role**

The search asks whether a value appears anywhere, not where it appears. The set deliberately discards both input order and multiplicity. This differs from the editorial’s sorting alternative, where ascending order is used to avoid moving backward through the list.

## Complexity detail

Let $n$ be the input length. Building `set(nums)` takes $O(n)$ expected time and $O(n)$ space in the worst case.

Let $d$ be the number of successful doublings. Each set lookup is expected $O(1)$, so the loop costs expected $O(d)$. Because the positive chain never repeats and each successful value must be a distinct member of `s`, $d \le |s| \le n$. Total expected time is $O(n)$.

The set dominates auxiliary storage at $O(n)$. The changing `original` and loop state use constant space. Python integers expand if doubling produces a larger value.

## Alternatives and edge cases

- **Sort then scan:** Sort ascending and double `original` whenever the current sorted value matches. Because `original` only increases, one pass after sorting suffices, for $O(n\log n)$ time and implementation-dependent sort space.
- **Repeated list membership:** This follows the statement directly but can take $O(nd)$ time, up to $O(n^2)$ under the distinct-chain bound.
- **Frequency map:** A counter also supports membership but stores counts that the process never uses.
- **Original absent initially:** The loop body never runs, and the input value is returned unchanged.
- **One successful match:** The value doubles once and stops if that doubled value is absent.
- **Long chain:** Values such as `1,2,4,8,...` trigger every corresponding doubling in order.
- **Duplicates:** Multiple copies trigger only the same one doubling step because membership is boolean and elements are not consumed.
- **Unrelated values:** Set elements not on the doubling chain never affect the result.
- **Original greater than every array value:** It is absent unless equal to some entry, so the method usually returns it immediately.
- **Final value above 1000:** This is valid and is represented safely by Python.
- **Positive-value guarantee:** Strict growth and termination reasoning use `original > 0`. A zero start would double to zero forever if zero were present, but zero is excluded by the contract.
- **Bit shift meaning:** `<<= 1` is exact integer multiplication by two, not a floating-point operation.
- **Input preservation:** Constructing `s` does not sort or modify `nums`.
- **Set expected complexity:** Hash membership is expected constant time; adversarial collision behavior is not the standard model used by the manifest.
