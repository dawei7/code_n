## General

**The repeated task is “find the maximum, then update it”**

For exactly $k$ seconds, the operation must select a pile with the greatest current number of gifts. After selection, a pile of size $x$ becomes

$$
\left\lfloor\sqrt{x}\right\rfloor.
$$

A simple scan can find the maximum, but repeating an $O(n)$ scan $k$ times costs $O(kn)$. A heap is designed for repeated access to one extreme element. It keeps the maximum available in logarithmic update time without fully sorting all piles after every change.

Python's standard heap is a min-heap: its root is the smallest stored value. The solution negates every pile size and stores `-v`. Among negative numbers, a larger original pile has a smaller, more negative representation. For example, original piles $100$, $25$, and $4$ become $-100$, $-25$, and $-4$, so the root $-100$ corresponds to the richest pile.

**Build the heap once**

The list comprehension `[-v for v in gifts]` creates the negated list `h`. Calling `heapify(h)` rearranges it into heap order in $O(n)$ time. Heap order does not mean the whole list is sorted. It guarantees only that each parent is no greater than its children, which is enough to place the smallest negative value at `h[0]`.

The original `gifts` list is not modified. All changes occur in the separate heap.

**Perform one second with `heapreplace`**

At the beginning of every iteration, `-h[0]` is the largest current pile. The expression `sqrt(-h[0])` computes its nonnegative square root, and `int(...)` removes the fractional part. Because the square root is nonnegative, truncation toward zero is the same as applying floor. The new pile size is negated before storage.

The call

`heapreplace(h, -int(sqrt(-h[0])))`

removes the root and inserts the replacement in one combined heap operation. Afterward, the heap property is restored, so the next iteration again sees a richest current pile at the root.

It is correct to use `heapreplace` rather than separately popping and pushing because the heap is never empty: the constraints guarantee at least one pile, and replacement preserves the heap's size. If several piles tie for maximum, any one may be selected. Their negated values are equal, and choosing any equal root gives the same multiset after replacement.

**Why the simulation matches every required operation**

Before the first iteration, the heap contains exactly one negated entry for every original pile. Assume before some second that it contains exactly the negations of all current pile sizes. Its root represents a maximum pile by the negation ordering. The replacement value is exactly the negative of that pile's required floored square root, while all other entries remain unchanged. Thus the heap contains exactly the new state after that second.

This reasoning repeats for all $k$ iterations. It is a direct induction: the representation is correct initially, and one iteration preserves it. Therefore, after the loop, `h` represents exactly the pile sizes remaining after $k$ required choices.

**Recover the remaining total**

Every heap entry is the negative of a remaining pile. Consequently, `sum(h)` is the negative of the desired total, and `-sum(h)` restores the positive answer. There is no need to pop elements in heap order because summation is independent of order.

For `[25,64,9,4,100]`, the first root represents $100$, which becomes $10$. The next maximum is $64$, which becomes $8$. The next is $25$, which becomes $5$. The current maximum is then $10$, which becomes $3$. The represented final multiset is $[5,8,9,4,3]$, whose sum is $29$.

**Why repeatedly choosing a pile of one is harmless**

When $x=1$, $\lfloor\sqrt{1}\rfloor=1$. If every pile is one, each mandatory operation removes a root value $-1$ and inserts $-1$ again. The state does not change, but the loop still correctly performs all $k$ seconds. No special stopping rule is necessary.

The use of floating-point `sqrt` is safe for the stated bound up to $10^9$: these square roots are far below the precision range where rounding could jump across a distant integer boundary in ordinary double precision. An integer-square-root function would nevertheless express the floor operation even more directly and avoid relying on floating-point behavior.

## Complexity detail

Let $n$ be the number of piles. Creating the negated list takes $O(n)$ time, and bottom-up `heapify` also takes $O(n)$ time. Each of the $k$ calls to `heapreplace` restores heap order along a path of height $O(\log n)$. The final sum scans $n$ entries. Total time is

$$
O(n+k\log n).
$$

The heap contains exactly $n$ integers, so auxiliary space is $O(n)$. The loop itself uses $O(1)$ extra space. The input remains unchanged because the heap is a new list.

## Alternatives and edge cases

- **Repeated linear scan:** Finding the maximum directly in `gifts` each second uses only constant auxiliary space if mutation is allowed, but costs $O(kn)$ time.
- **Keep a sorted list:** The maximum is easy to access, yet reinserting its square root can shift $O(n)$ elements per operation in a Python list.
- **Balanced multiset:** A tree-based multiset can remove the maximum and insert the replacement in $O(\log n)$ time, matching the heap asymptotically but with more machinery.
- **Integer square root:** `math.isqrt` computes the exact floored root with integer arithmetic and avoids any floating-point concern. It is a robust substitute for `int(sqrt(...))`.
- **One pile:** The heap has one entry, and every replacement simply updates that entry. The $O(\log 1)$ structural work is effectively constant.
- **Tied richest piles:** Selecting any tied pile creates the same multiset of values, exactly as the statement permits.
- **Perfect square:** A pile such as $64$ becomes exactly $8$; flooring makes no difference.
- **Non-perfect square:** A pile such as $10$ becomes $3$, not $4$, because the result is floored.
- **All piles equal one:** Operations no longer reduce the total, but they remain valid and the answer stays $n$.
- **Input preservation:** Negating into a new list means callers can safely reuse `gifts` after the function returns.
