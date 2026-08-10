## General

The desired output represents a set of inclusive integer points:

$$
\left(\bigcup \text{occupied intervals}\right)
\setminus
[freeStart,freeEnd].
$$

The source computes this in two clean stages:

1. sort and merge all overlapping or touching occupied intervals;
2. subtract the one free interval from each merged component.

Merging first is important. It turns an arbitrary overlapping input into disjoint maximal components, so subtraction can be reasoned about one component at a time and the output naturally uses the minimum number of intervals.

**Sorting establishes left-to-right order**

The source sorts `occupiedIntervals` by each interval's start. Afterward, when interval `[a,b]` is processed, every interval already in `busy` begins no later than `a`.

The first sorted interval initializes `busy`. Each later interval needs to be compared only with the last merged interval because earlier merged components end even farther left.

**Why touching intervals must merge**

Let the last merged component be `[s,e]` and the next sorted interval be `[a,b]`.

For inclusive integer intervals, they are truly separated only when at least one unoccupied integer lies between them. The first integer after `e` is `e+1`, so a gap exists exactly when

$$
e+1<a.
$$

That is the source's condition:

```python
if busy[-1][1] + 1 < interval[0]:
    busy.append(interval)
```

If this inequality is false, the intervals overlap or touch. Their union is one continuous integer interval beginning at `s` and ending at `\max(e,b)`. The source extends the existing endpoint accordingly.

Examples clarify the `+1`:

- `[1,3]` and `[4,7]` touch because four is immediately after three, so they merge to `[1,7]`;
- `[1,3]` and `[5,7]` leave integer four uncovered, so they remain separate.

After the loop, `busy` is sorted, non-overlapping, non-touching, and maximal. No two entries can be combined without incorrectly adding an unoccupied point.

**Subtracting the free interval**

Take one merged occupied interval `[s,e]`. There are two broad cases.

If it is entirely outside the free interval, meaning

$$
e<freeStart
\quad\text{or}\quad
freeEnd<s,
$$

no occupied point is removed. The entire interval is appended to the answer.

Otherwise the intervals overlap. Removing all points from `[freeStart,freeEnd]` can leave up to two pieces:

- a left piece `[s,freeStart-1]` when `s<freeStart`;
- a right piece `[freeEnd+1,e]` when `e>freeEnd`.

The strict comparisons ensure that an emitted piece is nonempty. If `s=freeStart`, there is no point before the free interval inside this component. If `e=freeEnd`, there is no point after it.

The source expresses those two pieces directly:

```python
if interval[0] < freeStart:
    ans.append([interval[0], freeStart - 1])
if interval[1] > freeEnd:
    ans.append([freeEnd + 1, interval[1]])
```

The `-1` and `+1` are required because endpoints are inclusive. The free endpoints themselves must not remain occupied.

**Why the result is sorted and minimal**

The merged components are processed in increasing order. Any surviving left piece precedes its right piece, and every piece from one component precedes pieces from later components. The result is therefore sorted.

Two original merged components were separated by at least one unoccupied integer. Removing more points cannot make them touch. Within one component, if subtraction creates two pieces, the nonempty free interval separates them. Therefore no two returned intervals overlap or touch.

Each returned interval is a maximal consecutive run of remaining occupied integer points. Encoding each such run as one interval is exactly the minimum possible interval count.

**A complete overlap example**

Suppose merging produces `[2,12]` and the free interval is `[7,9]`. The occupied points before seven remain as `[2,6]`, and those after nine remain as `[10,12]`. Points seven, eight, and nine are removed.

If the free interval instead covers `[1,20]`, neither strict side condition succeeds and the component disappears completely.

**The stored source is missing `List`**

The exact method annotations use `List[List[int]]` and `List[int]`, but the file does not import or define `List`. Under ordinary Python annotation evaluation, loading the module raises:

```text
NameError: name 'List' is not defined
```

Supplying `List` from `typing` is sufficient to expose the intended merge-and-subtract algorithm, which matches the set semantics above. The missing name is a genuine source defect and cannot be silently treated as present.

**The source mutates and aliases input data**

`occupiedIntervals.sort(...)` reorders the caller's outer list in place.

Furthermore, `busy` stores references to the original inner interval lists. When overlapping intervals merge, this assignment:

```python
busy[-1][1] = max(busy[-1][1], interval[1])
```

changes the endpoint of an inner list belonging to the caller's input. Unchanged components appended to `ans` are also the same list objects, while pieces created by subtraction are new lists.

These side effects do not change the computed interval values, but callers can observe both reordering and endpoint mutation after a successful execution.

## Complexity detail

Let `n` be the number of occupied intervals. Sorting dominates with `O(n\log n)` time. The merge scan and subtraction scan are each linear, so total time is `O(n\log n)`.

The `busy` list can contain `O(n)` interval references, and `ans` can contain `O(n)` output intervals. The slice `occupiedIntervals[1:]` also creates a shallow list of `O(n)` references. Python's sorting implementation may use `O(n)` temporary workspace. Total auxiliary and output-related storage is `O(n)`.

As stored, module loading fails before these bounds describe a completed call because `List` is unresolved. The bounds apply to the represented algorithm after that standard name is supplied.

The method does not enumerate integer points, so interval endpoints as large as `10^9` do not affect runtime beyond constant-size arithmetic.

## Alternatives and edge cases

- **Enumerate every occupied integer:** Endpoint values can span up to `10^9`, so point-by-point sets are infeasible. Interval arithmetic depends only on the number of intervals.

- **Subtract before merging:** This can produce overlapping or touching fragments from different inputs and requires another merge anyway. Merging first yields canonical components.

- **Merge overlaps but not touching intervals:** That would return more intervals than necessary under the problem's integer-touch definition. The `end+1` comparison is essential.

- **Use `end < start` as the separation test:** This treats `[1,1]` and `[2,2]` as separate even though they touch and must merge.

- **Free interval completely outside:** The occupied component is appended unchanged.

- **Free interval completely covers a component:** Neither side fragment exists, so nothing is appended.

- **Free interval strictly inside a component:** Exactly two nonempty pieces are emitted.

- **Overlap only at `freeStart`:** The left result ends at `freeStart-1`, removing the shared endpoint.

- **Overlap only at `freeEnd`:** The right result begins at `freeEnd+1`.

- **Equal starts:** Sorting by start alone is sufficient. Whichever equal-start interval appears first, repeated endpoint maxima produce the same merged component.

- **Duplicate intervals:** They merge into one component and do not duplicate occupied points.

- **One occupied interval:** The same outside, covered, clipped, or split cases apply without special handling.

- **No remaining points:** `ans` stays empty and the source returns an empty list.

- **Missing `List`:** The file cannot normally define its annotated method until `typing.List` is provided.

- **Outer-list mutation:** Sorting permanently changes the order of `occupiedIntervals`.

- **Inner-list mutation and output aliasing:** Merging can overwrite an original endpoint, and unchanged returned intervals may share identity with caller-owned lists. A nonmutating implementation would copy interval pairs first.
