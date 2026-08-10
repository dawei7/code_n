## General

**Split the structured input into corresponding halves.** The first `n` entries are `x_1` through `x_n`, and the remaining `n` entries are `y_1` through `y_n`. The slices `nums[:n]` and `nums[n:]` create those two sequences.

Because `nums.length = 2n`, both slices have exactly `n` elements. Position zero of the first slice corresponds to position zero of the second, position one corresponds to position one, and so on.

**Zip corresponding x and y values.** `zip(nums[:n], nums[n:])` lazily yields pairs `(x_1, y_1)`, `(x_2, y_2)`, through `(x_n, y_n)`. This captures the desired association directly.

General Python `zip` stops when its shorter input ends. Here the equal-half guarantee means no value is truncated.

**Flatten each pair in order.** The list comprehension has two nested clauses. It first iterates `pair` over the zipped pairs. For each pair, it iterates `x` over the pair's first element and then second element. Each pair therefore contributes its `x_i` value followed immediately by its `y_i` value.

The comprehension's loop variable happens to be named `x`, but it represents either member during flattening; it is not restricted to the original x half.

For `nums = [2, 5, 1, 3, 4, 7]` and `n = 3`, the slices are `[2, 5, 1]` and `[3, 4, 7]`. Zip yields `(2,3)`, `(5,4)`, and `(1,7)`. Flattening produces `[2,3,5,4,1,7]`.

**Why every output position is correct.** Zipped pair number `i` contains original positions `i` and `n + i`, which are `x_(i+1)` and `y_(i+1)`. Flattening places them at output positions `2i` and `2i + 1`. Those are exactly the required alternating positions.

Every input element belongs to exactly one half and exactly one zipped pair, then appears exactly once during pair iteration. The output therefore has `2n` values with no omissions or duplicates introduced by the algorithm.

**The source returns a new list.** It does not mutate `nums`. This is simple and safe, but it requires storage for the output. The problem's manifest counts `O(n)` space, matching the explicit result construction and the temporary slices.

**Python allocation details.** Both slices are new lists of length `n`, so together they temporarily hold `2n` references. `zip` itself is lazy and uses constant iterator state. Each yielded tuple has two elements and is short-lived. The output list stores `2n` references.

Thus the concise expression is linear in both time and peak space. It is not an in-place shuffle despite not naming an intermediate result.

**Read the comprehension from left to right.** Its written order mirrors two ordinary loops: obtain one paired tuple from `zip`, then emit each of that tuple's two members. The inner clause completes before the next tuple is requested. This is why the result alternates locally rather than placing all first tuple members or all first-half values together.

The two slices remain alive while `zip` is being consumed because the iterator references them. After the comprehension finishes, those temporary half lists and the iterator can be released; only the newly returned result must remain. Peak memory still includes all three lists during construction, which is why temporary allocations matter even though they are not assigned names.

## Complexity detail

Creating the two slices copies `2n` references in total, taking `O(n)` time and space. Zip yields `n` pairs, and flattening appends two values per pair, taking another `O(n)` time.

The returned list has `2n` elements and therefore `O(n)` output space. The temporary slices also use `O(n)` auxiliary space. Peak total additional storage remains `O(n)`, matching the manifest.

The zip iterator and current pair require only `O(1)` beyond those lists. No sorting, searching, or nested work beyond two values per pair occurs.

Any solution returning a separate array must spend `O(n)` time to write its `2n` elements.

## Alternatives and edge cases

- **Explicit result loop:** Append `nums[i]` and `nums[n+i]` for every `i`. It avoids the two half slices while still using `O(n)` output space.
- **Preallocated result:** Create a length-`2n` list and assign positions `2i` and `2i+1`. It makes the index mapping explicit.
- **In-place bit packing:** Given the bounded values, two numbers can temporarily share one integer's bits. This can achieve constant auxiliary space but is much harder to read and mutates input.
- **Generator output:** A generator could yield alternating values with constant working space, but the required return type is a list.
- **n equals one:** Zip creates one pair and the output is the two original values in the same order.
- **Duplicate values:** Pairing uses positions, so duplicates cause no ambiguity.
- **Equal halves:** Identical values are still copied once from every original position.
- **Equal-length guarantee:** It ensures `zip` does not silently drop an unmatched element.
- **Input preservation:** Slicing and result construction leave `nums` unchanged.
- **Output length:** Every one of the `n` pairs contributes two entries, giving exactly `2n`.
- **Order inside a pair:** Iterating the tuple yields first-half value before second-half value, as required.
- **Slice allocation:** The concise implementation uses linear temporary storage in addition to the linear output.
- **Value bounds:** They do not matter to this direct construction; they matter only for optional bit-packing alternatives.
