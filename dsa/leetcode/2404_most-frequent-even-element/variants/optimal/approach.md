## General

**Filter and count only eligible values**

Odd values can never be returned, so the Counter is built from a generator that yields only values satisfying `x % 2 == 0`. This includes zero, because zero is divisible by two.

The result `cnt` maps each distinct even value to its frequency in `nums`. Ignoring odds during construction saves unnecessary map entries and makes every later candidate valid by definition.

**Track both ranking criteria**

The desired ranking has two levels:

1. greater frequency is better;
2. among equal frequencies, smaller numeric value is better.

The source keeps `mx` as the best frequency seen and `ans` as the corresponding value. It updates when:

```python
v > mx or (v == mx and ans > x)
```

The first condition handles a new strictly more frequent even value. The second handles a frequency tie and chooses the smaller value.

This explicit comparison is necessary because Counter iteration order reflects first insertion order, not the problem's numeric tie-break.

**Why the initialization encodes the no-even answer**

`ans` begins at `-1` and `mx` at zero. Every real Counter frequency is positive, so the first even candidate always satisfies `v > mx` and replaces the sentinel.

If `cnt` is empty, the loop never runs and `ans` remains `-1`, exactly the required result when no even element exists.

The tie clause `ans > x` is not used before a real answer exists because every first candidate wins through frequency. Thus, using negative one as the sentinel does not interfere with smaller-value comparisons among valid nonnegative inputs.

**Trace the first example**

For `[0,1,2,2,4,4,1]`, the filtered Counter is:

```text
0 -> 1
2 -> 2
4 -> 2
```

Value zero first establishes frequency one. Value two has frequency two and replaces it. Value four ties at two, but `ans > x` becomes `2 > 4`, which is false, so two remains.

The algorithm does not need to sort the keys; the two-part update produces the same winner under any Counter iteration order.

**Why the scan returns the exact optimum**

After processing any subset of Counter entries, maintain that `mx` is the greatest frequency among them and `ans` is the smallest value having that frequency.

For a new entry with lower frequency, the invariant remains unchanged. With higher frequency, that entry uniquely improves the primary criterion and becomes the new answer. With equal frequency, choosing the smaller of the current answer and new value preserves the secondary criterion.

The invariant holds after the first candidate and therefore after all distinct even values. If there were none, the separately meaningful sentinel remains.

**Why frequency must be counted globally**

The most frequent even value may appear in separated parts of the array. A run-length count would miss occurrences outside one consecutive block. Counter aggregation correctly combines all positions because the task depends on value frequency, not adjacency.

**Alternative tuple interpretation**

One can view each candidate as ranked by tuple `(-frequency, value)` under ascending order. The exact code performs the equivalent comparison without allocating or sorting candidate tuples.

**Why a one-pass selection is enough**

Sorting all Counter entries by that tuple would place the desired candidate first, but it would compute a complete order that the problem never asks for. The running pair `(mx, ans)` is a sufficient summary of everything processed: future candidates need to be compared only with the current winner, not with every loser. This is the same reduction used when finding an ordinary maximum, extended with a deterministic tie rule. Once a candidate loses on frequency, its numeric value cannot rescue it; once it ties, only its value matters. These mutually exclusive cases make the single scan complete.

**A tie arriving before the eventual maximum**

Suppose values eight and two both first establish frequency three, so the tie rule makes two the current answer. If value ten later has frequency four, it replaces two even though ten is larger, because frequency is the primary rule. If value zero then also has frequency four, zero replaces ten through the secondary rule. This sequence demonstrates that the update remains correct regardless of when candidates appear.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct even values. The generator inspects every input once, and expected Counter updates take $O(1)$ each. Building counts costs expected $O(n)$ time.

The selection loop processes $u$ entries in $O(u)$ time. Since $u\le n$, total expected time is $O(n)$.

The Counter stores $u$ entries, giving $O(u)$ auxiliary space as stated in the manifest. All selection variables use constant space.

## Alternatives and edge cases

- **Sort even values:** Sorting groups equal values but costs $O(n\log n)$ time; hashing counts in expected linear time.
- **Frequency array:** Values are bounded by `10^5`, so a fixed count array is possible. It uses domain-sized space and can scan even indices in ascending order.
- **Counter all values then filter:** Correct but stores irrelevant odd keys.
- **No even values:** The empty loop leaves the answer at `-1`.
- **Only one even value:** It wins regardless of how many odd values appear.
- **Frequency tie:** The explicit numeric comparison selects the smaller even value.
- **Zero:** It is even and can be returned.
- **Separated occurrences:** Counter combines them globally.
- **Arbitrary Counter iteration order:** Correctness does not depend on it because both ranking criteria are checked explicitly.
