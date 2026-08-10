## General

Choosing an integer removes **all** of its occurrences, so the useful quantity is not the integer’s value but its frequency. If one value occurs seven times and another occurs twice, spending one set entry on the first value removes more array elements. This naturally leads to a greedy strategy: take frequencies from largest to smallest until at least half of the array has been removed.

**Compress the array into frequencies**

`Counter(arr)` maps each distinct value to its number of occurrences. If the input is `[3, 3, 3, 5, 5, 2]`, the frequency multiset is three, two, and one. The specific keys still identify which values would be selected, but the required return value is only the number of selected values, so the loop needs only the counts.

`cnt.most_common()` returns `(value, frequency)` pairs ordered from greatest frequency to least frequency. The loop unpacks each pair as `_, v`. The underscore discards the actual value, while `v` is the number of array positions removed by selecting it.

Two accumulators have distinct meanings:

- `m` is the total number of array elements covered by all frequencies selected so far.
- `ans` is the number of distinct values selected, which is the size of the removal set.

For each descending frequency, the code adds `v` to `m` and increments `ans` once. It stops as soon as `m * 2 >= len(arr)`. Multiplying by two avoids floating-point division and states “removed at least half” exactly.

For example, frequencies `[4, 3, 2, 1]` for an array of length ten have a target of five removed elements. Taking four is insufficient. Taking the next frequency three raises the removed total to seven, so two distinct values are enough. The code returns two without needing to build the shortened array.

**Why taking the largest remaining frequency is safe**

Suppose the frequencies in descending order are

$$
f_1 \ge f_2 \ge \cdots \ge f_u,
$$

where $u$ is the number of distinct values. Among every possible set of $r$ distinct values, the greatest number of removable elements is $f_1 + f_2 + \cdots + f_r$. Any set that omits one of those top frequencies and includes a smaller frequency instead can remove no more elements; swapping the smaller choice for the omitted larger one never hurts.

Let the loop stop after $r$ frequencies. Their sum reaches at least half of the array. The first $r - 1$ frequencies did not reach half, because otherwise the loop would already have stopped. Since those largest $r - 1$ frequencies are the maximum removal achievable with any $r - 1$ chosen values, no set of size $r - 1$ can meet the target. A set of size $r$ does meet it, so $r$ is the minimum.

This argument also explains why ties do not need a special rule. If several values have the same frequency, choosing any of them removes the same number of elements. `most_common` may order tied keys according to encounter order, but `ans` is unchanged.

The algorithm never mutates `arr` and never simulates deletion. It reasons only about coverage counts, which are enough because removing one value cannot change the number of occurrences belonging to another distinct value.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values.

Building `Counter(arr)` examines every element and uses expected $O(n)$ time with hash-table operations. Calling `most_common()` without a limit orders all $u$ entries by frequency, costing $O(u \log u)$ time. The loop examines at most $u$ frequencies, adding $O(u)$ time. The total is

$$
O(n + u\log u),
$$

which becomes $O(n\log n)$ in the worst case because $u \le n$.

The counter stores $u$ keys and counts. `most_common()` produces a list of $u$ pairs, and sorting that list also needs implementation-dependent temporary storage. The total auxiliary space is $O(u)$, which is $O(n)$ in the worst case.

The loop may stop early, but `most_common()` has already ordered every distinct value, so early termination does not improve the worst-case sorting cost. Hash-table complexity is expected rather than unconditional; adversarial collision behavior is outside the usual model for Python’s built-in counter.

## Alternatives and edge cases

- **Bucket frequencies:** A frequency cannot exceed $n$, so count how many values occur with each possible frequency and scan buckets downward. This yields $O(n)$ time and $O(n)$ space, avoiding comparison sorting.
- **Sort the original array:** Equal values become adjacent, allowing run lengths to be counted and then sorted. It still takes $O(n\log n)$ time and mutates the input unless a copy is made.
- **Max-heap of frequencies:** Repeatedly pop the largest count until the target is reached. Heap construction can be linear, and each selected value costs $O(\log u)$, which can help when very few values are needed.
- **Choosing values in input order:** This is not optimal because a rare value can consume one set entry while removing very few elements. Frequency order is the property supported by the exchange argument.
- **Exactly half removed:** The condition is inclusive. When `m * 2 == len(arr)`, the requirement has been met and the loop must stop.
- **More than half removed:** Removing all occurrences can overshoot the target, and overshooting is permitted. There is no need to remove only part of the final value’s occurrences.
- **All values equal:** The first frequency is $n$, so one selected integer empties the array and the answer is one.
- **All values distinct:** Every frequency is one. Because the input length is even, exactly $n / 2$ distinct values must be selected.
- **Tied frequencies:** Their internal order cannot affect how many selections are required because equal counts contribute equal coverage.
- **Large integer values:** The counter keys need not form a small numeric range. Complexity depends on the number of elements and distinct keys, not the magnitude of the values.
- **Odd length outside the contract:** The multiplication test would require removal of at least the ceiling of half and still works correctly, even though the stated array length is even.
- **Empty input outside the contract:** The code would return zero because the loop has no entries. The official constraints begin at length two, so the normal proof assumes a positive target.
