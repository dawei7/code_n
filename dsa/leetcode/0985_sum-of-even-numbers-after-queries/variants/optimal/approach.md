## General

**Maintain the answer instead of recomputing it**

After every query, the requested value is the sum of all even elements currently in `nums`. A straightforward solution could scan the complete array after each update. That repeats almost all work, because one query changes exactly one position and every other contribution stays the same.

The optimal idea is to maintain a running sum `s`. Before processing queries, the generator

`sum(x for x in nums if x % 2 == 0)`

computes the even-element sum once. From then on, a query repairs only the contribution of the modified index.

**The invariant carried between queries**

Immediately before and immediately after every query, `s` equals

> the sum of precisely those current elements of `nums` that are even.

This statement is stronger than merely saying `s` was correct initially. It explains why the same constant-time update can be repeated for thousands of queries, including many updates to the same index.

Suppose a query is `[v, i]`. Only `nums[i]` changes. All other values retain both their numeric values and their parity, so their combined contribution to `s` must remain untouched. The code removes the old contribution at index `i`, changes the number, and adds its new contribution.

**Remove the old value only when it currently contributes**

Before mutation, the code checks

`if nums[i] % 2 == 0:`

and subtracts `nums[i]` from `s` when the value is even. If the old value is odd, it contributes nothing to the even sum, so there is nothing to subtract.

This removal must occur before `nums[i] += v`. After mutation, the old value is no longer available at that index, and checking its old parity would require storing an extra variable. The chosen ordering keeps the logic direct.

Subtracting a negative even value is also correct. For example, if the running sum includes `-4`, removing that contribution performs `s -= -4`, which increases `s` by four. That is exactly what happens to a sum when a negative term is deleted.

**Apply the query and add the new contribution**

The assignment

`nums[i] += v`

implements the required update in place. The code then checks the updated value. If it is even, `s += nums[i]` inserts its complete new contribution. If it is odd, nothing is added.

This remove–change–add order handles all four parity transitions:

- **even to even:** remove the old even value and add the new even value;
- **even to odd:** remove the old value and add nothing;
- **odd to even:** remove nothing and add the new value;
- **odd to odd:** neither version contributes, so `s` does not change.

There is no need to determine whether `v` itself is odd or even. Testing the old and new array values directly covers every transition and is harder to get wrong.

**Record the answer after the mutation**

Each query asks for the even sum after its addition has been applied. Therefore, `ans.append(s)` appears after both the array update and the possible reinsertion into `s`.

The order of answers matches the order of queries because one value is appended during each loop iteration. Later queries operate on the already-mutated `nums`, as required; the updates are cumulative rather than independent.

**Trace the sample**

Start with `nums = [1, 2, 3, 4]`. The initial even values are two and four, so `s = 6`.

- Query `[1, 0]` changes one to two. The old one is odd, so nothing is removed. The new two is even, so add two. Now `s = 8` and append eight.
- Query `[-3, 1]` changes two to negative one. Remove the old two, obtaining six; the new value is odd, so add nothing. Append six.
- Query `[-4, 0]` changes two to negative two. Remove the old two, obtaining four, then add the new even value `-2`, obtaining two. Append two.
- Query `[2, 3]` changes four to six. Remove four from the running sum, obtaining negative two, and then add six, obtaining four. Append four.

The produced list is `[8, 6, 2, 4]`, and the trace shows that negative even elements are included with their actual negative value.

**Why the running sum remains exact**

Assume `s` is correct before a query. Split the correct sum into the possible contribution of index `i` and the contributions of every other index. The first conditional removes the index-`i` contribution exactly when it exists, leaving the sum of even values at all unchanged positions.

The assignment changes only `nums[i]`. The second conditional adds exactly the updated value if it is even, which is precisely its new contribution. Thus `s` becomes the correct even-element sum for the updated array. Since the initialization is correct, induction over the query sequence proves that every appended result is correct.

**Parity in Python**

The test `x % 2 == 0` works for positive numbers, negative numbers, and zero. Negative even integers still have remainder zero in Python, while zero is even and contributes zero. The same expression can therefore be used consistently without special cases.

**Why mutating `nums` is necessary for this implementation**

Future queries refer to the current array after all previous changes. Updating `nums[i]` in place preserves that evolving state. A separate map of changes could avoid mutation, but it would duplicate storage and complicate each lookup without improving the asymptotic bound.

## Complexity detail

Let `N` be the length of `nums` and `Q` the number of queries. Computing the initial even sum scans `N` values once, taking `O(N)` time. Every query performs a constant number of arithmetic operations, parity tests, one array update, and one append, so all queries take `O(Q)` time. Total time is `O(N + Q)`.

The returned `ans` list contains exactly `Q` integers, requiring `O(Q)` space. Apart from that required output, the method stores only `s`, the current query values, and loop bookkeeping, so auxiliary working space is `O(1)`. The input array is modified in place and does not require a copy.

The time bound is optimal up to constants because the algorithm must inspect the initial array to know its starting even sum and must produce one answer for each query.

## Alternatives and edge cases

- **Rescan after every query:** Update the index and sum all even values from scratch. It is easy to understand but costs `O(NQ)` time.
- **Segment tree:** Maintain a tree of even contributions with point updates and a root sum. It supports each update in `O(\log N)` but is unnecessary because the required aggregate can be repaired in constant time.
- **Track only parity changes:** One can derive cases from the parity of `v`, but the running sum still needs the old and new numeric values. Direct removal and addition is clearer.
- **Negative even values:** They contribute negatively to `s`. Subtracting the old negative value and adding the new negative value follow normal arithmetic.
- **Zero:** Zero passes the even test but changes the sum by zero, so no special handling is needed.
- **Repeated queries at one index:** Every iteration reads the current mutated value, removes its current contribution, and applies the next update correctly.
- **An update value of zero:** The old contribution is removed and then the identical new contribution is restored when even; the reported sum remains unchanged.
- **Odd-to-odd update:** Both conditionals skip the value, leaving `s` unchanged even though the stored number changes.
- **Single-element array:** The invariant reduces to whether that one current value is even, and the same code produces one answer per query.
- **Input mutation:** Callers that need the original `nums` afterward would have to pass a copy. The solution itself intentionally preserves the required cumulative query state in the given list.
