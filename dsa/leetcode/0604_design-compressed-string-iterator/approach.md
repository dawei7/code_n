## General

The uncompressed string may be enormous because one run count can be as large as $10^9$. Expanding every copy would waste time and memory. The iterator stores only run descriptions:

```text
[character, remaining count]
```

and a pointer to the current run. Each call to `next` consumes one count rather than materializing any repeated characters.

**Parsing the encoded input once**

The constructor scans `compressedString` from left to right. At the start of a run, `compressedString[i]` is the character `c`. It advances once, then parses all following digits into integer `x`:

```python
x = x * 10 + int(compressedString[i])
```

Multiplying the existing value by ten shifts its decimal digits left, and adding the new digit appends that digit. Thus, characters `'1'`, `'2'`, and `'3'` become count 123 rather than three separate counts.

The pair `[c, x]` is appended to `self.d`. A list rather than tuple is used because `next` will decrement the stored count in place.

The input grammar guarantees alternating letters and positive decimal counts, so the constructor does not need error recovery for missing digits, zero counts, or punctuation.

For `"L1e2t1"`, the parsed state becomes logically:

```text
[['L', 1], ['e', 2], ['t', 1]]
```

This storage is proportional to the compressed representation, not the potentially much larger expansion `"Leet"`.

**The pointer invariant**

`self.p` is the index of the first run that may still have output remaining. For a valid active iterator:

- every run before `p` has remaining count zero;
- run `p` has a positive count;
- later runs have their original positive counts.

The constructor establishes this with `p = 0` and positive counts. `next` preserves it by decrementing the current count and advancing exactly when that count becomes zero.

**Checking availability**

`hasNext` returns:

```python
self.p < len(self.d) and self.d[self.p][1] > 0
```

The first half ensures the pointer still names a run. Python’s short-circuit `and` prevents out-of-range access if all runs are exhausted. The second half verifies a remaining occurrence.

Under the pointer invariant, an in-range current run always has positive count, so the second test is defensive and documents the required state.

**Returning one character**

`next` first delegates exhaustion handling to `hasNext`. If false, it returns a single space exactly as required.

Otherwise, it saves the current run’s character, decrements its remaining count, and advances `p` if the run is exhausted. It then returns the saved character.

For an `e` run with count two, the first call returns `e` and changes the count to one without advancing. The second returns `e`, changes it to zero, and advances to the next run. Each logical character is produced once and in run order.

Calling `hasNext` never mutates counts or the pointer. Any number of availability checks between `next` calls therefore leaves iteration position unchanged.

**Why the iterator is correct**

The constructor parses each encoded character and its full decimal repetition count into one run, preserving source order. Maintain the pointer invariant above.

When `hasNext` is true, the current run represents exactly the next unreturned character in the conceptual expansion. `next` returns that character and reduces the total remaining conceptual expansion by one. If copies remain in the run, the pointer stays; otherwise, it moves to the next run. This is exactly how the expanded string would advance.

When the pointer reaches the run-list length, all encoded counts have been consumed. `hasNext` returns false and `next` returns space. By induction over calls, every successful `next` matches the corresponding character of the full expansion without constructing that expansion.

## Complexity detail

Let $C$ be encoded length, $r$ the number of runs, $q$ the number of operations, and $E$ the expanded length. Constructor parsing visits each encoded character once, taking $O(C)$ time. Each `hasNext` and `next` performs constant work, so all operations cost $O(q)$ and total lifetime time is $O(C+q)$.

The exact source stores one mutable pair per run, using $O(r)$ space. Since $r\le C/2$, this is $O(C)$. It does not use $O(E)$ space, which is the crucial compression benefit.

This conflicts with the manifest’s $O(1)$ space claim. Constant auxiliary state is achievable with the demand-parsing design that keeps only the original encoded string, a character/count, and an index, but the exact implementation explicitly allocates `self.d` proportional to the number of runs. References to the input string and output values do not change that fact.

## Alternatives and edge cases

- **Demand parsing:** Keep an index into the compressed string and parse the next run only when the current count reaches zero. Uses constant iterator state beyond the stored input.
- **Fully uncompress:** Makes `next` simple but takes $O(E)$ time and space and fails for counts near $10^9$.
- **Regex precomputation:** Split letters and counts into parallel arrays. Similar $O(C)$ storage, with more parsing machinery.
- **Multi-digit count:** Decimal accumulation must read all consecutive digits; treating digits individually is incorrect.
- **Count of one:** The first return exhausts the run and advances immediately.
- **Huge count:** Only one integer is stored; no repeated characters are allocated.
- **Exhausted iterator:** `hasNext` is false and `next` returns one space.
- **Repeated `hasNext` calls:** They do not consume data.
- **Uppercase and lowercase:** Both are stored as exact characters; case is preserved.
- **Adjacent runs with same letter:** If valid input supplied them separately, the iterator would return them consecutively; merging is unnecessary for correctness.
- **Positive-count guarantee:** Prevents constructor-created empty runs from violating the pointer invariant.
- **Short-circuit bound check:** Pointer range is tested before indexing the current pair.
- **Space fidelity:** Run precomputation is $O(C)$, not $O(1)$, even though it is exponentially smaller than a possible $O(E)$ expansion.
