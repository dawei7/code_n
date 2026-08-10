## General

**View a good string as a sequence of fixed-size chunks**

A run of ones must have length divisible by `oneGroup`. Such a run can be divided uniquely into consecutive chunks of exactly `oneGroup` ones.

Likewise, every zero run can be divided into chunks of exactly `zeroGroup` zeroes.

Therefore, every good binary string can be constructed by repeatedly appending one of two chunk types:

- `"1"*oneGroup`;
- `"0"*zeroGroup`.

Adjacent chunks of the same type simply combine into a longer valid run. The fixed chunk size gives that run a unique internal chunk division, so the construction does not overcount strings.

**Define DP by total length**

`f[i]` is the number of valid chunk constructions producing a binary string of total length exactly `i`.

The base `f[0]=1` represents the empty construction. Although length zero is not returned because `minLength>=1`, it is the starting point for creating the first chunk.

All other lengths initially have count zero.

**Append a ones chunk**

If `i-oneGroup>=0`, take any valid construction of length `i-oneGroup` and append exactly `oneGroup` ones. This creates a valid string of length `i`.

There are `f[i-oneGroup]` such prior strings, so this count is added to `f[i]`.

The appended ones may start a new run after zeroes or extend an existing ones run. Either way, the resulting ones-run length remains a multiple of `oneGroup`.

**Append a zeroes chunk**

Symmetrically, when `i-zeroGroup>=0`, append a fixed zero chunk to every valid string of the shorter length. Add `f[i-zeroGroup]`.

The two transitions are distinguished by their final bits, so a construction ending with a ones chunk and one ending with a zeroes chunk cannot produce the same non-empty string at the final step.

**Why every good string is counted**

Take any non-empty good string. Look at its final run:

- if it ends in ones, that run contains at least one final block of exactly `oneGroup` ones; removing that block leaves another valid construction;
- if it ends in zeroes, remove one final `zeroGroup` block analogously.

The recurrence includes the corresponding predecessor. Repeating this removal eventually reaches the empty string.

Conversely, every recurrence transition appends a legal fixed-size block and preserves divisibility of all runs. Thus `f[i]` counts exactly all good strings of length `i`.

**Why there is no overcount from adjacent equal chunks**

Suppose a ones run has length $q\cdot\texttt{oneGroup}$. Its boundaries into fixed-size chunks occur after exactly one group size, two group sizes, and so on. There is only one such segmentation.

The DP cannot create the same run using a zero chunk or a differently sized ones chunk. Each full binary string therefore has one chunk sequence.

**Sum the requested length interval**

After filling lengths 1 through `maxLength`, the slice `f[minLength:]` includes exactly lengths from `minLength` through `maxLength` because the array ends there.

Summing that slice counts all good strings in the allowed range. Strings of different lengths are necessarily distinct, so their counts can simply be added.

**Trace the first sample**

With `oneGroup=1` and `zeroGroup=2`:

- length one has `"1"`;
- length two has `"11"` and `"00"`;
- length three has `"111"`, `"100"`, and `"001"`.

The requested lengths two through three contribute $2+3=5$.

**Apply modulo at every state**

Counts grow exponentially. Each `f[i]` is reduced modulo $10^9+7$ after both possible additions. Modular addition preserves the final residue.

The final interval sum is reduced once more because adding many already reduced entries can exceed the modulus.

**Meaning of zero as a multiple**

A string containing no ones has zero total ones-run size outside its zero runs; the construction allows it using only zero chunks. Similarly, all-ones strings use only ones chunks. The empty base supports either first choice.

## Complexity detail

Let $L=\texttt{maxLength}$. The loop fills `L` states, each with at most two constant-time transitions. Time is $O(L)$.

Array `f` has `L+1` entries, so auxiliary space is $O(L)$. The final slice created by `f[minLength:]` can also contain $O(L)$ references or integers, remaining within the same bound.

All values are maintained modulo the required prime.

## Alternatives and edge cases

- **Rolling recurrence:** If only one final length were needed, older states might be managed differently, but the arbitrary offsets and range sum make the full array simple.
- **Equal group sizes:** The two transitions still represent different final bit chunks and both must be counted.
- **Group size above current length:** That transition contributes nothing.
- **All-zero string:** It exists only when its length is a multiple of `zeroGroup`.
- **All-one string:** It exists only when its length is a multiple of `oneGroup`.
- **Adjacent same-type chunks:** They form a larger valid run without duplicate segmentation.
- **Empty base:** It seeds constructions but is excluded by positive `minLength`.
- **Single allowed length:** The final sum selects exactly `f[minLength]`.
- **Modulo:** Reduce both each DP state and the final range sum.
- **Ordered chunks:** Different bit sequences produce different binary strings.
