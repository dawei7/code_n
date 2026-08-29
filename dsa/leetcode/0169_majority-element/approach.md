## General

**Replace full counting with pair cancellation**

The majority element appears more than half the time. Imagine repeatedly
removing pairs of different values from the array. Every such pair removes at
most one occurrence of the true majority and exactly one non-majority
occurrence.

Because the majority begins with more occurrences than all other values
combined, it cannot be completely eliminated by these opposite-value pairs.
After all possible cancellations, the surviving value must be the majority.

Boyer–Moore voting performs this cancellation in one left-to-right pass without
physically deleting elements. `m` is the current candidate and `cnt` is its
uncancelled balance.

**Start a new candidate when the balance is empty**

When `cnt == 0`, all elements represented by the previous voting segment have
been paired away. The current number `x` begins a new segment, so the source
sets `m = x` and `cnt = 1`.

The earlier balanced prefix can be forgotten. If it contained some occurrences
of the true majority, it also contained the same number of other values paired
against them. Removing equal numbers from the two sides of the majority
inequality cannot make a different value become the true global majority.

The initialization `cnt = m = 0` is only placeholder state. Since the input is
nonempty and the first iteration sees `cnt == 0`, `m` is replaced by
`nums[0]` before the placeholder could be returned.

**Update the balance for later values**

When a candidate is active, seeing the same value increments `cnt`. Seeing a
different value decrements it. A decrement conceptually pairs that different
element with one currently unmatched occurrence of `m`.

The counter is not the candidate's total frequency in the entire prefix. It is
the net surplus of candidate occurrences after cancellations within the
current unresolved segment. That is why it can fall back to zero even when the
candidate appeared several times earlier.

The source uses a special branch when zero: it assigns the candidate and count
one directly. Otherwise, the conditional expression adds either one or
negative one.

**Trace `[2,2,1,1,1,2,2]`**

The first two values select candidate two and raise its balance to two. The
next two ones lower the balance to zero; those four positions can be viewed as
two cancelled pairs.

The following one begins a new segment with candidate one and balance one. The
next two lowers the balance to zero. The final two starts another segment and
survives with positive balance, so the returned candidate is two.

Although the candidate changed temporarily, the global majority could not be
cancelled away permanently.

For `[3,2,3]`, three starts with balance one, two cancels it to zero, and the
final three becomes the surviving candidate.

**Why the final candidate is the majority**

Let the true majority occur $M$ times among $n$ elements, with
$M>n-M$. Each cancellation removes two different values. If one removed value
is the majority, the other is not; if neither is the majority, its advantage
does not decrease.

After any number of cancellations, the remaining multiset still has at least
one majority occurrence and the same value remains more frequent than all
remaining non-majority elements combined. Boyer–Moore's counter segments are
an online encoding of such cancellations.

At the end, any positive unmatched balance belongs to the current candidate.
Since the guaranteed majority must survive, that candidate is the majority.

**Why no verification pass appears**

If the input did not guarantee a majority, Boyer–Moore would still produce a
candidate but it might not occur more than half the time. For `[1,2,3]`, for
example, some final candidate survives even though no majority exists.

Under this problem's explicit guarantee, verifying the candidate by counting
it again is unnecessary. The method can return `m` immediately after one pass.

**Input and interface details**

Values can be negative, zero, or positive. The algorithm uses only equality,
so their magnitudes and signs are irrelevant.

The selected source annotates `List[int]` without importing `List`. A
standalone module needs `from typing import List`; the native harness may
already provide the typing name.

## Complexity detail

Let $n$ be the number of elements. The loop examines each value once and does
constant work, so time is $O(n)$.

Only the candidate, counter, and current loop value are stored. Auxiliary space
is $O(1)$. No input modification or frequency table is required. These bounds
match the manifest and the follow-up.

## Alternatives and edge cases

- **Frequency map:** Count every value and return the one above half. It is $O(n)$ time but can use $O(n)$ space.
- **Sorting:** The majority must occupy sorted index `n // 2`, but sorting costs $O(n\log n)$ time and may mutate the input.
- **Bit counting:** Reconstruct the majority bit by bit in linear time for a fixed integer width, with more implementation complexity around negatives.
- **Divide and conquer:** Combine half-majority candidates, generally taking $O(n\log n)$ time.
- **One element:** It immediately becomes the candidate and is returned.
- **Candidate changes:** A temporary candidate need not be the true majority; only the final guarantee matters.
- **Counter meaning:** It is a cancellation balance, not a global occurrence count.
- **Negative values:** Equality-only voting handles them unchanged.
- **No guaranteed majority:** A second counting pass would be required to validate the candidate.
- **Missing typing import:** `List` must be supplied for standalone evaluation of annotations.
