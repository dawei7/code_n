## General

**Separate customers who are always satisfied from customers the technique can rescue**

At each minute, `customers[i]` tells us how many customers arrive, while `grumpy[i]` tells us whether those customers are normally unsatisfied. A value of zero means the owner is not grumpy, so those customers are already satisfied. A value of one means the owner is grumpy, so those customers can become satisfied only if that minute lies inside the one chosen technique window.

This creates two non-overlapping parts of the final answer:

1. A fixed baseline containing every customer who arrives during a naturally non-grumpy minute.
2. An extra gain containing normally unsatisfied customers rescued by the best consecutive window of length `minutes`.

The baseline is independent of where the technique is used. The only decision is which fixed-length window produces the largest extra gain. Once the problem is split this way, it becomes a standard sliding-window maximum.

For a grumpy minute, the product `customers[i] * grumpy[i]` equals `customers[i]` because the flag is one. For a non-grumpy minute, the same product is zero. This product therefore measures the number of normally unsatisfied customers at one minute. Summing it over a candidate window gives exactly the customers that the technique would newly satisfy there.

It is important that the window gain excludes already satisfied customers. Including them would not change which customers remain satisfied, and adding them again to the baseline would double-count them.

**Measure the first complete window**

The exact solution begins with:

```python
mx = cnt = sum(c * g for c, g in zip(customers[:minutes], grumpy))
```

The slice `customers[:minutes]` contains the customer counts for indices zero through `minutes - 1`. The second input to `zip` is the complete `grumpy` list, but `zip` stops as soon as the shorter input ends. Consequently, the generator processes exactly the first `minutes` pairs.

Each product `c * g` contributes customers only when the corresponding minute is grumpy. Their sum is the recoverable gain of the first legal window.

Both `cnt` and `mx` receive that value. They have different roles:

- `cnt` is the gain of the window currently being examined.
- `mx` is the greatest gain seen among all complete windows examined so far.

The constraints guarantee `1 <= minutes <= len(customers)`, so the first window always exists and is complete. There is no need for a special empty-window value.

**Slide by changing only the two boundary contributions**

After measuring indices zero through `minutes - 1`, the loop lets `i` range from `minutes` through the final index:

```python
for i in range(minutes, len(customers)):
    cnt += customers[i] * grumpy[i]
    cnt -= customers[i - minutes] * grumpy[i - minutes]
    mx = max(mx, cnt)
```

Before one iteration, `cnt` represents the previous length-`minutes` window. Moving that window one step right introduces minute `i` and removes minute `i - minutes`.

The first update adds the normally unsatisfied customers at the entering right endpoint. The second update removes the normally unsatisfied customers at the departing left endpoint. Every minute strictly between those endpoints remains in the window, so its contribution must remain unchanged.

After both updates, `cnt` is exactly the gain for indices `i - minutes + 1` through `i`. The assignment `mx = max(mx, cnt)` preserves the greatest gain found so far.

This is why the algorithm does not recompute every window from scratch. A direct sum for each of roughly `N` windows would inspect up to `minutes` elements each time. The sliding update does constant work per new window by reusing the previous sum.

Consider a departing minute where `grumpy[i - minutes]` is zero. Its product is zero, so subtracting it changes nothing. That is correct because naturally satisfied customers were never part of the recoverable gain. The same reasoning applies when an entering minute is non-grumpy.

**Compute the fixed baseline**

The final expression includes:

```python
sum(c * (g ^ 1) for c, g in zip(customers, grumpy))
```

The problem guarantees that every `g` is either zero or one. XOR with one flips those two values:

- `0 ^ 1` becomes one.
- `1 ^ 1` becomes zero.

Therefore `c * (g ^ 1)` contributes `c` during a naturally non-grumpy minute and zero during a grumpy minute. Summing all pairs produces the number of customers satisfied even without the technique.

This use of XOR is valid specifically because `grumpy` is binary. The more descriptive arithmetic form `1 - g` would produce the same result under the same constraint.

The two input arrays have equal length, so `zip(customers, grumpy)` visits every minute exactly once and truncates neither array.

**Combine the disjoint contributions**

The return value is the natural baseline plus `mx`, the largest recoverable window gain:

```python
return sum(c * (g ^ 1) for c, g in zip(customers, grumpy)) + mx
```

There is no overlap between these terms. A customer counted in the baseline arrived when `g` was zero. A customer counted in a window gain arrived when `g` was one. Thus every satisfied customer in the chosen schedule is counted exactly once.

**Why the selected window is optimal**

Every legal use of the technique is one consecutive block of exactly `minutes` minutes. For any fixed block, its only improvement over normal operation is to satisfy customers at grumpy minutes inside that block. Its improvement is therefore exactly the window sum maintained in `cnt`.

The initialization evaluates the first legal block. Each loop iteration moves to the next block, so every possible starting position is evaluated exactly once. `mx` is initialized from the first block and updated with the maximum after every later block. It therefore equals the greatest improvement attainable by any legal placement.

The baseline is the same for every placement. Adding the largest possible improvement to that fixed baseline must produce the maximum possible total satisfaction.

## Complexity detail

Let `N` be the number of minutes and let `M` be `minutes`.

The initial window sum processes `M` entries. The sliding loop processes `N - M` entries, and the baseline sum processes `N` entries. These terms add to linear time, so the exact implementation takes `O(N)` time.

The sliding-window state itself consists only of `cnt`, `mx`, the loop index, and generator state. Algorithmically, this is `O(1)` extra state, which is the space target recorded in the manifest.

There is, however, a Python-specific allocation in the exact source: `customers[:minutes]` creates a new list containing `M` references. That makes the exact implementation's peak auxiliary space `O(M)` rather than strict `O(1)`. The generator does not create another list, and the slice becomes disposable after the initial sum, but it still exists temporarily.

The strict manifest bound can be achieved without changing the algorithm. Initialize `cnt` with an index-based loop over `range(minutes)`, or use an iterator view that does not copy the prefix. Then only a constant number of numeric variables is stored, giving `O(1)` auxiliary space.

No output-sized structure is required because the function returns a single integer.

## Alternatives and edge cases

- **Strict constant-space initialization:** Replace the prefix slice with an indexed sum over the first `M` positions. This preserves the exact `O(N)` sliding-window algorithm while making the manifest's `O(1)` auxiliary-space claim literal for the implementation.
- **Modify a copy of customer contributions:** One can zero out naturally satisfied minutes in a separate array and slide over the result. The logic is valid but requires `O(N)` extra space that the products already avoid.
- **Prefix sums:** Build a prefix sum of normally unsatisfied customers, then evaluate each window by subtracting two prefix values. This also takes `O(N)` time, but the prefix array uses `O(N)` space instead of constant sliding state.
- **Recompute every window:** Summing each length-`M` block independently takes `O(NM)` time in the worst case. It repeats almost all work between overlapping windows and is unnecessary.
- **Technique spans the full day:** When `minutes == N`, initialization measures the only legal window and the sliding loop is empty. The result includes every customer, because all grumpy minutes are rescued and all non-grumpy minutes remain in the baseline.
- **Technique length one:** Each candidate window contains one minute. `mx` becomes the largest customer count among grumpy minutes, or zero when every minute is already non-grumpy.
- **Owner is never grumpy:** Every window gain is zero. The baseline contains all customers, so the technique adds nothing and the full customer total is returned.
- **Owner is always grumpy:** The baseline is zero. The answer is the largest sum of any consecutive `minutes` customer counts.
- **Zero-customer minutes:** Such a minute contributes zero regardless of the grumpy flag. It can enter or leave the window without changing `cnt`.
- **Several equally good windows:** Only the maximum number of satisfied customers is requested, not the chosen start index. Keeping the first maximum or a later equal maximum produces the same returned value.
- **Binary-flag requirement:** The XOR expression relies on `grumpy[i]` being exactly zero or one. For arbitrary truthy integers, `g ^ 1` would not mean logical negation.
- **Input preservation:** The function reads both input lists and does not modify them. The temporary prefix slice is a separate list.
