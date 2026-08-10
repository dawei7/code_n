## General

**Sort so values can extend sequences from left to right.** Each element may remain $x$ or become $x+1$. After modification, selected elements must be distinct consecutive values. Processing original values in nondecreasing order ensures every sequence that a current element can extend has already been summarized.

The source uses `sorted(nums)`, which creates a sorted copy and leaves the caller's list unchanged.

**Define the dictionary state.** `longest[v]` represents a best consecutive selection, using processed elements, whose final modified value is $v$. Missing keys have length zero.

For current original value `value`, there are two meaningful choices.

If it is incremented to `value + 1`, it can extend a sequence ending at `value`. The resulting length is

`incremented = longest.get(value, 0) + 1`.

If it remains `value`, it can extend a sequence ending at `value - 1`. The resulting length is

`unchanged = longest.get(value - 1, 0) + 1`.

The source stores those results at `longest[value + 1]` and `longest[value]` respectively.

**Compute both candidates before updating.** This order prevents using the current element twice. In particular, `incremented` must read the old state ending at `value` before `longest[value]` is overwritten by the option that keeps the same current element unchanged.

If the write happened first, the incremented option could extend a sequence that already included the current element, effectively assigning that one array position two final values. The temporary variables avoid that error.

**Why direct assignment is safe.** At first glance, writing rather than taking a maximum may seem risky. Sorted processing provides the needed structure.

Before processing a copy of value $x$, an existing state ending at $x$ may describe a strong sequence formed from smaller elements. The algorithm immediately uses that state to create `incremented` ending at $x+1$ by assigning the current element to $x+1$. After that use, overwriting the state ending at $x$ with `longest[x-1] + 1` is safe: it records the best way for this current copy to end at $x$.

For duplicate $x$ values, the first may be kept as $x$ and another incremented to $x+1$. Later duplicates cannot make a consecutive set longer merely by duplicating an already used final value. The update equations capture exactly the two useful roles.

**A trace with duplicates.** Process sorted values `[1,1,2]`.

For the first 1, keeping it gives a length-one sequence ending at 1; incrementing it gives length one ending at 2.

For the second 1, `incremented` reads the length-one state ending at 1 and creates length two ending at 2, representing final values `[1,2]`. Keeping the second 1 still yields only length one ending at 1 because two final 1s cannot both belong to a strictly consecutive selection.

When original 2 arrives, incrementing it extends the length-two sequence ending at 2 to final value 3, producing `[1,2,3]` of length three.

**Why sorting is essential.** Without sorted order, a large value might be processed before the smaller predecessor that should extend into it. The dictionary state would then miss a feasible chain. Sorting creates a valid dynamic-programming order by original value.
Any optimal selection using the processed prefix and ending at $v$ has some last original element. If that element was kept unchanged, its original value is $v$ and the preceding selected values end at $v-1$. If it was incremented, its original value is $v-1$ and the preceding values end at $v-1$. The two transitions model these possibilities as each original value arrives. Updating `answer` with both candidates records the best endpoint across all values.

## Complexity detail

Sorting $N$ elements costs $O(N\log N)$ time. The loop performs expected-$O(1)$ dictionary work per element, adding $O(N)$. Total expected time is $O(N\log N)$.

`sorted(nums)` allocates an $O(N)$ list. The dictionary can contain keys around each distinct input value, at most $O(N)$ entries. Auxiliary space is $O(N)$. The input itself remains unchanged.

Expected dictionary bounds assume normal Python hash-table behavior. Values are bounded integers, so arithmetic is straightforward.

## Alternatives and edge cases

- **Sort and greedily take the next apparent value:** A local keep-or-increment decision can block a longer chain; the two endpoint states retain both useful possibilities.
- **Frequency-array DP:** Values are bounded by $10^6$, so a dense array is possible but uses space proportional to the value range rather than observed values.
- **Brute-force modification choices:** Each element has two choices, producing $2^N$ configurations before selection is even considered.
- **All values far apart:** No transition finds a predecessor, so the best length remains one.
- **Duplicate values:** At most two copies can be useful around one level—one unchanged and one incremented into the next value. The updates handle this without selecting duplicate final values.
- **Already consecutive values:** Keeping each one extends the state ending at its predecessor.
- **Gaps of one original unit:** Incrementing a lower value may bridge or extend the sequence, represented by `incremented`.
- **Single element:** Both options create a length-one sequence, so the result is one.
- **Compute-before-write requirement:** Reversing the statement order can reuse the current element and produce invalid lengths.
- **Input preservation:** `sorted` returns a copy rather than mutating `nums`.
