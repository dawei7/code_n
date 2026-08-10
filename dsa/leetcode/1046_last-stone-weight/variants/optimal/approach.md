## General

**The operation always needs the two current maximums**

After every smash, a new weight may be inserted. Repeatedly scanning the whole list for the two largest values would redo substantial work.

A priority queue is designed for this pattern: remove the extreme value, update it, and insert a result. Python's `heapq` implements a min-heap, while this problem needs a max-heap. The exact solution stores every weight with its sign negated.

For positive weights, a larger original weight becomes a smaller negative number. For example, weight eight becomes `-8` and weight seven becomes `-7`. The min-heap removes `-8` first, which corresponds to removing original maximum eight.

**Build the heap**

`h = [-x for x in stones]` creates a separate list of negated weights. The original input order and values are not modified.

`heapify(h)` rearranges that list in place into heap order. Heap order does not fully sort the list; it guarantees that `h[0]` is the smallest negative value, representing the largest remaining stone.

Bottom-up heap construction takes linear time.

**Remove the two heaviest stones**

While more than one heap entry remains, the code executes:

`y, x = -heappop(h), -heappop(h)`.

The first pop returns the smallest negative number, which becomes the largest positive weight `y` after negation. The second becomes the next-largest weight `x`. Therefore, `x <= y`, matching the source's notation.

The simultaneous assignment evaluates both right-hand expressions before assigning names, but the pops still occur left to right in Python.

**Represent the smash result correctly**

If `x == y`, both stones are destroyed. The method does not push anything.

If they differ, the remaining stone has positive weight `y - x`. The heap stores negative weights, so it must receive

$$
-(y-x)=x-y.
$$

That is why the code calls `heappush(h, x - y)`. Since `x < y`, this pushed value is negative and correctly represents a positive difference.

Pushing `y - x` directly would be a sign error: a positive number would sit behind all negative entries and no longer behave as a maximum stone.

**Trace the main example**

Start with weights `[2,7,4,1,8,1]`. The heap contains their negatives.

The first two pops recover `y = 8` and `x = 7`. They differ, so `x - y = -1` is pushed, representing new stone one.

The next largest stones are four and two. Push `2 - 4 = -2`, representing stone two.

Next, the largest weights are two and one. Push negative one.

Then two one-weight stones smash equally and both disappear.

One stone of weight one remains, so `-h[0]` returns one.

The heap's internal array order may not resemble a sorted list, but every pair of pops still yields the correct two maxima.

**Why the loop terminates**

Each iteration removes two stones. It pushes at most one result. The number of stones therefore decreases by at least one.

Starting from `N` stones, at most `N - 1` smash iterations occur before the heap has size zero or one. The process exactly mirrors the game's guaranteed termination.

**Why returning the root is enough**

When one heap entry remains, it is trivially the only and therefore heaviest stone. Its stored value is negative, so `-h[0]` restores the positive weight.

When no entries remain, all stones were destroyed in equal pairs and the required answer is zero. The conditional expression `0 if not h else -h[0]` handles both outcomes without popping the final element.


At the start of every loop iteration, `h` contains exactly one negated entry for each currently existing stone and satisfies min-heap order.

The two pops select precisely the two largest current weights. Equal weights add no entry, while unequal weights add the negation of their required difference. `heappush` restores heap order.

Thus the invariant holds after every smash. When fewer than two entries remain, the game has ended, and the return expression gives exactly the remaining weight or zero.

**Why sorting once is not enough**

An initial sort makes the first two maximums easy to remove, but a difference stone can belong anywhere in the remaining order. Inserting it into a Python list while preserving sorted order can shift `O(N)` elements.

A heap keeps only partial order, which is enough to find maxima and allows both removal and insertion in logarithmic time.

## Complexity detail

Let `N = len(stones)`. Negating values takes `O(N)` time, and `heapify` takes `O(N)` time.

There are at most `N - 1` iterations. Each performs two `O(\log N)` pops and at most one `O(\log N)` push. Total time is `O(N \log N)`, matching the manifest.

The heap list stores up to `N` integers and uses `O(N)` space. All other variables are scalar. The separate heap also preserves the input list, so total auxiliary space is `O(N)`, matching the manifest.

## Alternatives and edge cases

- **Scan for two maximums each turn:** It avoids a heap but costs `O(N)` per smash and `O(N^2)` total time.
- **Maintain a sorted list:** Maximum removal is constant time at the end, but inserting each difference can shift linearly many entries, retaining quadratic worst-case time.
- **Re-sort after every smash:** This is even more expensive, up to `O(N^2 \log N)`.
- **Bucket counts by weight:** With maximum weight `W`, frequency buckets can run in `O(N + W)` time and `O(W)` space. It is useful only because weights are bounded and is pseudo-polynomial in `W`.
- **Custom max-heap:** It removes the negation trick but requires more implementation code. Python's standard min-heap plus negative values is simpler.
- **Single stone:** The loop never runs, and negating `h[0]` returns its original weight.
- **Two equal stones:** Both are popped, nothing is pushed, and the result is zero.
- **Two unequal stones:** Their difference is pushed as one negative entry and returned as the final positive weight.
- **Many equal maximums:** Each pair is destroyed correctly; heap ordering among equal entries is irrelevant.
- **New difference becomes the maximum:** `heappush` places it appropriately, and it can be selected on the next iteration.
- **Sign discipline:** Heap entries are always negative. `x - y` is the correct stored representation because `y >= x`.
- **Input preservation:** The comprehension builds `h` rather than negating `stones` in place, so callers retain their original list.
- **Positive-weight contract:** Every original stone is positive, and unequal smashes produce a strictly positive difference.
