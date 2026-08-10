## General

**Compare concatenation orders, not numeric values alone**

Sorting the integers in ordinary descending order is not sufficient. With
three and 30, placing three first gives `"330"`, while placing 30 first gives
`"303"`. The better order depends on both complete decimal strings.

After converting every value to text, define that `a` should precede `b` when:

$$
\texttt{a+b}>\texttt{b+a}.
$$

Both compared strings have the same total length, so lexicographic string
comparison is equivalent to numeric comparison of those two nonnegative
concatenations without risking integer overflow.

**Why the pairwise rule gives a global maximum**

Consider any proposed output with adjacent pieces `a` then `b`. Everything
before them is a common prefix and everything after them is a common suffix.
If `a+b < b+a`, swapping just those two pieces makes the entire result larger
at the first differing position.

Therefore an optimal arrangement cannot contain an adjacent inversion under
this rule. Sorting removes all such inversions. Once every adjacent pair is in
the preferred order, no exchange can improve the concatenation, and the sorted
sequence is globally maximal.

The relation is a valid ordering when equality is treated correctly. One way
to see transitivity is to compare the infinite repetitions of each finite
string; `a+b` versus `b+a` gives the same relative order as those periodic
extensions.

**Adapt the comparator to Python sorting**

Python 3 sorting normally accepts a key function, not a two-argument
comparator. `cmp_to_key` wraps a comparator result in objects whose ordering
methods Python's sort can use.

The source lambda returns positive one when `a+b < b+a`, telling the ascending
sort that `a` belongs after `b`. Otherwise it returns negative one, telling it
to place `a` before `b`. This produces the desired largest-first sequence for
strictly unequal comparisons.

**Comparator equality defect**

A comparator must return zero when its two inputs are equivalent. The selected
lambda returns negative one even when `a+b == b+a`.

That can happen for identical strings or related repetitions such as `"12"`
and `"1212"`. The comparator then claims both that `a < b` and that `b < a`,
violating antisymmetry and Python's expected ordering contract.

Either relative order yields the same concatenated text, so the mathematical
answer does not care which tied item comes first. Nevertheless, relying on an
inconsistent comparator is unsafe. The conforming comparator should return
zero for equality, for example by comparing both concatenations with a
three-way expression.

**Trace the main example**

For `[3,30,34,5,9]`, comparisons place nine before five because `"95"` exceeds
`"59"`. Five belongs before 34, and 34 belongs before three because `"343"`
exceeds `"334"`. Three belongs before 30 because `"330"` exceeds `"303"`.

The sorted string list is `["9","5","34","3","30"]`. Joining it yields
`"9534330"`.

For `[10,2]`, `"210"` exceeds `"102"`, so two comes first and the answer is
`"210"`.

**Normalize an all-zero result**

If the first sorted string is `"0"`, then every input must be zero. Any
positive number would compare ahead of zero because a concatenation beginning
with a nonzero digit is larger.

The source returns exactly `"0"` instead of joining several zeros into
`"000"`. If the first string is nonzero, joining all pieces preserves every
input digit and produces the maximal representation.

The nonempty input guarantee makes `nums[0]` safe after conversion and sorting.

**Input conversion and dependencies**

Converting all numbers once avoids repeating integer-to-string conversion in
every comparator call. The input list variable is rebound to a new string list;
the caller's original list object is not sorted or mutated.

The source uses `List` and `cmp_to_key` without imports. Standalone execution
needs `from typing import List` and
`from functools import cmp_to_key`.

## Complexity detail

Let $n$ be the number of values and $k$ the maximum decimal digit count.
There are $O(n\log n)$ comparisons, and each may build and compare strings of
$O(k)$ length. Time is $O(nk\log n)$. Conversion and final joining add
$O(nk)$.

The string list, sort support, comparator concatenations, and output occupy
$O(nk)$ space in the usual bound. These match the manifest. The comparator's
missing equality case is a correctness-contract issue, not a complexity change.

## Alternatives and edge cases

- **Three-way comparator:** Return `-1`, `0`, or `1` from comparing `b+a` with `a+b`; this repairs tied-order consistency.
- **Repeated-string sort key:** With bounded digit length, repeating strings to a common comparison length can work, but a true comparator states the rule exactly.
- **Ordinary descending sort:** Fails for shared-prefix pairs such as three and 30.
- **All zeros:** Collapse the joined representation to one `"0"`.
- **One number:** Its decimal string is returned, with zero normalized normally.
- **Duplicate numbers:** They compare equivalent and may appear in either relative order.
- **Periodic ties:** `"12"` and `"1212"` concatenate equally in both orders.
- **Large final number:** It remains a string, avoiding numeric overflow.
- **Nonnegative guarantee:** No minus signs complicate concatenation ordering.
- **Missing imports:** `List` and `cmp_to_key` must be supplied.
- **Comparator contract:** Equality must return zero even when either tied order has the same final text.
