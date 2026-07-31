## General

**Why only five results are possible**

Let `minimum` and `maximum` be the smallest and largest characters in `s`.
The permitted operation sorts characters but does not change their multiset,
so the only successful final string is the globally sorted arrangement.

If `s` is already non-descending, the answer is `0`. Otherwise, one operation
is possible exactly when `s[0]` is `minimum` or `s[-1]` is `maximum`. In the
first case, sorting the proper suffix after index `0` finishes the string; in
the second, sorting the proper prefix before the last index does so. Conversely,
any proper substring omits at least one endpoint. An omitted first character
must already equal the target's minimum, or an omitted last character must
already equal its maximum, so no other unsorted string can have answer `1`.

For an unsorted string of length two, every proper substring has length one
and sorting it changes nothing. Its answer is therefore `-1`. Strings of
length at least three are always reachable in no more than three operations.

**Distinguish two operations from three**

The three-operation case occurs exactly when the only `minimum` is the last
character and the only `maximum` is the first character. Equivalently, the
first occurrence of `minimum` is at `N - 1` and the last occurrence of
`maximum` is at `0`.

Both extremes must move to the opposite endpoints. One proper substring
cannot contain both endpoints. If a first operation moves the leading maximum
without the trailing minimum, a second operation that includes the minimum
must omit index `0`; it cannot move that minimum all the way to the first
position while also finishing the maximum's journey. The symmetric ordering
has the same obstruction, so two operations are insufficient.

Three operations do suffice: sort the prefix omitting the last character,
then the suffix omitting the first character, then that prefix again. The
first step moves the unique maximum next to the end. The second places the
unique minimum at index `1` and the maximum at the end. The final prefix sort
moves the minimum to index `0` and orders everything before the already fixed
maximum.

Every remaining unsorted string of length at least three needs exactly two
operations. If a minimum occurs in a proper prefix, sort such a prefix to put
a minimum first, then sort the remaining suffix. Otherwise the minimum exists
only at the end; because this is not the three-operation case, a maximum occurs
in a proper suffix. Sort such a suffix to put a maximum last, then sort the
remaining prefix. The earlier one-operation test supplies the matching lower
bound.

The implementation evaluates these cases in order: sorted, one operation,
impossible length two, three operations, and finally two operations.

## Complexity detail

Let $N$ be the string length. The adjacent-order check, extrema searches, and
endpoint-occurrence searches each take linear time, so the total is $O(N)$.
Only a fixed number of characters, indices, and flags are retained, giving
$O(1)$ auxiliary space.

The benchmark defines size as $N$. Repeated reverse-alphabet blocks force a
full classification and produce answer `2`. The accepted method is linear,
while the correct slower control insertion-sorts a copy before applying the
same exact case classification, producing quadratic work on the same tiers.

## Alternatives and edge cases

- **Sort the entire string for analysis:** Comparing with `sorted(s)` can
  detect the target arrangement, but comparison sorting costs
  $O(N\log N)$ time and materializes an $O(N)$ copy.
- **Enumerate operation sequences:** Trying every proper substring and every
  follow-up operation is combinatorial and unnecessary once the endpoint
  conditions are derived.
- **Single-character or constant string:** It is already non-descending, so
  the answer is `0` rather than `-1`.
- **Descending two-character string:** Sorting either one-character proper
  substring has no effect, making this the only impossible unsorted case.
- **Repeated extreme:** A minimum before the last index or a maximum after the
  first index breaks the three-operation obstruction and permits two moves.
- **Proper substring:** A prefix or suffix is allowed, but selecting all $N$
  characters in one operation is forbidden.
