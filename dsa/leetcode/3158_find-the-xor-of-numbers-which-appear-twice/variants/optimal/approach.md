## General

**Separate frequency detection from XOR aggregation**

The result includes a value exactly when its total frequency is two. The exact source first builds

`cnt = Counter(nums)`,

which maps every distinct number to how many times it appears.

The list comprehension

`[x for x, v in cnt.items() if v == 2]`

keeps only keys whose frequency is exactly two. Under the problem guarantee that each number appears once or twice, this is precisely the set of duplicated values.

Finally,

`reduce(xor, duplicated_values, 0)`

folds bitwise XOR across that list, starting from zero. The identity $0\mathbin{\operatorname{XOR}}x=x$ makes the initial value neutral.

**Why each duplicate is XORed once**

We must XOR the numbers that appear twice, not XOR every occurrence in the original array. XORing the original array directly would cancel each duplicate because $x\operatorname{XOR}x=0$ and would instead leave values appearing once—the opposite of the requested set.

The counter's key appears once regardless of its frequency. Filtering the key and reducing it means a duplicated number contributes exactly one copy to the final XOR.

For `[1,2,2,1]`, the filtered list contains 1 and 2. The reduction computes $0\operatorname{XOR}1\operatorname{XOR}2=3$.

For `[1,2,3]`, the filtered list is empty. `reduce` returns its initializer 0, matching the required result when no number appears twice. Without the initializer, reducing an empty list would raise an error.

**XOR order does not matter**

Bitwise XOR is associative and commutative:

$$
(a\oplus b)\oplus c=a\oplus(b\oplus c)
$$

and

$$
a\oplus b=b\oplus a.
$$

Therefore, the iteration order of `Counter.items()` does not affect the answer. The code need not sort duplicated values.


For each distinct input value $x$, `Counter` records its exact frequency. The constraint limits that frequency to one or two. The comprehension selects $x$ if and only if it belongs to the problem's duplicate set.

The reduction then computes the XOR of every selected value exactly once and nothing else. This is the requested mathematical result. If the set is empty, the identity initializer produces zero.

**Relation to the manifest**

The manifest describes a different streaming implementation: use a fixed-domain bit mask to recognize second occurrences and XOR a value when seen again. The exact source does not use a mask. It allocates a full frequency counter and a filtered list, so its space complexity differs materially.

The values happen to lie between 1 and 50, making a 51-bit mask possible. That alternative would realize constant auxiliary space under the fixed domain, but it is not the code being explained.

**Why exact frequency two is safe**

The filter tests `v == 2` rather than `v > 1`. Under the stated guarantee, these are equivalent. If arbitrary frequencies were allowed, a value appearing three times would not be selected by this source even though ordinary language might still call it duplicated. The contract makes the exact comparison correct.

## Complexity detail

Let $n$ be the input length and $u$ the number of distinct values.

Building `Counter` takes $O(n)$ expected time. Filtering its $u$ entries and reducing at most $u$ selected keys takes $O(u)$, which is $O(n)$. Total expected time is $O(n)$.

The counter stores $O(u)$ entries, and the list comprehension can store $O(u)$ duplicated values. Exact auxiliary space is $O(u)$, or $O(n)$ in the worst case.

This contradicts the manifest's $O(1)$ space claim for the mask-based method. Because the numeric domain is fixed at 50, one can describe $u\le50$ as constant under the literal constraints, but structurally the exact source allocates in proportion to the number of distinct inputs. The general input-size bound is $O(u)$.

The output is one integer, and `nums` is not modified.

## Alternatives and edge cases

- **Seen bit mask:** Set bit $x$ on first occurrence; on second occurrence, XOR $x$ into the answer. This matches the manifest and uses one fixed-size integer for values up to 50.
- **Seen set:** Add unseen values and XOR a value when it is already present. It uses $O(u)$ space but avoids a second pass and filtered list.
- **Frequency array of length 51:** Count values in fixed slots, then XOR indices with count two. It has constant domain-bounded storage.
- **XOR the whole input:** Incorrect because duplicate pairs cancel and singletons remain.
- **No duplicated value:** The initializer makes the reduction return zero.
- **One duplicated value:** The output is that value because zero is XOR's identity.
- **Several duplicates:** Associativity and commutativity make iteration order irrelevant.
- **Values appearing exactly twice:** Each counter key is selected once, not twice.
- **Frequency greater than two outside the contract:** `v == 2` would exclude it; correctness relies on the once-or-twice guarantee.
- **Duplicate list allocation:** A generator expression could feed `reduce` lazily and avoid this extra list, but the exact code builds it.
- **Fixed small domain:** It enables the constant-space alternatives but does not change the source's data structures.
- **Input preservation:** Counting reads the array and leaves it intact.
