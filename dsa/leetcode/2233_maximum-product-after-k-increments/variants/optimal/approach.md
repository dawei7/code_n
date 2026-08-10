## General

**An increment is most valuable on a smallest factor**

Consider two current factors `a <= b` while all other factors stay fixed. If one operation is assigned to `a`, their contribution becomes `(a + 1)b`. If assigned to `b`, it becomes `a(b + 1)`. The difference is

$$
(a+1)b - a(b+1) = b-a \ge 0.
$$

Therefore, incrementing the smaller factor produces a product at least as large as incrementing the larger one. This pairwise exchange remains valid when either value is zero.

Repeatedly applying this reasoning shows that every unit operation should go to a currently smallest array element. The goal is to level small factors before making already large factors even larger.

**Use a min-heap to expose the current minimum**

`heapify(nums)` rearranges the input list into a min-heap. Its root `nums[0]` is always a smallest current element.

For each of the `k` operations, the solution executes

`heapreplace(nums, nums[0] + 1)`.

`heapreplace` removes the root and inserts its incremented value in one heap operation, then restores heap order. This is equivalent to popping a smallest factor, adding one, and pushing it back, but with a combined primitive.

The same array element need not stay at the root. Once incremented, another value may become smaller, and the heap automatically makes that value the next choice.

**Why the greedy sequence is globally optimal**

Take any allocation of the remaining increments that first disagrees with the greedy choice. It increments some factor `b` while a current factor `a <= b` is available. Move that one increment from `b` to `a`. The pairwise calculation proves the product does not decrease.

After this exchange, the allocation agrees with the greedy choice for one more operation. Repeating the argument transforms an optimal allocation into the heap's sequence without reducing its product. Consequently, the greedy sequence attains a maximum.

This is also the familiar balancing property of products: for a fixed sum, nonnegative factors produce a larger product when they are closer together. The increments increase the total sum by a fixed amount, and always raising a minimum performs that balancing one unit at a time.

**Using all `k` operations is safe**

The statement permits at most `k` operations, while the loop always performs exactly `k`. Incrementing a nonnegative factor can never decrease the ordinary product. If all other factors make the product zero, an increment might leave it unchanged, but never makes it worse. Therefore, some maximum is achieved after using all available operations.

This detail matters when several zeros exist. Until enough zeros are raised, the product remains zero, yet spending those operations is still necessary before a positive product can become possible.

**Take the modulus only after optimizing**

After all increments, the solution multiplies heap entries with

`reduce(lambda x, y: x * y % mod, nums)`,

where `mod = 10**9 + 7`. Applying modulo after each multiplication gives the same final remainder as multiplying the full product first, by modular arithmetic.

The heap order is irrelevant to multiplication. Every final factor is present exactly once in `nums`.

Crucially, modulo is not used during greedy comparisons. The problem asks to maximize the true product before taking its remainder. Heap choices depend on actual factor values, not modular products.

**Trace the balancing**

For `nums = [6, 3, 3, 2]` and `k = 2`, heapification exposes two. The first operation changes it to three, leaving values equivalent to `[3, 3, 3, 6]`. The next operation raises any one of the tied threes to four. The product is `6 * 4 * 3 * 3 = 216`.

For `[0, 4]` with five operations, the zero remains the smallest until it has been raised to four. The fifth increment changes one of the tied fours to five, producing factors four and five and product twenty.

**Exact mutation behavior**

`heapify` and `heapreplace` operate in place, so the caller's `nums` list no longer retains its original order or values. The method returns only the product.

The constraints guarantee at least one element, so `nums[0]` and `reduce` without an explicit initializer are safe.

## Complexity detail

Let `n = len(nums)`. `heapify` takes `O(n)` time. Each of `k` replacements costs `O(\log n)`, and the final reduction costs `O(n)`. The tight total is `O(n + k \log n)`; the manifest's `O((n + k) \log n)` is a valid looser upper bound.

The heap reuses the input list. Aside from the input-backed heap, the method uses constant auxiliary space. Counting the heap representation as the algorithm's data structure gives `O(n)` space, as declared by the manifest.

The modulo keeps multiplication intermediates bounded during reduction. Python would handle arbitrary precision regardless.

## Alternatives and edge cases

- **Sort after every increment:** It exposes the minimum but costs `O(k n \log n)` time due to repeated full sorting.
- **Scan for the minimum each time:** This uses constant extra space but costs `O(kn)` time.
- **Sort once and level groups in batches:** A more intricate method can distribute many increments across equal low values without one heap operation per increment, improving some parameter regimes. The heap is direct and fits `k <= 10^5`.
- **Increment a maximum factor:** The pairwise exchange shows this cannot beat incrementing an available smaller factor.
- **Several equal minima:** Incrementing any tied minimum gives an equivalent multiset choice.
- **One element:** Every operation increments it, and the result is its final value modulo the constant.
- **One zero:** Raising it is essential because the entire product is otherwise zero.
- **Several zeros with too few operations:** The maximum product remains zero; using all operations still does not reduce it.
- **`k = 0`:** Although the stated constraint makes `k` positive, the loop would simply skip and return the original product modulo the constant.
- **Modulo ordering:** A numerically larger true product may have a smaller remainder. Optimization must precede modular reporting.
- **Input mutation:** Heap operations change both ordering and values in `nums`; callers needing the original must pass a copy.
- **Nonnegative guarantee:** The smallest-factor proof uses nonnegative factors. With negative values, product signs would make the strategy invalid.
