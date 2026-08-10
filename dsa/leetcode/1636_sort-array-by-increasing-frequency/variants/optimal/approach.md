## General

**Turn the two sorting rules into one key**

Every element is ranked by two criteria:

1. a smaller frequency comes first;
2. when frequencies tie, a larger numeric value comes first.

Python's sorting key can represent both criteria as a tuple. Tuples are compared from left to right, so the source uses

`(cnt[x], -x)`.

The first component is the frequency and is naturally sorted upward. The second is the negated value. If $x_1>x_2$, then $-x_1<-x_2$, so ordinary ascending order on the negatives places the larger original value first.

Combining the rules into one tuple avoids writing a custom pairwise comparator and makes the priority order explicit.

**Count before sorting**

`Counter(nums)` traverses the input and creates `cnt`, a mapping from each distinct value to its number of occurrences. Every later key computation can then retrieve `cnt[x]` in expected constant time.

Counting first is essential. Frequency is a property of the complete input, not of the part of the list already visited by the sorting algorithm. Trying to update counts while sorting would make keys unstable and invalidate comparison consistency.

The source then calls `sorted(nums, key=...)`. `sorted` returns a new list and leaves `nums` unchanged. The key function is evaluated for the input elements, and the resulting keys determine their order.

**Why repeated values remain together**

Every occurrence of the same integer `x` receives the identical tuple `(cnt[x], -x)`. Therefore no different key can be ordered between two occurrences of `x` once the full sort is complete. Repeated values form one contiguous block.

Within that block, occurrence order does not matter because the values are identical. Across blocks, the first tuple component orders frequencies, and the second orders values descending among equal frequencies.

**A trace with tied frequencies**

For `nums = [2, 3, 1, 3, 2]`, the counter is:

- value 1 has frequency 1,
- value 2 has frequency 2,
- value 3 has frequency 2.

Their keys are:

- 1 receives `(1, -1)`,
- 2 receives `(2, -2)`,
- 3 receives `(2, -3)`.

The frequency-1 key comes first. Between the two frequency-2 values, `(2,-3)` is smaller than `(2,-2)`, so 3 precedes 2. Repeating each value according to its input occurrence count gives `[1,3,3,2,2]`.

Negative values work with the same transformation. If -1 and -6 tie in frequency, -1 is the numerically larger value. Their second key components are 1 and 6, so -1 correctly comes first.

**Why the returned order is correct**

Take any two output elements $x$ and $y$ with $x$ before $y$. If their frequencies differ, tuple ordering can place $x$ first only when `cnt[x] < cnt[y]`, satisfying the primary rule. If frequencies match, their first key components tie and ordering is decided by `-x <= -y`, equivalent to $x\ge y$, satisfying decreasing numeric order.

Conversely, whenever the problem requires $x$ before $y$, its corresponding key is smaller under exactly those same cases. Sorting all elements by this key therefore produces precisely the required total order.

The algorithm sorts occurrences rather than just distinct values. This directly returns a list of the same length and multiplicities as the input, with no separate reconstruction step.

## Complexity detail

Let $n$ be the number of input elements and $k$ the number of distinct values. Building the Counter takes $O(n)$ expected time and $O(k)$ space.

Python sorting takes $O(n\log n)$ worst-case comparison time. Each cached-key tuple takes constant time to create because Counter lookup is expected $O(1)$. Sorting dominates counting, so total expected time is $O(n\log n)$.

`sorted` allocates a new $n$-element result, and Python's Timsort can use $O(n)$ temporary storage in the worst case. The Counter holds at most $n$ entries. Total additional and output space is $O(n)$, matching the manifest.

The value constraints provide only 201 possible integers, so Counter itself is bounded by a small constant with respect to $n$. The returned list and sorting workspace still scale with $n$, so $O(n)$ remains the appropriate overall space statement.

## Alternatives and edge cases

- **Count distinct values, sort the keys, then expand blocks:** Sort the $k$ unique values by `(frequency, -value)` and append each value its frequency times. This costs $O(n+k\log k)$ and can reduce comparison work when many values repeat.
- **Bucket by frequency:** Frequencies range from 1 through $n$. Values in each bucket can be sorted descending, then expanded. This can be useful with a tightly bounded value domain but requires more bookkeeping.
- **Custom comparator:** Compare counts first and values second. It is equivalent, but a tuple key is shorter and avoids repeatedly looking up comparison operands during sorting.
- **All values distinct:** Every frequency is one, so the entire output is the input values sorted in decreasing numeric order.
- **All values equal:** All occurrences have the same key and the returned list is unchanged in value.
- **Two values share a frequency:** The numerically larger one must come first; negation converts that descending rule into ascending-key order.
- **Negative integers:** Negation still reverses numeric order correctly. “Larger” means, for example, $-1>-6$.
- **Zero:** Its secondary key is also zero and participates normally between positive and negative values.
- **Input preservation:** `sorted` returns a new list. Using `nums.sort` would mutate the caller's array, which the exact source does not do.
- **Stable sorting is not relied upon:** Equal values have identical keys, and their relative occurrence order is unobservable. Different values are fully distinguished by the secondary component when counts tie.
