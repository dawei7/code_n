## General

**There can be at most two qualifying values**

A qualifying value occurs more than $\lfloor n/3 \rfloor$ times. Three
different values cannot each occur more than one third of an array: their
combined occurrences would exceed $n$. Therefore the answer contains at most
two values.

This bound suggests keeping two candidate slots rather than a frequency map for
every distinct number. The generalized Boyer-Moore voting algorithm uses
candidates `m1` and `m2` with counters `n1` and `n2`. The first pass does not
try to preserve exact frequencies. It repeatedly cancels groups of three
different values so that any value too frequent to be completely canceled must
remain in one of the two slots.

**Interpret the counters as unmatched candidate votes**

For each current value `m`, the exact source evaluates these cases in order:

1. If `m == m1`, increment `n1`.
2. Otherwise, if `m == m2`, increment `n2`.
3. Otherwise, if `n1 == 0`, place `m` in the first slot with count 1.
4. Otherwise, if `n2 == 0`, place `m` in the second slot with count 1.
5. Otherwise `m` differs from both active candidates, so decrement both counts.

The final case can be understood as deleting one unmatched occurrence of
`m1`, one of `m2`, and the current third distinct value `m`. Removing three
different values cannot change which original value occurs more than one third
of the total in the sense needed for candidate survival: a truly frequent
value cannot be canceled away without consuming enough nonmatching values.

When a counter reaches zero, its candidate value becomes stale and the slot may
represent a new distinct value later. No array elements are physically removed;
the counters compactly record the same cancellation effect.

**Why the branch order matters**

Candidate comparisons occur before zero-count replacement. A slot whose count
is zero may still contain an old value. If the current value equals it, simply
incrementing the corresponding count reactivates that candidate. More
importantly, checking both candidate equalities before filling an empty slot
prevents the same value from occupying both slots.

The source initializes `m1 = 0` and `m2 = 1`, two different arbitrary values,
with both counts zero. These are not assumed to occur in the input. If the
first input value equals one of them, its equality branch correctly raises that
slot's count. Otherwise an empty slot is replaced. Because replacement occurs
only after confirming the new value differs from both stored candidates, `m1`
and `m2` remain distinct.

Using concrete initial values is safe because the second pass verifies real
frequency. An unused sentinel cannot enter the answer merely by remaining in a
candidate variable.

**Trace cancellation on a mixed input**

Consider `[1, 2, 3, 1, 2, 1, 1]`. The first two distinct values occupy the two
slots. Value 3 differs from both while both counts are positive, so one vote is
removed from each candidate; conceptually the triple `(1,2,3)` is canceled.
The later 1 and 2 refill or strengthen their slots. The final two 1 values make
1 survive with positive support.

The counters at the end are not necessarily the original frequencies. They
measure votes remaining after cancellation. That is why the method does not
return every positive-count candidate immediately.

**Why every true answer survives as a candidate**

Imagine applying every final-case cancellation to the array. Each cancellation
removes three pairwise distinct values. For a particular value `x`, one such
group removes at most one occurrence of `x` but removes three total elements.
If `x` originally occurs more than one third of all elements, it cannot be
completely eliminated while all remaining unmatched votes belong only to other
values; there are not enough non-`x` occurrences to pair with every `x` in
three-distinct groups.

Once no more groups represented by the scan remain, at most two distinct
candidate types can have unmatched votes. Every value whose frequency exceeds
$n/3$ must be among them. The first pass therefore narrows the only possible
answers to `m1` and `m2`, but it does not guarantee either one actually crosses
the threshold.

**Verification turns candidates into exact answers**

An array such as `[1,2,3,4]` can leave arbitrary survivors even though no value
appears more than `floor(4/3) = 1` time. The list comprehension checks each of
the two candidates with `nums.count(m)` and includes it only when the true
count is strictly greater than `len(nums) // 3`.

Strict `>` is required. A value occurring exactly $\lfloor n/3 \rfloor$ times
does not qualify. Because `m1` and `m2` remain distinct, the comprehension
cannot append the same value twice. The output order follows candidate-slot
order, and the contract permits any order.

Combining the two phases gives complete correctness: cancellation guarantees
that every qualifying value is in a candidate slot, and verification removes
every candidate that does not truly meet the frequency condition.

## Complexity detail

Let $n$ be `len(nums)`. The voting pass processes each element once in $O(n)$
time. The list comprehension calls `nums.count` once for each of two candidates;
each call scans the array, adding $2n$ work. Total time is still $O(n)$.

The algorithm retains two candidate values, two counters, and an answer of at
most two elements, so auxiliary space is $O(1)$. The `nums.count` operations do
not build frequency tables. Required output size is itself bounded by two.

## Alternatives and edge cases

- **Frequency dictionary:** Count every value, then filter counts above $\lfloor n/3\rfloor$. It is simpler but uses $O(n)$ space in the all-distinct case, missing the constant-space follow-up.
- **Sorting:** Equal values become contiguous, allowing run counts in $O(n\log n)$ time. It may mutate the input or require a copy and does not improve on voting.
- **General threshold $n/k$:** Keep at most $k-1$ candidates, cancel one vote from all when a new distinct value finds every slot occupied, then verify. This solution is the $k=3$ case.
- **One element:** Since the threshold is `0`, its real count 1 qualifies. One initialized candidate slot is activated and verification returns that value.
- **Two different elements:** The threshold is also `0`, so both occur more than it and both correctly survive verification.
- **Exactly one-third frequency:** Verification uses strict greater-than and excludes a candidate occurring only `len(nums) // 3` times.
- **No qualifying element:** Candidates may still exist after voting, but both exact counts fail and the result is empty.
- **Two qualifying elements:** Both fit the mathematical maximum and survive in separate slots.
- **Initial values 0 and 1 absent from input:** Their zero counts make the slots replaceable, and final verification prevents them from appearing spuriously.
- **Initial values 0 or 1 present:** Equality increments the relevant zero-count slot, which is equivalent to selecting that value as a candidate.
- **Negative and large integers:** Only equality and counting are used, so numeric range and sign do not affect the algorithm.
- **Input preservation:** Voting changes only local candidates and counters; `nums` remains unchanged.
