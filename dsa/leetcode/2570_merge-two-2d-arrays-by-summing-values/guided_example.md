# Guided Example: Merge Two 2D Arrays by Summing Values

## 1. What the merged array must be

Each input is a list of records `[id, val]`, the ids inside one list are unique, and each list is already in strictly ascending id order. The task is to build a single list in ascending id order that contains every id occurring in at least one input exactly once, whose value is the sum of that id's values across the two inputs, substituting `0` for an input that does not mention the id.

Writing $v_1(k)$ and $v_2(k)$ for the value attached to id $k$ in `nums1` and `nums2`, with the convention that a missing id contributes $0$, the required output is the sequence

$$\bigl[\,k,\; v_1(k) + v_2(k)\,\bigr] \quad \text{for every } k \in \operatorname{keys}(\texttt{nums1}) \cup \operatorname{keys}(\texttt{nums2}),$$

presented in increasing order of $k$. Nothing else about the records matters: a value contributes to its own id and to no other, and an id that occurs in only one input keeps that single value rather than being doubled or dropped.

For the instance we trace, `nums1 = [[1,2],[2,3],[4,5]]` and `nums2 = [[1,4],[3,2],[4,1]]`, the contribution view is:

| id $k$ | Value from `nums1` | Value from `nums2` | Sum | Present in which input |
|---|---|---|---|---|
| 1 | 2 | 4 | 6 | both |
| 2 | 3 | absent, so 0 | 3 | `nums1` only |
| 3 | absent, so 0 | 2 | 2 | `nums2` only |
| 4 | 5 | 1 | 6 | both |

So the answer must be `[[1,6],[2,3],[3,2],[4,6]]`, which is exactly the authored expectation for this input. The interesting part is producing that sequence in order without ever building a lookup structure, because the inputs are handed to us already sorted.

## 2. The merge invariant

Keep one read cursor per input: $i$ indexes the next unread record of `nums1`, $j$ the next unread record of `nums2`. Both cursors start at $0$. The invariant maintained before every step is:

> every id smaller than $\min(\texttt{nums1}[i].id,\ \texttt{nums2}[j].id)$ has already been emitted exactly once with its complete sum, the emitted prefix is strictly increasing in id, and no record before either cursor still needs to be read.

The invariant tells us which id is next in the output: it must be the smaller of the two ids currently under the cursors, because that id is the smallest key not yet accounted for. Three cases arise, and each advances at least one cursor:

- **The two head ids are equal.** Both inputs hold a contribution for this id, so emit one record with the added values and advance both cursors — the id is finished and must never be emitted again.
- **The head of `nums1` is smaller.** `nums2` has no record for this id at all: its ascending order means every later record in `nums2` also has a larger id, and any earlier one was already consumed. Emit the record unchanged and advance $i$.
- **The head of `nums2` is smaller.** Symmetrically, emit that record unchanged and advance $j$.

## 3. Step-by-step trace of the chosen instance

`nums1 = [[1,2],[2,3],[4,5]]` has length 3, `nums2 = [[1,4],[3,2],[4,1]]` has length 3.

| Step | `i` | `j` | `nums1[i]` | `nums2[j]` | Comparison | Emitted | Cursors after |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | `[1,2]` | `[1,4]` | ids equal | `[1, 2+4] = [1,6]` | both advance: `i=1`, `j=1` |
| 2 | 1 | 1 | `[2,3]` | `[3,2]` | $2 < 3$ | `[2,3]`, copied unchanged | `i=2`, `j=1` |
| 3 | 2 | 1 | `[4,5]` | `[3,2]` | $4 > 3$ | `[3,2]`, copied unchanged | `i=2`, `j=2` |
| 4 | 2 | 2 | `[4,5]` | `[4,1]` | ids equal | `[4, 5+1] = [4,6]` | both advance: `i=3`, `j=3` |
| 5 | 3 | 3 | past the end | past the end | both exhausted | — | stop |

The emitted prefix after each step is `[1,6]`, then `[[1,6],[2,3]]`, then `[[1,6],[2,3],[3,2]]`, then `[[1,6],[2,3],[3,2],[4,6]]`. Two properties are visible in the table and are worth naming:

- **The emitted ids strictly increase** — $1 < 2 < 3 < 4$ — because each step emits the smallest id not yet accounted for and then permanently retires it.
- **Each input's cursor never moves backward and never skips a record.** Every record of both inputs is read exactly once, either into a summed record or into a copied record.

Both arrays happened to be exhausted at the same moment here. That is convenient, not structural; the next section handles the general case.

## 4. When one input runs out first

If the cursor of one input reaches its end while the other still has records, the surviving records cannot match anything: the exhausted input has no remaining id, and every later record of the live input has an id larger than every id emitted so far. They are therefore appended verbatim, in their existing order, with their values untouched. Two authored cases isolate exactly this branch:

| `nums1` | `nums2` | Merge behaviour | Output |
|---|---|---|---|
| `[[1,4],[2,5]]` | `[[3,6],[4,7],[5,8]]` | emit `[1,4]`, emit `[2,5]`, then the first cursor is exhausted | append `nums2` unchanged: `[[1,4],[2,5],[3,6],[4,7],[5,8]]` |
| `[[3,6],[4,7],[5,8]]` | `[[1,4],[2,5]]` | emit `[1,4]`, emit `[2,5]`, then the second cursor is exhausted | append `nums1` unchanged: `[[1,4],[2,5],[3,6],[4,7],[5,8]]` |

The two outputs coincide, which is the point: the merge result depends on the union of the key sets and their sums, not on which input carries the tail. Note also that no addition happens in the tail — an id present in only one input keeps its single value, and the missing input contributes the additive identity $0$.

## 5. Why the output is complete, sorted and duplicate-free

- **Completeness.** Every record of `nums1` is either matched with an equal id in `nums2` and summed, or copied when `nums2` can no longer contain that id. The same holds symmetrically for `nums2`. Hence every id of the union appears, and each of its two possible contributions is used exactly once.
- **Uniqueness.** An id is emitted only when it becomes the smaller head. If both heads carry it, one emission consumes both records at once; if only one carries it, the other input's ascending order guarantees that its copy, if any, would already have been consumed. An emitted id can therefore never be emitted again.
- **Order.** The sequence of emitted ids is non-decreasing because each emission takes the minimum of two heads whose values only increase over time. Combined with uniqueness, the sequence is strictly increasing, which is precisely "sorted in ascending order by id".
- **No lost values.** Values are added only in the equal-head case, where both contributions belong to the same id. In the other two cases the surviving value is copied, so no contribution is silently dropped and none is counted twice.

The invariant of Section 2 is re-established after each step: the emitted id was the minimum of the two frontier ids, so the set of ids strictly below the new frontier minimum is exactly the emitted set, and the prefix remains increasing.

## 6. Alternatives and what they cost

| Method | Idea | Time | Auxiliary space | Tradeoff |
|---|---|---|---|---|
| Two-pointer merge (used above) | walk both sorted arrays, compare heads | $O(m+n)$ | $O(1)$ beyond the output | exploits the given order; needs careful handling of the equal case and the tail |
| Dictionary of id to summed value, then sort the keys | accumulate every record into a map, sort its keys | $O((m+n)\log(m+n))$ | $O(m+n)$ | simpler bookkeeping but discards the sortedness that is handed to us for free |
| Concatenate and group after a global sort | sort all $m+n$ records by id, then fold equal ids | $O((m+n)\log(m+n))$ | $O(m+n)$ | loses the per-input uniqueness that makes the merge trivial |
| Merge with binary search per record | for each record, search the other array for its id | $O(m\log n + n\log m)$ | $O(1)$ | worse than the linear walk and does not simplify the equal case |

The two-pointer walk wins because the input order already encodes exactly the information the output needs. The dictionary alternative is the one the app-local reference uses; it is correct but pays a logarithmic factor that the sorted inputs make unnecessary.

## 7. Traps this instance exposes

| Tempting reasoning | Where it breaks | Correct view |
|---|---|---|
| "On equal ids, advance only one cursor." | step 4 of the trace would emit `[4,6]` and then emit `[4,1]` again | advance **both** cursors; the id is finished once it is emitted |
| "Ids that appear in one input only should be copied twice." | id 2 appears once and its value is `3`, not `6` | a missing contribution is $0$, so the value is unchanged, not doubled |
| "The two inputs always have the same length." | the tail cases have lengths 2 and 3 | exhaustion is per input; append the remaining records of whichever input still has them |
| "Output values stay within the value bound." | `[[1000,1000]]` and `[[1000,1000]]` merge to `[1000,2000]` | the bound $1 \le \text{val} \le 1000$ applies to input values; a summed value may reach $2000$ |
| "The equal case needs a special lookup of the other array." | — | one comparison of the two heads decides it; the arrays are already sorted |
| "Sorting the merged result is required at the end." | — | the merge emits ids in increasing order, so no final sort is needed |
| "Values from the two arrays should overwrite one another." | id 1 would become `4` instead of `6` | the contract is summation, for every id of the union |

## 8. Time and auxiliary space

Let $m = \texttt{nums1.length}$ and $n = \texttt{nums2.length}$.

- **Time** $O(m+n)$: each step of the loop advances $i$, $j$, or both, and no cursor ever moves backward. There are at most $m+n$ steps before both cursors reach the ends of their arrays, and each step performs one id comparison and at most one addition.
- **Auxiliary space** $O(1)$ beyond the returned list: the two cursors and a handful of scalars are the entire working state. The returned list holds at most $m+n$ records, which is output rather than auxiliary storage.

The bound matches the information-theoretic minimum for reading both inputs once, and it is exactly the gain that the pre-sorted inputs, per-array unique ids, and the ascending-order requirement make available.
