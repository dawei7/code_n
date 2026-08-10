## General

**Maintain the fully merged result of the processed prefix**

The operation always chooses the leftmost equal adjacent pair. A stack can simulate this rule online because, before a new input value arrives, the processed prefix can be kept in its fully reduced final form.

The stack invariant is:

> After processing the first `i` original elements, `stk` equals the result of repeatedly applying the required leftmost merge rule to exactly that prefix, and no adjacent stack values are equal.

The stack begins empty, which is the correct reduced result for an empty prefix.

**Append one value and inspect only the new boundary**

When the next original value `x` is appended, the old stack had no equal adjacent pair. Therefore every adjacency wholly inside the old stack remains ineligible. The only pair that can become equal is the new final pair:

`stk[-2], stk[-1]`.

If those values differ, the extended stack is already fully reduced.

If they are equal, that final pair is not merely an eligible pair; it is the only eligible pair. It is therefore also the leftmost eligible pair demanded by the rules. The source merges it.

**A merge may cascade left**

Replacing two equal values `v, v` by their sum `2v` can make the new final value equal to the preceding stack value. That creates another eligible pair, so one comparison is not enough.

The source uses:

`while len(stk) > 1 and stk[-1] == stk[-2]`.

Inside the loop:

`stk.append(stk.pop() + stk.pop())`

removes the final two equal values, adds them, and appends their merged sum.

After each merge, the portion before the newly appended sum was already reduced. Again, the only possible new equality is at the final boundary, so repeating the same check performs the complete forced cascade.

For `[3,1,1,2]`:

- 3 and then 1 append without a merge;
- the second 1 matches the top, producing 2, so the reduced prefix becomes `[3,2]`;
- the final input 2 matches that merged 2, producing 4;
- the result is `[3,4]`.

The second merge did not correspond to two adjacent equal values in the original input, but it is required after the first merge changes the current array.

**Why the stack respects the global leftmost rule**

The concern with an online stack is whether merging at the right edge could happen before an eligible pair farther left. The invariant prevents that problem.

Before appending `x`, no adjacent pair in `stk` is equal. Appending changes no old adjacency and creates only one new adjacency at the right edge. If it is equal, no earlier eligible pair exists.

After merging that pair, all old adjacencies except the one touching the merged sum are still unchanged and unequal. Once again, any eligible pair must be the new final pair.

Thus every merge performed by the stack is exactly the leftmost merge in the current processed array. Once the cascade stops, the entire prefix is fully reduced and the invariant is restored for the next input value.

**Why processing a prefix early cannot conflict with future input**

Future values are appended only to the right. They cannot create a new equality between two existing interior stack values, because those values and their adjacency do not change.

The only interaction with future input occurs through the current stack top. Keeping the reduced prefix therefore loses no information needed for later merges. The stack contains precisely the surviving current array values for that prefix.

**Amortized linear behavior**

The nested `while` might appear capable of many operations per input value. However, each original value is pushed once. Every successful merge decreases stack length by one: it pops two existing entries and pushes one replacement.

Across an input of length $N$, there can be at most $N-1$ merges because the current array cannot shrink below one element. Each stack entry is removed only as part of such a merge. The total amount of loop work is linear, even though a single arrival can trigger a long cascade.

For example, a carefully formed prefix may collapse several times when one final value arrives, but those collapses consume entries that can never be consumed again.

**The returned stack is already final**

After the last input value and its cascade, the invariant says `stk` contains no equal adjacent pair. No operation remains possible, so returning the stack directly gives the required final array.

The input `nums` is not modified. Merged values live only in `stk` and may exceed the original element bound; Python integer addition handles them exactly.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each original value is appended once, and each merge reduces stack size by one. There are at most $N-1$ merges, so total time is $O(N)$.

The stack can hold all $N$ values when no pair ever merges, giving $O(N)$ auxiliary space. The returned stack is also the output object.

A literal list simulation that searches from the beginning after every merge can shift elements repeatedly and become quadratic. End-stack operations avoid those shifts while the invariant preserves the leftmost semantics.

## Alternatives and edge cases

- **Literal repeated list scan:** Find the first equal pair, replace it, and restart. This directly follows the statement but may cost $O(N^2)$ because of repeated scanning and middle deletion.
- **Linked list plus eligible-pair tracking:** It can support local merges without shifts, but maintaining the globally leftmost eligible pair is substantially more complex than the prefix stack.
- **Recursive cascade:** A helper can merge the top recursively after each append. It has the same logic but risks recursion depth and is less direct than the loop.
- **No equal neighbors:** Every value remains on the stack and the original array is returned unchanged in content.
- **Complete collapse:** Cascading merges may reduce the whole array to one value, as with `[2,2,4]`.
- **Three equal values:** The first two merge to `2v`, which is not equal to the remaining `v`, so the result is `[2v,v]`; merges are pairwise and order-sensitive.
- **Long cascades:** One appended value may trigger several merges, but total merges remain at most $N-1$.
- **One element:** It is appended once, the while condition fails, and it is returned unchanged.
- **Merged values beyond the input bound:** The contract allows them, and no fixed-size value table is used.
- **Leftmost requirement:** The stack is valid specifically because every processed prefix is fully reduced before the next value arrives, leaving only the newest boundary eligible.
