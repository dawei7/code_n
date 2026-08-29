## General

**Distinguish values from occurrences**

The result is not the number of distinct values tied for maximum frequency. It is the total number of array positions occupied by all such values.

If two values each occur twice, there are two maximum-frequency values but four qualifying elements. The required answer is $2+2=4$, not two.

**Count every value**

`Counter(nums)` builds a mapping from each distinct value to its number of occurrences. For `[1,2,2,3,1,4]`, the counts are:

- one maps to two;
- two maps to two;
- three maps to one;
- four maps to one.

The input is guaranteed nonempty, so `cnt.values()` contains at least one frequency.

**Find the maximum frequency**

`mx = max(cnt.values())` identifies the largest occurrence count among distinct values. In the example, `mx=2`.

This step asks only how often the most common values occur; it does not yet ask how many values attain that count.

**Sum every tied frequency**

The return expression scans the count values and keeps each `x` equal to `mx`:

`sum(x for x in cnt.values() if x == mx)`.

If $q$ distinct values have frequency $mx$, the generator yields $mx$ exactly $q$ times, so the sum is $q\cdot mx$. This equals the number of original array elements whose value belongs to a maximum-frequency class.

The code could count the tied keys and multiply, but summing the frequencies expresses the requested “total frequencies” directly.


`Counter` partitions every array position by its value. Each mapping entry is therefore the exact size of one value class.

`mx` is the greatest class size. The generator includes exactly those classes whose size equals that greatest value and excludes all smaller classes. Adding their sizes counts every qualifying position once because value classes are disjoint. Hence the returned sum is exact.

**Trace both samples**

In the first sample, count values are two, two, one, and one. The maximum is two, and summing the two entries equal to two returns four.

In an all-distinct array of length five, every frequency is one. The maximum is one, all five entries qualify, and their sum is five. This demonstrates why the answer can equal the entire input even though no value repeats.

**Why a second pass over distinct counts is still linear**

The first stage scans $N$ array elements. The maximum and sum stages each scan $U$ count entries, where $U\le N$. The three passes therefore remain $O(N)$; constants do not change asymptotic complexity.

**Exact source versus the editorial one-pass variant**

The editorial also describes updating the current maximum and total during the same input scan. That method is valid, but the protected Optimal source uses a completed `Counter` followed by two simple scans. Explaining these stages separately matches the actual data flow and reduces the chance of using a subtle incorrect running-total update.

**Why the positive-value bound is not needed**

The algorithm relies only on hashable equality. Although the source limits values to positive integers at most 100, a `Counter` works just as well for larger or negative integers. A fixed 100-entry array would use the bound more directly, but the general mapping remains simple.

The source list is not mutated.

**View the answer as a union of disjoint index groups**

For every value $v$, imagine the set of indices where `nums[i] == v`. These index sets never overlap and together cover the array. The frequency is exactly one group’s size. Selecting all groups of maximum size and adding their sizes is therefore the cardinality of their union.

This viewpoint explains why no occurrence-level rescan is necessary after counting. Once group sizes are known, the total number of qualifying original positions follows entirely from the frequency values. It also shows that duplicate occurrences are neither lost nor counted twice.

## Complexity detail

Let $N$ be the input length and $U$ the number of distinct values. Building the counter takes expected $O(N)$ time. Finding the maximum and summing tied values each take $O(U)$, so total expected time is $O(N+U)=O(N)$.

The counter stores $U$ entries, giving $O(U)$ auxiliary space and $O(N)$ in the worst case. The generator is lazy and adds only constant iteration state.

## Alternatives and edge cases

- **Return the number of tied keys:** This undercounts because the task asks for their total occurrences.
- **Multiply maximum by tie count:** It is equivalent to summing matching frequencies.
- **One-pass running maximum:** It can compute the result during counting, but requires careful resets when a new maximum appears.
- **Fixed frequency array:** Values are at most 100, so a 101-entry list works in constant bounded space; the exact source uses `Counter`.
- **All values identical:** One frequency equals $N$, so the answer is $N$.
- **All values distinct:** Every one of the $N$ frequency-one classes qualifies, so the answer is $N$.
- **Several tied modes:** Every tied class contributes its full frequency.
- **Nonempty guarantee:** It makes `max(cnt.values())` safe without a default.
- **Input preservation:** Counting reads but does not rearrange `nums`.
