## General

**Precompute distinct suffix counts**

At index $i$, the required suffix excludes `nums[i]` and begins at $i+1$.

The solution first builds array `suf` where:

$$
\texttt{suf[i]}
=
\#\text{ distinct values in }\texttt{nums[i..n-1]}.
$$

An extra entry `suf[n] = 0` represents the empty suffix after the last index.

This lets the second pass read the required suffix count as `suf[i + 1]` in constant time.

**Build suffix values from right to left**

Set `s` begins empty. For `i` descending from $n-1$ to zero:

- add `nums[i]` to the set;
- assign `suf[i] = len(s)`.

The set contains exactly the values from current index through the end.

Repeated occurrences do not increase set size, which is precisely the meaning of distinct count.

**Why the extra array entry avoids a special case**

For final index $n-1$, the required suffix `nums[n..n-1]` is empty.

Reading `suf[n]` returns initialized zero. No conditional is needed inside the forward pass.

This sentinel-style entry makes the same formula valid at every index.

**Reuse the set for prefix counting**

After suffix preprocessing, `s.clear()` empties the same set object.

The forward loop adds `nums[i]`, so after insertion:

$$
\texttt{len(s)}
=
\#\text{ distinct values in }\texttt{nums[0..i]}.
$$

The answer assignment is:

`ans[i] = len(s) - suf[i + 1]`.

This is exactly prefix distinct count minus excluded-current suffix distinct count.

**Trace the repeated-value example**

For `nums = [3,2,3,4,2]`, suffix distinct counts include:

- `suf[5]=0`;
- `suf[4]=1` for `[2]`;
- `suf[3]=2` for `[4,2]`;
- `suf[2]=3` for `[3,4,2]`;
- earlier suffixes remain size three.

During forward pass:

- at index zero, prefix set is `{3}`, size one; suffix from index one has size three, difference $-2$;
- at index one, prefix size two and suffix from two size three, difference $-1$;
- at index two, adding repeated three does not change prefix size two; suffix from three has size two, difference zero;
- final values become two and three.

The result is `[-2,-1,0,2,3]`.

**Why negative answers are valid**

The suffix may contain more distinct values than the current prefix. Subtracting can therefore produce a negative integer.

The algorithm performs ordinary signed subtraction and does not take absolute value or clamp at zero.

**Two invariants prove correctness**

After backward iteration at index $i$, set `s` contains exactly values in suffix `nums[i..n-1]`, so `suf[i]` is correct.

After clearing, during forward iteration at index $i$, set `s` contains exactly values in prefix `nums[0..i]`.

Therefore:

$$
\texttt{len(s)}-\texttt{suf[i+1]}
=
|\operatorname{distinct}(\texttt{nums[0..i]})|
-
|\operatorname{distinct}(\texttt{nums[i+1..n-1]})|.
$$

That is the definition of `diff[i]`.

**Why one suffix array is useful**

Prefix counts can be maintained online while moving left to right, but suffix counts would shrink as values leave. A frequency map could maintain them dynamically.

The exact solution instead precomputes all suffix distinct counts in one simple backward pass. This uses linear storage and keeps the forward calculation straightforward.

**Why clearing and reusing the set is safe**

The suffix information needed later is no longer stored only in the set. At every backward step, the current set size was copied into the corresponding integer entry of `suf`. Clearing `s` therefore discards only the temporary collection used to construct those counts; it does not alter any integer already written to `suf`. The same set object can then begin a logically separate job as the prefix set. This reuse saves the need to allocate a second named set, but correctness would be identical with two different set objects. The crucial requirement is to clear it before the forward pass, because leftover suffix values would make the supposed prefix set contain elements that have not yet appeared in the prefix.

**Every value is processed only twice**

One backward insertion and one forward insertion occur per element. Set operations are expected constant time.

There is no nested scan of prefixes or suffixes, avoiding the $O(n^2)$ direct method.

**Input preservation**

The algorithm never sorts or modifies `nums`. Both passes read elements in different directions.

## Complexity detail

The backward and forward passes each visit $n$ elements. Expected set insertion is $O(1)$, so total expected time is $O(n)$.

`suf` and `ans` each contain $O(n)$ integers. The set can hold $O(n)$ distinct values. Total space is $O(n)$.

## Alternatives and edge cases

- **Suffix frequency map updated forward:** Start with all counts, remove current value, and track distinct suffix size while building prefix set; also $O(n)$.
- **Rebuild prefix and suffix sets per index:** Correct but $O(n^2)$.
- **Frequency arrays:** Values are bounded by 50, so fixed arrays can replace sets.
- **Single element:** Prefix distinct count is one, empty suffix count zero, result `[1]`.
- **All values distinct:** Prefix size rises while suffix size falls predictably.
- **All values equal:** Every nonempty prefix/suffix has distinct count one; final suffix is zero.
- **Empty suffix:** `suf[n]=0` handles the final index.
- **Negative difference:** It is valid and must not be clamped.
- **Repeated prefix value:** Set size remains unchanged.
- **Input preservation:** No mutation or sorting occurs.
