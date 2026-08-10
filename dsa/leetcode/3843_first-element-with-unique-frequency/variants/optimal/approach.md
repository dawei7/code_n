## General

**Unique frequency is different from frequency one**

The task does not ask for the first value that appears once. It asks for a value whose occurrence count is not shared by any other distinct value.

For example, in `[20,20,10,30,30,30]`:

- 10 has frequency 1;
- 20 has frequency 2;
- 30 has frequency 3.

All three frequencies are unique because each count belongs to only one distinct value. The answer is 20 because its first array occurrence comes earliest.

This requires two levels of counting: values first, then the frequencies themselves.

**Count each distinct value**

`cnt = Counter(nums)` creates:

$$
\texttt{cnt}[x]=F(x),
$$

the number of occurrences of value `x` in the complete array.

The full-array count must be known before deciding any position. A value appearing once in a prefix may appear again later, so a one-pass early decision without future information is unsafe.

**Count how many values share each frequency**

`cnt.values()` contains one frequency for every distinct value, not one entry per array position.

The source builds:

`freq = Counter(cnt.values())`.

Its meaning is:

$$
\texttt{freq}[f]
=
\left\lvert\{x:F(x)=f\}\right\rvert.
$$

A value `x` has a unique frequency exactly when:

`freq[cnt[x]] == 1`.

For `[20,10,30,30]`, `cnt` is `{20:1, 10:1, 30:2}`. The second Counter records that frequency 1 belongs to two values while frequency 2 belongs to one. Only 30 qualifies.

**Scan the original array to preserve first-position order**

Counters preserve aggregate information but the requested choice depends on the smallest original index. The source therefore scans `nums` from left to right after both counting passes.

At each element `x`, it looks up the value's frequency and then how many distinct values share that frequency. The first time the multiplicity is one, it returns `x` immediately.

All occurrences of one value have the same global frequency status. If a qualifying value appears several times, its first occurrence is the earliest possible index for that value, and the left-to-right scan reaches it correctly.

If the loop finishes, every distinct value shares its count with at least one other value. The source returns -1.

**Why the second Counter must count distinct values**

Suppose `x` appears three times. Frequency 3 should be represented once in `freq` for the distinct value `x`, not three times for its occurrences.

Building `Counter(cnt[x] for x in nums)` would incorrectly multiply every frequency by its occurrence count. Using `cnt.values()` avoids this mistake because the first Counter has one entry per distinct value.

**Why the algorithm returns exactly the required element**

The first Counter gives the exact $F(x)$ for every value. The second gives exact $M(F(x))$, the number of distinct values having that count. Thus the condition tested in the final loop is identical to the formal definition.

The loop order is the original index order, so the first successful test has the smallest possible index. If none succeeds, no value has unique frequency and -1 is required.

**Return the element, not its frequency or index**

The successful condition is discovered while scanning an array position, but the contract requests `nums[i]` itself. The source therefore returns `x`.

It does not return `cnt[x]`, which would be the unique frequency, and it does not return the loop index. This distinction matters in the first example: the qualifying value is 30, its frequency is 2, and its first index is also 2. Only 30 is the requested result.

Because the array contains positive values, sentinel -1 cannot be confused with a real returned element.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and $D$ be the number of distinct values. Building `cnt` takes expected $O(N)$ time. Building `freq` takes $O(D)$, and the final scan takes at most $O(N)$. Total expected time is $O(N)$.

`cnt` stores $D$ entries. `freq` stores at most $D$ distinct frequency values. Total auxiliary space is $O(D)$.

## Alternatives and edge cases

- **Sort the array:** Frequencies can be derived from equal-value runs, but sorting costs $O(N\log N)$ and loses original order unless positions are separately preserved.
- **Fixed value-frequency arrays:** Since values are bounded by $10^5$, arrays can replace Counters for deterministic indexing. They reserve the entire domain even when $D$ is small.
- **Nested comparison of frequencies:** Count values, then compare every pair of distinct frequencies. This costs $O(D^2)$ instead of using the second Counter.
- **Single element:** Its frequency 1 belongs to one distinct value, so that element is returned.
- **All elements distinct:** If there is more than one distinct value, all share frequency 1 and none qualifies.
- **All elements equal:** There is one distinct value, so its frequency is unique and the first element is returned.
- **Several qualifying values:** The scan returns whichever qualifying value appears first, not the one with smallest value or smallest frequency.
- **Repeated qualifying value:** Its first occurrence triggers the return.
- **No qualifying frequency:** The complete scan ends and returns -1.
- **Frequency multiplicity:** It counts distinct values having a frequency, not total array positions belonging to those values.
