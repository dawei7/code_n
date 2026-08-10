## General

**Use rearrangement to put small values first.** The final array must start at one and adjacent values may rise by at most one. Since elements can be rearranged freely, their original order carries no useful restriction. Sorting `arr` in ascending order assigns the smallest original values to the earliest, lowest positions, preserving larger values for positions that may reach greater heights.

The exact solution then modifies this sorted list in place. First, `arr[0] = 1`. Because all original values are positive, changing the smallest value to one is either no change or an allowed decrease.

**Choose the largest feasible value at every later position.** At index `i`, two upper bounds apply:

- The element cannot exceed its sorted original value `arr[i]` because increases are forbidden.
- It cannot exceed the finalized previous value plus one, or the adjacent difference would be too large.

The assignment

`arr[i] = min(arr[i], arr[i - 1] + 1)`

chooses the largest value satisfying both bounds. Keeping it as large as possible is helpful rather than risky: the objective is to maximize some value, and a larger feasible predecessor can only allow later positions to be larger.

**Why the lower side of the absolute-difference rule is also satisfied.** After sorting, the original `arr[i]` is at least the original preceding value. The preceding value may only have been decreased. The new current value is either its own original value or `arr[i - 1] + 1`. In either case it is at least `arr[i - 1]`, so the transformed array is nondecreasing. Its adjacent difference is therefore between zero and one, satisfying the absolute bound.

**Trace `[100, 1, 1000]`.** Sorting gives `[1, 100, 1000]`. The first value becomes one. The second is capped at two, and the third is capped at three. The final list `[1, 2, 3]` is valid and the returned last value is three.

For `[2, 2, 1, 2, 1]`, sorting gives `[1, 1, 2, 2, 2]`. The recurrence leaves these values within the step bound, and the last value is two. This valid arrangement differs from the sample’s displayed arrangement but attains the same maximum.

**Why sorting is a safe assignment of original capacities.** Think of each original number as the greatest final value that one element can support. Early positions have low permitted heights because the sequence starts at one. Giving a large capacity to an early position while leaving a smaller capacity for later cannot help. Swapping those capacities places the smaller one where requirements are lower and preserves the larger one for a potentially higher position. Repeating this exchange yields ascending capacity order.

**Prefix optimality.** After processing index `i`, the modified prefix is valid, and `arr[i]` is the greatest endpoint achievable using the first `i + 1` sorted capacities.

The property begins with endpoint one, which is forced. For the next position, every valid endpoint is bounded by both its assigned capacity and the prior endpoint plus one. The minimum of those bounds is therefore an absolute upper limit, and the algorithm reaches it. Since the previous endpoint was already maximal, no alternative prefix can provide a larger allowance. Induction proves every computed endpoint is maximal.

**Why the last element is the answer.** The transformed array is nondecreasing, so its maximum is `arr[-1]`. Prefix optimality says no valid use of all capacities can produce a larger final endpoint under the sorted assignment, and the exchange argument says no other rearrangement can do better. Thus returning the last value gives the maximum possible element.

**The exact method produces a valid witness.** It does more than calculate a number: after execution, `arr` itself is one valid rearranged-and-decreased array attaining the answer. This is useful for reasoning but also means the caller’s input order and values are destroyed.

## Complexity detail

Let `n = arr.length`. Sorting takes `O(n log n)` time, and the recurrence scans the array once in `O(n)`, for total `O(n log n)` time.

The loop uses `O(1)` scalar space, but Python’s in-place sort can require `O(n)` temporary memory. The safe auxiliary bound for the exact Python implementation is therefore `O(n)`. The input list is reused for the transformed witness rather than allocating another length-`n` array.

## Alternatives and edge cases

- **Counting by capped value:** Since no final maximum can exceed `n`, count each original value as `min(value, n)` and process capacities in linear time with `O(n)` space.
- **Track only the endpoint after sorting:** A scalar answer can replace rewriting every later array entry, but the exact source stores the full valid witness.
- **Already valid ascending array:** Every minimum keeps the original value, and the existing maximum is returned.
- **No original one:** The smallest positive value is decreased to one, satisfying the required first element.
- **Many duplicate small values:** They create flat portions, which are allowed because adjacent difference may be zero.
- **Very large values:** Each is reduced only as much as the previous-plus-one rule requires.
- **Single element:** It is set to one and returned, which is the only valid first value.
- **Maximum possible result:** No length-`n` valid sequence starting at one can exceed `n`, and the recurrence reaches `n` exactly when capacities support every step.
- **Only decreases:** The `min` assignment never raises a sorted capacity, so every modification is legal.
- **Absolute difference:** The produced sequence is nondecreasing with rises at most one, which is a sufficient stronger structure.
- **Input mutation:** Sorting and overwriting values permanently transform `arr`. Use a copy if the caller needs the original data.
- **Positive-value guarantee:** Setting the first sorted entry to one is always a decrease or no-op; zero or negative inputs would require separate reasoning.
