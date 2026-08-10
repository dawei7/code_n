## General

A harmonious subsequence has maximum minus minimum exactly one. Because all chosen values lie between the minimum and maximum, such a subsequence can contain only two distinct integers:

$$
x\quad\text{and}\quad x+1.
$$

Both must occur. A subsequence containing only copies of one value has difference zero, not one.

Once a valid adjacent pair of values is chosen, the longest subsequence using that pair should include *every* occurrence of both values. Removing an occurrence cannot improve the maximum/minimum condition and only shortens the result. This reduces an apparent subsequence search to frequency counting.

**Counting values**

`cnt = Counter(nums)` creates a mapping from each distinct number to its number of occurrences. For the first sample, relevant entries include:

```text
1 -> 1
2 -> 3
3 -> 2
```

The candidate pair $(2,3)$ therefore produces length $3+2=5$.

Why is it legal to take every occurrence while preserving subsequence order? A subsequence may delete elements but must keep the relative order of those retained. Scan the original array and keep every element equal to $x$ or $x+1$. Their original relative order is automatically preserved, and their minimum and maximum differ by one. No rearrangement is required.

**Considering each adjacent pair exactly from its lower value**

The generator iterates over `cnt.items()`. For current value `x` with count `c`, it checks `cnt[x + 1]`. If that count is nonzero, the pair exists and its candidate length is:

```python
c + cnt[x + 1]
```

There is no need to also check `x - 1`. When the loop reaches lower value `x - 1`, it considers pair $(x-1,x)$. Looking only upward examines each unordered adjacent pair once.

Python’s `Counter` returns zero for a missing key, so `if cnt[x + 1]` is simultaneously an existence/count test. Unlike an ordinary `defaultdict` access, reading a missing Counter key does not need a separate membership expression for correctness.

`max(..., default=0)` returns the largest candidate. The default is essential when no adjacent-value pair exists: the generator is empty, and the correct answer is zero rather than an exception.

**Why frequencies are sufficient**

Suppose a harmonious subsequence has minimum $a$ and maximum $a+1$. It cannot contain any other integer, since integer values strictly between consecutive integers do not exist and values outside would expand the range. Its length is at most:

$$
\operatorname{count}(a)+\operatorname{count}(a+1).
$$

The algorithm evaluates exactly this sum for every $a$ whose successor exists. Conversely, taking all occurrences of any such pair produces a valid subsequence of exactly that length. Thus, each computed candidate is achievable, and every possible harmonious subsequence is bounded by one computed candidate.

Taking the maximum therefore gives the global optimum.

**Tracing important cases**

For `[1,2,3,4]`, all counts are one. Pairs $(1,2)$, $(2,3)$, and $(3,4)$ each produce two, so the answer is two.

For `[1,1,1,1]`, `cnt[2]` is zero. There are no generator values, and `default=0` returns zero. Returning four would be wrong because maximum and minimum would both be one.

Negative numbers require no special logic. If `x = -3`, the adjacent larger value is `-2`, and ordinary integer dictionary keys handle both.

## Complexity detail

Let $n$ be the array length and $u$ the number of distinct values. Building the Counter takes expected $O(n)$ time through hash-table updates. Iterating over its $u$ entries and doing expected constant-time successor lookups takes $O(u)$. Since $u\le n$, total expected time is $O(n)$.

The Counter stores $u$ key/count pairs, using $O(u)$ auxiliary space and $O(n)$ in the worst case. The generator itself is lazy and does not materialize all candidate sums; `max` consumes them one at a time.

Hash-table bounds are expected/amortized. The standard interview model treats integer hashing as constant expected time.

## Alternatives and edge cases

- **Sort and scan runs:** Sorting groups equal values, after which adjacent runs differing by one can be combined. It takes $O(n\log n)$ time and may modify the input.
- **One-pass incremental Counter:** Update each value’s count and compare with current counts of both neighbors. It can update the answer online, though the two-pass frequency reasoning is simpler.
- **Brute-force subsequences:** There are exponentially many and most differ only in which duplicate occurrences were chosen. Frequency reasoning eliminates this redundancy.
- **Nested comparison:** For every base value, scan the whole array to count it and its neighbor, taking $O(n^2)$ time.
- **All values equal:** Difference is zero, so return zero.
- **No consecutive keys:** The generator is empty and `default=0` handles it.
- **Several adjacent pairs:** A value may participate in $(x-1,x)$ and $(x,x+1)$, but these are separate candidates; all three values cannot appear together because their range would be two.
- **Duplicate-heavy pair:** Every occurrence of both adjacent values should be included.
- **Negative values:** Successor lookup `x + 1` works across the full integer range.
- **Subsequence versus subarray:** Selected occurrences need not be contiguous. Filtering the original sequence by two values always creates a valid subsequence.
- **Exactly one difference:** Checking only that values differ by *at most* one would incorrectly accept a single-value subsequence.
- **Missing Counter key:** It reads as zero, making the truth test false without creating a valid candidate.
- **Lazy candidate generation:** Memory stays at Counter size rather than allocating another list of $u$ sums.
