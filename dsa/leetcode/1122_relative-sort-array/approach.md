## General

**Turn the desired order into a numeric key**

Every value appearing in `arr2` must come first, ordered by its position in `arr2`. All other values must follow in ascending numeric order.

The dictionary comprehension `pos = {x: i for i, x in enumerate(arr2)}` maps each listed value to its required priority index. Distinctness of `arr2` makes every mapping unique.

**Key listed values by their required position**

For a value `x` found in `pos`, the sorting key is `pos[x]`. These keys range from zero through `len(arr2) - 1`.

All copies of one listed value receive the same key and therefore form one block. Blocks themselves appear in the exact order given by `arr2`.

Python’s sort is stable, but stability is not essential among equal numeric copies because they are indistinguishable in the returned integer array.

**Place unlisted values after every listed value**

For a value absent from `pos`, the key is `1000 + x`. Input values are between zero and one thousand, so these keys begin at one thousand.

`arr2` has at most one thousand distinct values, so its largest position key is at most 999. Therefore, every unlisted key is strictly greater than every listed key, placing all unlisted elements at the end.

Among two unlisted values $a$ and $b$, their keys are `1000 + a` and `1000 + b`. Adding the same constant preserves order, so smaller numeric values sort first. This supplies the required ascending tail.

**Why the sentinel is safe only because of the constraints**

The literal one thousand is not arbitrary. It is one greater than the largest possible listed position key. If `arr2` could contain more than one thousand distinct values, a listed position might collide with or exceed an unlisted key.

A generalized version could use `len(arr2) + x`, or better, a tuple key such as `(0, position)` for listed values and `(1, x)` for unlisted values. The exact source relies correctly on the provided bounds.

**Complete correctness argument**

If two values are both listed, their keys compare exactly like their indices in `arr2`. If one is listed and one is not, the listed key is at most 999 while the unlisted key is at least 1000, so the listed value comes first. If neither is listed, their key comparison equals their numeric comparison.

These three cases cover every pair of elements and exactly reproduce the requested total ordering. Sorting `arr1` by that key therefore returns the correct relative sort.

The function uses `sorted` rather than `arr1.sort`, so it returns a new list and leaves the input order unchanged.

Python evaluates the key function once per element and stores those keys for sorting. It does not repeatedly look up `pos` for every comparison. This keeps dictionary work linear even though the comparison phase is $O(n\log n)$.

For the first example, listed value two receives key zero, value one receives key one, and value seven, which is unlisted, receives key 1007. All copies of two therefore precede one, while seven joins the ascending unlisted tail before nineteen.

## Complexity detail

Let $n$ be the length of `arr1` and $m$ the length of `arr2`. Building `pos` costs $O(m)$ expected time and space. Python comparison sorting costs $O(n\log n)$ time, with constant-time key computation per element.

The exact implementation therefore does not achieve the manifest’s $O(n+m+V)$ counting-sort bound. That bound is achievable by counting values across the bounded range $V$ and emitting them in the required order.

The key cache and sorting machinery can use $O(n)$ temporary space, while `pos` uses $O(m)$. The returned list also has $n$ elements. Exact total storage is $O(n+m)$, not merely the manifest’s $O(V)$ description.

## Alternatives and edge cases

- **Counting sort:** Count every value from zero through one thousand, emit `arr2` values by priority, then emit remaining values in numeric order. This achieves the manifest’s $O(n+m+V)$ time and $O(V)$ space.
- **Tuple key:** Use listed key `(0, pos[x])` and unlisted key `(1, x)`. It avoids numeric-sentinel assumptions and is easier to generalize.
- **Custom comparator:** It can express the same cases but is more verbose and often slower in Python than key extraction.
- **Repeated listed value:** Every copy receives the same priority and appears in one block.
- **Repeated unlisted value:** Copies remain together in the ascending tail.
- **All values listed:** No tail exists; blocks follow `arr2` exactly.
- **No unlisted duplicates:** Ascending order still follows numeric keys.
- **Value zero unlisted:** Its key is exactly 1000, still above every possible listed position.
- **Position 999 listed:** Its key is 999, still below the smallest unlisted key.
- **Distinct `arr2`:** Required so one value does not receive conflicting priorities.
- **Every `arr2` value occurs in `arr1`:** No requested priority block is empty under the contract.
- **Input preservation:** `sorted` returns a new list rather than mutating `arr1`.
- **Manifest mismatch:** The approach must distinguish the exact comparison sort from the theoretically optimal bounded counting method.
